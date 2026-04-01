# Sensor Monitoring Script

class Sensor:
    def __init__(self, id, type, location):
        self.id = id
        self.type = type
        self.location = location
        self.data = []

    def read_data(self):
        # Simulate reading data from a sensor
        import random
        self.data.append(random.uniform(20.0, 100.0))

    def get_last_data(self):
        return self.data[-1] if self.data else None

# Example usage
if __name__ == '__main__':
    sensor = Sensor(1, 'Temperature', 'Site A')
    sensor.read_data()
    print(f'Last recorded data from sensor {sensor.id}: {sensor.get_last_data()}')