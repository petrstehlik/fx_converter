"""FIXME: THIS IS AN EXAMPLARY SCHEMA!!!

Source: https://github.com/timfeirg/flask-graphene-boilerplate/blob/master/graphene_boilerplate/schema.py
"""

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from fx_converter.database import db
from fx_converter.models import Rate as RateModel


class Rate(SQLAlchemyObjectType):
    class Meta:
        model = RateModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_items = SQLAlchemyConnectionField(Rate)


class CreateItem(graphene.Mutation):
    class Arguments:
        key = graphene.String()
        value = graphene.JSONString()

    ok = graphene.Boolean()
    item = graphene.Field(lambda: Rate)

    def mutate(self, info, key, value):
        item = RateModel(key=key, value=value)
        db.session.add(item)
        db.session.commit()
        return CreateItem(ok=True, item=item)


class DeleteItem(graphene.Mutation):
    class Arguments:
        id_ = graphene.Int(required=False)
        key = graphene.String(required=False)

    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        item = None
        if not kwargs:
            raise Exception("Must provide either id_ or key")
        if kwargs.get("_id"):
            item = RateModel.get(kwargs["id_"])
        else:
            item = RateModel.get_by_key(kwargs["key"])

        if not item:
            raise Exception("Item not found")
        item.delete()
        return DeleteItem(ok=True)


class Mutations(graphene.ObjectType):
    create_item = CreateItem.Field()
    delete_item = DeleteItem.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
