"""
energy_config.py

Configuration settings for energy monitoring in SmartHomeHub.

This module provides the configuration necessary for setting up and managing 
the energy monitoring features of the SmartHomeHub system.
"""

# Default settings for energy monitor
DEFAULT_ENERGY_MONITOR_SETTINGS = {
    "enabled": True,  # Enable/Disable energy monitoring
    "interval": 300,  # Interval between readings in seconds (5 minutes)
    "units": "KWh",  # Unit of measurement for energy consumption
    "thresholds": {
        "high": 1000,  # High threshold for energy usage in KWh
        "critical": 2000  # Critical threshold for energy usage in KWh
    }
}

# Configuration for logging in energy monitor
ENERGY_MONITOR_LOGGING = {
    "level": "INFO",  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    "file": "energy_monitor.log"  # Path to the log file
}