from flask_wtf import FlaskForm
from wtforms import validators, StringField,IntegerField, SelectField

class PostForm(FlaskForm):
    title = StringField("Title", [
        validators.DataRequired(),
        validators.Length(min=4, max=200)
        ])

class ProductosForm(FlaskForm):
    nombre = StringField('nombre',[validators.Length(min=4, max=200)])
    descripcion = StringField('descripcion',[validators.Length(min=4, max=255)])
    precio_unitario = IntegerField('precio', validators=[validators.DataRequired(), validators.NumberRange(min=0)])


class AlbaranForm(FlaskForm):
    id_producto =  SelectField('id_producto', choices=[], coerce=int)
    cantidad_pedido = IntegerField('cantidad_pedido', validators=[validators.DataRequired(), validators.NumberRange(min=1)])
    proveedor = StringField('proveedor',[validators.Length(min=4, max=200)])
    usuario=StringField('proveedor',[validators.Length(min=2, max=100)])

class FacturasForm(FlaskForm):
    id_producto =  SelectField('id_producto', choices=[], coerce=int)
    cantidad_vendida = IntegerField('cantidad_vendida', validators=[validators.DataRequired(), validators.NumberRange(min=1)])
    id_cliente=StringField('proveedor',[validators.Length(min=2, max=100)])