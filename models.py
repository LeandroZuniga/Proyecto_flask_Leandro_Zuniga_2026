from base import db
 
class Pedido(db.Model):
    __tablename__ = 'pedidos'
    Codigo      = db.Column(db.Integer, primary_key=True)
    Nombre      = db.Column(db.String(100))
    Stock       = db.Column(db.Integer)
    NombreCaja  = db.Column(db.String(100))
    Telefono    = db.Column(db.String(50))
    Direccion   = db.Column(db.String(255))
 
    def __repr__(self):
        return f'<Pedido {self.Nombre}>'
 
 
class Factura(db.Model):
    __tablename__ = 'facturas'
    Factura_id   = db.Column(db.Integer, primary_key=True)
    CodigoPedido = db.Column(db.Integer)
    Fecha        = db.Column(db.Date)
    Total        = db.Column(db.Float)
    MetodoPago   = db.Column(db.String(100))
    Estado       = db.Column(db.String(100))
 
    def __repr__(self):
        return f'<Factura {self.Factura_id}>'