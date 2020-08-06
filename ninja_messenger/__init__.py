import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localhost.sqlite'
#db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from ninja_messenger import routes


    #session_token = request.cookies.get("session_token")
    #if session_token:
    #    user = db.query(User).filter_by(session_token=session_token).first()
    #else:
     #   user = None

    #return render_template("index.html", user=user)


    #response = make_response(render_template("index.html"))
    #if not secret_number:
    #    secret_number = randint(1,30)
    #   response.set_cookie("secret_number", str(secret_number))

    #return response




#@app.route("/login", methods=["GET", "POST"])
#def login():

 #   email = request.form.get("user-email")
  #  password = request.form.get("user-password")

   # return render_template('login.html')


#@app.route("/register", methods=["GET", "POST"])
#def register():
 #   name = request.form.get("user-name")
  #  email = request.form.get("user-email")
   # password = request.form.get("user-password")

#    return render_template('register.html')



