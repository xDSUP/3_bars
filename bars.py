import json
from math import fabs


def load_data(filepath):
    with open(filepath, 'r') as bar_list:
        bar_list_parsed = json.loads(bar_list.read())
        return bar_list_parsed


def get_biggest_bar(bar_list):
    biggest_bar = max(bar_list, key=lambda bar: bar['SeatsCount'])
    return biggest_bar['Name']


def get_smallest_bar(bar_list):
    smallest_bar = min(bar_list, key=lambda bar: bar["SeatsCount"])
    return smallest_bar['Name']


def get_closest_bar(bar_list, longitude, latitude):
    closest_bar = min(bar_list, key=lambda
                      bar: fabs(longitude - float(bar['Longitude_WGS84']) +
                                latitude - float(bar['Latitude_WGS84'])))
    return closest_bar['Name']


def print_result(biggest_bar, smallest_bar, closest_bar):
    print_txt = """
    the biggest bar: {biggest_bar} .
    the smallest bar: {smallest_bar} .
    the closest bar : {closest_bar} ."""
    result_program = print_txt.format(biggest_bar=biggest_bar,
                                      smallest_bar=smallest_bar,
                                      closest_bar=closest_bar)
    print(result_program)

if __name__ == '__main__':
    filepath = input("Enter the path to the json file with the database: ")
    longitude = float(input('Input coordinates(longitude):  '))
    latitude = float(input('Input coordinates(latitude):  '))
    bar_list = load_data(filepath)
    biggest_bar = get_biggest_bar(bar_list)
    smallest_bar = get_smallest_bar(bar_list)
    closest_bar = get_closest_bar(bar_list, longitude, latitude)
    print_result(biggest_bar, smallest_bar, closest_bar)
