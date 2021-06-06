# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:07:52 2021

@author: hp
"""

from flask import Flask
from flask_restful import Api

#security related imports
from flask_jwt import JWT
from security import authenticate, identity

#User defined resources
from Resources.UserResource import UserResource
from Resources.DatasetResource import DatasetListResource, DatasetResource


app = Flask(__name__)
app.secret_key = 'pranav'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserResource,"/userlist")
api.add_resource(DatasetListResource,"/datasetlist")
api.add_resource(DatasetResource,"/dataset")



if __name__ == '__main__':
    app.run(host='localhost', port=5100)  