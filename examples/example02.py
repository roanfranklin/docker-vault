import hvac
import sys
import os
from dotenv import load_dotenv 

load_dotenv() 

_VAULT_URL = os.getenv('VAULT_URL')
_VAULT_TOKEN = os.getenv('VAULT_TOKEN')

client = hvac.Client(
    url = _VAULT_URL,
    token = _VAULT_TOKEN,
)


# Escrever um segredo
create_response = client.secrets.kv.v2.create_or_update_secret(
    path='my-secret-password',
    secret=dict(password='Hashi123'),
)

print('Secret written successfully.')


# Leitura de um segredo
read_response = client.secrets.kv.read_secret_version(path='my-secret-password')

password = read_response['data']['data']['password']


if password != 'Hashi123':
    sys.exit('unexpected password')

print('Access granted!')