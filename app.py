from flask import Flask
from flask_restful import Api
from flask_apispec import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_swagger_ui import get_swaggerui_blueprint

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "REST API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# APISpec specification
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='REST API',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': SWAGGER_URL,
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})
docs = FlaskApiSpec(app)

# Import resources and register with API
from resources.product import ProductResource, ProductByIdResource

api = Api(app)
api.add_resource(ProductResource, '/api/products', endpoint='product_resource')
api.add_resource(ProductByIdResource, '/api/products/<int:id>', endpoint='product_by_id_resource')

# Register resources for documentation
docs.register(ProductResource)
docs.register(ProductByIdResource)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
