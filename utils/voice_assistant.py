from core.engine import SmartHomeEngine
from api.routes import create_api_app

if __name__ == "__main__":
    engine = SmartHomeEngine()
    app = create_api_app(engine)

    # Start the Flask app
    app.run(debug=True)