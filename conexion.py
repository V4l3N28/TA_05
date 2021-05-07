from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

def based():
    #estamos conectando una base de datos SQLite3 a python mediante el comando sqlite3.connect('')
    #Conexión a base de datos
    conexion= sqlite3.connect('bases_0704.db')
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

    #TABLA USUARIO
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios ("+
	"id INTEGER, "+
	"nombre TEXT NOT NULL, "+
	"apellido TEXT NOT NULL, "+
    "usuario TEXT NOT NULL, "+
	"email TEXT NOT NULL, "+
    "contrasena TEXT NOT NULL, "+
	"PRIMARY KEY('id' AUTOINCREMENT) " ")")
    #Se utiliza un comando .commit para realizar cambios
    conexion.commit() 
    return conexion
based()