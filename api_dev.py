from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#lista desenvolvedores

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

    # o metodo PUT vai atualizar ou criar recursos. ele é usado para atualizar os dados de um usuario por exemplo.
    # ele é usado para alterações completas.
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'registro excluido'})

# lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route('/dev/', methods = ['POST', 'GET', 'DELETE'])
def lista_desenvolvedores():

    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)

        # agora eu quero inserir tbm um ID para o desenvolvedor então
        posicao = len(desenvolvedores)

        #crio uma nova variavel chamada ID dentro da lista
        dados['ID'] = posicao
        # acrescentando a lista de desenvolvedores a nova variável ID
        desenvolvedores.append(dados)

        mensagem = 'desenvolvedor inserido com sucesso'
        return jsonify({'status': 'sucesso!', 'mensagem': mensagem}, desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)