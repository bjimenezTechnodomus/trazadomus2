import mysql.connector
from mysql.connector import Error
import mariadb
from getmac import get_mac_address


def is_connected(connection):
    try:
        connection.ping()
    except:
        return False
    return True

try:
    connection1 = mysql.connector.connect(host='10.0.100.217',
                                         database='db_trazadomus_dev',
                                         user='admin',
                                         password='Trazadomus.2022')
    if connection1.is_connected():
        mac = get_mac_address()
        db_Info = connection1.get_server_info()
        cursor = connection1.cursor()
        sql = 'SELECT * FROM medida_clientes_equipos WHERE ID_cliente=1 AND mac="'+mac+'" AND status=0;'
        cursor.execute(sql)
        row = cursor.fetchone()
        count = cursor.rowcount
        if count > 0 :
            cursor.execute("SELECT * FROM medida_clientes_pagina WHERE ID_cliente=1;")
            row = cursor.fetchone()
            pags = []
            while row is not None:
                pags.append(row)
                row = cursor.fetchone()
            for pagina in pags:
                if(pagina[3]==1):
                    sql = "SELECT * FROM medida_clientes_kits WHERE ID_pagina="+str(pagina[0])+";"
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    data = []
                    while row is not None:
                        data.append(row)
                        row = cursor.fetchone()

                    try:
                        connection2 = mariadb.connect(host='localhost',
                                                             database='trazadomus',
                                                             user='equipo',
                                                             password='trazadomus')
                        if is_connected(connection2):
                            connection2.autocommit = True
                            connection1.autocommit = True
                            cursor2 = connection2.cursor()

                            for dato in data:
                                try: 
                                    codigo = str(dato[1])
                                    cursor2.execute("INSERT INTO medida_kits (codigo,descripcion,caducidad) VALUES (?, ?, ?) ON DUPLICATE KEY UPDATE descripcion=?;", (codigo,dato[2],dato[5],dato[2]))
                                except mariadb.Error as e: 
                                    print(f"Error: {e}")
                            try: 
                                sql = "UPDATE medida_clientes_equipos SET status=1 WHERE ID_cliente=1 AND mac='"+mac+"';"
                                cursor.execute(sql)

                            except Error as e: 
                                print(f"Error: {e}")

                    except mariadb.Error as e:
                        print("Error while connection2 to MariaDB", e)
                    finally:
                        if is_connected(connection2):
                            cursor2.close()
                            connection2.close()
                elif(pagina[3]==2):
                    sql = "SELECT * FROM medida_clientes_usrs WHERE ID_pagina="+str(pagina[0])+";"
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    data = []
                    while row is not None:
                        data.append(row)
                        row = cursor.fetchone()

                    try:
                        connection2 = mariadb.connect(host='localhost',
                                                             database='trazadomus',
                                                             user='equipo',
                                                             password='trazadomus')
                        if is_connected(connection2):
                            connection2.autocommit = True
                            connection1.autocommit = True
                            cursor2 = connection2.cursor()

                            for dato in data:
                                try: 
                                    codigo = str(dato[1])
                                    cursor2.execute("INSERT INTO medida_usuarios (codigo,nombre) VALUES (?, ?) ON DUPLICATE KEY UPDATE nombre=?;", (codigo,dato[2],dato[2]))
                                except mariadb.Error as e: 
                                    print(f"Error: {e}")
                            try: 
                                sql = "UPDATE medida_clientes_equipos SET status=1 WHERE ID_cliente=1 AND mac='"+mac+"';"
                                cursor.execute(sql)

                            except Error as e: 
                                print(f"Error: {e}")

                    except mariadb.Error as e:
                        print("Error while connection2 to MariaDB", e)
                    finally:
                        if is_connected(connection2):
                            cursor2.close()
                            connection2.close()
                elif(pagina[3]==3):
                    sql = "SELECT * FROM medida_clientes_esterilizadores WHERE ID_pagina="+str(pagina[0])+";"
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    data = []
                    while row is not None:
                        data.append(row)
                        row = cursor.fetchone()

                    try:
                        connection2 = mariadb.connect(host='localhost',
                                                             database='trazadomus',
                                                             user='equipo',
                                                             password='trazadomus')
                        if is_connected(connection2):
                            connection2.autocommit = True
                            connection1.autocommit = True
                            cursor2 = connection2.cursor()

                            for dato in data:
                                try: 
                                    codigo = str(dato[1])
                                    cursor2.execute("INSERT INTO medida_esterilizadores (codigo,descripcion) VALUES (?, ?) ON DUPLICATE KEY UPDATE descripcion=?;", (codigo,dato[2],dato[2]))
                                except mariadb.Error as e: 
                                    print(f"Error: {e}")
                            try: 
                                sql = "UPDATE medida_clientes_equipos SET status=1 WHERE ID_cliente=1 AND mac='"+mac+"';"
                                cursor.execute(sql)

                            except Error as e: 
                                print(f"Error: {e}")

                    except mariadb.Error as e:
                        print("Error while connection2 to MariaDB", e)
                    finally:
                        if is_connected(connection2):
                            cursor2.close()
                            connection2.close()
                elif(pagina[3]==4):
                    sql = "SELECT * FROM medida_clientes_destinos WHERE ID_pagina="+str(pagina[0])+";"
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    data = []
                    while row is not None:
                        data.append(row)
                        row = cursor.fetchone()

                    try:
                        connection2 = mariadb.connect(host='localhost',
                                                             database='trazadomus',
                                                             user='equipo',
                                                             password='trazadomus')
                        if is_connected(connection2):
                            connection2.autocommit = True
                            connection1.autocommit = True
                            cursor2 = connection2.cursor()

                            for dato in data:
                                try: 
                                    codigo = str(dato[1])
                                    cursor2.execute("INSERT INTO medida_destinos (codigo,descripcion) VALUES (?, ?) ON DUPLICATE KEY UPDATE descripcion=?;", (codigo,dato[2],dato[2]))
                                except mariadb.Error as e: 
                                    print(f"Error: {e}")
                            try: 
                                sql = "UPDATE medida_clientes_equipos SET status=1 WHERE ID_cliente=1 AND mac='"+mac+"';"
                                cursor.execute(sql)

                            except Error as e: 
                                print(f"Error: {e}")

                    except mariadb.Error as e:
                        print("Error while connection2 to MariaDB", e)
                    finally:
                        if is_connected(connection2):
                            cursor2.close()
                            connection2.close()
        
except Error as e:
    print("Error while connection1 to MySQL", e)
finally:
    if connection1.is_connected():
        cursor.close()
        connection1.close()        