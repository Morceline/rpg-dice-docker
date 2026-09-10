from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    resultado = random.randint(1, 20)
    efeito = ""
    
    if resultado == 20:
        mensagem = "🎯 ACERTO CRÍTICO! O dragão chora perante sua glória!"
        efeito = "brilho-dourado"
    elif resultado == 1:
        mensagem = "💀 FALHA CRÍTICA! Você atacou o próprio pé e tomou dano..."
        efeito = "tela-tremendo"
    elif resultado <= 9:
        mensagem = "😬 Rolagem ruim... Tente se esconder ou correr!"
    else:
        mensagem = "⚔️ Boa rolagem, aventureiro! Prepare o ataque!"
        
    return render_template("face.html", resultado=resultado, mensagem=mensagem, efeito=efeito)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)