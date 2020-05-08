from datetime import timedelta

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from db import db

from resources.item import Item, ItemList
from security import authenticate, identity
from resources.user_register import UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data-Sec6.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'kdjfsdjjkf'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


# JWT configuration options
app.config['JWT_AUTH_URL_RULE'] = '/login'
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# config JWT auth key name to be 'email' instead of default 'username'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister,'/register')

db.init_app(app)
if __name__ == '__main__':
    # db.init_app(app)
    app.run(debug=True)
