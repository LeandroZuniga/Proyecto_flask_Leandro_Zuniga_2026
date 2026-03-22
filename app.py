from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clientes',   # aquí tu base de datos
    ssl_disabled=True
)

@app.route("/pedidos/")
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM pedidos")
    datos = cur.fetchall()
    cur.close()
    return render_template('pedidos/index.html', lista_pedidos=datos)


@app.route("/pedidos/agregar", methods=["GET", "POST"])
def agregar_datos():
    if request.method == 'POST':
        cursor = conn.cursor()
        Nombre = request.form['Nombre']
        Stock = request.form['Stock']
        NombreCaja = request.form['NombreCaja']
        Telefono = request.form['Telefono']
        Direccion = request.form['Direccion']
        cursor.execute(
            "INSERT INTO pedidos (Nombre, Stock, NombreCaja, Telefono, Direccion) VALUES (%s, %s, %s, %s, %s)",
            (Nombre, Stock, NombreCaja, Telefono, Direccion)
        )
        conn.commit()
        return redirect(url_for('index'))   
    return render_template('pedidos/agregar.html')


@app.route("/pedidos/editar/<string:codigo>", methods=["GET", "POST"])
def editar(codigo):
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM pedidos WHERE Codigo=%s", (codigo,))
        pedido = cur.fetchone()
        return render_template('pedidos/editar.html', pedido=pedido)  
    elif request.method == 'POST':
        cursor = conn.cursor()
        Nombre = request.form['Nombre']
        Stock = request.form['Stock']
        NombreCaja = request.form['NombreCaja']
        Telefono = request.form['Telefono']
        Direccion = request.form['Direccion']
        cursor.execute(
            "UPDATE pedidos SET Nombre=%s, Stock=%s, NombreCaja=%s, Telefono=%s, Direccion=%s WHERE Codigo=%s",
            (Nombre, Stock, NombreCaja, Telefono, Direccion, codigo)
        )
        conn.commit()
        return redirect(url_for('index'))   


@app.route("/pedidos/eliminar/<string:codigo>", methods=["GET", "POST"])
def eliminar(codigo):
    if request.method == 'GET':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE Codigo=%s", (codigo,))
        pedido = cursor.fetchone()
        return render_template('pedidos/eliminar.html', pedido=pedido)  
    elif request.method == 'POST':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pedidos WHERE Codigo=%s", (codigo,))
        conn.commit()
        return redirect(url_for('index'))   
    





@app.route("/facturas/")
def facturas_index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM facturas")
    datos = cur.fetchall()
    cur.close()
    return render_template('facturas/index.html', lista_facturas=datos)


@app.route("/facturas/agregar", methods=["GET", "POST"])
def facturas_agregar_datos():
    if request.method == 'POST':
        cursor = conn.cursor()
        codigo_pedido = request.form['CodigoPedido']
        fecha = request.form['Fecha']
        total = request.form['Total']
        metodo_pago = request.form['MetodoPago']
        estado = request.form['Estado']
        cursor.execute(
            "INSERT INTO facturas(CodigoPedido, Fecha, Total, MetodoPago, Estado) VALUES(%s, %s, %s, %s, %s)",
            (codigo_pedido, fecha, total, metodo_pago, estado)
        )
        conn.commit()
        return redirect(url_for('facturas_index'))
    elif request.method == 'GET':
        return render_template('/facturas/agregar.html')


@app.route("/facturas/editar/<string:factura_id>", methods=["GET", "POST"])
def facturas_editar_datos(factura_id):
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM facturas WHERE Factura_id=%s", (factura_id,))
        factura = cur.fetchone()
        return render_template('/facturas/editar.html', factura=factura)
    elif request.method == 'POST':
        cursor = conn.cursor()
        codigo_pedido = request.form['CodigoPedido']
        fecha = request.form['Fecha']
        total = request.form['Total']
        metodo_pago = request.form['MetodoPago']
        estado = request.form['Estado']
        cursor.execute(
            "UPDATE facturas SET CodigoPedido=%s, Fecha=%s, Total=%s, MetodoPago=%s, Estado=%s WHERE Factura_id=%s",
            (codigo_pedido, fecha, total, metodo_pago, estado, factura_id)
        )
        conn.commit()
        return redirect(url_for('facturas_index'))


@app.route("/facturas/eliminar/<string:factura_id>", methods=["GET", "POST"])
def facturas_eliminar_datos(factura_id):
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM facturas WHERE Factura_id=%s", (factura_id,))
        factura = cur.fetchone()
        return render_template('/facturas/eliminar.html', factura=factura)
    elif request.method == 'POST':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM facturas WHERE Factura_id=%s", (factura_id,))
        conn.commit()
        return redirect(url_for('facturas_index'))



if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)



