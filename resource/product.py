from flask_restful import Resource
from flask_apispec import doc, marshal_with
from models.product import Product
from schemas.product import ProductSchema

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class ProductResource(Resource):

    @doc(description='Create a new product', tags=['Product'])
    @marshal_with(product_schema)
    def post(self):
        # Logic to create a new product
        pass

    @doc(description='Get all products', tags=['Product'])
    @marshal_with(products_schema)
    def get(self):
        # Logic to get all products
        pass

class ProductByIdResource(Resource):

    @doc(description='Get a product by ID', tags=['Product'])
    @marshal_with(product_schema)
    def get(self, id):
        # Logic to get a product by ID
        pass

    @doc(description='Update a product by ID', tags=['Product'])
    @marshal_with(product_schema)
    def put(self, id):
        # Logic to update a product by ID
        pass

    @doc(description='Delete a product by ID', tags=['Product'])
    @marshal_with(product_schema)
    def delete(self, id):
        # Logic to delete a product by ID
        pass
