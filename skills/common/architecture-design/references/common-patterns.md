# Architecture Design — Extended Guidance

## Common Patterns

### Pattern 1: Strangler Fig Migration

Incrementally replace a legacy system by routing traffic through a facade:

```
     ┌────────────┐
     │   Facade   │
     │  (Router)  │
     └─────┬──────┘
           │
    ┌──────┼──────────┐
    │      │          │
    ▼      ▼          ▼
 ┌─────┐ ┌─────┐ ┌────────┐
 │ New │ │ New │ │ Legacy │
 │ Svc │ │ Svc │ │ System │
 │  A  │ │  B  │ │(rest)  │
 └─────┘ └─────┘ └────────┘

Phase 1: Facade routes 100% to legacy
Phase 2: Migrate feature A to new service, route A-traffic to new
Phase 3: Migrate feature B, route B-traffic to new
Phase N: Decommission legacy when 0% traffic remains
```

### Pattern 2: Backend for Frontend (BFF)

Separate API layers tailored to each client type:

```
 ┌──────┐  ┌────────┐  ┌─────────┐
 │ Web  │  │ Mobile │  │ Partner │
 │ App  │  │ App    │  │ API     │
 └──┬───┘  └───┬────┘  └────┬────┘
    │          │             │
 ┌──▼───┐  ┌──▼─────┐  ┌────▼────┐
 │ Web  │  │ Mobile │  │ Partner │
 │ BFF  │  │ BFF    │  │ BFF     │
 └──┬───┘  └───┬────┘  └────┬────┘
    │          │             │
    └──────────┼─────────────┘
               │
    ┌──────────▼──────────┐
    │  Shared Domain APIs  │
    └──────────────────────┘
```

### Pattern 3: Anti-corruption Layer

Isolate your domain from a messy external system:

```python
# anticorruption/legacy_adapter.py
from domain.models import Customer
from legacy_client import LegacyERPClient

class LegacyCustomerAdapter:
    """Translates between legacy ERP data and our domain model."""

    def __init__(self, client: LegacyERPClient):
        self._client = client

    def get_customer(self, customer_id: str) -> Customer:
        raw = self._client.fetch_account(customer_id)
        return Customer(
            id=str(raw["ACCT_NUM"]),
            name=f"{raw['FIRST_NM']} {raw['LAST_NM']}".strip(),
            email=raw.get("EMAIL_ADDR", "").lower(),
            tier=self._map_tier(raw.get("CUST_CLASS", "Z")),
        )

    @staticmethod
    def _map_tier(legacy_class: str) -> str:
        mapping = {"A": "platinum", "B": "gold", "C": "silver"}
        return mapping.get(legacy_class, "standard")
```
