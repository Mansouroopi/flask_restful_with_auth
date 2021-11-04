# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)


# class ProductResource(Resource):
#     def get(self):
#         return [{'name': 'some product', 'price': 100, 'stock': 12},
#                 {'name': 'some product1', 'price': 200, 'stock': 24},
#                 {'name': 'some product2', 'price': 300, 'stock': 36}]



# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')
# api.add_resource(ProductResource, '/products')
# if __name__ == '__main__':
#     app.run(debug=True)