from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Joshua P. in 3308'

@app.route('db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_database_neu6_user:R4HMkxxlwa3rjNVNE29EUhRn505UKS17@dpg-cvmb2mnfte5s73akthv0-a/lab_10_database_neu6")
    conn.close()
    return "Database Connection Successful"