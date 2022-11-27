from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar producto']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    """
    * get the user's ip, and saved ip user in a cookie
    * finally we are going to redirect it to the /hello route
    """

    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response



@app.route('/hello')
def hello():
    """
    * get cookie user
    * render html and we passed the user ip
    """
    user_ip = request.cookies.get('user_ip')

    kwargs = {
        'user_ip': user_ip,
        'todos': todos
    }
    
    return render_template('hello.html', **kwargs)







