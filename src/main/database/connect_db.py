import mysql.connector

def create_database(host:str, user:str, password:str, database: str):
    mydb = mysql.connector.connect(
        host=f'{host}',
        user=f'{user}',
        password=f'{password}',
        database=f'{database}'
    )
    return mydb