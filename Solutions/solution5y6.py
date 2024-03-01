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


cursor_bs.execute("SELECT COUNT(*) FROM transacciones_bansur")
cursor_cl.execute("SELECT COUNT(*) FROM transacciones_clap")

cursor_cl_comp.execute("""SELECT COUNT(*)
FROM transacciones_clap
WHERE recibed IS NOT NULL;
""")
cursor_bs_comp.execute("""SELECT COUNT(*)
FROM transacciones_bansur
WHERE recibed IS NOT NULL;
""")

filas_bs = cursor_bs.fetchall()
filas_cl = cursor_cl.fetchall()
filas_bs_comp = cursor_bs_comp.fetchall()
filas_cl_comp = cursor_cl_comp.fetchall()
        
solution5 = (filas_cl_comp*100)/filas_cl
solution6 = ((filas_bs-filas_bs_comp)*100)/filas_bs

print("--------------------------------")
print(f"Transacciones conciliables de CLAP hacia BanSur: {solution5}")
print("--------------------------------")
print(f"Transacciones conciliables de BanSur que no fueron hacia CLAP: {solution6}")
print("--------------------------------")
cursor_bs.close()
conn_bansur.close()
cursor_cl.close()
conn_clap.close()
cursor_bs_comp.close()
cursor_cl_comp.close()