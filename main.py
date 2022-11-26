from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    """
    get the user's ip, and saved ip user in a cookie
    and finally we are going to redirect it to the /hello route
    """

    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response



@app.route('/hello')
def hello():
    """
    get cookie user
    """
    user_ip = request.cookies.get('user_ip')
    return f'Hola te hackee, tu ip es: {user_ip}'






