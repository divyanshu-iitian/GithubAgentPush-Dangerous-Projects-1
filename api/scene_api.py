from flask import Flask, request, jsonify, abort
from core.scene_automation import SceneManager, SceneNotFoundError

app = Flask(__name__)
scene_manager = SceneManager()

@app.route('/api/scenes', methods=['POST'])
def create_scene():
    """
    Create a new scene.
    
    :param json: Name of the scene and list of device actions (e.g., [{'device_id': '123', 'action': 'turn_on'}])
    :return: JSON response with created scene details
    """
    try:
        data = request.get_json()
        name = data['name']
        actions = data['actions']

        new_scene = scene_manager.create_scene(name, actions)
        return jsonify(new_scene), 201
    except KeyError as e:
        abort(400, description=f"Missing parameter: {e}")
    except Exception as e:
        abort(500, description=str(e))

@app.route('/api/scenes', methods=['GET'])
def get_all_scenes():
    """
    Retrieve all scenes.
    
    :return: JSON response with list of all scenes
    """
    try:
        scenes = scene_manager.get_all_scenes()
        return jsonify(scenes)
    except Exception as e:
        abort(500, description=str(e))

@app.route('/api/scenes/<int:scene_id>', methods=['GET'])
def get_scene_by_id(scene_id):
    """
    Retrieve a specific scene by ID.
    
    :param scene_id: ID of the scene
    :return: JSON response with details of the specified scene
    """
    try:
        scene = scene_manager.get_scene_by_id(scene_id)
        return jsonify(scene)
    except SceneNotFoundError:
        abort(404, description=f"Scene with ID {scene_id} not found")
    except Exception as e:
        abort(500, description=str(e))

@app.route('/api/scenes/<int:scene_id>', methods=['PUT'])
def update_scene(scene_id):
    """
    Update a specific scene by ID.
    
    :param scene_id: ID of the scene
    :param json: Updated name and actions (e.g., {'name': 'New Scene', 'actions': [{'device_id': '123', 'action': 'turn_on'}]})
    :return: JSON response with updated scene details
    """
    try:
        data = request.get_json()
        new_name = data['name']
        new_actions = data['actions']

        updated_scene = scene_manager.update_scene(scene_id, new_name, new_actions)
        return jsonify(updated_scene)
    except KeyError as e:
        abort(400, description=f"Missing parameter: {e}")
    except SceneNotFoundError:
        abort(404, description=f"Scene with ID {scene_id} not found")
    except Exception as e:
        abort(500, description=str(e))

@app.route('/api/scenes/<int:scene_id>', methods=['DELETE'])
def delete_scene(scene_id):
    """
    Delete a specific scene by ID.
    
    :param scene_id: ID of the scene
    :return: JSON response with success message
    """
    try:
        scene_manager.delete_scene(scene_id)
        return jsonify({"message": "Scene deleted successfully"})
    except SceneNotFoundError:
        abort(404, description=f"Scene with ID {scene_id} not found")
    except Exception as e:
        abort(500, description=str(e))