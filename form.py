from flask_wtf import FlaskForm
from wtforms import validators, StringField,IntegerField, SelectField

class PostForm(FlaskForm):
    title = StringField("Title", [
        validators.DataRequired(),
        validators.Length(min=4, max=200)
        ])

class ProductosForm(FlaskForm):
    producto = SelectField('Producto', choices=[], coerce=int)
    cantidad = IntegerField('Cantidad', validators=[validators.DataRequired(), validators.NumberRange(min=1)])

class AlbaranForm(FlaskForm):
    id_albaran = SelectField('id_albaran', choices=[], coerce=int)
    id_producto = IntegerField('id_producto', validators=[validators.DataRequired(), validators.NumberRange(min=0)])
    cantidad_pedido = IntegerField('cantidad_pedido', validators=[validators.DataRequired(), validators.NumberRange(min=0)])
    proveedor = StringField('proveedor',[validators.Length(min=4, max=200)])
    usuario=StringField('proveedor',[validators.Length(min=2, max=100)])