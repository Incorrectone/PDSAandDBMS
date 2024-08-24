import sys
import os
import psycopg2

file = open("", r)
name = file.read().strip()

try:
    connection = psycopg2.connect(
        database = sys.argv[1],
        user = os.environ.get('PGUSER'),
        password = os.environ.get('PGPASSWORD'),
        host = os.environ.get('PGHOST'),
        port = os.environ.get('PGPORT')
    )
    
    cursor = connection.cursor()
    query = ''
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    for res in result:
        print(res)
    
    cursor.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    connection.close()