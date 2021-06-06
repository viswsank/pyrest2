# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:30:49 2021

@author: hp
"""
import os
import psycopg2

class UserModel():
    TABLE_NAME = 'user_dtls'
    DATABASE_URL = os.environ['DATABASE_URL']  
    
    def __init__(self, _id, nameu, email, pwd, admin):
        print('DATABASE_URL:',self.DATABASE_URL)
        self.id = _id
        self.nameu = nameu
        self.email = email
        self.pwd = pwd
        self.admin = admin
        
    def json(self):
        return {"id": self.id, 
                "nameu": self.nameu,
                "email": self.email,
                "pwd": self.pwd,
                "admin": self.admin
                }
    
    @classmethod
    def get_by_email(cls, email):      
        connection = psycopg2.connect(cls.DATABASE_URL)  
        cursor = connection.cursor()
        query = "SELECT id, nameu, email, pwd, admin FROM {0} WHERE email='{1}'".format(cls.TABLE_NAME,email)
        print("\nquery @UserModel @get_by_email:",query)
        cursor.execute(query)
        
        row = cursor.fetchone()
        if row:
            print(row)
            user = cls(*row)
        else:
            print("no results fetched")
            user = None

        connection.close()
        return user
    @classmethod
    def get_by_id(cls, _id): 
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "SELECT id, nameu, email, pwd, admin FROM {0} WHERE id='{1}'".format(cls.TABLE_NAME,_id)
        #print("\nquery @UserModel @get_by_id:",query)
        cursor.execute(query)
        
        row = cursor.fetchone()
        if row:
            print(row)
            user = cls(*row)
        else:
            print("no results fetched")
            user = None

        connection.close()
        return user
    @classmethod
    def get_list(cls):
        
        print('DATABASE_URL:',cls.DATABASE_URL) 
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "SELECT id, nameu, email, pwd, admin FROM {0}".format(cls.TABLE_NAME)
        print("\nquery @UserModel @get_list:",query)
        cursor.execute(query)
        
        rows = cursor.fetchall()
        ul=[]
        for row in rows:
            #print(row)
            user = cls(*row)
            ul.append(user)
            print(user.json())
        connection.close()
        return ul
    def save_to_db(self): 
        connection = psycopg2.connect(self.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "INSERT INTO {0}(nameu, email, pwd, admin) VALUES ('{1}','{2}','{3}','{4}')".format(self.TABLE_NAME, self.nameu, self.email, self.pwd, self.admin)
        print("\nquery @UserModel @save_to_db:",query)
        cursor.execute(query)
        connection.commit()

        connection.close()
        return True
        