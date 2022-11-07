import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from datetime import date
import calendar
import datetime
import re
import mariadb
from dateutil.relativedelta import relativedelta
import subprocess
import json



class home_window:
    
    def __init__(self):
        
        with open('config/init.json') as f:
            data = json.load(f)
            f.close()
        self.printer = data["printer"]    
        print(self.printer)
        self.kitCode = ""
        self.userCode = ""
        self.esteriCode = ""
        self.loteCode = ""
        self.paqueteCode = ""
        self.destinoCode = ""
        self.date = ""
        self.caducidad = ""
        self.currentPage = 0
        self.currentUser = ""
        self.nextLote = ""
        self.id_kit = ""
        self.kit_nombre = ""
        self.id_user = ""
        self.id_paquete = ""
        self.id_esteri = ""
        self.nextPaquete = ""
        self.loteList = []
        self.loteListNames = []
        self.loteContador = 0
        
        self.home_screen = Tk()
        self.home_screen.title('GUI')
        self.home_screen.geometry('1280x720')
        self.home_screen.config(bg='#155696')
        self.home_screen.resizable(False, False)

        self.entry_box = Entry(self.home_screen, font=("Helvetica", 12), width=25)
        self.entry_box.focus_set()
        self.entry_box.place(x=1280, y=800)

        self.home_screen.bind("<Return>", self.change_screen)
        
        self.kit_text = StringVar()
        self.alert_text = StringVar()
        self.lote_text = StringVar()
        self.fecha_text = StringVar()
        self.fecha_corta_text = StringVar()
        self.pack_text = StringVar()
        self.caducidad_text = StringVar()
        self.caducidad_corta_text = StringVar()
        self.user_text = StringVar()
        self.id_text = StringVar()
        self.esteri_text = StringVar()
        self.content_text = StringVar()
        self.destino_text = StringVar()
        self.main_window(closing_window_name=None)
        
        # self.ws.attributes('-fullscreen', True)
    def clearVars(self):
        self.id_paquete = ""
        self.id_esteri = ""
        self.nextPaquete = ""
        self.loteList = []
        self.loteContador = 0
        self.kitCode = ""
        self.esteriCode = ""
        self.loteCode = ""
        self.paqueteCode = ""
        self.destinoCode = ""
        self.date = ""
        self.caducidad = ""
        self.nextLote = ""
        self.id_kit = ""
        self.kit_nombre = ""
        self.alert_text.set("")
        self.esteri_text.set("")
        
    def is_connected(self,connection):
        try:
            connection.ping()
        except:
            return False
        return True

    
    def main_window(self, closing_window_name):
        try:
            closing_window_name.destroy()
        except:
            pass

        self.main_widnow_frame = Frame(master=self.home_screen, width=1280, height=720,bg='#155696')
        self.main_widnow_frame.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.main_widnow_frame, image=img, background="#155696",borderwidth = 0)
        img_button.pack(pady=(50,0))

        Trazadomus_label = Label(self.main_widnow_frame, text='Trazadomus', background="#155696", fg='white',font=("Helvetica", 25, 'bold'))
        Trazadomus_label.pack(pady=(5,0))

        scan_img = ImageTk.PhotoImage(Image.open("images/scan 1.png"))
        scan_img_button = Label(self.main_widnow_frame, image=scan_img, background="#155696",borderwidth = 0)
        scan_img_button.pack(pady=(130,0))

        scaner_label = Label(self.main_widnow_frame, text='Escanea tu QR de usuario', background="#155696", fg='white',font=("Helvetica", 25, 'bold'))
        scaner_label.pack(pady=(5, 0))

        # Label(main_widnow_frame, image=img).pack()

        self.main_widnow_frame.mainloop()

        self.home_screen.mainloop()
    
    
    def printLabel(self):
        if self.kitCode != "":
            self.alert_text.set("")
            try:
                connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                connection.autocommit = True
                cursor = connection.cursor()
                print(self.kitCode)
                sql = "SELECT * FROM medida_kits WHERE codigo="+self.kitCode
                cursor.execute(sql)
                row = cursor.fetchone()
                e = datetime.datetime.now()
                today=e.strftime("%Y-%m-%d %H:%M")
                todayCorto=e.strftime("%d-%m-%Y")
                cadu = e + relativedelta(months=+row[3])
                caducidadCorta = cadu.strftime("%d-%m-%Y")
                caducidad = cadu.strftime("%d-%m-%Y %H:%M")
                sql = "INSERT INTO medida_paquetes (id_kit,id_usuario,codigo,descripcion,fecha,caducidad,indicador,status) VALUES(?,?,?,?,?,?,?,?)"
                cursor.execute(sql,(self.id_kit,self.id_user,self.nextPaquete,self.kit_nombre,today,self.caducidad,0,0))
            except mariadb.Error as e:
                print("Error while connection2 to MariaDB", e)
            finally:
                if self.is_connected(connection):
                    idPack = self.nextPaquete[4::]
                    sql = "INSERT INTO medida_localizacion_paquete (id_paquete,id_destino,fecha) VALUES(?,?,?)"
                    cursor.execute(sql,(idPack,0,today))
                    cursor.close()
                    connection.close()
                self.alert_text.set("Paquete creado")
                self.entry_1.config(highlightbackground = "gray", highlightcolor= "gray")
                #GENERAR ARCHIVO ZPL O EPL E IMPRIMIR
                x = self.kit_nombre.split(" ")
                kitStrM = ""
                kitStrC = ""
                for i in range(0,len(x)):
                    if i < (len(x)/2):
                        kitStrM += x[i]+" "
                    else:
                        kitStrC += x[i]+" "
                
                content = "^XA^CFE,22^FO30,40^FDTrazadomus^FS^CFA,22^FO30,65^BQN,2,5,H^FDQA,"+self.nextPaquete+"^FS^FO150,75^FDKit de Cirugia Menor^FS^FO150,100^FDUsuario: "+self.currentUser+"^FS^FO150,125^FDFecha: "+todayCorto+"^FS^FO150,150^FDCaducidad:"+caducidadCorta+"^FS^FO150,175^FDID: "+self.nextPaquete+"^FS^FO30,300^BQN,2,5,H^FDQA,"+self.nextPaquete+"^FS^CFA,22^FO150,310^FD"+kitStrM+"^FS^FO150,335^FD"+kitStrC+"^FS^FO150,360^FDFecha: "+todayCorto+"^FS^FO150,385^FDCaducidad:^FS^FO150,410^FD"+caducidadCorta+"^FS^CFA,22^FO445,300^BQN,2,5,H^FDQA,"+self.nextPaquete+"^FS^FO565,310^FD"+kitStrM+"^FS^FO565,335^FD"+kitStrC+"^FS^FO565,360^FDFecha: "+todayCorto+"^FS^FO565,385^FDCaducidad:^FS^FO565,410^FD"+caducidadCorta+"^FS^CFE,22^XZ";
                
                filename = "labelGen.zpl"
                f = open(filename, 'w')
                f.write(content)
                f.close()
                p = subprocess.run(["lp", "-d", self.printer,"-o","raw","labelGen.zpl"])

                self.checkPaquete()
        else:
            self.alert_text.set("Favor de escanear un QR de kit!")
            
            
    def getLabelDatos(self,code):
        try:
            self.alert_text.set("")
            connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
            connection.autocommit = True
            cursor = connection.cursor()
            sql = "SELECT * FROM medida_kits WHERE codigo="+code
            cursor.execute(sql)
            row = cursor.fetchone()
            e = datetime.datetime.now()
            today=e.strftime("%d-%m-%Y %H:%M")
            todayCorto=e.strftime("%d-%m-%Y")
            self.id_kit = str(row[0])
            self.kit_nombre = str(row[2])
            caducidad = str(e + relativedelta(months=+row[3]))
            cadu = e + relativedelta(months=+row[3])
            caducidadCorta = cadu.strftime("%d-%m-%Y")
            self.kit_text.set(row[2])
            #self.lote_text.set("")
            self.date = today
            self.caducidad = caducidad
            self.fecha_text.set("Fecha:"+today)
            self.fecha_corta_text.set("Fecha:"+todayCorto)
            self.caducidad_text.set("Caducidad:"+caducidad)
            self.caducidad_corta_text.set("Caducidad:"+caducidadCorta)
            self.user_text.set(self.currentUser)
            self.id_text.set("ID:"+self.nextPaquete)
            self.entry_1.config(highlightbackground = "green", highlightcolor= "green")
            
        except mariadb.Error as e:
            print("Error while connection2 to MariaDB", e)
        finally:
            if self.is_connected(connection):
                cursor.close()
                connection.close()
    
    
    def checkLote(self):
        try:
            connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
            cursor = connection.cursor()
            sql = "SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'dimension_lotes' AND table_schema = 'trazadomus';"
            cursor.execute(sql)
            row = cursor.fetchone()
            
            self.nextLote = "1105"+str(row[0])
            self.lote_text.set(self.nextLote)
            
        except mariadb.Error as e:
            print("Error while connection to MariaDB", e)
        finally:
            if self.is_connected(connection):
                cursor.close()
                connection.close()
                
                
    def checkPaquete(self):
        try:
            connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
            cursor = connection.cursor()
            sql = "SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'medida_paquetes' AND table_schema = 'trazadomus';"
            cursor.execute(sql)
            row = cursor.fetchone()
            self.nextPaquete = "1104"+str(row[0])
            self.kit_text.set("Kit")
            self.fecha_text.set("Fecha:")
            self.caducidad_text.set("Caducidad:")
            self.user_text.set(self.currentUser)
            self.id_text.set("ID:"+self.nextPaquete)
            self.lote_text.set(self.nextLote)
            
        except mariadb.Error as e:
            print("Error while connection to MariaDB", e)
        finally:
            if self.is_connected(connection):
                cursor.close()
                connection.close()
                
    
    def indicadorPaquete(self,ind):
        if self.paqueteCode != "":
            try:
                connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                connection.autocommit = True
                cursor = connection.cursor()
                sql = "UPDATE medida_paquetes SET indicador=? WHERE codigo=?"
                cursor.execute(sql,(ind,self.paqueteCode))
                self.alert_text.set("Indicador de paquete registrado")
            except mariadb.Error as e:
                print("Error while connection to MariaDB", e)
            finally:
                self.pack_text.set("")
                
                if self.is_connected(connection):
                    cursor.close()
                    connection.close()
                    
    def destinoPaquete(self):
        if self.paqueteCode != "":
            try:
                connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                connection.autocommit = True
                cursor = connection.cursor()
                e = datetime.datetime.now()
                today=e.strftime("%Y-%m-%d %H:%M")
                sql = "SELECT * FROM medida_destinos WHERE codigo="+self.destinoCode
                cursor.execute(sql)
                row = cursor.fetchone()
                idPack = self.paqueteCode[4::]
                if row is not None:
                    destinoID = row[0]
                    sql = "INSERT INTO medida_localizacion_paquete (id_paquete,id_destino,fecha) VALUES(?,?,?)"
                    cursor.execute(sql,(idPack,destinoID,today))
                    self.alert_text.set("Nuevo destino de paquete registrado")
            except mariadb.Error as e:
                print("Error while connection to MariaDB", e)
            finally:
                self.pack_text.set("")
                if self.is_connected(connection):
                    cursor.close()
                    connection.close()
                    
    def crearLote(self):
        loteID = self.nextLote[4::]
        try:
            connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
            connection.autocommit = True
            cursor = connection.cursor()
            e = datetime.datetime.now()
            today=e.strftime("%Y-%m-%d %H:%M")
            sql = "INSERT INTO dimension_lotes (codigo,id_usuario,id_esterilizador,fecha,indicador,status) VALUES(?,?,?,?,?,?)"
            cursor.execute(sql,(self.nextLote,self.id_user,self.id_esteri,today,0,0))
        except mariadb.Error as e:
            print("Error while connection2 to MariaDB", e)
        finally:
            
            if self.is_connected(connection):
                for pack in self.loteList:
                    sql = "INSERT INTO medida_lotes_contenido (id_lote,id_paquete) VALUES(?,?)"
                    cursor.execute(sql,(loteID,pack))
                    sql = "UPDATE medida_paquetes SET status=? WHERE id_paquete=?"
                    cursor.execute(sql,(1,pack))
                self.alert_text.set("Lote creado")
                cursor.close()
                connection.close()
        #IMPRIMIR ETIQUETA CON QR DE ID DE LOTE
            content = "^XA^CFE,22^FO30,40^FDTrazadomus^FS^CFA,22^FO30,65^BQN,2,5,H^FDQA,1105"+str(loteID)+"^FS^FO150,75^FDLote: "+str(loteID)+"^FS^FO150,100^FDUsuario:"+self.currentUser+"^FS^FO150,125^FDFecha: "+today+"^FS^FO150,150^FDEsterilizador: "+self.currentEsteri+"^FS^XZ";
            filename = "labelGenLote.zpl"
            f = open(filename, 'w')
            f.write(content)
            f.close()
            p = subprocess.run(["lp", "-d", self.printer,"-o","raw","labelGenLote.zpl"])
            
    def indicadorLote(self,ind):
        if self.loteCode != "":
            try:
                connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                connection.autocommit = True
                cursor = connection.cursor()
                sql = "UPDATE dimension_lotes SET indicador=? WHERE codigo=?"
                cursor.execute(sql,(ind,self.loteCode))
                self.alert_text.set("Indicador de lote registrado")
            except mariadb.Error as e:
                print("Error while connection2 to MariaDB", e)
            finally:
                if self.is_connected(connection):
                    cursor.close()
                    connection.close()
                    
        
    def checkPaqueteLote(self):
        if self.paqueteCode != "":
            try:
                connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                cursor = connection.cursor()
                sql = "SELECT * FROM medida_paquetes WHERE codigo="+self.paqueteCode
                cursor.execute(sql)
                row = cursor.fetchone()
                if row is not None:
                    status = str(row[8])
                    if status == "1":
                        return True
                    else:
                        return False
            except mariadb.Error as e:
                print("Error while connection to MariaDB", e)
            finally:
                if self.is_connected(connection):
                    cursor.close()
                    connection.close()
    
    def checkPaqueteIndicador(self):
        if self.paqueteCode != "":
            try:
                connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                cursor = connection.cursor()
                sql = "SELECT * FROM medida_paquetes WHERE codigo="+self.paqueteCode
                cursor.execute(sql)
                row = cursor.fetchone()
                if row is not None:
                    status = str(row[7])
                    if status == "1":
                        return True
                    else:
                        return False
            except mariadb.Error as e:
                print("Error while connection to MariaDB", e)
            finally:
                if self.is_connected(connection):
                    cursor.close()
                    connection.close()
                    
                    
    def almacenPaquete(self):
        loteCheck=self.checkPaqueteLote()
        indicadorCheck=self.checkPaqueteIndicador()
        if self.paqueteCode != "":
            if loteCheck:
                if indicadorCheck:
                    try:
                        connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                        connection.autocommit = True
                        cursor = connection.cursor()
                        sql = "UPDATE medida_paquetes SET status=? WHERE codigo=?"
                        cursor.execute(sql,(2,self.paqueteCode))
                        idPack = self.paqueteCode[4::]
                        e = datetime.datetime.now()
                        today=e.strftime("%Y-%m-%d %H:%M")
                        sql = "INSERT INTO medida_localizacion_paquete (id_paquete,id_destino,fecha) VALUES(?,?,?)"
                        cursor.execute(sql,(idPack,1,today))
                        self.alert_text.set("Paquete registrado en almacen")
                    except mariadb.Error as e:
                        print("Error while connection to MariaDB", e)
                    finally:
                        self.pack_text.set("")
                        if self.is_connected(connection):
                            cursor.close()
                            connection.close()
                else:
                    self.alert_text.set("Indicador no verificado")
            else:
                self.alert_text.set("Paquete no pertenece a un lote")
        else:
            self.alert_text.set("Escanea un codigo de paquete")
            
    def procesarLote(self):
        if self.loteCode != "":
            try:
                connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                connection.autocommit = True
                cursor = connection.cursor()
                sql = "UPDATE dimension_lotes SET status=? WHERE codigo=?"
                cursor.execute(sql,(1,self.loteCode))
                self.alert_text.set("Lote procesado")
            except mariadb.Error as e:
                print("Error while connection2 to MariaDB", e)
            finally:
                if self.is_connected(connection):
                    cursor.close()
                    connection.close()
                
                
                
    def change_screen(self,event):
        code = self.entry_box.get()
        pre = code[0]+code[1]
            
        if pre == '10':
            pares = re.findall('..',code)
            nivel = len(pares)
            
            if pares[1] == "01":
            #1001
                if nivel > 2:
                    if pares[2] == "01":
                        #Regresar en empaquetado
                        self.entry_box.delete(0, END)
                        self.currentPage = 1
                        self.clearVars()
                        self.home_window_2(self.Empaquetado_screen)
                    elif pares[2] == "02":
                        #Imprimir en empaquetado
                        self.entry_box.delete(0, END)
                        self.printLabel()
                        
                else:
                    self.entry_box.delete(0, END)
                    self.currentPage = 2
                    self.checkPaquete()
                    self.Empaquetado_window(self.home_screen_2)
            elif pares[1] == "02":
            #1002
                if nivel > 2:
                    if pares[2] == "01":
                        #Regresar en crear lote
                        self.entry_box.delete(0, END)
                        self.currentPage = 1
                        self.loteContador = 0
                        self.loteList = []
                        self.entry_3.delete("1.0", "end")
                        self.clearVars()
                        self.home_window_2(self.Crear_lote_screen)
                    elif pares[2] == "02":
                        #Crear lote
                        print("CREAR LOTE")
                        
                        self.crearLote()
                        self.entry_box.delete(0, END)
                        self.currentPage = 0
                        self.loteContador = 0
                        self.loteList = []
                        self.entry_3.delete("1.0", "end")
                        self.clearVars()
                        
                        self.main_window(self.Crear_lote_screen)
                else:
                    self.entry_box.delete(0, END)
                    self.currentPage = 3
                    e = datetime.datetime.now()
                    today=e.strftime("%d-%m-%Y %H:%M")
                    self.fecha_text.set(today)
                    self.checkLote()
                    self.Crear_lote_window(self.home_screen_2)
            elif pares[1] == "03":
            #1003
                if nivel > 2:
                    if pares[2] == "01":
                        #100301
                        #Regresar en actualizar
                        self.entry_box.delete(0, END)
                        self.currentPage = 1
                        self.clearVars()
                        self.home_window_2(self.actualizar_lote_paquete_screen)
                    elif pares[2] == "02":
                        #100302
                        if nivel > 3:
                            if pares[3] == "01":
                                #10030201
                                self.entry_box.delete(0, END)
                                self.currentPage = 4
                                self.actualizar_lote_paquete_window(self.actualizar_lote_screen)
                            elif pares[3] == "02":
                                #10030202
                                if nivel > 4:
                                    if pares[4] == "01":
                                        #1003020201
                                        self.currentPage = 5
                                        #Regresar en actualizar lote procesado
                                        self.lote_text.set("")
                                        self.entry_box.delete(0, END)
                                        self.clearVars()
                                        self.actualizar_lote_window(self.Actualizar_lote_2_screen)
                                    elif pares[4] == "02":
                                        #1003020202
                                        self.currentPage = 9
                                        #Confirmar lote procesado
                                        print("CONFIRMAR LOTE PROCESADO")
                                        self.procesarLote()
                                        self.lote_text.set("")
                                        self.entry_box.delete(0, END)
                                        self.clearVars()
                                        self.Actualizar_paquete_2_window(self.Actualizar_lote_2_screen)
                                else:
                                    self.entry_box.delete(0, END)
                                    self.currentPage = 6
                                    self.Actualizar_lote_2_window(self.actualizar_lote_screen)
                            elif pares[3] == "03":
                                #10030203
                                if nivel > 4:
                                    if pares[4] == "01":
                                        #1003020301
                                        #Regresar en actualizar lote indicador
                                        self.entry_box.delete(0, END)
                                        self.currentPage = 5
                                        self.clearVars()
                                        self.actualizar_lote_window(self.Actualizar_lote_3_screen)
                                    elif pares[4] == "02":
                                        #1003020302
                                        #Actualizar lote indicador fallido
                                        print("LOTE INDICADOR FALLIDO")
                                        self.indicadorLote(2)
                                        self.lote_text.set("")
                                        self.currentPage = 0
                                        self.entry_box.delete(0, END)
                                        self.main_window(self.Actualizar_lote_3_screen)
                                    elif pares[4] == "03":
                                        #1003020303
                                        #Actualizar lote indicador verificado
                                        print("LOTE INDICADOR VERIFICADO")
                                        self.currentPage = 0
                                        self.indicadorLote(1)
                                        self.lote_text.set("")
                                        self.entry_box.delete(0, END)
                                        self.main_window(self.Actualizar_lote_3_screen)
                                else:
                                    self.entry_box.delete(0, END)
                                    self.currentPage = 7
                                    self.Actualizar_lote_3_window(self.actualizar_lote_screen)
                        else:
                            #Entrar a actualizar lote
                            self.entry_box.delete(0, END)
                            self.currentPage = 5
                            self.actualizar_lote_window(self.actualizar_lote_paquete_screen)
                    elif pares[2] == "03":
                        #100303
                        if nivel > 3:
                            if pares[3] == "01":
                                #10030301
                                #Regresar en actualizar paquete
                                self.entry_box.delete(0, END)
                                self.currentPage = 4
                                self.clearVars()
                                self.actualizar_lote_paquete_window(self.actualizar_paquete_screen)
                            elif pares[3] == "02":
                                #10030302
                                #Actualizar paquete indicador
                                if nivel > 4:
                                    if pares[4] == "01":
                                        #1003030201
                                        #Regresar en actualizar paquete indicador
                                        self.currentPage = 8
                                        self.entry_box.delete(0, END)
                                        self.pack_text.set("")
                                        self.clearVars()
                                        self.actualizar_paquete_window(self.Actualizar_paquete_2_screen)
                                    elif pares[4] == "02":
                                        #1003030202
                                        #Actualizar paquete indicador fallido
                                        self.entry_box.delete(0, END)
                                        self.indicadorPaquete(2)
                                        print("PAQUETE INDICADOR FALLIDO")
                                        self.pack_text.set("")
                                    elif pares[4] == "03":
                                        #1003030203
                                        self.indicadorPaquete(1)
                                        print("PAQUETE INDICADOR VERIFICADO")
                                        self.pack_text.set("")
                                        self.entry_box.delete(0, END)
                                        #Actualizar paquete indicador verificado
                                    elif pares[4] == "04":
                                        #1003030204
                                        #Terminar indicadores
                                        self.entry_box.delete(0, END)
                                        self.currentPage = 0
                                        self.pack_text.set("")
                                        self.clearVars()
                                        self.main_window(self.Actualizar_paquete_2_screen)
                                else:
                                    self.entry_box.delete(0, END)
                                    self.currentPage = 9
                                    self.Actualizar_paquete_2_window(self.actualizar_paquete_screen)
                            elif pares[3] == "03":
                                #10030303
                                #Actualizar paquete almacen
                                if nivel > 4:
                                    if pares[4] == "01":
                                        #1003030301
                                        #Regresar en actualizar paquete almacen
                                        self.entry_box.delete(0, END)
                                        self.currentPage = 8
                                        self.pack_text.set("")
                                        self.clearVars()
                                        self.actualizar_paquete_window(self.Actualizar_paquete_3_screen)
                                    elif pares[4] == "02":
                                        #1003030302
                                        #Actualizar paquete entrada almacen
                                        self.entry_box.delete(0, END)
                                        self.almacenPaquete()
                                        print("PAQUETE ENTRA A ALMACEN")
                                    elif pares[4] == "03":
                                        #1003030303
                                        self.entry_box.delete(0, END)
                                        self.currentPage = 0
                                        self.pack_text.set("")
                                        self.clearVars()
                                        self.main_window(self.Actualizar_paquete_3_screen)
                                        #Terminar entrada a almacen paquetes
                                else:
                                    self.entry_box.delete(0, END)
                                    self.currentPage = 10
                                    self.Actualizar_paquete_3_window(self.actualizar_paquete_screen)
                            elif pares[3] == "04":
                                #10030304
                                #Actualizar paquete destino
                                if nivel > 4:
                                    if pares[4] == "01":
                                        #1003030301
                                        #Regresar en actualizar paquete destino
                                        self.entry_box.delete(0, END)
                                        self.currentPage = 8
                                        self.destino_text.set("")
                                        self.clearVars()
                                        self.actualizar_paquete_window(self.Actualizar_paquete_4_screen)
                                    elif pares[4] == "02":
                                        #1003030302
                                        #Actualizar paquete CONFIRMA DESTINO
                                        print("PAQUETE CAMBIA DESTINO")
                                        self.entry_box.delete(0, END)
                                        self.destinoPaquete()
                                        self.destino_text.set("")
                                        self.currentPage = 0
                                        self.main_window(self.Actualizar_paquete_4_screen)
                                else:
                                    self.entry_box.delete(0, END)
                                    self.currentPage = 11
                                    self.Actualizar_paquete_4_window(self.actualizar_paquete_screen)
                        else:
                            #Entrar a actualizar paquete
                            self.entry_box.delete(0, END)
                            self.currentPage = 8
                            self.actualizar_paquete_window(self.actualizar_lote_paquete_screen)
                else:
                    self.entry_box.delete(0, END)
                    self.currentPage = 4
                    self.actualizar_lote_paquete_window(self.home_screen_2)
        elif pre == "11":
            tipo = code[2]+code[3]
            length = len(code)
            i = 4
            resto = ""
            pagina = str(self.currentPage)
            print(pagina)
            print(code)
            while i<length:
                resto+=code[i]
                i=i+1
                
            if tipo == "01":
                #KIT
                self.kitCode=code
                if pagina == "2":
                    # Empaquetado
                    self.entry_box.delete(0, END)
                    self.getLabelDatos(self.kitCode)
            elif tipo == "02":
                #USUARIO
                try:
                    connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                    connection.autocommit = True
                    cursor = connection.cursor()
                    sql = "SELECT * FROM medida_usuarios WHERE codigo="+code
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    if row is not None:
                        self.currentUser = row[2]
                        self.user_text.set(row[2])
                        self.userCode = code
                        self.id_user = str(row[0])
                        pagina = str(self.currentPage)
                        if pagina == "0":
                            self.entry_box.delete(0, END)
                            self.home_window_2(self.main_widnow_frame)
                except mariadb.Error as e:
                    print("Error while connection to MariaDB", e)
                finally:
                    if self.is_connected(connection):
                        cursor.close()
                        connection.close()
                
            elif tipo == "03":
                #ESTERILIZADOR
                try:
                    connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                    connection.autocommit = True
                    cursor = connection.cursor()
                    sql = "SELECT * FROM medida_esterilizadores WHERE codigo="+code
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    if row is not None:
                        self.currentEsteri = row[2]
                        self.esteri_text.set(row[2])
                        self.esteriCode = code
                        self.id_esteri = str(row[0])
                except mariadb.Error as e:
                    print("Error while connection to MariaDB", e)
                finally:
                    if self.is_connected(connection):
                        cursor.close()
                        connection.close()
                    
            elif tipo == "04":
                #PAQUETE
                self.paqueteCode=code
                if pagina == "3":
                    try:
                        connection = mariadb.connect(host='localhost',database='trazadomus',user='equipo',password='trazadomus')
                        connection.autocommit = True
                        cursor = connection.cursor()
                        sql = "SELECT * FROM medida_paquetes WHERE codigo="+code+" AND status=0"
                        cursor.execute(sql)
                        row = cursor.fetchone()
                        if row is not None:
                            existe = self.loteList.count(row[0])
                            if existe>0:
                                print(row[0])
                                print(self.loteList)
                                self.alert_text.set("Paquete eliminado")
                                idxR = self.loteList.index(row[0])
                                print(idxR)
                                self.loteList.pop(idxR)
                                self.loteListNames.pop(idxR)
                                print(self.loteList)
                                self.loteContador -= 1
                                self.entry_3.delete("1.0", END)
                                for x in range(0,len(self.loteList)):
                                    self.entry_3.insert(str(x+1)+".0", self.loteListNames[x]+"\n")
                                #self.loteList.remove(row[0])
                                #idx = str(self.loteListIdxs[idxR])+".0"
                                #self.entry_3.delete(idx,str(self.loteListIdxs[idxR])+'.end')
                            else:
                                self.alert_text.set("")
                                self.loteList.append(row[0])
                                self.loteListNames.append(row[4])
                                self.loteContador += 1
                                idx = str(self.loteContador)+".0"
                                self.entry_3.insert(idx, row[4]+"\n")
                        else:
                            self.alert_text.set("Favor de escanear un paquete sin lote.")

                    except mariadb.Error as e:
                        print("Error while connection to MariaDB", e)
                    finally:
                        if self.is_connected(connection):
                            cursor.close()
                            connection.close()
                if pagina == "9" or pagina == "10" or pagina == "11":
                    self.pack_text.set(code)
                
            elif tipo == "05":
                #LOTE
                self.loteCode=code
                if pagina == "6" or pagina == "7" :
                    self.lote_text.set(code)
                    
            elif tipo == "06":
                #DESTINO
                self.destinoCode=code
                if pagina == "11" :
                    self.destino_text.set(code)
                    
            

        self.entry_box.delete(0, END)

        
    def home_window_2(self, closing_window_name):
        # main_widnow_frame
        try:
            closing_window_name.destroy()
        except:
            pass
        # self.main_widnow_frame.destroy()
        # self.home_screen.destroy()
        self.home_screen_2 = Frame(self.home_screen, height=720, width=1280, bg='#155696', relief='raised')
        self.home_screen_2.pack()
        self.home_screen_2.pack_propagate(0)

        # self.home_screen_2.title('GUI')
        # self.home_screen_2.geometry('1280x720')
        # self.home_screen_2.config(bg='#155696')
        # self.home_screen_2.resizable(False, False)
        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.home_screen_2, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        img2 = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img = PhotoImage(file="background image.png")

        img_button = Label(self.home_screen_2, image=img2, background="#155696",borderwidth = 0)
        img_button.pack(pady=(50,0))

        Trazadomus_label = Label(self.home_screen_2, text='Trazadomus', background="#155696", fg='white',font=("Helvetica", 25, 'bold'))
        Trazadomus_label.pack(pady=(5,0))

        # scan_img = ImageTk.PhotoImage(Image.open("images/scan 1.png"))
        # scan_img_button = Label(self.home_screen_2, image=scan_img, background="#155696",borderwidth = 0)
        # scan_img_button.pack(pady=(130,0))
        #
        # scaner_label = Label(self.home_screen_2, text='Escanea tu QR de usuario', background="#155696", fg='white',
        #                          font=("Helvetica", 25, 'bold'))
        # scaner_label.pack(pady=(5, 0))

        # Label(self.home_screen_2, image=img).pack()

        self.user_label = Label(self.home_screen_2, text='Usuario:', background="#155696", fg='white',font=("Helvetica", 25, 'bold'))
        self.user_label.place(x=460,y=250)

        self.username = Label(self.home_screen_2, textvariable=self.user_text, background="#155696", fg='white',font=("Helvetica", 25))
        self.username.place(x=612,y=250)


        Empaquetado = ImageTk.PhotoImage(Image.open("updated QR codes with labels/Empaquetado.png"))
        Empaquetado_button = Label(self.home_screen_2, image=Empaquetado, background="#155696", borderwidth=0)
        Empaquetado_button.place(x=180,y=340)

        crear_lote = ImageTk.PhotoImage(Image.open("updated QR codes with labels/crear lote.png"))
        crear_lote_button = Label(self.home_screen_2, image=crear_lote, background="#155696", borderwidth=0)
        crear_lote_button.place(x=530,y=340)

        actualizar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/actualizar.png"))
        actualizar_button = Label(self.home_screen_2, image=actualizar, background="#155696", borderwidth=0)
        actualizar_button.place(x=880,y=340)


        # self.entry_box = Entry(self.home_screen_2, font=("Helvetica", 12), width=25)
        # self.entry_box.place(x=0, y=0)
        # self.entry_box.focus_set()
        # self.home_screen_2.focus_set()

        # def change_screen(event):
        #
        # self.home_screen_2.bind("<Return>", change_screen)

        self.home_screen_2.mainloop()

    def Empaquetado_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.Empaquetado_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.Empaquetado_screen.pack()
        self.Empaquetado_screen.pack_propagate(0)

        # self.Empaquetado_screen.title('GUI')
        # self.Empaquetado_screen.geometry('1280x720')
        # self.Empaquetado_screen.config(bg='#D6D6D6')
        # self.Empaquetado_screen.resizable(False, False)
        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.Empaquetado_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.Empaquetado_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.Empaquetado_screen, image=img, background="#155696", borderwidth=0)
        img_button.place(x=50, y=25)

        Trazadomus_label = Label(self.Empaquetado_screen, text='Trazadomus', background="#155696", fg='white',
                                 font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160, y=55)

        Empaquetado_label = Label(self.Empaquetado_screen, text='Empaquetado', background="#155696", fg='white',
                                  font=("Helvetica", 25))
        Empaquetado_label.place(x=540, y=55)

        Empaquetar_label = Label(self.Empaquetado_screen, text='Empaquetar', background="#D6D6D6", fg='black',
                                 font=("Helvetica", 25))
        Empaquetar_label.place(x=80, y=200)
        
        label_2 = Label(self.Empaquetado_screen, text='Escanea el QR del kit empaquetado:', background="#D6D6D6",
                        fg='black', font=("Helvetica", 17))
        label_2.place(x=80, y=260)
        
        
        self.entry_1 = Entry(self.Empaquetado_screen, width=35, highlightthickness=2, textvariable=self.id_text, font=("Helvetica", 17))
        self.entry_1.place(x=80, y=310)
        
        self.label_3 = Label(self.Empaquetado_screen, textvariable=self.alert_text, background="#D6D6D6",
                        fg='blue', font=("Helvetica", 17))
        self.label_3.place(x=80, y=350)

        Regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/Regresar.png"))
        Regresar_button = Label(self.Empaquetado_screen, image=Regresar, background="#155696", borderwidth=0)
        Regresar_button.place(x=80, y=400)

        Imprimir = ImageTk.PhotoImage(Image.open("updated QR codes with labels/Imprimir.png"))
        Imprimir_button = Label(self.Empaquetado_screen, image=Imprimir, background="#155696", borderwidth=0)
        Imprimir_button.place(x=400, y=400)

        self.frame = Frame(self.Empaquetado_screen, width=550, height=300, bg='white')
        self.frame.place(x=670, y=260)

        image_frame_1 = ImageTk.PhotoImage(Image.open("updated QR codes with labels/frame_1.png"))
        image_frame_1_L = Label(self.frame, image=image_frame_1, background="white", borderwidth=0)
        image_frame_1_L.place(x=15, y=20)

        self.kit_1_label = Label(self.frame, text='Kit:', textvariable=self.kit_text,background="white", fg='black', font=("Helvetica", 10))
        self.kit_1_label.place(x=100, y=28)

        self.fecha_1_label = Label(self.frame, textvariable=self.fecha_corta_text,text='Fecha:', background="white", fg='black', font=("Helvetica", 10))
        self.fecha_1_label.place(x=100, y=50)

        self.Caducidad_1_label = Label(self.frame, textvariable=self.caducidad_corta_text,text='Caducidad:', background="white", fg='black', font=("Helvetica", 10))
        self.Caducidad_1_label.place(x=100, y=72)

        image2_frame_1 = ImageTk.PhotoImage(Image.open("updated QR codes with labels/frame_2.png"))
        image2_frame_1_L = Label(self.frame, image=image2_frame_1, background="white", borderwidth=0)
        image2_frame_1_L.place(x=270, y=20)

        self.kit_2_label = Label(self.frame, text='Kit:',textvariable=self.kit_text, background="white", fg='black', font=("Helvetica", 10))
        self.kit_2_label.place(x=350, y=28)

        self.fecha_2_label = Label(self.frame, text='Fecha:', textvariable=self.fecha_corta_text,background="white", fg='black', font=("Helvetica", 10))
        self.fecha_2_label.place(x=350, y=50)

        self.Caducidad_2_label = Label(self.frame, textvariable=self.caducidad_corta_text,text='Caducidad:', background="white", fg='black', font=("Helvetica", 10))
        self.Caducidad_2_label.place(x=350, y=72)

        image3_frame_1 = ImageTk.PhotoImage(Image.open("updated QR codes with labels/frame_3.png"))
        image3_frame_1_L = Label(self.frame, image=image3_frame_1, background="white", borderwidth=0)
        image3_frame_1_L.place(x=15, y=140)

        self.kit_3_label = Label(self.frame, textvariable=self.kit_text, text='Kit:', background="white", fg='black', font=("Helvetica", 10))
        self.kit_3_label.place(x=100, y=148)

        self.usuario_label = Label(self.frame, text='Usuario:', textvariable=self.user_text,background="white", fg='black', font=("Helvetica", 10))
        self.usuario_label.place(x=100, y=170)

        self.fecha_3_label = Label(self.frame, textvariable=self.fecha_text,text='Fecha:', background="white", fg='black', font=("Helvetica", 10))
        self.fecha_3_label.place(x=100, y=192)

        self.Caducidad_3_label = Label(self.frame, text='Caducidad:', textvariable=self.caducidad_text, background="white", fg='black', font=("Helvetica", 10))
        self.Caducidad_3_label.place(x=100, y=212)

        self.id_label = Label(self.frame, text='ID:', textvariable=self.id_text, background="white", fg='black', font=("Helvetica", 10))
        self.id_label.place(x=100, y=232)

        self.Empaquetado_screen.mainloop()

    def Crear_lote_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass
        self.Crear_lote_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.Crear_lote_screen.pack()
        self.Crear_lote_screen.pack_propagate(0)

        # self.Crear_lote_screen.title('GUI')
        # self.Crear_lote_screen.geometry('1280x720')
        # self.Crear_lote_screen.config(bg='#D6D6D6')
        # self.Crear_lote_screen.resizable(False, False)
        # # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.Crear_lote_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.Crear_lote_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.Crear_lote_screen, image=img, background="#155696",borderwidth = 0)
        img_button.place(x=50,y=25)

        Trazadomus_label = Label(self.Crear_lote_screen, text='Trazadomus', background="#155696", fg='white',font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160,y=55)

        crear_lote_label = Label(self.Crear_lote_screen, text='Crear lote', background="#155696", fg='white',font=("Helvetica", 25))
        crear_lote_label.place(x=540,y=55)


        de_lote_label = Label(self.Crear_lote_screen, text='# de lote:', background="#D6D6D6", fg='black',font=("Helvetica",18))
        de_lote_label.place(x=80,y=200)

        self.entry_1 = Entry(self.Crear_lote_screen, textvariable=self.lote_text, width=35, font=("Helvetica", 17))
        self.entry_1.place(x=80, y=240)

        fecha_label = Label(self.Crear_lote_screen, text='Fecha:', background="#D6D6D6", fg='black',font=("Helvetica",18))
        fecha_label.place(x=80,y=300)

        self.entry_2 = Entry(self.Crear_lote_screen, textvariable=self.fecha_text ,width=35 , font=("Helvetica", 17))
        self.entry_2.place(x=80, y=340)

        Escanea_label = Label(self.Crear_lote_screen, text='Escanea los contenidos:', background="#D6D6D6", fg='black',font=("Helvetica",18))
        Escanea_label.place(x=80,y=400)
        
        
        
        self.entry_3 = Text(self.Crear_lote_screen, width=35, font=("Helvetica", 17))
        self.entry_3.place(x=80, y=440, height=240)
        
        self.label_3 = Label(self.Crear_lote_screen, textvariable=self.alert_text, background="#D6D6D6",
                        fg='blue', font=("Helvetica", 17))
        self.label_3.place(x=670, y=520)
        
        Esterilizador_label = Label(self.Crear_lote_screen, text=' Esterilizador:', background="#D6D6D6", fg='black',
                             font=("Helvetica", 18))
        Esterilizador_label.place(x=670, y=560)

        self.entry_2 = Entry(self.Crear_lote_screen, textvariable=self.esteri_text, width=30, font=("Helvetica", 17))
        self.entry_2.place(x=670, y=610)

        Regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar_2.png"))
        Regresar_button = Label(self.Crear_lote_screen, image=Regresar, background="#155696", borderwidth=0)
        Regresar_button.place(x=650,y=240)

        Imprimir = ImageTk.PhotoImage(Image.open("updated QR codes with labels/crear_2.png"))
        Imprimir_button = Label(self.Crear_lote_screen, image=Imprimir, background="#155696", borderwidth=0)
        Imprimir_button.place(x=950,y=240)


        self.Crear_lote_screen.mainloop()

    def actualizar_lote_paquete_window(self, closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.actualizar_lote_paquete_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.actualizar_lote_paquete_screen.pack()
        self.actualizar_lote_paquete_screen.pack_propagate(0)

        # self.actualizar_lote_paquete_screen.title('GUI')
        # self.actualizar_lote_paquete_screen.geometry('1280x720')
        # self.actualizar_lote_paquete_screen.config(bg='#D6D6D6')
        # self.actualizar_lote_paquete_screen.resizable(False, False)

        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.actualizar_lote_paquete_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.actualizar_lote_paquete_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.actualizar_lote_paquete_screen, image=img, background="#155696", borderwidth=0)
        img_button.place(x=50, y=25)

        Trazadomus_label = Label(self.actualizar_lote_paquete_screen, text='Trazadomus', background="#155696", fg='white',
                                 font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160, y=55)

        crear_lote_label = Label(self.actualizar_lote_paquete_screen, text='Actualizar lote o paquete', background="#155696", fg='white',
                                 font=("Helvetica", 25))
        crear_lote_label.place(x=500, y=55)

        label_1 = Label(self.actualizar_lote_paquete_screen, text='Elija la opción:', background="#D6D6D6", fg='black',
                                 font=("Helvetica", 20))
        label_1.place(x=180, y=220)

        regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar3.png"))
        regresar_button = Label(self.actualizar_lote_paquete_screen, image=regresar, background="#D6D6D6", borderwidth=0)
        regresar_button.place(x=180,y=340)

        lote = ImageTk.PhotoImage(Image.open("updated QR codes with labels/lote3.png"))
        lote_button = Label(self.actualizar_lote_paquete_screen, image=lote, background="#D6D6D6", borderwidth=0)
        lote_button.place(x=530,y=340)

        paquete = ImageTk.PhotoImage(Image.open("updated QR codes with labels/paquete.png"))
        paquete_button = Label(self.actualizar_lote_paquete_screen, image=paquete, background="#D6D6D6", borderwidth=0)
        paquete_button.place(x=880,y=340)

        self.actualizar_lote_paquete_screen.mainloop()

    def actualizar_lote_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.actualizar_lote_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.actualizar_lote_screen.pack()
        self.actualizar_lote_screen.pack_propagate(0)

        # self.actualizar_lote_screen.title('GUI')
        # self.actualizar_lote_screen.geometry('1280x720')
        # self.actualizar_lote_screen.config(bg='#D6D6D6')
        # self.actualizar_lote_screen.resizable(False, False)

        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.actualizar_lote_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.actualizar_lote_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.actualizar_lote_screen, image=img, background="#155696", borderwidth=0)
        img_button.place(x=50, y=25)

        Trazadomus_label = Label(self.actualizar_lote_screen, text='Trazadomus', background="#155696", fg='white',
                                 font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160, y=55)

        actualizar_lote_label = Label(self.actualizar_lote_screen, text='Actualizar lote', background="#155696", fg='white',
                                 font=("Helvetica", 25))
        actualizar_lote_label.place(x=550, y=55)

        label_1 = Label(self.actualizar_lote_screen, text='Elija la opción:', background="#D6D6D6", fg='black',
                                 font=("Helvetica", 20))
        label_1.place(x=180, y=220)
        
        regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar4.png"))
        regresar_button = Label(self.actualizar_lote_screen, image=regresar, background="#D6D6D6", borderwidth=0)
        regresar_button.place(x=180,y=340)

        procesado = ImageTk.PhotoImage(Image.open("updated QR codes with labels/procesado.png"))
        procesado_button = Label(self.actualizar_lote_screen, image=procesado, background="#D6D6D6", borderwidth=0)
        procesado_button.place(x=530,y=340)

        indicador = ImageTk.PhotoImage(Image.open("updated QR codes with labels/indicador.png"))
        indicador_button = Label(self.actualizar_lote_screen, image=indicador, background="#D6D6D6", borderwidth=0)
        indicador_button.place(x=880,y=340)

        self.actualizar_lote_screen.mainloop()

    def actualizar_paquete_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.actualizar_paquete_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.actualizar_paquete_screen.pack()
        self.actualizar_paquete_screen.pack_propagate(0)

        # self.actualizar_paquete_screen.title('GUI')
        # self.actualizar_paquete_screen.geometry('1280x720')
        # self.actualizar_paquete_screen.config(bg='#D6D6D6')
        # self.actualizar_paquete_screen.resizable(False, False)

        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.actualizar_paquete_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.actualizar_paquete_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.actualizar_paquete_screen, image=img, background="#155696", borderwidth=0)
        img_button.place(x=50, y=25)

        Trazadomus_label = Label(self.actualizar_paquete_screen, text='Trazadomus', background="#155696", fg='white',
                                 font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160, y=55)

        crear_lote_label = Label(self.actualizar_paquete_screen, text='Actualizar paquete', background="#155696", fg='white',
                                 font=("Helvetica", 25))
        crear_lote_label.place(x=500, y=55)

        label_1 = Label(self.actualizar_paquete_screen, text='Elija la opción:', background="#D6D6D6", fg='black',
                                 font=("Helvetica", 20))
        label_1.place(x=180, y=220)
        
        regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar6.png"))
        regresar_button = Label(self.actualizar_paquete_screen, image=regresar, background="#D6D6D6", borderwidth=0)
        regresar_button.place(x=100,y=340)

        indicador = ImageTk.PhotoImage(Image.open("updated QR codes with labels/indicador2.png"))
        indicador_button = Label(self.actualizar_paquete_screen, image=indicador, background="#D6D6D6", borderwidth=0)
        indicador_button.place(x=400,y=340)

        almacen = ImageTk.PhotoImage(Image.open("updated QR codes with labels/almacen.png"))
        almacen_button = Label(self.actualizar_paquete_screen, image=almacen, background="#D6D6D6", borderwidth=0)
        almacen_button.place(x=700,y=340)

        destino = ImageTk.PhotoImage(Image.open("updated QR codes with labels/destino.png"))
        destino_button = Label(self.actualizar_paquete_screen, image=destino, background="#D6D6D6", borderwidth=0)
        destino_button.place(x=1000,y=340)

        self.actualizar_paquete_screen.mainloop()

    def Actualizar_lote_2_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.Actualizar_lote_2_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.Actualizar_lote_2_screen.pack()
        self.Actualizar_lote_2_screen.pack_propagate(0)

        # self.Actualizar_lote_2_screen.title('GUI')
        # self.Actualizar_lote_2_screen.geometry('1280x720')
        # self.Actualizar_lote_2_screen.config(bg='#D6D6D6')
        # self.Actualizar_lote_2_screen.resizable(False, False)
        # # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.Actualizar_lote_2_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.Actualizar_lote_2_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.Actualizar_lote_2_screen, image=img, background="#155696",borderwidth = 0)
        img_button.place(x=50,y=25)

        Trazadomus_label = Label(self.Actualizar_lote_2_screen, text='Trazadomus', background="#155696", fg='white',font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160,y=55)

        actualizar_label = Label(self.Actualizar_lote_2_screen, text='Actualizar lote', background="#155696", fg='white',font=("Helvetica", 25))
        actualizar_label.place(x=540,y=55)

        registrar_label = Label(self.Actualizar_lote_2_screen, text='Registrar lote como procesado', background="#D6D6D6", fg='black',font=("Helvetica", 25))
        registrar_label.place(x=80,y=200)
        
        self.label_3 = Label(self.Actualizar_lote_2_screen, textvariable=self.alert_text, background="#D6D6D6",
                        fg='blue', font=("Helvetica", 17))
        self.label_3.place(x=80, y=350)
        
        label_2 = Label(self.Actualizar_lote_2_screen, text='Escanea el QR del lote:', background="#D6D6D6", fg='black',font=("Helvetica", 17))
        label_2.place(x=80,y=260)

        self.entry_1 = Entry(self.Actualizar_lote_2_screen, textvariable=self.lote_text ,width=35, font=("Helvetica", 17))
        self.entry_1.place(x=80, y=310)

        Regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar5.png"))
        Regresar_button = Label(self.Actualizar_lote_2_screen, image=Regresar, background="#D6D6D6", borderwidth=0)
        Regresar_button.place(x=350,y=400)

        Imprimir = ImageTk.PhotoImage(Image.open("updated QR codes with labels/confirmar.png"))
        Imprimir_button = Label(self.Actualizar_lote_2_screen, image=Imprimir, background="#D6D6D6", borderwidth=0)
        Imprimir_button.place(x=700,y=400)






        self.Actualizar_lote_2_screen.mainloop()

    def Actualizar_lote_3_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.Actualizar_lote_3_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.Actualizar_lote_3_screen.pack()
        self.Actualizar_lote_3_screen.pack_propagate(0)

        # self.Actualizar_lote_3_screen.title('GUI')
        # self.Actualizar_lote_3_screen.geometry('1280x720')
        # self.Actualizar_lote_3_screen.config(bg='#D6D6D6')
        # self.Actualizar_lote_3_screen.resizable(False, False)
        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.Actualizar_lote_3_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.Actualizar_lote_3_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.Actualizar_lote_3_screen, image=img, background="#155696",borderwidth = 0)
        img_button.place(x=50,y=25)

        Trazadomus_label = Label(self.Actualizar_lote_3_screen, text='Trazadomus', background="#155696", fg='white',font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160,y=55)

        actualizar_label = Label(self.Actualizar_lote_3_screen, text='Actualizar lote', background="#155696", fg='white',font=("Helvetica", 25))
        actualizar_label.place(x=540,y=55)

        registrar_label = Label(self.Actualizar_lote_3_screen, text='Registrar estado de indicador biológico/químico', background="#D6D6D6", fg='black',font=("Helvetica", 25))
        registrar_label.place(x=80,y=200)

        label_2 = Label(self.Actualizar_lote_3_screen, text='Escanea el QR del lote:', background="#D6D6D6", fg='black',font=("Helvetica", 17))
        label_2.place(x=80,y=260)
        
        self.label_3 = Label(self.Actualizar_lote_3_screen, textvariable=self.alert_text, background="#D6D6D6",
                        fg='blue', font=("Helvetica", 17))
        self.label_3.place(x=80, y=350)
        
        self.entry_1 = Entry(self.Actualizar_lote_3_screen, width=35, textvariable=self.lote_text, font=("Helvetica", 17))
        self.entry_1.place(x=80, y=310)

        Regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar7.png"))
        Regresar_button = Label(self.Actualizar_lote_3_screen, image=Regresar, background="#D6D6D6", borderwidth=0)
        Regresar_button.place(x=230,y=400)

        fallido = ImageTk.PhotoImage(Image.open("updated QR codes with labels/fallido.png"))
        fallido_button = Label(self.Actualizar_lote_3_screen, image=fallido, background="#D6D6D6", borderwidth=0)
        fallido_button.place(x=530,y=400)

        verificado = ImageTk.PhotoImage(Image.open("updated QR codes with labels/verificado.png"))
        verificado_button = Label(self.Actualizar_lote_3_screen, image=verificado, background="#D6D6D6", borderwidth=0)
        verificado_button.place(x=830,y=400)






        self.Actualizar_lote_3_screen.mainloop()

    def Actualizar_paquete_2_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.Actualizar_paquete_2_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.Actualizar_paquete_2_screen.pack()
        self.Actualizar_paquete_2_screen.pack_propagate(0)

        # self.Actualizar_paquete_2_screen.title('GUI')
        # self.Actualizar_paquete_2_screen.geometry('1280x720')
        # self.Actualizar_paquete_2_screen.config(bg='#D6D6D6')
        # self.Actualizar_paquete_2_screen.resizable(False, False)
        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.Actualizar_paquete_2_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.Actualizar_paquete_2_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.Actualizar_paquete_2_screen, image=img, background="#155696", borderwidth=0)
        img_button.place(x=50, y=25)

        Trazadomus_label = Label(self.Actualizar_paquete_2_screen, text='Trazadomus', background="#155696", fg='white',
                                 font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160, y=55)

        actualizar_label = Label(self.Actualizar_paquete_2_screen, text='Actualizar paquete', background="#155696",
                                 fg='white', font=("Helvetica", 25))
        actualizar_label.place(x=540, y=55)

        registrar_label = Label(self.Actualizar_paquete_2_screen,
                                text='Registrar estado de indicador biológico/químico', background="#D6D6D6",
                                fg='black', font=("Helvetica", 25))
        registrar_label.place(x=80, y=200)

        label_2 = Label(self.Actualizar_paquete_2_screen, text='Escanea el QR del paquete:', background="#D6D6D6",
                        fg='black', font=("Helvetica", 17))
        label_2.place(x=80, y=260)
        
        self.label_3 = Label(self.Actualizar_paquete_2_screen, textvariable=self.alert_text, background="#D6D6D6",
                        fg='blue', font=("Helvetica", 17))
        self.label_3.place(x=80, y=350)
        
        self.entry_1 = Entry(self.Actualizar_paquete_2_screen, textvariable=self.pack_text ,width=35, font=("Helvetica", 17))
        self.entry_1.place(x=80, y=310)

        Regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar8.png"))
        Regresar_button = Label(self.Actualizar_paquete_2_screen, image=Regresar, background="#D6D6D6", borderwidth=0)
        Regresar_button.place(x=170, y=400)

        fallido = ImageTk.PhotoImage(Image.open("updated QR codes with labels/fallido2.png"))
        fallido_button = Label(self.Actualizar_paquete_2_screen, image=fallido, background="#D6D6D6", borderwidth=0)
        fallido_button.place(x=420, y=400)

        verificado = ImageTk.PhotoImage(Image.open("updated QR codes with labels/verificado2.png"))
        verificado_button = Label(self.Actualizar_paquete_2_screen, image=verificado, background="#D6D6D6",
                                   borderwidth=0)
        verificado_button.place(x=670, y=400)

        terminar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/terminar.png"))
        terminar_button = Label(self.Actualizar_paquete_2_screen, image=terminar, background="#D6D6D6", borderwidth=0)
        terminar_button.place(x=920, y=400)

        self.Actualizar_paquete_2_screen.mainloop()

    def Actualizar_paquete_3_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.Actualizar_paquete_3_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.Actualizar_paquete_3_screen.pack()
        self.Actualizar_paquete_3_screen.pack_propagate(0)

        # self.Actualizar_paquete_3_screen.title('GUI')
        # self.Actualizar_paquete_3_screen.geometry('1280x720')
        # self.Actualizar_paquete_3_screen.config(bg='#D6D6D6')
        # self.Actualizar_paquete_3_screen.resizable(False, False)
        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.Actualizar_paquete_3_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.Actualizar_paquete_3_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.Actualizar_paquete_3_screen, image=img, background="#155696", borderwidth=0)
        img_button.place(x=50, y=25)

        Trazadomus_label = Label(self.Actualizar_paquete_3_screen, text='Trazadomus', background="#155696", fg='white',
                                 font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160, y=55)

        actualizar_label = Label(self.Actualizar_paquete_3_screen, text='Actualizar paquete', background="#155696",
                                 fg='white', font=("Helvetica", 25))
        actualizar_label.place(x=520, y=55)

        registrar_label = Label(self.Actualizar_paquete_3_screen, text='Registrar entrada a almacen',
                                background="#D6D6D6", fg='black', font=("Helvetica", 25))
        registrar_label.place(x=80, y=200)

        label_2 = Label(self.Actualizar_paquete_3_screen, text='Escanea el QR del paquete:', background="#D6D6D6",
                        fg='black', font=("Helvetica", 17))
        label_2.place(x=80, y=260)
        
        self.label_3 = Label(self.Actualizar_paquete_3_screen, textvariable=self.alert_text, background="#D6D6D6",
                        fg='blue', font=("Helvetica", 17))
        self.label_3.place(x=80, y=350)
        
        self.entry_1 = Entry(self.Actualizar_paquete_3_screen, textvariable=self.pack_text, width=35, font=("Helvetica", 17))
        self.entry_1.place(x=80, y=310)

        Regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar9.png"))
        Regresar_button = Label(self.Actualizar_paquete_3_screen, image=Regresar, background="#D6D6D6", borderwidth=0)
        Regresar_button.place(x=230, y=400)

        confirmar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/confirmar2.png"))
        fallido_button = Label(self.Actualizar_paquete_3_screen, image=confirmar, background="#D6D6D6", borderwidth=0)
        fallido_button.place(x=530, y=400)

        terminar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/terminar2.png"))
        terminar_button = Label(self.Actualizar_paquete_3_screen, image=terminar, background="#D6D6D6", borderwidth=0)
        terminar_button.place(x=830, y=400)

        self.Actualizar_paquete_3_screen.mainloop()

    def Actualizar_paquete_4_window(self,closing_window_name):

        try:
            closing_window_name.destroy()
        except:
            pass

        self.Actualizar_paquete_4_screen = Frame(self.home_screen, height=720, width=1280, bg='#D6D6D6', relief='raised')
        self.Actualizar_paquete_4_screen.pack()
        self.Actualizar_paquete_4_screen.pack_propagate(0)

        # self.Actualizar_paquete_4_screen.title('GUI')
        # self.Actualizar_paquete_4_screen.geometry('1280x720')
        # self.Actualizar_paquete_4_screen.config(bg='#D6D6D6')
        # self.Actualizar_paquete_4_screen.resizable(False, False)
        # self.ws.attributes('-fullscreen', True)

        # img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        # img_label = Label(self.Actualizar_paquete_4_screen, image=img, background="#155696")
        # img_label.pack(pady=(50,0))

        canvas = Canvas(
            self.Actualizar_paquete_4_screen,
            height=150,
            width=1280,
            bg="#155696",
            highlightbackground='#155696'
        )
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/image_1.png"))
        img_button = Label(self.Actualizar_paquete_4_screen, image=img, background="#155696", borderwidth=0)
        img_button.place(x=50, y=25)

        Trazadomus_label = Label(self.Actualizar_paquete_4_screen, text='Trazadomus', background="#155696", fg='white',
                                 font=("Helvetica", 25, 'bold'))
        Trazadomus_label.place(x=160, y=55)

        crear_lote_label = Label(self.Actualizar_paquete_4_screen, text='Actualizar paquete', background="#155696",
                                 fg='white', font=("Helvetica", 25))
        crear_lote_label.place(x=520, y=55)

        register_label = Label(self.Actualizar_paquete_4_screen, text='Registrar nuevo destino para paquete',
                               background="#D6D6D6", fg='black', font=("Helvetica", 18))
        register_label.place(x=80, y=195)

        escanea_paqueta_label = Label(self.Actualizar_paquete_4_screen, text='Escanea el QR del paquete:',
                                      background="#D6D6D6", fg='black', font=("Helvetica", 18))
        escanea_paqueta_label.place(x=80, y=295)
        
        self.label_3 = Label(self.Actualizar_paquete_4_screen, textvariable=self.alert_text, background="#D6D6D6",
                        fg='blue', font=("Helvetica", 17))
        self.label_3.place(x=80, y=230)
        
        self.entry_1 = Entry(self.Actualizar_paquete_4_screen,textvariable=self.pack_text, width=35, font=("Helvetica", 17))
        self.entry_1.place(x=80, y=340)

        escanea_destino_label = Label(self.Actualizar_paquete_4_screen, text='Escanea el QR del destino:',
                                      background="#D6D6D6", fg='black', font=("Helvetica", 18))
        escanea_destino_label.place(x=80, y=415)

        self.entry_2 = Entry(self.Actualizar_paquete_4_screen,textvariable=self.destino_text, width=35, font=("Helvetica", 17))
        self.entry_2.place(x=80, y=460)

        Regresar = ImageTk.PhotoImage(Image.open("updated QR codes with labels/regresar10.png"))
        Regresar_button = Label(self.Actualizar_paquete_4_screen, image=Regresar, background="#D6D6D6", borderwidth=0)
        Regresar_button.place(x=650, y=240)

        Imprimir = ImageTk.PhotoImage(Image.open("updated QR codes with labels/confirmar3.png"))
        Imprimir_button = Label(self.Actualizar_paquete_4_screen, image=Imprimir, background="#D6D6D6", borderwidth=0)
        Imprimir_button.place(x=950, y=240)

        self.Actualizar_paquete_4_screen.mainloop()

        
if __name__ == '__main__':
    obj_1 = home_window()
