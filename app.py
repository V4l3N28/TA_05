from from flask import Flask, request, render_template, url_for, redirect
from datetime import datetime
from flask_mysqldb import MySQLdb

app= Flask(__name__)

#conexion a la base de datos
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'bases'

mysql= MySQL(app)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000, debug=True)

#este .py tiene la finalidad de mapear cada uno de los links con su respectiva funcion
#Conexion a \templates\HOME la cual seria establecida como la pagina principal
# este @app.route('/') siempre tiene que estar definido con un solo "/"
@app.route('/')
def HOME():
  return render_template("HOME.html")

##Conexion a \templates\ventanaInicioSESION


@app.route('/IniciarSesion/', methods=['GET', 'POST'])
def ventanaInicioSESION():
    if request.method == 'GET':

        contrasena = request.form['contrasena']
        ususario = request.form['usuario']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuario VALUES(NULL, %s, %s"), (contrasena, ususario)
        cursor.conection.commit()

        return redirect(url_for('HOME'))

  return render_template("ventanaInicioSESION.html")

##Conexion a \templates\entanvaRegistroUSUARIO
@app.route('/Registrarse/', methods=['GET', 'POST'])
def ventanaRegistroUSUARIO():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        email2 = request.form['email']
        contrasena = request.form['contrasena']
        contrasena2 = request.form['contrasena']
        ususario = request.form['usuario']

        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO usuario VALUES(NULL, %s, %s, %s, %s, %s, %s, %s"), (nombre, apellido, email, email2, contrasena, contrasena2, ususario)
        cursor.conection.commit()

        return redirect(url_for('HOME'))
  
    return render_template("ventanaRegistroUSUARIO.html")

##Conexion a \templates\CambiarCLAVE
@app.route('/ChangePassword/')
def CambiarCLAVE():
  return render_template("CambiarCLAVE.html")

##Conexion a \templates\RecuperarCLAVE
@app.route('/RecuperarClave/')
def RecuperarCLAVE():
  return render_template("RecuperarCLAVE.html")

##Conexion a \templates\PRONOSTICOS
@app.route('/Pronosticos/')
def PRONOSTICOS():
  return render_template("PRONOSTICOS.html")

##Conexion a \templates\GENERAL
@app.route('/General/')
def GENERAL():
  return render_template("GENERAL.html")

##Conexion a \templates\ESTACIONES
@app.route('/Estaciones/')
def ESTACIONES():
  return render_template("ESTACIONES.html")
