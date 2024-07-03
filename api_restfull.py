from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'ID': 0,
        'nome': 'Juarez',
        'habilidades': 'frontend'
    },

    {
        'ID': 1,
        'nome': 'Juguernauth',
        'habilidades': 'backend'
    }
]

class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não exeiste'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    def delete(self, id):
        desenvolvedores.pop(id)
        return jsonify({'status': 'registro excluido'})

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        posicao = len(desenvolvedores)
        dados['ID'] = posicao
        desenvolvedores.append(dados)

        mensagem = 'desenvolvedor inserido com sucesso'
        return jsonify({'status': 'sucesso!', 'mensagem': mensagem}, desenvolvedores[posicao])


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)