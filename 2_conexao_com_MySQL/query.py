#!/usr/bin/env python3

import mysql.connector
#pip install mysql-connector-python
import streamlit as st
import pandas as pd

conn = mysql.connector.connect(
host = "localhost",
port = "3306",
user = "root",
password = "54321",
db = "karina_db"
)

c = conn.cursor()



def view_all_data():
    c.execute("SELECT * FROM my_dataframe")
    data = c.fetchall()
    return data



if __name__ == "__main__":
    print(view_all_data())