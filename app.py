from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Pessoa nao encontrada'
            }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')

if __name__ == '__main__':
    app.run(debug=True)