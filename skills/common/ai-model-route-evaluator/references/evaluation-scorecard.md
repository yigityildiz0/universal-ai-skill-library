# Model route scorecard

Record raw evidence before assigning a score.

| Dimension | Evidence to capture |
|---|---|
| Identity | Provider, exact model ID/version/date, endpoint/product, fixed or floating alias |
| Task fit | Representative workload, success rubric, language, modality, tools/agents |
| Quality | Version-pinned benchmark or controlled A/B result; judge agreement and failure cases |
| Access | Plan/API distinction, region, quota, rate/concurrency limits, availability |
| Economics | Input/output/cached/tool pricing, subscription allocation, retry/failure cost |
| Speed | Time to first token, completion latency, throughput, variance, cold start |
| Context | Advertised and practical context, output cap, retrieval/file behavior |
| Privacy | Retention, training use, enterprise/API terms, data residency, trust boundary |
| Reliability | Error rate, alias drift, deprecation policy, support and status evidence |
| Local route | Required RAM/VRAM/storage, quantization, speed, quality loss, setup burden |

Use hard gates first: unsupported modality, unavailable route, unacceptable data
handling, unaffordable worst-case cost, or hardware mismatch disqualifies a route
before weighted ranking.
