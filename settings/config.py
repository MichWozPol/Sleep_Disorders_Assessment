import os
import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sleep_disorders_copy"
)