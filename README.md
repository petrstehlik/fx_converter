# FX Converter

You are given a very easy task from a product manager: "Build me a currency converter."

In front of you lies a simple skeleton app which you can and should use to build such an amazing service.

## What Is Expected

You will fetch the fx rates from a publicly available source such as:
  - https://exchangeratesapi.io/
  - https://openexchangerates.org/
  - https://fixer.io
  - https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html

The choice is up to you but you should say why you chose that one.

### The API

It is expected to have the data exposed via a GraphQL API and even the first-time user of GraphQL should be able to use it and understand the data present there.

We want to:
- query the latest fx rates
- query historical fx rates from a specific time (day or hour)
- convert from one currency to any other
- list all available currencies
- query all this even when the fx source is offline

### Data

You should store the data on your side as we want to query this API tens of thousands of times every hour.

### Tests

Yes, please.

### Deployment

Via Docker to Kubernetes cluster. Don't do the k8s part.

### Versioning

Via git.

## Final remarks

Show me what you got.

Any questions, remarks, and notes put into NOTES.md.

The task is not time-limited but it shouldn't take you longer than 6 hours. Commit regularly to show progress and remember `import this`.