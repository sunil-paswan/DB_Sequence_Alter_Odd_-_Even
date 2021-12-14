import psycopg2
import os

####################################################
# export DB_NAME=""
# export DB_USER=""
# export DB_PASS=""
# export DB_HOST=""
# Create the Environment Variable With Mentioned Name
# Make sure to install psycopg2 module before executing this script 
#####################################################

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
for row in rows:
    sequence.append(row[0])
for name in sequence:
    cur.execute("""ALTER SEQUENCE %s AS integer INCREMENT BY 1""" % name)
    conn.commit()
   
print ("Sequence Alter Operation done successfully");
conn.close()    
