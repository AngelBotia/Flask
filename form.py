from flask_wtf import FlaskForm
from wtforms import validators, StringField,IntegerField, SelectField

class PostForm(FlaskForm):
    title = StringField("Title", [
        validators.DataRequired(),
        validators.Length(min=4, max=200)
        ])

class ProductosForm(FlaskForm):
    producto = SelectField('producto', choices=[], coerce=lambda x: int(x) if x is not None else None)
    cantidad = IntegerField('cantidad', validators=[validators.DataRequired(), validators.NumberRange(min=0)])
    nombre = StringField('nombre',[validators.Length(min=4, max=200)])
    descripcion = StringField('descripcion',[validators.Length(min=4, max=255)])
    precio_unitario = IntegerField('precio', validators=[validators.DataRequired(), validators.NumberRange(min=0)])
class AlbaranForm(FlaskForm):
    id_albaran = SelectField('id_albaran', choices=[], coerce=int)
    id_producto =  SelectField('id_producto', 'Producto', choices=[], coerce=int)
    cantidad_pedido = IntegerField('cantidad_pedido', validators=[validators.DataRequired(), validators.NumberRange(min=1)])
    proveedor = StringField('proveedor',[validators.Length(min=4, max=200)])
    usuario=StringField('proveedor',[validators.Length(min=2, max=100)])