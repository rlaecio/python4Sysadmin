#!/usr/bin/env python3
from ldap3 import MODIFY_REPLACE, Server, Connection
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


email = "joao.hummel@4linux.com.br"
dn = "uid={},dc=prowene,dc=net".format(email)
changes = {
    "cn": [(MODIFY_REPLACE, ["joao gabriel"])],
    "sn": [(MODIFY_REPLACE, ["hummel"])]
}
ldap_con.modify(
    dn,
    changes
)
print(ldap_con.result)
