import mysql.connector
from mysql.connector import Error
import mariadb
import json

def is_connected(connection):
    try:
        connection.ping()
    except:
        return False
    return True

try:
    connection1 = mysql.connector.connect(host='10.0.100.217',database='db_trazadomus_dev',user='admin',password='Trazadomus.2022')
    connection2 = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
    
    with open('/home/trazadomus/GUI/config/init.json') as f:
        data = json.load(f)
        f.close()
    id_cliente = data["id_cliente"]  
    id_equipo = data["id_equipo"]  
    if is_connected(connection2):
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()
        
        sql = "SELECT * FROM dimension_lotes WHERE status_nube=0;"
        cursor2.execute(sql)
        updts = cursor2.fetchall()
        count = cursor2.rowcount
        if count > 0 :
            for r in updts:
                sql = "INSERT INTO bitacora_lotes (id_cliente,id_equipo,id_lote,codigo,id_usuario,id_esterilizador,fecha,indicador,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor1.execute(sql,(id_cliente,id_equipo,r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
                sqlUpdt = "UPDATE dimension_lotes SET status_nube=1 WHERE id_lote="+str(r[0])
                cursor2.execute(sqlUpdt)
                
        sql = "SELECT * FROM medida_paquetes WHERE status_nube=0;"
        cursor2.execute(sql)
        updts = cursor2.fetchall()
        count = cursor2.rowcount
        if count > 0 :
            for r in updts:
                sql = "INSERT INTO bitacora_paquetes (id_cliente,id_equipo,id_paquete,id_kit,id_usuario,codigo,descripcion,fecha,caducidad,indicador,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor1.execute(sql,(id_cliente,id_equipo,r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
                sqlUpdt = "UPDATE medida_paquetes SET status_nube=1 WHERE id_paquete="+str(r[0])
                cursor2.execute(sqlUpdt)
                
        sql = "SELECT * FROM medida_localizacion_paquete WHERE status_nube=0;"
        cursor2.execute(sql)
        updts = cursor2.fetchall()
        count = cursor2.rowcount
        if count > 0 :
            for r in updts:
                sql = "INSERT INTO bitacora_localizacion_paquete (id_cliente,id_equipo,id_registro_local,id_paquete,id_destino,fecha) VALUES(%s,%s,%s,%s,%s,%s);"
                cursor1.execute(sql,(id_cliente,id_equipo,r[0],r[1],r[2],r[3]))
                sqlUpdt = "UPDATE medida_localizacion_paquete SET status_nube=1 WHERE id_registro="+str(r[0])
                cursor2.execute(sqlUpdt)
                
        sql = "SELECT * FROM medida_lotes_contenido WHERE status_nube=0;"
        cursor2.execute(sql)
        updts = cursor2.fetchall()
        count = cursor2.rowcount
        if count > 0 :
            for r in updts:
                sql = "INSERT INTO bitacora_lotes_contenido (id_cliente,id_equipo,id_registro_local,id_lote,id_paquete) VALUES(%s,%s,%s,%s,%s);"
                cursor1.execute(sql,(id_cliente,id_equipo,r[0],r[1],r[2]))
                sqlUpdt = "UPDATE medida_lotes_contenido SET status_nube=1 WHERE id_registro="+str(r[0])
                cursor2.execute(sqlUpdt)
        
except Error as e:
    print("Error while connection1 to MySQL", e)
finally:
    
    if connection1.is_connected():
        connection1.commit()
        connection1.close()
        
    if is_connected(connection2):
        connection2.commit()
        connection2.close()
