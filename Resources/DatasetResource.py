# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:02:26 2021

@author: hp
"""

from flask_restful import Resource, request
from Models.Dataset import DatasetModel

from flask_jwt import jwt_required

class DatasetResource(Resource):
    
    @jwt_required()
    def get(self):
        print("@DatasetResource:get")
        id = request.args.get('id')
        #print("id:",id)
        return DatasetModel.get_by_id(id).json()
    
    @jwt_required()
    def put(self):   
        #print(request.get_json())
        request_data = request.get_json()
        
        ds = DatasetModel(request_data['id'], 
                  request_data['Beach_Name'], 
                  request_data['Wave_Period'], 
                  request_data['Water_Temperature'], 
                  request_data['Turbidity'])
        #print(ds.json())
        if(ds.update()):
            return "Beach record successfully updated"
        
    @jwt_required()
    def post(self):   
        #print(request.get_json())
        request_data = request.get_json()
        
        ds = DatasetModel(request_data['id'], 
                  request_data['Beach_Name'], 
                  request_data['Wave_Period'], 
                  request_data['Water_Temperature'], 
                  request_data['Turbidity'])
        #print(ds.json())
        if(ds.add()):
            return "Beach record successfully updated"
        
    @jwt_required()
    def delete(self):   
        print("@DatasetResource:delete")
        beachName = request.args.get('BeachName')
        if beachName:            
            beachName = beachName.replace('+',' ')
        if(DatasetModel.delete(beachName)):
            return "Beach record successfully updated"
        else:
            return "Beach record delete failed"
    

class DatasetListResource(Resource):
    
    @jwt_required()
    def get(self):
        beachName = request.args.get('BeachName')
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        #print("BeachName:",beachName,"limit:",limit,"offset:",offset)
        if beachName:            
            beachName = beachName.replace('+',' ')
            return {"BeachRecords": [x.json() for x in DatasetModel.get_list_by_name(limit,offset,beachName)]}
        else:
            return {"BeachRecords": [x.json() for x in DatasetModel.get_list(limit,offset)]}
        
    @jwt_required()
    def post(self):
        request_data = request.get_json()
        bR=True
        for beachRec in request_data["BeachRecords"]:
            #print("@DatasetListResource:post beachRec: ",beachRec)
            ds = DatasetModel(
                    -999,
                    beachRec['Beach_Name'],
                    beachRec['Wave_Period'],
                    beachRec['Water_Temperature'],
                    beachRec['Turbidity'])
            #print("@DatasetListResource:ds.json()",ds.json())
            if(not ds.add()):
                bR=False
                print( "Beach record {0} add failed".format(beachRec['Beach_Name']))
        return bR