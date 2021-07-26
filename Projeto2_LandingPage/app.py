from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message

app = Flask(__name__)

mail_settings ={
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'coletivoturmac6blue@gmail.com',
    "MAIL_PASSWORD": 'BlueC6123'
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self,nome,email,mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']
        )

        msg =Message(
            subject="Email de contato - Portifólio Victor Luz",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["victor.fernando.moura@hotmail.com"],
            body=f'''O {formContato.nome}, com e-mail de contato {formContato.email}, enviou a seguinte mensagem:
            {formContato.mensagem}
            '''
        )

        mail.send(msg)
        return render_template('send.html',formContato=formContato)
    
if __name__ == '__main':
    app.run(debug=True)