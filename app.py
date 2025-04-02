#
# This script was written by: Joshua Peters
# Date: 4/1/25
# Modified: 4/1/2025
# Purpose: 
# Usage:

from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Joshua P. in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_database_neu6_user:R4HMkxxlwa3rjNVNE29EUhRn505UKS17@dpg-cvmb2mnfte5s73akthv0-a/lab_10_database_neu6")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://lab_10_database_neu6_user:R4HMkxxlwa3rjNVNE29EUhRn505UKS17@dpg-cvmb2mnfte5s73akthv0-a/lab_10_database_neu6")
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')

    conn.commit()
    conn.close()

    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://lab_10_database_neu6_user:R4HMkxxlwa3rjNVNE29EUhRn505UKS17@dpg-cvmb2mnfte5s73akthv0-a/lab_10_database_neu6")
    cur = conn.cursor()

    cur.execute(''''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);'
        ''')
    
    conn.commit()
    conn.close()

    return "Basketball Table Successfully Populated"