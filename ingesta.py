import pymysql
import pandas as pd
import boto3

# Datos de conexión (puedes cambiar estos datos según tu setup de Docker)
host = "mysql"
user = "admin"
password = "admin123"
database = "testdb"
table = "clientes"

# Conexión a MySQL
conn = pymysql.connect(host=host, user=user, password=password, database=database)
query = f"SELECT * FROM {table};"
df = pd.read_sql(query, conn)
conn.close()

# Guardar en CSV
csv_file = "data.csv"
df.to_csv(csv_file, index=False)

# Subir a S3
nombreBucket = "flanche-storage-s3"
s3 = boto3.client('s3')
s3.upload_file(csv_file, nombreBucket, "ingesta/" + csv_file)

print("Ingesta completada")
