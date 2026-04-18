@app.route("/")
def home():
    return '''
    <html>
    <head>
        <title>Cadastro</title>
        <style>
            body {
                background-color: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                margin-top: 50px;
            }

            h1 {
                font-size: 40px;
            }

            input {
                padding: 10px;
                border-radius: 10px;
                border: none;
                outline: none;
                width: 200px;
            }

            button {
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                background-color: #22c55e;
                color: white;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                background-color: #16a34a;
                transform: scale(1.1);
            }

            a {
                display: block;
                margin-top: 20px;
                color: #38bdf8;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>

    <body>
        <h1>Cadastro 😎</h1>

        <form method="POST" action="/salvar">
            <input name="nome" placeholder="Digite seu nome">
            <br><br>
            <button type="submit">Enviar</button>
        </form>

        <a href="/ver">Ver nomes</a>
    </body>
    </html>
    '''
