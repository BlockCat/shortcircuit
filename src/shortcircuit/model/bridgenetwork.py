import requests
import logging
import re
from solarmap import SolarMap

class BridgeNetwork:

    def __init__(self, eve_db, url):
        self.eve_db = eve_db
        self.url = url

    #Returns [(source, destination)]
    def loadNetwork(self):
        try:
            r = requests.get(self.url)
        except requests.exceptions.RequestException:
            logging.warning("Unable to connect to Bridge file")
        else:
            if r.status_code == 200:
                return self.parse_text(r.text)

        return []

    def parse_text(self, text):
        regex = re.compile(r"([A-Z0-9-]+) --> ([A-Z0-9-]+)", re.MULTILINE)
        text = text.upper()
        list = []
        for match in regex.finditer(text):

            source = self.eve_db.name2id(self.eve_db.normalize_name(match.group(1).strip()))
            destination = self.eve_db.name2id(self.eve_db.normalize_name(match.group(2).strip()))
            print match.group(1) + ": " + match.group(2)
            print source
            print destination
            list.append((source, destination))

        return list

    def augment_map(self, solar_map):
        bridges = self.loadNetwork()

        for bridge in bridges:
            solar_map.add_connection(
                bridge[0],
                bridge[1],
                SolarMap.BRIDGE)
        return bridges.__len__()

def main():
    bridgenetwork = BridgeNetwork(None)
    bridgenetwork.augment_map(None)

if __name__ == "__main__":
    main()