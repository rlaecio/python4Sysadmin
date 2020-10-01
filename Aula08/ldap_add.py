#!/usr/bin/env python3
from ldap3 import Server, Connection
from hashlib import md5
from binascii import b2a_base64

username="admin"
password="louvor01"

server =Server("ldap://192.168.1.12:389")
ldap_con=Connection(
    server,
    "cn={},dc=prowene,dc=net".format(username),
    password
)
ldap_con.bind()

md5json = md5("senhapadrao".encode("utf-8")).digest()
user = {
    "cn": "joao",
    "sn": "hummel",
    "mail": "joao.hummel@4linux.com.br",
    "uidNumber": "123",
    "gidNumber": "123",
    "uid": "joao",
    "homeDirectory": "/home/joao",
    "userPassword": "{MD5}" + b2a_base64(md5json).decode("utf-8")
}
objectClass = ["top", "person", "inetOrgPerson", "posixAccount", "organizationalPerson"]
dn = "uid={},dc=prowene,dc=net".format(user["mail"])
user_added = ldap_con.add(dn, objectClass, user)
print(user_added)