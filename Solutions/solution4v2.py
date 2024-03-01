#ALTER TABLE transacciones_bansur/clap
#ADD id INT AUTO_INCREMENT PRIMARY KEY;
#ADD recibed VARCHAR(15);

import mysql.connector

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
sql = """
    SELECT *
    FROM transacciones_clap
    WHERE id_banco = %s
"""

filas_bs = cursor_bs.fetchall()

for fila_bs in filas_bs:
    print(f"Row {fila_bs[7]}")
    id_clap = fila_bs[5]
    cursor_cl.execute(sql,(id_clap,))
    filas_cl = cursor_cl.fetchall()

    for fila_cl in filas_cl:
       cl_arr = fila_cl[4]
       cl_date = f"{cl_arr.year}-{cl_arr.month}-{cl_arr.day}"
       if fila_bs[5] ==  fila_cl[6] and str(fila_bs[0]).startswith(str(fila_cl[0])) and str(fila_bs[0]).endswith(str(fila_cl[1])) and -1<fila_bs[2]-fila_cl[3]<1 and cl_date[0] == fila_bs[3] and fila_cl[2] == "PAGADA" and fila_bs[1] == "PAGO":
           consulta_bs = "UPDATE transacciones_bansur SET recibed = %s WHERE id = %s"
           values_bs = ("RECIBED",  fila_bs[7])
           consulta_cl = "UPDATE transacciones_clap SET recibed = %s WHERE id = %s"
           values_cl = ("RECIBED",  fila_cl[8])
           cursor_bs.execute(consulta_bs,values_bs)
           cursor_cl.execute(consulta_cl,values_cl)
           
cursor_bs.close()
conn_bansur.close()
cursor_cl.close()
conn_clap.close()
