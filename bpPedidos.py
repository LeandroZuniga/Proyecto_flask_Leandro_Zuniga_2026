from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection
 
bpPedidos = Blueprint('pedidos', __name__, url_prefix='/pedidos')
 
@bpPedidos.route("/")
def pedidos_index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pedidos")
    datos = cur.fetchall()
    cur.close()
    return render_template('pedidos/index.html', lista_pedidos=datos)
 
@bpPedidos.route("/agregar", methods=["GET", "POST"])
def agregar_datos():
    if request.method == 'POST':
        conn = get_connection()
        cursor = conn.cursor()
        nombre     = request.form['Nombre']
        stock      = request.form['Stock']
        nombreCaja = request.form['NombreCaja']
        telefono   = request.form['Telefono']
        direccion  = request.form['Direccion']
        cursor.execute(
            "INSERT INTO pedidos(Nombre, Stock, NombreCaja, Telefono, Direccion) VALUES(%s, %s, %s, %s, %s)",
            (nombre, stock, nombreCaja, telefono, direccion)
        )
        conn.commit()
        return redirect(url_for('pedidos.pedidos_index'))
    elif request.method == 'GET':
        return render_template('pedidos/agregar.html')
 
@bpPedidos.route("/editar/<string:codigo>", methods=["GET", "POST"])
def editar(codigo):
    if request.method == 'GET':
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pedidos WHERE Codigo=%s", (codigo,))
        pedido = cur.fetchone()
        return render_template('pedidos/editar.html', pedido=pedido)
    elif request.method == 'POST':
        conn = get_connection()
        cursor = conn.cursor()
        nombre     = request.form['Nombre']
        stock      = request.form['Stock']
        nombreCaja = request.form['NombreCaja']
        telefono   = request.form['Telefono']
        direccion  = request.form['Direccion']
        cursor.execute(
            "UPDATE pedidos SET Nombre=%s, Stock=%s, NombreCaja=%s, Telefono=%s, Direccion=%s WHERE Codigo=%s",
            (nombre, stock, nombreCaja, telefono, direccion, codigo)
        )
        conn.commit()
        return redirect(url_for('pedidos.pedidos_index'))
 
@bpPedidos.route("/eliminar/<string:codigo>", methods=["GET", "POST"])
def eliminar(codigo):
    if request.method == 'GET':
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE Codigo=%s", (codigo,))
        pedido = cursor.fetchone()
        return render_template('pedidos/eliminar.html', pedido=pedido)
    elif request.method == 'POST':
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pedidos WHERE Codigo=%s", (codigo,))
        conn.commit()
        return redirect(url_for('pedidos.pedidos_index'))