import cx_Oracle

conn=cx_Oracle.connect('sys/"sivaMS@35"@localhost:1521/orclpdb', mode=cx_Oracle.SYSDBA)
print('Connection version is:',conn.version)
c=conn.cursor()
c.execute('create table student(rollno number(5),name varchar2(20),fee number(10,2))')
print('table created.')
conn.commit()
conn.close()