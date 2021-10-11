import jwt
import base64
public = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArmaa8+ul/ynJ5V9IqffI
2p+9E+6P7tgCKMXBc/pBtAziUvBvGqZcYxbaKk7fMkxdBXK/DxQ3u6gMwvf40fOq
qgWahpg0flZpfnpyBly/HvC9eBzNwH00NOWmUDFiJbcBT7UmVCP/wdmNLTH4yKKE
I7KcfE/84dZaVMmhu/zLcPoshA9iYlRWlZ5OgQJbrxEh8ck5yXuNLxKQzO5X/fAs
my1lqnlnoFEuvH8DnRQSBPkQtZViBoSBtyf/kfZTlw1wH2R4AapgA0l1gLxuHBIA
nIljQMaFwQQbGcp6h8E9KEMz3+PfohXQthyKTIHmodhKH+1VH8e5rNIYgo233yii
EQIDAQAB
-----END PUBLIC KEY-----
'''
payload={
  "username": "admin",
  "role": "admin"
}
print(jwt.encode(payload, key=public, algorithm='HS256'))