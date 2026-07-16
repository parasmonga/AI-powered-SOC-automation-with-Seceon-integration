import os

# Seceon Server
SECEON_BASE_URL = os.getenv(
    "SECEON_BASE_URL",
    "https://172.23.123.129"
)

# Tenant
TENANT_ID = os.getenv(
    "SECEON_TENANT_ID",
    "TAS9999"
)

# Bearer Token
BEARER_TOKEN = os.getenv(
    "SECEON_BEARER_TOKEN",
    ""
)

# Ignore SSL (internal lab)
VERIFY_SSL = False