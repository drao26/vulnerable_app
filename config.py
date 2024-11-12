# config.py

# Hardcoded Azure Key Vault secret values (from Azure Key Vault)
AZURE_KEY_VAULT_URL = "https://ghaskeyvault.vault.azure.net/"
SECRET_NAME = "ghaskeyvault"  # The name of the secret stored in Azure Key Vault
SECRET_VALUE = "1234567890"  # Hardcoded secret value (for demo purposes)
client_id = "9442bdfb-f1aa-48a2-ad2c-dbb7c1ca7a58"
client_secret = "QXs8Q~qXnFLTVs-WX424nLp7rC42gAL~bhprKbNf"
tenant_id = "3c731193-87b2-48b6-9ac2-0fac6c2fe244"




# Example of other non-sensitive config values
DATABASE_URI = "postgres://user:password@localhost:5432/mydb"  # Non-sensitive value
API_KEY = "my-hardcoded-api-key"  # Another non-sensitive value

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

