# Real example, valve control program. We have a gui that has 10
# buttons that correspond to open and close state of 10 valves. To
# change the state of the valve, we need to send a command to a socket
# with its name and the value

class ValveControl(object):

    def __init__(self):
        # NOT SHOWN. Call GUI magic builder command, that creates all
        # the widgets and makes them available as properties

        # Create list of valves
        valve_names = [
            'inlet1', 'inlet2', 'inlet3', 'inlet4', 'inlet5',
            'mix1into2', 'mix3into4', 'mix3into5', 'pump_out1', 'pumptout2'
        ]

        # Bind callback functions
        for valve_name in valve_names:
            widget = getattr(self, valve_name)
            callbackfunction = partial(self.send_valve_command, valve_name)
            # The function that you pass to bind, is called with the
            # new value when the button changes value
            widget.bind(callbackfunction)

    def send_valve_command(valve_name, value):
        socket.send('{}:{}'.format(valve_name, value)


class ValveControl2(object):

    def __init__(self):
        # NOT SHOWN. Call GUI magic builder command, that creates all
        # the widgets and makes them available as properties

        # Create list of valves
        valve_names = [
            'inlet1', 'inlet2', 'inlet3', 'inlet4', 'inlet5',
            'mix1into2', 'mix3into4', 'mix3into5', 'pump_out1', 'pumptout2'
        ]

        # Bind callback functions
        for valve_name in valve_names:
            widget = getattr(self, valve_name)
            callbackfunction = partial(self.send_valve_command, valve_name)
            # The function that you pass to bind, is called with the
            # new value when the button changes value
            widget.bind(callbackfunction)

    def send_valve_command(valve_name, value):
        socket.send('{}:{}'.format(valve_name, value)
