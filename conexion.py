from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

def based():
    #estamos conectando una base de datos SQLite3 a python mediante el comando sqlite3.connect('')
    #Conexión a base de datos
    conexion= sqlite3.connect('bases.db')
    #Crear cursor
    cursor = conexion.cursor()
    """Para crear una tabla de nombre "name" se usa el comando  .execute("CREATE TABLE name
    Se usara el comando .execute("CREATE TABLE IF NOT EXISTS name para que cree una taba si no hay existencia de ella en una base de datos
    Se crearan 4 tablas con los nombres fincas, observadores,registros y veredas
    Se utilizan diferentes tipos de variables como INTEGER, TEXT, NUMERIC y REAL para definir el contenido de cada columna"""
    
    cursor.execute("CREATE TABLE IF NOT EXISTS veredas ("+
	"id INTEGER, "+
	"departamento TEXT NOT NULL, "+
	"ciudad TEXT NOT NULL, "+
	"vereda TEXT NOT NULL, "+
	"PRIMARY KEY('id' AUTOINCREMENT) " ")")

    cursor.execute("CREATE TABLE IF NOT EXISTS observadores ("+
	"id INTEGER, "+
	"primerNombre TEXT NOT NULL, "+
	"segundoNombre TEXT, "+
	"apellidos TEXT NOT NULL, "+
	"celular INTEGER, "+
	"latitud NUMERIC, "+
	"longitud NUMERIC, "+
	"PRIMARY KEY('id' AUTOINCREMENT)" ")")

    cursor.execute("CREATE TABLE IF NOT EXISTS fincas ("+
	"id INTEGER, "+
	"idArea INTEGER NOT NULL, "+
	"finca INTEGER NOT NULL, "+
	"PRIMARY KEY('id' AUTOINCREMENT), "+
	"FOREIGN KEY('idArea') REFERENCES 'veredas'('id') "
    ")")
    #Se utiliza NOT NULL para especificar que el dato introducido en aquella columna no puede estar vacío
    #FOREIGN KEY son variables que utilizan para traer atributos de otra parte por medio de REFERENCES

    cursor.execute("CREATE TABLE IF NOT EXISTS registros (" +
	"id INTEGER, "+
	"idFinca INTEGER NOT NULL, "+
	"fecha TEXT, "+
	"precipitacion REAL, "+
	"temperaturaMaxima REAL, "+
	"temperaturaMinima REAL, "+
	"PRIMARY KEY('id' AUTOINCREMENT)" ")")


    #Se utiliza un comando .commit para realizar cambios
    conexion.commit() 
    #Para insertar datos en una tabla de nombre "nametable" se usa el comando  .execute("INSERT INTO nametable VALUES() donde INSERT INTO nametable indica la el nombre de la tabla en donde se van a insertar los datos dentro de VALUES()
  
    #insertar datos en la tabla fincas
    cursor.execute("INSERT INTO fincas VALUES (null, 4, 9)")
  
    #insertar datos en la tabla observadores   
    cursor.execute("INSERT INTO  observadores VALUES (null, 'luca', 'leon', 'monsalve', 3113128486, 345701, 345701)")
 
    #insertar datos en la tabla registros
    cursor.execute("INSERT INTO registros VALUES (null, 3,'06/04/2021', 8, 33, 13)")
  
    #insertar datos en la tabla veredas
    cursor.execute("INSERT INTO veredas VALUES (null, 'CAUCA', 'POPAYAN','SANTA ROSA')")
  
  
    '''Para pedir datos de una tabla de nombre "nametable" se usa el comando .execute("SELECT name FROM nametable;") donde SELECT name se utiliza para selecciónar UNA columna específica de la tabla nametable
    Se crea una variable en donde se va a usar el comando .fetchall() para seleccionar todos los datos de la columna anteriormente seleccionada
    cursor.execute("SELECT name  FROM nametable;")
    variable = cursor.fetchall() 
     pedir datos de la columna finca de la tabla fincas'''
    
    cursor.execute("SELECT finca FROM fincas;")
    fincas= cursor.fetchall()

    #pedir datos de la columna apellidos de la tabla observadores
    cursor.execute("SELECT apellidos  FROM observadores;")
    apellidos= cursor.fetchall()

    cursor.execute("SELECT fecha  FROM registros;")
    fechas= cursor.fetchall()
    #Para pedir todos los datos de una tabla nametable, se usa el comando .execute("SELECT * FROM nametable;") donde el símbolo * significa TODOS los datos
    cursor.execute("SELECT  * FROM veredas;")
    localizacion= cursor.fetchall()

    #Se utiliza un comando .commit para realizar cambios
    conexion.commit() 
    
    return (fincas,apellidos,fechas,localizacion)
    
Variable = based()
print(Variable)