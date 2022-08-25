import socket
import requests
import json

BRL = "BRL"
USD = "USD"
EUR = "EUR"
ASK = "ask"

class ConversorDeMoedas():
  def __init__(self):
    self.moedas = f"{BRL}-{USD},{BRL}-{EUR}"
    self.url = "https://economia.awesomeapi.com.br/last/"

  # realiza a requisicao na api de conversao
  def __realizar_requisicao(self):
    requisicao = requests.get(self.url + self.moedas)
    
    return requisicao.json()

  # converte o valor na moeda de saida
  def __converter_valor(self, json_entrada, valor, moeda_saida):
    return float(json_entrada[f"{BRL}{moeda_saida}"][ASK]) * valor

  # formata o valor para ficar com, no maximo, duas casas decimais
  def __formatar_valor(self, valor):
    return float(f"{valor:.2f}")

  # retorna o json com os dados pedidos no enunciado
  def converter_real_para_dolar_e_euro(self, valor):
    json_entrada = self.__realizar_requisicao()
    valor_em_dolar = self.__converter_valor(json_entrada, valor, USD)
    valor_em_euro = self.__converter_valor(json_entrada, valor, EUR)

    return json.dumps({
      "maquina": socket.gethostname(),
      "conversao" : {
        "real": self.__formatar_valor(valor),
        "dolar": self.__formatar_valor(valor_em_dolar),
        "euro": self.__formatar_valor(valor_em_euro)
      }
    })

  def teste(self):
    print(self.converter_real_para_dolar_e_euro(6.73))

if __name__ == "__main__":
  c = ConversorDeMoedas()
  c.teste()
