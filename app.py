from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    #port default is 5000
    #debug true means the program refreshes after changes automatically
    #views are the endpoints of a website like /home
    app.run(debug=True, port=8000)