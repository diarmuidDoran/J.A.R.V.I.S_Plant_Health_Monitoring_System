class Sensor(object):
    id = 0
    sensor_name = ""
    call_frequency = ""
    connection_pin = 0
    is_deleted = bool

    # The class "constructor" - an initializer
    def __init__(self, id, sensor_name, call_frequency, connection_pin, is_deleted):
        self.id = id
        self.sensor_name = sensor_name
        self.call_frequency = call_frequency
        self.connection_pin = connection_pin
        self.is_deleted = is_deleted


class Sensor_Sensor_Readings(object):
    id = 0
    sensor_name = ""
    call_frequency = ""
    connection_pin = 0
    is_deleted = bool
    sensor_readings = []

    # The class "constructor" - an initializer
    def __init__(self, id, sensor_name, call_frequency, connection_pin, is_deleted, sensor_readings):
        self.id = id
        self.sensor_name = sensor_name
        self.call_frequency = call_frequency
        self.is_deleted = is_deleted
        self.connection_pin = connection_pin
        self.sensor_readings = sensor_readings


class Sensor_Plant_Health_Attribute(object):
    id = 0
    plant_health_attribute_id = 0
    sensor_id = 0
    is_deleted = bool

    # The class "constructor" - an initializer
    def __init__(self, id, plant_health_attribute_id, sensor_id, is_deleted):
        self.id = id
        self.plant_health_attribute_id = plant_health_attribute_id
        self.sensor_id = sensor_id
        self.is_deleted = is_deleted


def make_sensor(id, sensor_name, call_frequency, connection_pin, is_deleted):
    sensor = Sensor(id, sensor_name, call_frequency, connection_pin, is_deleted)
    return sensor


def make_new_sensor(sensor_name, call_frequency, connection_pin):
    sensor = Sensor(
        sensor_name=sensor_name, call_frequency=call_frequency, connection_pin=connection_pin, is_deleted=False
    )
    return sensor


def make_sensor_with_sensor_readings_list(
    id, sensor_name, call_frequency, connection_pin, is_deleted, sensor_readings
):

    sensor_data = Sensor_Sensor_Readings(
        id, sensor_name, call_frequency, connection_pin, is_deleted, sensor_readings
    )
    return sensor_data


def make_sensor_plant_health_attribute_list(
    id, plant_health_attribute_id, sensor_id, is_deleted
):
    data = Sensor_Plant_Health_Attribute(
        id, plant_health_attribute_id, sensor_id, is_deleted
    )
    return data
