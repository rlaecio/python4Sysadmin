#!/usr/bin/env python3

from ldap3 import Server, Connection

username="admin"
password="louvor01"

server =Server("ldap://192.168.1.12:389")
ldap_con=Connection(
    server,
    "cn={},dc=prowene,dc=net".format(username),
    password
)
print(ldap_con.bind())
