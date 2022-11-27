from flask import Blueprint, render_template, make_response, redirect, request

app_router = Blueprint('app_router', __name__)

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar producto']

@app_router.route('/')
def index():
    """
    * get the user's ip, and saved ip user in a cookie
    * finally we are going to redirect it to the /hello route
    """

    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response



@app_router.route('/hello')
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
