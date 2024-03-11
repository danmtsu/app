from flask import Blueprint, request, jsonify
from src.main.database.connect_db import create_database
from src.validators.gas_stations_validate import validate_gas_station
from src.main.database.GasStation_querys import GasStationQuery

posts_routes_bp = Blueprint('postos_routes', __name__)

# Criando a conexão com o banco de dados
gas_stationdb = GasStationQuery()

@posts_routes_bp.route('/postos', methods=['GET'])
def listar_postos():
    try:
        gas_stations_all = gas_stationdb.gas_station_listBy()
        return jsonify(message="Lista de postos", data=gas_stations_all), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@posts_routes_bp.route('/postos', methods=['POST'])
def criar_posto():
    data = request.json
    novo_posto = {
        'name': data.get('name'),
        'address': data.get('address'),
        'city': data.get('city'),
        'state': data.get('state'),
        'preco_etanol': data.get('preco_etanol'),
        'preco_gasolina': data.get('preco_gasolina'),
        'preco_diesel': data.get('preco_diesel')
    }
    errors = validate_gas_station(novo_posto)
    if errors:
        return jsonify({'error': errors[0]}), 400
    try:
        message = gas_stationdb.create_gas_station(novo_posto)
        return jsonify({'message': message}), 201 if message == 'Posto criado com sucesso' else 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@posts_routes_bp.route('/postos/<int:id_posto>', methods=['PUT'])
def atualizar_posto(id_posto):
    try:
        data = request.json
        posto_atualizado = {
            'name': data['name'],
            'address': data['address'],
            'city': data['city'],
            'state': data['state'],
            'preco_etanol': data['preco_etanol'],
            'preco_gasolina': data['preco_gasolina'],
            'preco_diesel': data['preco_diesel']
        }
        errors = validate_gas_station(posto_atualizado)
        if len(errors)> 0:
            return jsonify({'error': f'{errors[0]}'}), 400
        message_update_gasStation = gas_stationdb.update_gas_station(posto_atualizado,id_posto)
        if message_update_gasStation == 'Posto atualizado com sucesso':
            return jsonify({'message': f'{message_update_gasStation}'}), 200
        elif message_update_gasStation == 'Posto não encontrado':
            return jsonify({'message': f'{message_update_gasStation}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@posts_routes_bp.route('/postos/<int:id_posto>', methods=['DELETE'])
def deletar_posto(id_posto):
    message = gas_stationdb.delete_gas_station(id_posto)
    try:
        if message == "Gas station has been deleted":
            return jsonify({'message': f'{message}'}), 200
        else:
            return jsonify({'message': f'{message}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

