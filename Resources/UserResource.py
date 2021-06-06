# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:50:08 2021

@author: hp
"""

from flask_restful import Resource, request
from Models.User import UserModel

class UserResource(Resource):
    
    '''
    def get(self, email):
        #print("args:",request.args.get)
        #email = request.args.get('email')
        print("email:",email)
        return UserModel.get_by_email(email)
        '''
    def get(self):
        return {"users": [x.json() for x in UserModel.get_list()]}
    
    def post(self):
        print(request.get_json())
        request_data = request.get_json()
        
        user = UserModel(None, 
                  request_data['nameu'], 
                  request_data['email'], 
                  request_data['pwd'], 
                  request_data['admin'])
        #print(user.json())
        if(user.save_to_db()):
            return "User successfully added"
        