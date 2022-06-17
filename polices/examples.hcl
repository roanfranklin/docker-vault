
# CRUD dos segredos do myapp
path "secret/myapp" {
  capabilities = ["create", "read", "update", "delete", "list"]
}