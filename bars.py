import json
from math import fabs

def load_data(filepath):
    file = open(filepath, 'r')
    data = file.read()
    data = json.loads(data)
    file.close()
    return data

def get_biggest_bar(data):
    global MAX
    global MAXname
    if data['SeatsCount'] > MAX:
        MAX = data['SeatsCount']
        MAXname = data['Name']

def get_smallest_bar(data):
    global MIN
    global MINname
    if data['SeatsCount'] < MIN:
        MIN = data['SeatsCount']
        MINname = data['Name']

def get_closest_bar(data, longitude, latitude):
    global minX
    global minY    
    global nearest_bar
    global coordinates
    x = fabs(latitude - float(data['Latitude_WGS84']))
    y = fabs(longitude - float(data['Longitude_WGS84']))
    if x < minY and y < minY:
        mixX = x
        minY = y
        nearest_bar = data['Name']
        coordinates = [data['Latitude_WGS84'], data['Longitude_WGS84']]
    

if __name__ == '__main__':

    MAX = 0; MAXname = ""; MIN = 100; MINname = ""
    minX = 100 ; minY = 100 ; nearest_bar = ''; coordinates = None
    data = load_data("data.json")
    longitude,latitude = map(float,input('Input coordinates(Longitude,Latitude):  ').split(","))

    for number in range(0,len(data)):
        if data[number]['TypeObject'] == 'бар':
            get_biggest_bar(data[number])
            get_smallest_bar(data[number])
            get_closest_bar(data[number], longitude, latitude)

            
    print(MAXname,MINname,nearest_bar.join(' ')
