from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
jwt = JWTManager(app)

# Импорт и регистрация blueprint'ов
# from .routes import main, auth, catalog, cart, orders, sales, delivery, contacts, favorites, profile
# app.register_blueprint(main)
# app.register_blueprint(auth)
# ...

if __name__ == '__main__':
    app.run(debug=True) 