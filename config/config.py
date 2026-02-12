# main.py

from flask import Flask
from core.engine import SmartHomeEngine
from api.device_api import device_blueprint
from api.scene_api import scene_blueprint
from api.energy_api import energy_blueprint
import config.config as config

app = Flask(__name__)

# Register blueprints for different API routes
app.register_blueprint(device_blueprint, url_prefix='/api/device')
app.register_blueprint(scene_blueprint, url_prefix='/api/scene')
app.register_blueprint(energy_blueprint, url_prefix='/api/energy')

# Initialize the SmartHomeEngine with configuration
engine = SmartHomeEngine(config)

if __name__ == '__main__':
    app.run(debug=True)