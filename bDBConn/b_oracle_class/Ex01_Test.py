import cx_Oracle as oci
conn = oci.connect('scott/tiger@localhost:1521/orcl')
#print(conn.version)

cur = conn.cursor()
sql = "select * from emp"
cur.execute(sql)
datas = cur.fetchall()

for row in datas:
    print(row[0],row[1],row[5])
cur.close()
conn.close()

