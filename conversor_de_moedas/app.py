from flask import Flask
from conversor_de_moedas import ConversorDeMoedas

# inicializa aplicação flask
app = Flask(__name__)
conversor = ConversorDeMoedas()

# define rota de chamada da api
@app.route("/convertemoeda/<valor_em_real>")
def converter_moeda(valor_em_real):
  return conversor.converter_real_para_dolar_e_euro(float(valor_em_real))
