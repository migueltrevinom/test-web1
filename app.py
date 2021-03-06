from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from config import Config
from Authentication.authentication import AuthenticationController, AuthenticationService
from Modules.KitchenModule.Controllers.KitchenController import KitchenController
from routes import Router
from flask import Flask
from Commands.BackgroundCommands import BackGroundCommandsController

app = Flask(__name__)
api = Api(app)
AuthenticationService.get_auth_token()
kitchen = KitchenController.init_kitchen()

# Steps
# must run export APP_SETTINGS=/path/settings.cfg first
# then python app.py

Router.init_routes(app, api)

BackGroundCommandsController.init()

if __name__ == '__main__':
    print('start server ' + __name__)
    app.run(host='0.0.0.0')
