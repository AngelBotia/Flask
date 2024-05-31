from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Date, Integer, String, ForeignKey, Column, Numeric,TIMESTAMP,func
import models
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'producto'
    id_producto = Column(Integer, primary_key=True,autoincrement=True)
    cantidad = Column(Integer, nullable=False)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(String(255))
    precio_unitario = Column(Numeric(precision=10,scale=2), nullable=False)
    albaran = relationship('Albaran',backref='producto')
    facturacion = relationship('Facturacion', backref='producto')
class Albaran(db.Model):
    __tablename__ = 'albaran'
    id_albaran = Column(Integer, primary_key=True,autoincrement=True)
    id_producto = Column(Integer,ForeignKey('producto.id_producto'),nullable=False)
    cantidad_pedido = Column(Integer, nullable=False)
    proveedor = Column(String(200),server_default='Proveedor de ejemplo')
    fecha_creacion = Column(TIMESTAMP,server_default = func.current_timestamp(), comment='Se guarda la fecha actual ya que se entiende que si se ha registrado en la base de datos significa que todo el proceso a sido un exito')
    usuario = Column(String(100),server_default='Usuario de ejemplo')

class Facturacion(db.Model):
    __tablename__ = 'facturacion'
    id_factura= Column(Integer,primary_key=True,autoincrement=True)
    id_producto = Column(Integer, ForeignKey('producto.id_producto'),nullable=False)
    cantidad_vendida = Column(Integer,nullable=False)
    fecha_venta = Column(TIMESTAMP,server_default = func.current_timestamp(), comment='Se guarda la fecha actual ya que se entiende que si se ha registrado en la base de datos significa que todo el proceso a sido un exito')
    id_cliente = Column(String(100),server_default='Cliente ejemplo')