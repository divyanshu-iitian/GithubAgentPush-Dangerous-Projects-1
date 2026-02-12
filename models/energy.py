# energy.py

class EnergyModel:
    def __init__(self):
        self.electrical_consumption = 0
        self.renewable_sources = 0
        self.usage_history = []
        self.forecast = {}
    
    def update_usage(self, consumption, timestamp):
        """Update the electrical consumption and append to usage history."""
        self.electrical_consumption += consumption
        self.usage_history.append((timestamp, consumption))
    
    def add_renewable_energy(self, amount):
        """Add renewable energy sources to the model."""
        self.renewable_sources += amount
    
    def update_forecast(self, forecast_data):
        """Update the energy forecast with new data."""
        self.forecast = forecast_data
    
    def calculate_efficiency_ratio(self):
        """Calculate the efficiency ratio based on consumption and renewable sources."""
        if self.electrical_consumption == 0:
            return 1.0
        return (self.renewable_sources / self.electrical_consumption)
    
    def get_usage_summary(self):
        """Get a summary of the usage history."""
        total_consumption = sum(consumption for _, consumption in self.usage_history)
        average_consumption = total_consumption / len(self.usage_history) if self.usage_history else 0
        return {
            "total_consumption": total_consumption,
            "average_consumption": average_consumption,
            "max_usage": max(consumption for _, consumption in self.usage_history),
            "min_usage": min(consumption for _, consumption in self.usage_history)
        }