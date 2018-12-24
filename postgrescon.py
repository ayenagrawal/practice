import psycopg2

conn = psycopg2.connect(host="localhost", database="smartiddb", user="ADMIN", password="atmecs@1234")
cur = conn.cursor()
cur.execute("SELECT * FROM public.user")
# to check the version and ensure connection onject works
'''cur.execute("SELECT version()")
db_ver = cur.fetchone()
print(db_ver)'''
db_table = cur.fetchall()
for list in db_table:
    print(list)
    print()
cur.close()
conn.close()
