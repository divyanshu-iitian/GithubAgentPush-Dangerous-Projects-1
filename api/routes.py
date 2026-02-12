from flask import Blueprint, request, jsonify
from core.energy_monitor import get_energy_usage, optimize_energy_usage
from utils.helpers import validate_json

energy_api = Blueprint('energy', __name__)

@energy_api.route('/monitor', methods=['GET'])
def monitor_energy():
    """
    Gets the current energy usage.
    
    :param:
        None
    
    :return: JSON response containing the energy usage data.
            Example: {"usage": 123.4, "unit": "kW"}
    """
    try:
        energy_usage = get_energy_usage()
        return jsonify(energy_usage)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@energy_api.route('/optimize', methods=['POST'])
def optimize():
    """
    Optimizes the energy usage based on given parameters.
    
    :param: JSON object with energy optimization parameters
            Example: {"device_id": "123", "action": "increase"}
    
    :return: JSON response indicating the success or failure of the optimization action.
            Example: {"message": "Energy optimization successful"}
    """
    if not validate_json(request.json, ["device_id", "action"]):
        return jsonify({"error": "Invalid JSON data"}), 400

    device_id = request.json.get('device_id')
    action = request.json.get('action')

    try:
        optimize_energy_usage(device_id, action)
        return jsonify({"message": "Energy optimization successful"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500