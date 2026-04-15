import flask
import flask_cors
import Conexao
import Calculo
import Tabela

app = flask.Flask(__name__)
flask_cors.CORS(app)

Tabela.Base.metadata.create_all(bind=Conexao.engine)

@app.route("/api/calcular", methods=["POST"])

def calcular():
    try:
        dado = flask.request.get_json()
        valor = float(dado["valor"])
        nome = str(dado["nome"])
        desconto = float(dado["desconto"])
        vip = bool(dado["vip"])

        cashback = Calculo.calculadora_de_cashback(valor, desconto, vip)

        banco_dados = Conexao.SessionLocal()

        ip = flask.request.headers.get("x-forwarded-for", flask.request.remote_addr)

        registro = Tabela.Historico(ip=ip,nome=nome, valor=valor, desconto=desconto, cashback=cashback) 

        banco_dados.add(registro)
        banco_dados.commit()
        banco_dados.close()

        return flask.jsonify({"cashback": cashback})
    except Exception as e:
        print("ERRO:", e)
        return flask.jsonify({"erro": str(e)}), 500

@app.route("/api/historico", methods=["GET"])

def historico():

    banco_dados = Conexao.SessionLocal()
    ip = flask.request.headers.get("x-forwarded-for", flask.request.remote_addr)
    registros = banco_dados.query(Tabela.Historico).filter(Tabela.Historico.ip == ip).all()

    historico_list = []

    for registro in registros:
        historico_list.append({"id": registro.id, "ip": registro.ip, "nome": registro.nome, "valor": registro.valor, "desconto": registro.desconto, "cashback": registro.cashback})

    banco_dados.close()
    return flask.jsonify(historico_list)

if __name__ == "__main__":
    app.run(debug=True)
