from flask import Blueprint, render_template,request,redirect,flash
from models import Producto, Albaran, Facturacion,db
from form import AlbaranEditForm, ProductosForm, AlbaranForm, FacturasForm
main = Blueprint("main",__name__)



@main.route("/")
def home():
   return render_template("index.html")

@main.route('/productos',methods=["GET","POST"])
def mostrar_productos():
    productos = Producto.query.all()
    form = ProductosForm()
    if form.validate_on_submit():
     try:    
         newProduct= Producto(cantidad=0,nombre=form.nombre.data,
                              descripcion=form.descripcion.data,
                              precio_unitario=form.precio_unitario.data)
         if not Producto.query.filter_by(nombre=newProduct.nombre).first():#usaremos el nombre como identificador para que no se duplique
          db.session.add(newProduct)
          db.session.commit()
          form.nombre.data=""
          form.descripcion.data=""
          form.precio_unitario.data=""
          flash('✅Se ha añadido el producto correctamente','success')
          return redirect("/productos")
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
        
    return render_template("albaranes.html",albaranes=albaranes,formAlbaran=formAlbaran)

@main.route('/albaranes/edit', methods=["GET", "POST"])
def editar_albaranes():
    productos = Producto.query.all()
    albaranes = Albaran.query.all()
    formAlbaran = AlbaranForm()
    formEditAlbaran = AlbaranEditForm()
    formEditAlbaran.id_albaran.choices = [(albaran.id_albaran, albaran.id_albaran) for albaran in albaranes]
    formAlbaran.id_producto.choices = [(producto.id_producto, producto.nombre) for producto in productos]
    
    if formEditAlbaran.validate_on_submit():
        albaranToEdit = Albaran.query.filter_by(id_albaran=formEditAlbaran.id_albaran.data).first()
        albaranToEdit.id_producto= formAlbaran.id_producto.data
        albaranToEdit.cantidad_pedido= formAlbaran.cantidad_pedido.data
        albaranToEdit.usuario= formAlbaran.usuario.data
        albaranToEdit.proveedor= formAlbaran.proveedor.data
        db.session.add(albaranToEdit)
        db.session.commit()

        formAlbaran.cantidad_pedido.data=0
        formAlbaran.usuario.data=''
        formAlbaran.proveedor.data=''
        flash('✅Se ha realizado el albaran correctamente','success')
        return redirect('/albaranes/edit')
        
    return render_template("albaranesEdit.html",form=formAlbaran,albaranes=albaranes,formEditAlbaran=formEditAlbaran)

@main.route('/albaranes/delete', methods=["GET", "POST"])
def borrar_albaranes():
    productos = Producto.query.all()
    albaranes = Albaran.query.all()
    formAlbaran = AlbaranForm()
    formEditAlbaran = AlbaranEditForm()
    formEditAlbaran.id_albaran.choices = [(albaran.id_albaran, albaran.id_albaran) for albaran in albaranes]
    formAlbaran.id_producto.choices = [(producto.id_producto, producto.nombre) for producto in productos]
    
    if formEditAlbaran.validate_on_submit():
        albaranToEdit = Albaran.query.filter_by(id_albaran=formEditAlbaran.id_albaran.data).first()
        db.session.delete(albaranToEdit)
        db.session.commit()
        flash('✅Se ha borrado el albaran correctamente','success')
        return redirect('/albaranes/delete')
        
    return render_template("alabaranesDelete.html",form=formAlbaran,albaranes=albaranes,formEditAlbaran=formEditAlbaran)




@main.route('/facturacion', methods=["GET", "POST"])
def crear_facturas():
    productos = Producto.query.all()
    facturas = Facturacion.query.all()
    form = FacturasForm()
    form.id_producto.choices = [(producto.id_producto, producto.nombre) for producto in productos]

    productToEdit = Producto.query.filter_by(id_producto=form.id_producto.data).first()
    if form.validate_on_submit() and productToEdit: 
        if(productToEdit.cantidad >= form.cantidad_vendida.data):
            productToEdit.cantidad -= form.cantidad_vendida.data
            newFactura=Facturacion(id_producto=productToEdit.id_producto,
                                   cantidad_vendida=form.cantidad_vendida.data,
                                   id_cliente=form.id_cliente.data)
            db.session.add(newFactura)
            db.session.commit()
            form.cantidad_vendida.data=0
            form.id_cliente.data=""
            flash('✅Se ha realizado la factura correctamente','success')
            return redirect("/facturacion")
        else:
            flash("❌NO SE PUEDE VENDER MAS PRODUCTOS DE LOS QUE HAY EN STOCK",'error')
    return render_template("facturas.html",form=form,facturas=facturas)
