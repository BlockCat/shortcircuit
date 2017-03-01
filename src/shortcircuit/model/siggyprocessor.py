# navprocessor.py

from PySide import QtCore


class SiggyProcessor(QtCore.QObject):
    """
    Navigation Processor (will work in a separate thread)
    """

    finished = QtCore.Signal(int)

    def __init__(self, nav, parent=None):
        super(SiggyProcessor, self).__init__(parent)
        self.nav = nav

    def process(self):
        solar_map = self.nav.solar_map
        siggy_connections = self.nav.siggy_augment(solar_map)

        if siggy_connections > 0:
            self.nav.solar_map = solar_map
        self.finished.emit(siggy_connections)
