from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Inicializar la app
app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Definir el modelo de producto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Esquema del producto
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Endpoint para crear un producto
@app.route('/api/products', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    new_product = Product(name, price, quantity)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Endpoint para obtener todos los productos
@app.route('/api/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# Endpoint para obtener un producto por id
@app.route('/api/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Endpoint para actualizar un producto
@app.route('/api/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    product.name = name
    product.price = price
    product.quantity = quantity

    db.session.commit()
    return product_schema.jsonify(product)

# Endpoint para eliminar un producto
@app.route('/api/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
