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
    form = ProductosForm()
   
    try:    
        newProduct= Producto(cantidad=0,nombre=form.nombre.data,descripcion=form.descripcion.data,precio_unitario=form.precio_unitario.data)
        if not Producto.query.filter_by(nombre=newProduct.nombre).first():#usaremos el nombre como identificador para que no se duplique
         db.session.add(newProduct)
         db.session.commit()
         flash('✅Se ha añadido el producto correctamente','success')
         redirect("/productos")
    except Exception as e:
        db.session.rollback()
        print("Hubo un problema durante la insercion del producto")
    return render_template("productos.html",productos=productos,form=form)



@main.route('/albaranes', methods=["GET", "POST"])
def crear_albaranes():
    productos = Producto.query.all()
    albaranes = Albaran.query.all()
    formAlbaran = AlbaranForm()
    formAlbaran.id_producto.choices = [(producto.id_producto, producto.nombre) for producto in productos]
    productToEdit = Producto.query.filter_by(id_producto=formAlbaran.id_producto.data).first()
    if formAlbaran.validate_on_submit() and productToEdit: 
        newAlbaran=Albaran(id_producto=productToEdit.id_producto,
                            cantidad_pedido=formAlbaran.cantidad_pedido.data,
                            proveedor=formAlbaran.proveedor.data,
                            usuario=formAlbaran.usuario.data)
        
      
        db.session.add(newAlbaran)
        productToEdit.cantidad += formAlbaran.cantidad_pedido.data
        db.session.commit()
        formAlbaran.proveedor.data=""
        formAlbaran.usuario.data=""
        flash('✅Se ha realizado el albaran correctamente','success')
        return redirect("/albaranes")
    else:
        flash('❌ Hubo un problema durante la creacion del albaran')
        
    return render_template("albaranes.html",albaranes=albaranes,formAlbaran=formAlbaran)

@main.route('/albaranes/edit', methods=["GET", "POST"])
def editar_albaranes():
    productos = Producto.query.all()
    albaranes = Albaran.query.all()
    formAlbaran = AlbaranForm()
    formAlbaran.id_albaran.choices = [(albaran.id_albaran, albaran.id_albaran) for albaran in albaranes]
    formAlbaran.id_producto = [(producto.id_producto, producto.nombre) for producto in productos]
    
    
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
        
    return render_template("albaranesEdit.html",form=formAlbaran,albaranes=albaranes,productos=productos)




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
            redirect("/facturacion")
        else:
            flash("❌NO SE PUEDE VENDER MAS PRODUCTOS DE LOS QUE HAY EN STOCK",'error')

    return render_template("facturas.html",form=form,facturas=facturas)
