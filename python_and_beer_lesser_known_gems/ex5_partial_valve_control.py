"""Real example, valve control program. We have a gui that has 10
buttons that correspond to open and close state of 10 valves. To
change the state of the valve, we need to send a command to a socket
with its name and the value

"""

from __future__ import print_function

import sys
from functools import partial
from PyQt4 import QtGui, uic

ValveApp = uic.loadUiType("valves.ui")[0]


class ValveControl1(QtGui.QMainWindow, ValveApp):
    """First stab at valve control

    The physical valves are connect to a binary output card on these channels

      inlet1 -> 0
      inlet2 -> 1
      inlet3 -> 2
      outlet1 -> 3
      outlet2 -> 4
      outlet3 -> 5
    """

    def __init__(self, parent=None):

        # Call GUI magic builder command, that creates all the widgets
        # and makes them available as properties
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # Bind callback functions
        self.inlet1.clicked.connect(self.inlet1_clicked)
        self.inlet2.clicked.connect(self.inlet2_clicked)
        self.inlet3.clicked.connect(self.inlet3_clicked)
        self.outlet1.clicked.connect(self.outlet1_clicked)
        self.outlet2.clicked.connect(self.outlet2_clicked)
        self.outlet3.clicked.connect(self.outlet3_clicked)

    def set_binary_out(self, valve_channel, value):
        """Set the high or low state on the binary output card"""
        print('Set binary out', valve_channel, 'to', value)

    def inlet1_clicked(self, value):
        """Sets binary out for channel 0"""
        self.set_binary_out(0, value)

    def inlet2_clicked(self, value):
        """Sets binary out for channel 0"""
        self.set_binary_out(1, value)

    def inlet3_clicked(self, value):
        """Sets binary out for channel 0"""
        self.set_binary_out(2, value)

    def outlet1_clicked(self, value):
        """Sets binary out for channel 0"""
        self.set_binary_out(3, value)

    def outlet2_clicked(self, value):
        """Sets binary out for channel 0"""
        self.set_binary_out(4, value)

    def outlet3_clicked(self, value):
        """Sets binary out for channel 0"""
        self.set_binary_out(5, value)


#
#
#
#
#
### Now with partial

class ValveControl2(QtGui.QMainWindow, ValveApp):
    """First stab at valve control"""

    def __init__(self, parent=None):

        # Call GUI magic builder command, that creates all the widgets
        # and makes them available as properties
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # Create valve name to binary out translation
        valves_to_channels = {
            'inlet1': 0,
            'inlet2': 1,
            'inlet3': 2,
            'outlet1': 3,
            'outlet2': 4,
            'outlet3': 5,
        }

        # Bind callback functions
        for valve_name, channel in valves_to_channels.items():
            widget = getattr(self, valve_name)
            callbackfunction = partial(self.set_binary_out, channel)
            widget.clicked.connect(callbackfunction)

    def set_binary_out(self, valve_channel, value):
        """Set the high or low state on the binary output card"""
        print(valve_channel, value)


#
#
#
#


def main1():
    """Start the ValveControl1 program"""
    app = QtGui.QApplication(sys.argv)
    my_window = ValveControl1(None)
    my_window.show()
    app.exec_()


def main2():
    """Start the ValveControl2 program"""
    app = QtGui.QApplication(sys.argv)
    my_window = ValveControl2(None)
    my_window.show()
    app.exec_()

if __name__ == '__main__':
    main1()
    #main2()
