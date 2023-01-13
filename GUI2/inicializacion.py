import mysql.connector
from mysql.connector import Error
import mariadb
import json
import sys
import socket
from getmac import get_mac_address
import netifaces
import os
import subprocess

try:
    args = sys.argv
    mac = get_mac_address()
    
    id_cliente = args[1]
    nube = args[2]
    
    iface = netifaces.ifaddresses('tun0')[netifaces.AF_INET][0]
    ip = iface["addr"]
    
    connection1 = mysql.connector.connect(host=nube,database='db_trazadomus_dev',user='admin',password='Trazadomus.2022')
    cursor1 = connection1.cursor()
    
    sql = "INSERT INTO medida_clientes_equipos SET ID_cliente="+id_cliente+",ip='"+ip+"',mac='"+mac+"',candado1=1,candado2=1"
    cursor1.execute(sql)
    connection1.commit()
    id_equipo=cursor1.lastrowid
    
    data={"printer":"Zebra-Technologies-ZTC-ZD220-203dpi-ZPL","id_cliente":id_cliente,"id_equipo":id_equipo,"nube":nube}
    
    try:
        with open("/home/trazadomus/GUI/config/init.json", "x") as file:
            json.dump(data, file)
    except:
        with open("/home/trazadomus/GUI/config/init.json", "w") as file:
            json.dump(data, file)
    
    
except Error as e:
    print("Error while connection1 to MySQL", e)
finally:
    completed = subprocess.run(['sh', '/home/trazadomus/launch.sh'])
    

