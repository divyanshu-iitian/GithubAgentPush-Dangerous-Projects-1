# main.py

from core.engine import SmartHomeHubEngine
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to initialize and start the Smart Home Hub Engine.
    
    This function is responsible for creating an instance of SmartHomeHubEngine,
    setting up any necessary configurations, and starting the engine.
    """
    try:
        # Initialize the Smart Home Hub Engine
        engine = SmartHomeHubEngine()
        
        # Start the engine
        engine.start()
        
        logging.info("Smart Home Hub Engine started successfully.")
    
    except Exception as e:
        # Log any exceptions that occur during startup
        logging.error(f"Failed to start Smart Home Hub Engine: {e}")
        raise

if __name__ == "__main__":
    main()