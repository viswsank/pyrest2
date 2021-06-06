# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:46:37 2021

@author: hp
"""

import os
import psycopg2

class DatasetModel():
    TABLE_NAME = 'dataset'
    DATABASE_URL = os.environ['DATABASE_URL']  
    
    def __init__(self, _id, beach_Name, wave_Period, water_Temperature, turbidity,
                 measurement_Timestamp=None, transducer_Depth=None, wave_Height=None, 
                 battery_Life=None, measurement_Timestamp_Label=None, measurement_ID=None):
        #print('DATABASE_URL:',self.DATABASE_URL)
        self.id = _id
        self.beach_Name = beach_Name
        self.wave_Period = wave_Period
        self.water_Temperature = water_Temperature
        self.turbidity = turbidity 
        
        '''
        #Unused in updates
        self.measurement_Timestamp = measurement_Timestamp;
        self.transducer_Depth = transducer_Depth;
        self.wave_Height = wave_Height;
        self.battery_Life = battery_Life;
        self.measurement_Timestamp_Label = measurement_Timestamp_Label;
        self.measurement_ID = None; 
        '''
        
    def json(self):
        #Note: Decimal is not json seriablizable so converting it to float for printing purpose
        return {"id": self.id, 
                "Beach_Name": self.beach_Name,
                "Wave_Period": float(self.wave_Period),
                "Water_Temperature": float(self.water_Temperature),
                "Turbidity": float(self.turbidity)
                }
    
    @classmethod
    def get_list(cls, limit, offset):   
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "SELECT id,Beach_Name,Wave_Period,Water_Temperature,Turbidity FROM {0} ORDER BY id LIMIT {1} OFFSET {2}".format(cls.TABLE_NAME, limit, offset)
        print("\nquery @DatasetModel @get_list:",query)
        cursor.execute(query)
        
        rows = cursor.fetchall()
        dsl=[]
        for row in rows:
            #print(row)
            ds = cls(*row)
            #print(ds.json())
            dsl.append(ds)
        connection.close()
        return dsl
    
    @classmethod
    def get_list_by_name(cls, limit, offset, beachName):   
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "SELECT id,Beach_Name,Wave_Period,Water_Temperature,Turbidity FROM {0} WHERE Beach_Name={1} ORDER BY id LIMIT {2} OFFSET {3}".format(cls.TABLE_NAME,beachName, limit, offset)
        print("\nquery @DatasetModel @get_list_by_name:",query)
        cursor.execute(query)
        
        rows = cursor.fetchall()
        dsl=[]
        for row in rows:
            #print(row)
            ds = cls(*row)
            #print(ds.json())
            dsl.append(ds)
        connection.close()
        return dsl
    
    @classmethod
    def get_by_id(cls, _id):   
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "SELECT id,Beach_Name,Wave_Period,Water_Temperature,Turbidity FROM {0} WHERE id={1}".format(cls.TABLE_NAME, _id)
        print("\nquery @DatasetModel @get_by_id:",query)
        cursor.execute(query)
        
        row = cursor.fetchone()
        return cls(*row)
    
    
    def update(self): 
        connection = psycopg2.connect(self.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "UPDATE {0} SET Beach_Name ='{1}', Wave_Period={2}, Water_Temperature= {3}, Turbidity={4} where id={5}".format(self.TABLE_NAME, self.beach_Name, self.wave_Period, self.water_Temperature, self.turbidity, self.id)
        print("\nquery @DatasetModel @update:",query)
        cursor.execute(query)
        connection.commit()
        return True
    
    
    def add(self): 
        connection = psycopg2.connect(self.DATABASE_URL)     
    
        cursor = connection.cursor()
        #query = "INSERT INTO {0}(Beach_Name, Measurement_Timestamp, Water_Temperature, Turbidity, Transducer_Depth, Wave_Height, Wave_Period, Battery_Life, Measurement_Timestamp_Label, Measurement_ID) VALUES ('{1}', '{2}', {3}, {4}, {5}, {6}, {7}, {8}, '{9}', '{10}')".format(self.TABLE_NAME, self.beach_Name, self.measurement_Timestamp, self.water_Temperature, self.turbidity, self.transducer_Depth, self.wave_Height, self.wave_Period, self.battery_Life, self.measurement_Timestamp_Label, self.measurement_ID);
        query = "INSERT INTO {0}(Beach_Name, Wave_Period, Water_Temperature, Turbidity) VALUES ('{1}', {2}, {3}, {4})".format(self.TABLE_NAME, self.beach_Name, self.wave_Period, self.water_Temperature, self.turbidity);
        print("\nquery @DatasetModel @add:",query)
        cursor.execute(query)
        connection.commit()

        connection.close()
        return True
    
    @classmethod
    def delete(cls, beachName): 
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "DELETE FROM {0} WHERE Beach_Name={1}".format(cls.TABLE_NAME, beachName)
        print("\nquery @DatasetModel @delete:",query)
        cursor.execute(query)
        connection.commit()

        connection.close()
        return True
    
    