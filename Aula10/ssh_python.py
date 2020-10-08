#!/usr/bin/env python3
import paramiko


try:
    con = paramiko.SSHClient()
    con.load_system_host_keys()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.connect('192.168.1.8', 
                username='rlaecio',
                password='louvor01')
    
except Exception as e:
    print('Erro: {}',format(e))
    exit()
    

## - ex1: 
print(con.exec_command('cat /etc/*-release')[1].read().decode('utf-8'))

stdin, stdout,stderr = con.exec_command("ls -la")
if stdout.channel.recv_exit_status()==0:
    print(stdout.read().decode("utf-8"))
else:
    print(stderr.read().decode("utf-8"))