# siggy.py

import json
import requests
import urlparse
import logging
from datetime import datetime
from solarmap import SolarMap


class Siggy:
    """
    Siggy handler
    """
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"

    #url = https://siggy.borkedlabs.com/account/login
    def __init__(self, eve_db, username, password):
        self.eve_db = eve_db
        self.username = username
        self.password = password
        self.url = "https://siggy.borkedlabs.com"
        self.session_requests = self.login()

    def login(self):
        response = None

        login_url = urlparse.urljoin(self.url, "account/login")
        session_requests = requests.session()
        payload = {
            "username": self.username,
            "password": self.password
        }

        headers = {
            "Referer": login_url,
            "User-Agent": Siggy.USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            result = session_requests.post(
                login_url,
                data=payload,
                headers=headers
            )
        except requests.exceptions.RequestException:
            logging.warning("Unable to connect to Siggy")
        else:
            if result.status_code == 200:
                response = session_requests

        return response

    def get_chain(self):
        response = None

        if self.session_requests:
            refresh_url = urlparse.urljoin(self.url, "siggy/siggy")
            payload = {
                "forceUpdate": "true",
                "lastUpdate": "0",
                "mapLastUpdate": "0",
                "mapOpen": "true",
                "systemID": "30000439"
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
            }

            try:
                result = self.session_requests.post(
                    refresh_url,
                    data=payload,
                    headers=headers
                )

            except requests.exceptions.RequestException as e:
                logging.error(e, exc_info=True)
            else:
                if result.status_code == 200:
                    if is_json(result.text):
                        response = result.json()


        return response

    def augment_map(self, solar_map):
        connections = -1  # not logged in, yet
        chain = self.get_chain()

        if chain:
            # we get some sort of response so at least we're logged in
            connections = 0

            # let's see how many wormhole signatures exist (if any...)
            for sig in chain["chainMap"]["wormholes"]:
                entry = chain["chainMap"]["wormholes"][sig]

                connections += 1

                # Retrieve signature meta data
                source = convert_to_int(entry["from_system_id"])
                dest = convert_to_int(entry["to_system_id"])

                if "life" in entry and entry["life"] == "Stable":
                    wh_life = 1
                else:
                    wh_life = 0
                if "mass" in entry:
                    wh_mass = entry["mass"]
                elif "mass" in entry and entry["mass"] == "Destab":
                    wh_mass = 1
                else:
                    wh_mass = 0

                # Compute time elapsed from this moment to when the signature was updated
                last_modified = datetime.strptime(entry["created_at"], "%Y-%m-%d %H:%M:%S")
                delta = datetime.utcnow() - last_modified
                time_elapsed = round(delta.total_seconds() / 3600.0, 1)

                if source != 0 and dest != 0:
                    # Determine wormhole size


                        # Wormhole codes are unknown => determine size based on class of wormholes
                    wh_size = self.eve_db.get_whsize_by_system(source, dest)

                    # Add wormhole conection to solar system
                    solar_map.add_connection(
                        source,
                        dest,
                        SolarMap.WORMHOLE,
                        ['', '', '', '', wh_size, wh_life, wh_mass, time_elapsed],
                    )

        return connections


def is_json(response):
    """
    Check if the response parameter is a valid JSON string
    :param response:
    :return:
    """
    try:
        json.loads(response)
    except ValueError:
        return False
    return True


def convert_to_int(s):
    """
    Convert string to integer
    :param s: Input string
    :return: Interpreted value if successful, 0 otherwise
    """
    try:
        nr = int(s)
    except (ValueError, TypeError):
        nr = 0

    return nr
