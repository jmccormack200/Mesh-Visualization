#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='password'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()