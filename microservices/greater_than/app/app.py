from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = '080_087_092_111'

class GreaterThan(Resource):
    def __init__(self):
        pass
    
    def get(self, n1, n2):
        return n1 > n2

api.add_resource(GreaterThan, "/gt/<float:n1>/<float:n2>")

if __name__ == "__main__":
    app.run(
        debug = True,
        port = 5059,
        host = "0.0.0.0"
    )
