# Functions for measurement sets
def ms_get_measurement_set():
    return []

def ms_add_measurement(measurement_set, measurement):
    measurement_set.append(measurement)

def ms_get_measurement_by_name(measurement_set, name):
    for measurement in measurement_set:
        if measurement['name'] == name:
            return measurement

# Functions for measurements
def m_create_measurement(name, points):
    return {'name': '##_{}'.format(name), 'points': points}

def m_change_name(measurement, new_name):
    measurement['name'] = new_name

