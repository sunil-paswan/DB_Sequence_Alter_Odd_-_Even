import psycopg2
import os

#####################################################################
# export DB_NAME=""
# export DB_USER=""
# export DB_PASS=""
# export DB_HOST=""
# Create the Environment Variable With Mentioned Name
# Make sure to install psycopg2 module before executing this script
#####################################################################


db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')

conn = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = "5432")
print ("Sequence Alter Operation started")
cur = conn.cursor()

cur.execute("select sequencename,last_value from pg_sequences")
rows = cur.fetchall()
sequence= []
lastvalue=[]

for row in rows:
    sequence.append(row[0])
    lastvalue.append(row[1])
for name,value in zip(sequence,lastvalue):
    name = str(name)
    new_value = str(value+1)
    cur.execute('ALTER SEQUENCE %s AS integer INCREMENT BY 2 START WITH %s RESTART WITH %s' % (name,new_value,new_value))
    conn.commit()

print ("Operation done successfully");
conn.close()    
