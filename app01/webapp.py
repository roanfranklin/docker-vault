import hvac
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv() 

_VAULT_URL = os.getenv('VAULT_URL')
_VAULT_TOKEN = os.getenv('VAULT_TOKEN')

client = hvac.Client(
    url = _VAULT_URL,
    token = _VAULT_TOKEN,
)

app = Flask(__name__)

# vault kv put secret/webapp \
#              endpoint=rds-prd-cluster-pgsql.chf3ca2aqz12c.us-east-1.rds.amazonaws.com \
#              database=xwebapp \
#              username=usertest \
#              password=sup4s3cr3t

@app.route('/')
def index():
    read_response = client.secrets.kv.read_secret_version(path='webapp')
    _ENDPOINT = read_response['data']['data']['endpoint']
    _DATABASE = read_response['data']['data']['database']
    _USERNAME = read_response['data']['data']['username']
    _PASSWORD = read_response['data']['data']['password']

    _MSG = '''<h3>[ K/V | KEY/VALUE | CHAVE/VALOR ]</h3><br>
    <strong>endpoint:</strong> {3}<br>
    <strong>database:</strong> {0}<br>
    <strong>username:</strong> {1}<br>
    <strong>password:</strong> {2}
'''.format(_DATABASE, _USERNAME, _PASSWORD, _ENDPOINT)

    return _MSG