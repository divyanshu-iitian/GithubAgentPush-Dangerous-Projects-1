import unittest
from core.energy_monitor import EnergyMonitor

class TestEnergyMonitor(unittest.TestCase):

    def setUp(self):
        self.monitor = EnergyMonitor()

    def test_calculate_daily_energy_usage(self):
        # Mock the energy data retrieval method to return a fixed value
        self.monitor._get_daily_energy_data = lambda: 100.5
        expected_usage = 100.5
        result = self.monitor.calculate_daily_energy_usage('device123')
        self.assertEqual(result, expected_usage)

    def test_calculate_monthly_energy_saving(self):
        daily_usage = [80.75, 90.25, 100.50, 110.00, 120.75, 130.25, 140.00]
        expected_saving = 7
        result = self.monitor.calculate_monthly_energy_saving('device123', daily_usage)
        self.assertEqual(result, expected_saving)

    def test_alert_high_energy_consumption(self):
        # Mock the energy data retrieval method to return a high value
        self.monitor._get_daily_energy_data = lambda: 200.0
        alert_threshold = 150.0
        result = self.monitor.alert_high_energy_consumption('device123', alert_threshold)
        self.assertTrue(result)

    def test_alert_low_energy_usage(self):
        # Mock the energy data retrieval method to return a low value
        self.monitor._get_daily_energy_data = lambda: 40.0
        alert_threshold = 50.0
        result = self.monitor.alert_low_energy_usage('device123', alert_threshold)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()