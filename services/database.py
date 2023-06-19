import pyodbc 

server = 'LAPTOP-N03QU36Q\MSSQLSERVER01' 
database = 'SQL_DB_1' 
username = 'sa' 
password = '123' 

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()