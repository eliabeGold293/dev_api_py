from flask import Flask, jsonify, request
import json
app = Flask(__name__)

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

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):

    if request.method == 'GET':

        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não exeiste'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'registro excluido'})

@app.route('/dev/', methods = ['POST', 'GET', 'DELETE'])
def lista_desenvolvedores():

    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        posicao = len(desenvolvedores)
        dados['ID'] = posicao
        desenvolvedores.append(dados)

        mensagem = 'desenvolvedor inserido com sucesso'
        return jsonify({'status': 'sucesso!', 'mensagem': mensagem}, desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)