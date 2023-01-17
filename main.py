from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import mail_username, mail_password

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods =['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        subject = request.form.get('subject')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(
            subject=f"Mail from {name}", 
            body=f"Name: {name}\nSubject: {subject}\nE-mail: {email}\n\n{message}",
            sender = mail_username,
            recipients = [f"{mail_username}"]
        ) 

        mail.send(msg)


        return render_template('send_msg.html', success = True)

    return render_template('index.html')