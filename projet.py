import streamlit as st
import pandas as pd
import sqlite3
import os
#fonction de connextion et d'execution de requete a la base de donnee
def connect(chemin):
    return sqlite3.connect(chemin)
    
def sql_executor(raw_code,conn):
    c = conn.cursor()
    c.execute(raw_code)
    data=c.fetchall()
    return data 
st.title("SQLITE with streamlit")
chemin=st.text_input("Entrer le chemin de la BD")
if chemin:
    if not os.path.exists(chemin):
        st.error("fichier introuvable")
    else:
        conn=connect(chemin)
        st.success("database connected")
with st.expander("liste des tables"):
    sql_table=("name FROM sqlite_master WHERE type='table';")
    tables =sql_executor(sql_table,conn)
    st.write(tables) 
    
    
