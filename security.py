# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:16:05 2021

@author: hp
"""

from werkzeug.security import safe_str_cmp
from Models.User import UserModel


def authenticate(username, password):
    user = UserModel.get_by_email(username)
    print("@authenticate: user:",user.json())
    if user and safe_str_cmp(user.pwd, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.get_by_id(user_id)