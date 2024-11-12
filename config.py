# config.py

# Hardcoded Azure Key Vault secret values (from Azure Key Vault)
AZURE_KEY_VAULT_URL = "https://ghaskeyvault.vault.azure.net/"
SECRET_NAME = "ghaskeyvault"  # The name of the secret stored in Azure Key Vault
SECRET_VALUE = "1234567890"  # Hardcoded secret value (for demo purposes)

# Example of other non-sensitive config values
DATABASE_URI = "postgres://user:password@localhost:5432/mydb"  # Non-sensitive value
API_KEY = "my-hardcoded-api-key"  # Another non-sensitive value
