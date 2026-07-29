# Security guidance for this repo

## Logging

- Do not log `customer_id`, `account_number` or `national_id` at INFO level or above.
- Never log full request bodies on any route under `/payments`.

## Authorization

- All routes under `/admin` must call `require_role("admin")` before any database read.
- All routes under `/api/v1` must resolve the tenant from the session, never from a request parameter.

## Data access

- Every query against a tenant-scoped table must filter by `org_id`.
- Raw SQL must use parameter binding. String concatenation or f-strings in SQL are never acceptable.

## Secrets and comparisons

- Use `hmac.compare_digest` for token comparison, never `==`.
- Credentials load from the secret manager at runtime. No literal keys in source, including test fixtures.
EOF
