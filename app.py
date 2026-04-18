from flask import Flask, request, redirect
import os

app = Flask(__name__)

ARQUIVO = "dados.txt"
SENHA = "0314"

@app.route("/")
def home():
    return '''
    <html>
    <head>
        <title>Cadastro</title>
        <style>
            body {
                background: linear-gradient(135deg, #0f172a, #020617);
                color: white;
                font-family: Arial;
                text-align: center;
                margin-top: 80px;
            }

            h1 {
                font-size: 45px;
                text-shadow: 0 0 15px #22c55e;
            }

            input {
                padding: 12px;
                border-radius: 12px;
                border: none;
                width: 220px;
            }

            button {
                padding: 12px 25px;
                border-radius: 12px;
                background-color: #22c55e;
                color: white;
                border: none;
                cursor: pointer;
            }

            a {
                display: block;
                margin-top: 20px;
                color: #38bdf8;
            }

            .box {
                background-color: rgba(255,255,255,0.05);
                padding: 30px;
                border-radius: 20px;
                display: inline-block;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>Cadastro:3</h1>

            <form method="POST" action="/salvar">
                <input name="nome" placeholder="Digite seu nomezinho:0">
                <br><br>
                <button type="submit">Enviar</button>
            </form>

            <a href="/ver">Ver nomes</a>
            <a href="/login">Login 🔐</a>
        </div>
    </body>
    </html>
    '''

@app.route("/salvar", methods=["POST"])
def salvar():
    nome = request.form.get("nome")

    with open(ARQUIVO, "a") as f:
        f.write(nome + "\n")

    return redirect("/")

@app.route("/ver")
def ver():
    try:
        with open(ARQUIVO, "r") as f:
            nomes = f.read()
            return f"""
            <html>
            <body style="background:#020617;color:white;text-align:center;font-family:Arial;">
            <h1>Nomes salvos</h1>
            <p>{nomes.replace("\\n","<br>")}</p>
            <a href="/">Voltar</a>
            </body>
            </html>
            """
    except:
        return "<h1>Nada salvo ainda</h1><a href='/'>Voltar</a>"

@app.route("/login")
def login():
    return '''
    <h1>Login</h1>
    <form method="POST" action="/auth">
        <input type="password" name="senha" placeholder="Senha">
        <button type="submit">Entrar</button>
    </form>
    '''

@app.route("/auth", methods=["POST"])
def auth():
    senha = request.form.get("senha")

    if senha == SENHA:
        return '''
        <html>
        <head>
        <style>
            body {
                background-color: black;
                color: #00ff00;
                font-family: monospace;
                text-align: center;
                margin-top: 100px;
            }

            h1 {
                font-size: 40px;
                text-shadow: 0 0 10px #00ff00;
            }

            p {
                animation: piscar 1s infinite;
            }

            @keyframes piscar {
                0% {opacity: 1;}
                50% {opacity: 0.2;}
                100% {opacity: 1;}
            }

            a {
                color: #00ff00;
                display: block;
                margin-top: 20px;
            }
        </style>
        </head>

        <body>
            <h1>ACESSO LIBERADEXX 💻</h1>
            <p>Invadindo sistema...</p>
            <p>Bypass firewall...</p>
            <p>Root access granted</p>
            <a href="/">Entrar no sistema</a>
        </body>
        </html>
        '''
    else:
        return '''
        <h1>Senha errada 😡</h1>
        <a href="/login">Tentar de novo</a>
        '''

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
