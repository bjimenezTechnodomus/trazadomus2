import mysql.connector
from mysql.connector import Error
import mariadb
import json

try:
    with open('/home/trazadomus/GUI/config/init.json') as f:
        data = json.load(f)
        f.close()
    nubeHost = data["nube"]
    connection1 = mysql.connector.connect(host=nubeHost,database='db_trazadomus_dev',user='admin',password='Trazadomus.2022')
    id_cliente = data["id_cliente"]  
    id_equipo = data["id_equipo"]  

    cursor1 = connection1.cursor()
    sql = "SELECT * FROM medida_clientes_equipos WHERE ID_equipo="+str(id_equipo)
    cursor1.execute(sql)
    row = cursor1.fetchone()

    candado1=row[6]
    candado2=row[7]
    
    with open("/home/trazadomus/GUI/config/candados.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["candado1"] = candado1
    data["candado2"] = candado2

    with open("/home/trazadomus/GUI/config/candados.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    
except Error as e:
    print("Error while connection1 to MySQL", e)
finally:
    if connection1.is_connected():
        connection1.close()
