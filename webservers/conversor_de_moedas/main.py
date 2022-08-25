from app import app

if __name__ == "__main__":
  # inicializa o servidor web aberto para rede externa
  app.run(host="0.0.0.0")
