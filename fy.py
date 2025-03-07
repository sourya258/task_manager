import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname="task_manager",user="postgres",password= "gublu@sql9",port = 5432, host = "localhost")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query

cur.execute("CREATE DATABASE task_manager")

print(cur.fetchall())
    
    

conn.commit()
# Retrieve query results
cur.close()
conn.close()