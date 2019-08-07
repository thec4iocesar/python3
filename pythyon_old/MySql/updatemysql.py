#!/usr/bin/python3

import MySQLdb

try:
    con = MySQLdb.connect(
        host     = 'localhost',
        user     = 'admin',
        passwd   = '4linux',
        db       = 'projeto'
    )

    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    cur.execute("update usuarios\
        set nome='Palhaço' where id=7;")
    con.commit()

except Exception as e:
    con.rollback()
    print('Erro: {}'.format(e))

finally:
    cur.close()
    con.close()