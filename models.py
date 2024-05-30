import models

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from sqlalchemy import Column, Date, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Productos(db.Model):
    __tablename__ = 'productos'
    ID = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)

# class Albaran(db.Model):
#     __tablename__ = 'albaranes'
#     id = Column(Integer, primary_key=True)
#     fecha_recepcion = Column(Date, nullable=False)
#     proveedor = Column(String(255), nullable=False)
#     lineas_albaran = relationship("LineaAlbaran", backref="albaran")

# class LineaAlbaran(db.Model):
#     __tablename__ = 'lineas_albaran'
#     id = Column(Integer, primary_key=True)
#     albaran_id = Column(Integer, ForeignKey('albaranes.id'), nullable=False)
#     producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
#     cantidad = Column(Integer, nullable=False)
#     producto = relationship("Producto")

# class Factura(db.Model):
#     __tablename__ = 'facturas'
#     id = Column(Integer, primary_key=True)
#     fecha_venta = Column(Date, nullable=False)
#     cliente = Column(String(255), nullable=False)
#     lineas_factura = relationship("LineaFactura", backref="factura")

# class LineaFactura(db.Model):
#     __tablename__ = 'lineas_factura'
#     id = Column(Integer, primary_key=True)
#     factura_id = Column(Integer, ForeignKey('facturas.id'), nullable=False)
#     producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
#     cantidad = Column(Integer, nullable=False)
#     producto = relationship("Producto")