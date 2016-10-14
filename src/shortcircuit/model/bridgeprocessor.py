# navprocessor.py

from PySide import QtCore


class BridgeProcessor(QtCore.QObject):
    """
    Navigation Processor (will work in a separate thread)
    """

    finished = QtCore.Signal(int, int)

    def __init__(self, nav, parent=None):
        super(BridgeProcessor, self).__init__(parent)
        self.nav = nav
        self.url = None

    def process(self):
        solar_map = self.nav.eve_db.get_solar_map()
        connections = self.nav.bridgenetwork_augment(solar_map, self.url)


        if connections > 0:
            self.nav.solar_map = solar_map
        self.finished.emit(connections, 0)
