from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection
 
bpFacturas = Blueprint('facturas', __name__, url_prefix='/facturas')
 
@bpFacturas.route("/")
def facturas_index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM facturas")
    datos = cur.fetchall()
    cur.close()
    return render_template('facturas/index.html', lista_facturas=datos)
 
@bpFacturas.route("/agregar", methods=["GET", "POST"])
def facturas_agregar_datos():
    if request.method == 'POST':
        conn = get_connection()
        cursor = conn.cursor()
        codigoPedido = request.form['CodigoPedido']
        fecha        = request.form['Fecha']
        total        = request.form['Total']
        metodoPago   = request.form['MetodoPago']
        estado       = request.form['Estado']
        cursor.execute(
            "INSERT INTO facturas(CodigoPedido, Fecha, Total, MetodoPago, Estado) VALUES(%s, %s, %s, %s, %s)",
            (codigoPedido, fecha, total, metodoPago, estado)
        )
        conn.commit()
        return redirect(url_for('facturas.facturas_index'))
    elif request.method == 'GET':
        return render_template('facturas/agregar.html')
 
@bpFacturas.route("/editar/<string:factura_id>", methods=["GET", "POST"])
def facturas_editar_datos(factura_id):
    if request.method == 'GET':
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM facturas WHERE Factura_id=%s", (factura_id,))
        factura = cur.fetchone()
        return render_template('facturas/editar.html', factura=factura)
    elif request.method == 'POST':
        conn = get_connection()
        cursor = conn.cursor()
        codigoPedido = request.form['CodigoPedido']
        fecha        = request.form['Fecha']
        total        = request.form['Total']
        metodoPago   = request.form['MetodoPago']
        estado       = request.form['Estado']
        cursor.execute(
            "UPDATE facturas SET CodigoPedido=%s, Fecha=%s, Total=%s, MetodoPago=%s, Estado=%s WHERE Factura_id=%s",
            (codigoPedido, fecha, total, metodoPago, estado, factura_id)
        )
        conn.commit()
        return redirect(url_for('facturas.facturas_index'))
 
@bpFacturas.route("/eliminar/<string:factura_id>", methods=["GET", "POST"])
def facturas_eliminar_datos(factura_id):
    if request.method == 'GET':
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM facturas WHERE Factura_id=%s", (factura_id,))
        factura = cursor.fetchone()
        return render_template('facturas/eliminar.html', factura=factura)
    elif request.method == 'POST':
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM facturas WHERE Factura_id=%s", (factura_id,))
        conn.commit()
        return redirect(url_for('facturas.facturas_index'))