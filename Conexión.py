from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

def based():
    #Conexión a base de datos
    conexion= sqlite3.connect('basedatos.db')

    #Crear cursor
    cursor = conexion.cursor()
    #Crear tabla
    cursor.execute("CREATE TABLE IF NOT EXISTS fincas("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT, "+
	"idArea	INTEGER NOT NULL FOREIGN KEY REFERENCES veredas(id),"+
	"finca	INTEGER NOT NULL,"+
	")")

    cursor.execute("CREATE TABLE observadores ("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT,"+
	"primerNombre	TEXT NOT NULL,"+
	"segundoNombre	TEXT,"+
	"apellidos	TEXT NOT NULL,"+
	"celular	INTEGER,"+
	"latitud	NUMERIC,"+
	"longitud	NUMERIC,"+
	")")

    cursor.execute("CREATE TABLE registros ("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT,"+
	"idFinca	INTEGER NOT NULL,"+
	"fecha	TEXT,"+
	"precipitacion	REAL,"+
	"temperaturaMaxima	REAL,"+
	"temperaturaMinima	REAL,"+
	")")
    cursor.execute("CREATE TABLE veredas ("+
	"id	INTEGER PRIMARY KEY AUTOINCREMENT,"+
	"departamento	TEXT NOT NULL,"+
	"ciudad	TEXT NOT NULL,"+
	"vereda	TEXT NOT NULL,"+
	")")

    conexion.commit() 