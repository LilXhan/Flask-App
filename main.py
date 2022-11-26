from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar producto']


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






