import mysql.connector
from mysql.connector import Error
import json
from datetime import datetime

try:
    with open('/home/trazadomus/GUI/config/init.json') as f:
        data = json.load(f)
        f.close()
        
    nubeHost  = data["nube"]
    id_equipo = data["id_equipo"]
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    connection1 = mysql.connector.connect(host=nubeHost,database='db_trazadomus_dev',user='admin',password='Trazadomus.2022')
    cursor1 = connection1.cursor()
    sql = "UPDATE medida_clientes_equipos SET ultima_actualizacion='"+dt_string+"',status=1 WHERE ID_equipo="+str(id_equipo)
    cursor1.execute(sql)
    connection1.commit()
except Error as e:
    print("Error while connection1 to MySQL", e)
finally:
    if connection1.is_connected():
        connection1.close()