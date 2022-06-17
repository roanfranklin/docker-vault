## Vault com Docker

Para essa PoC, usei o Vault Cloud rodando em um container Docker. E para a aplicação, usei um script python+flask somente para exibir os valores.



>**OBS.:**
>
>Tem outros [vault-examples](https://github.com/hashicorp/vault-examples) com outras liguagens de programações como Go, Ruby, C#, Python e Java (Spring).

---

### Requesitos

- docker
- docker-compose
- vault-cli

### Instalação do Docker e docker-compose

- Debian/Ubuntu:

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
```

Mais informações acesse: https://docs.docker.com/compose/install/

### Instalação do Vault

- Debian/Ubuntu:
```bash
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install vault
```

Para instalar em outros Sistemas Operacionais, verifique o link: https://www.vaultproject.io/downloads

---

### Levantar o Vault e testar algumas aplicações

Vamos levanta/carregar o Vault com o *docker-compose*:

```bash
docker-compose up -d
```

Depois que carregar, verifique se está UP/Rodando com o comando:

```bash
docker ps
```

Tudo rodando 100% então é so abrir no navegador:

- http://{SEU_IP}:8200
- http://localhost:8200

OBS.: O Token escolhido/setado neste exemplo foi *74cc1c60799e0a786ac7094b532f01b1*. Então acesso o gerenciamento com o token.

---

### Acesso a interface de gerenciamento do VAULT localmente

Variáveis de ambientes:
  - VAULT_ADDR
  - VAULT_TOKEN

```bash
export VAULT_ADDR=http://localhost:8200
export VAULT_TOKEN=74cc1c60799e0a786ac7094b532f01b1
```


Execute os 3 (três) exemplos escritos em python:

Os exemplos são 2 (dois) somente texto/terminal/console e o último/3º (terceiro) uma aplicação web simples.
  
```bash
cd examples/
```

- Exemplo 01

Guardar um segredor Key/Value que será usado pelo *example.py*:
```bash
vault kv put secret/myapp/password password=OnEsuP4s3cr3t
```

Depois de adicionado o segrado, é só instalar a(s) bilioteca(s) usada(s) pelo script/aplicação e executar:
```bash
pip3 install -r requirements.txt
python3 example01.py
```

- Exemplo 02

O segundo exemplo está gravando um segredo e depois lendo esse segredo:
```bash
pip3 install -r requirements.txt
python3 example02.py
```

>**OBS.:**
>
>É possível criar politicas de segurança como somente leitura em um segredo.


- WebApp

```bash
vault kv put secret/webapp \
             endpoint=rds-prd-cluster-pgsql.chf3ca2aqz12c.us-east-1.rds.amazonaws.com \
             database=xwebapp \
             username=usertest \
             password=sup4s3cr3t
```

---

Fontes:
- https://www.vaultproject.io/docs/get-started/developer-qs
- https://github.com/hashicorp/vault-examples