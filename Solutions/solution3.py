import mysql.connector

transacciones_bansur = 0
monto_bansur = 0
transacciones_clap = 0
monto_clap = 0

conn_bansur = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bansur"
)

conn_clap = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="clap"
)

cursor_bs = conn_bansur.cursor()

cursor_cl = conn_clap.cursor()


cursor_bs.execute("SELECT * FROM transacciones_bansur")
cursor_cl.execute("SELECT * FROM transacciones_clap")

filas_bs = cursor_bs.fetchall()
filas_cl = cursor_cl.fetchall()

for fila in filas_bs:
 
   transacciones_bansur = transacciones_bansur+1
   monto_bansur = monto_bansur + fila[2]

for fila in filas_cl:

   transacciones_clap = transacciones_clap+1
   monto_clap = monto_clap + fila[3]
        

print("--------------------------------")
print(f"Transacciones totales en BanSur:{transacciones_bansur}\nMonto total:{monto_bansur}")
print("--------------------------------")
print(f"Transacciones totales en Clap:{transacciones_clap}\nMonto total:{monto_clap}")
print("--------------------------------")
cursor_bs.close()
conn_bansur.close()
cursor_cl.close()
conn_clap.close()
