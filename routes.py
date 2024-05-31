from flask import Blueprint, render_template,request,redirect,flash
from models import Producto, Albaran, Facturacion,db
from form import ProductosForm, AlbaranForm
main = Blueprint("main",__name__)



@main.route("/")
def home():
   return render_template("index.html")

@main.route('/productos',methods=["GET","POST"])
def mostrar_productos():
    productos = Producto.query.all()
    return render_template("productos.html",productos=productos)



@main.route('/albaranes', methods=["GET", "POST"])
def crear_albaranes():
    productos = Producto.query.all()
    albaranes = Albaran.query.all()
    form = ProductosForm()
    form.producto.choices = [(producto.id_producto, producto.nombre) for producto in productos]
    productToEdit = Producto.query.filter_by(id_producto=form.producto.data).first()
    if (productToEdit):
        productToEdit.cantidad += form.cantidad.data
        newAlbaran=Albaran(id_producto=productToEdit.id_producto, cantidad_pedido=form.cantidad.data)
        db.session.add(newAlbaran)
        db.session.commit()
        flash('✅Se ha realizado el albaran correctamente','success')
        redirect("/albaranes")
  
        
    return render_template("albaranes.html",form = form,albaranes=albaranes)

@main.route('/albaranes/edit', methods=["GET", "POST"])
def editar_albaranes():
    productos = Producto.query.all()
    albaranes = Albaran.query.all()
    form = AlbaranForm()
    form.id_albaran.choices = [(albaran.id_albaran, albaran.id_albaran) for albaran in albaranes]
    
    
    
    # productToEdit = Producto.query.filter_by(id_producto=form.producto.data).first()
    # if (productToEdit):
    #     productToEdit.cantidad += form.cantidad.data
    #     newAlbaran=Albaran(id_producto=productToEdit.id_producto, cantidad_pedido=form.cantidad.data)
    #     db.session.add(newAlbaran)
    #     db.session.commit()
    #     print('Se ha realizado el albaran correctamente')
    #     redirect("/albaranes")
    # else:
    #     print("NO SE HA ENCONTRADO EL PRODUCTO EN LA BASE DE DATOS")
        
    return render_template("albaranesEdit.html",form = form,albaranes=albaranes)




@main.route('/facturacion', methods=["GET", "POST"])
def crear_facturas():
    productos = Producto.query.all()
    facturas = Facturacion.query.all()
    form = ProductosForm()
    form.producto.choices = [(producto.id_producto, producto.nombre) for producto in productos]

    productToEdit = Producto.query.filter_by(id_producto=form.producto.data).first()
    if (productToEdit):
        if(productToEdit.cantidad >= form.cantidad.data):
            productToEdit.cantidad -= form.cantidad.data
            newFactura=Facturacion(id_producto=productToEdit.id_producto, cantidad_vendida=form.cantidad.data)
            db.session.add(newFactura)
            db.session.commit()
            flash('✅Se ha realizado la factura correctamente','success')
            redirect("/albaranes")
        else:
            flash("❌NO SE PUEDE VENDER MAS PRODUCTOS DE LOS QUE HAY EN STOCK",'error')

    return render_template("facturas.html",form=form,facturas=facturas)
