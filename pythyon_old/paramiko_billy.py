#!/usr/bin/python3

import paramiko

try:
    con = paramiko.client.SSHClient()
    con.load_system_host_keys()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    con.connect('192.168.201.138', username ='developer', password ='4linux')
    
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

stdin, stdout, stderr = con.exec_command('init 6')

#Se o comando foi executado com sucesso
if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))

con.close()