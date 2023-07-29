from flask import Flask, jsonify, request
import os
import json
from translator import transliterate

PARSER_DIR = os.path.dirname(__file__)
app = Flask(__name__)

main_data = PARSER_DIR + '/RU.txt'
timezone_data = PARSER_DIR + '/timeZones.txt'


def open_txt(txt_file):
    with open(txt_file, 'r', encoding='utf8') as f:
        mydata = f.read().splitlines()
    return mydata


def parse_data(datatxt):
    data = {}
    data_id = {}
    counter_id = 0
    for datatmp in datatxt:
        tmp = datatmp.split('\t')
        data[tmp[0]] = {
            'geocodeid' : tmp[0],
            'name' : tmp[1],
            'asciiname' : tmp[2],
            'alternatenames' : tmp[3],
            'latitude' : tmp[4],
            'longitude' : tmp[5],
            'feature class' : tmp[6],
            'feature code' : tmp[7],
            'country code' : tmp[8],
            'cc2' : tmp[9],
            'admin1 code' : tmp[10],
            'admin2 code' : tmp[11],
            'admin3 code' : tmp[12],
            'admin4 code' : tmp[13],
            'population' : tmp[14],
            'elevation' : tmp[15],
            'dem' : tmp[16],
            'timezone' : tmp[17],
            'modification date' : tmp[18]
        }
        data_id[counter_id] = tmp[0]
        counter_id += 1
    return data, data_id


def generate_dict_city(geonameid, row):
    city = {
        'geonameid': geonameid,
        'name': row['name'],
        'asciiname': row['asciiname'],
        'alternatenames': row['alternatenames'],
        'latitude': row['latitude'],
        'longitude': row['longitude'],
        'feature class': row['feature class'],
        'feature code': row['feature code'],
        'country code': row['country code'],
        'cc2': row['cc2'],
        'admin1 code': row['admin1 code'],
        'admin2 code': row['admin2 code'],
        'admin3 code': row['admin3 code'],
        'admin4 code': row['admin4 code'],
        'population': row['population'],
        'elevation': row['elevation'],
        'dem': row['dem'],
        'timezone': row['timezone'],
        'modification date': row['modification date']
    }
    return city

def parse_timezone(timezonetxt):
    data = {}
    for datatmp in timezonetxt:
        tmp = datatmp.split('\t')
        data[tmp[1]] = tmp[2]
    return data


@app.route('/city/<int:geonameid>', methods=['GET'])
def get_city_by_id(geonameid):
    try:
        # return jsonify(data[f'{geonameid}'])
        return json.dumps(data[f'{geonameid}'], ensure_ascii=False).encode('utf8')
    except KeyError:
        return jsonify({'message': 'City not found.'}), 404


@app.route('/city', methods=['GET'])
def get_cities():
    start = (request.args.get('page', default=1, type=int) - 1) * request.args.get('per_page', default=10, type=int)
    end = start + request.args.get('per_page', default=10, type=int)
    cities = []
    for key in range(start, end + 1):
        city = data[f'{data_id[key]}']
        cities.append(city)
    # return jsonify(cities[start:end])
    return json.dumps(cities, ensure_ascii=False).encode('utf8')


@app.route('/cities', methods=['GET'])
def get_cities_info():
    city1_name = transliterate(request.args.get('city1_name'))
    city2_name = transliterate(request.args.get('city2_name'))
    cities = [None, None]
    population_city1, population_city2 = -1, -1
    for geonameid, row in data.items():
        if row['asciiname'] == city1_name and population_city1 < int(row['population']):
            cities[0] = generate_dict_city(geonameid, row)
            population_city1 = int(row['population'])
        if row['asciiname'] == city2_name and population_city2 < int(row['population']):
            cities[1] = generate_dict_city(geonameid, row)
            population_city2 = int(row['population'])
    if cities[0] == None:
        return jsonify({'message': f'City not found.           {city1_name}'}), 404
    if cities[1] == None:
        return jsonify({'message': f'City not found.           {city2_name}'}), 404
    if cities[0]['latitude'] > cities[1]['latitude']:
        north_city_name = cities[0]['name']
    elif cities[0]['latitude'] < cities[1]['latitude']:
        north_city_name = cities[1]['name']
    else:
        north_city_name = 'Both cities are on the same latitude.'
    if cities[0]['timezone'] == cities[1]['timezone']:
        same_timezone = True
    else:
        same_timezone = float(data_time[cities[0]['timezone']]) - float(data_time[cities[1]['timezone']])
    return json.dumps({
        'city1': cities[0],
        'city2': cities[1],
        'north_city_name': north_city_name,
        'same_timezone': same_timezone
    }, ensure_ascii=False).encode('utf8')


@app.route('/suggest-city', methods=['GET'])
def suggest_city():
    partial_name = transliterate(request.args.get('name'))
    suggestions = []
    if partial_name:
        for geonameid, row in data.items():
            if row['asciiname'].find(partial_name) == 0:
                suggestions.append(data[geonameid]['asciiname'])
            elif row['asciiname'].find(partial_name) != -1 and row['asciiname'][row['asciiname'].find(partial_name) - 1] == ' ':
                suggestions.append(data[geonameid]['asciiname'])
        return json.dumps({'suggestions': suggestions},  ensure_ascii=False).encode('utf8')
    else:
        return jsonify({'error': 'Please provide a partial city name as input'})


if __name__ == '__main__':
    txtdata = open_txt(main_data)
    txttimezone = open_txt(timezone_data)
    data, data_id = parse_data(txtdata)
    data_time = parse_timezone(txttimezone)
    app.run(host="127.0.0.1", port=8000, debug=True)




#