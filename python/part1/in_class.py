class Measurement(object):

    def __init__(self, name, points):
        self.name = '##_{}'.format(name)
        self.points = points

    def change_name(self, new_name):
        self.name = '##_{}'.format(new_name)

class MeasurementSet(object):

    def __init__(self, measurements=None):
        if measurements is not None:
            self.measurements = list(measurements)
        else:
            self.measurements = []

    def add_measurement(self, measurement):
        self.measurements.append(measurement)

    def find_measurement(self, name):
        for measurement in self.measurements:
            if measurement.name == name:
                return measurement
