#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect(
        'host=localhost dbname=consultorio user=admin password=4linux'
    )
    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

consultafuncionario = input('Para um cadastro de consulta, por favor informe seu nome de usuário:')
consultadiasemana = input('Olá {}, qual o dia da semana da consulta? '.format(consultafuncionario))
consultacliente = input('Digite o nome do paciente: ')
consultamedico = input('Digite o nome do Médico: ')
consultadia = input('Qual o dia e horário da consulta? Seguindo o modelo "Ano, Mes, Dia" e horário "00:00"')

consultainsert = input('Para finalizar o cadastro da consulta, escreva "cadastro":')
if consultainsert == 'cadastro':
    cur.execute("insert into consultas (funcionarios, dia_da_semana, cliente, medico, dia)\
        values ('{}', '{}', '{}', '{}', '{}');".format(consultafuncionario,consultadiasemana,consultacliente,consultamedico,consultadia))
    con.commit()
    print("Consulta Cadatrada com sucesso:")
    print('Informações da consulta:')
    print('Consulta cadastrada para {} dia {}, paciente {} , médico {}.'.format(consultadiasemana,consultadia,consultacliente,consultamedico))

consultaquery = input('Para validar informações completas de todas as consultas, escreva a palavra "all":')
if consultaquery == 'all':
        cur.execute("select * from consultas;")
        print(cur.fetchall())

cur.close()
con.close()