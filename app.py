def welcome_page():
    return "Bienvenido a la primera pagina de Emilia. <a href='/Miguel'> Miguel_page</a>"
def Miguel_page():
    return"klk.  <a href='/'> back</a>"

import flask
web_app= flask.Flask(__name__)
web_app.route("/")(welcome_page)
web_app.route("/Miguel")(Miguel_page)
web_app.run()