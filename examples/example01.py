import hvac
import os
from dotenv import load_dotenv 

load_dotenv() 

_VAULT_URL = os.getenv('VAULT_URL')
_VAULT_TOKEN = os.getenv('VAULT_TOKEN')

client = hvac.Client(
    url = _VAULT_URL,
    token = _VAULT_TOKEN,
)


## Escrita pela linha de comando:
# vault kv put secret/myapp/password password=123


## Leitura do valor da chave "myapp/password"
read_response = client.secrets.kv.read_secret_version(path='myapp/password')

password = read_response['data']['data']['password']


print('A chave {0}'.format(password))