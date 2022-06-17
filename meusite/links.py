# Importando flask e app
from flask import render_template
from meusite import app

@app.route('/')
def Inicial():
    return render_template('Inicial.html')

@app.route('/CCIH')
def CCIH():
    return render_template('CCIH.html')

@app.route('/NUCLEO')
def NUCLEO():
    return render_template('NUCLEO.html')