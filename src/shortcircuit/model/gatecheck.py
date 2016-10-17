import requests
import logging
import json
import re
from solarmap import SolarMap

class GateCheck:

    def __init__(self, eve_db):
        self.eve_db = eve_db

    """Json format:
	{  
   "premium":false,
   "30000152":{  
      "kills":{  
         "killCount":6,
         "gateKillCount":1,
         "data":{  
            "Jakanerva":{  
               "killCount":1,
               "checks":{  
                  "smartbombs":null,
                  "dictors":null,
                  "hictors":null
               }
            },
            "Not on a gate":{  
               "killCount":5,
               "checks":{  
                  "smartbombs":null,
                  "dictors":null,
                  "hictors":null
               }
            }
         }
      }
   },
   "30000142":{  
      "kills":{  
         "killCount":4,
         "gateKillCount":0,
         "data":{  
            "Not on a gate":{  
               "killCount":4,
               "checks":{  
                  "smartbombs":null,
                  "dictors":null,
                  "hictors":null
               }
            }
         }
      }
   },
   "30000146":{  
      "kills":{  
         "killCount":1,
         "gateKillCount":0,
         "data":{  
            "Not on a gate":{  
               "killCount":1,
               "checks":{  
                  "smartbombs":null,
                  "dictors":null,
                  "hictors":null
               }
            }
         }
      }
   },
   "30000783":{  
      "kills":{  
         "killCount":2,
         "gateKillCount":2,
         "data":{  
            "G-QTSD":{  
               "killCount":2,
               "checks":{  
                  "smartbombs":null,
                  "dictors":true,
                  "hictors":null
               }
            }
         }
      }
   }
}
	"""
    def get_gates(self, route):

        query = ",".join(str(x) for x in route)
        try:
            r = requests.get("http://eve-gatecheck.space/eve/get_kills.php?systems=" + query)
        except requests.exceptions.RequestException:
            logging.warning("Unable to connect to eve-gatecheck")
        else:
            if r.status_code == 200 and is_json(r.text):
                return r.json()
        return None

    def get_warnings(self, route):
        json = self.get_gates(route)

        warnings = {} #solarid: "hictors, dictors and smartbombs, 2 killed at Jita gate, killed at Amarr gate"

        if (json == None): return warnings
        for system, kills in json.iteritems():
            if system == "premium": continue

            systemId = convert_to_int(system)
            totalKills = convert_to_int(kills["kills"]["killCount"])
            warningLine = ["{} kills".format(totalKills)]


            if len(kills["kills"]["data"]) == 0: continue

            for gate, data in kills["kills"]["data"].iteritems():
                if gate == "Not on a gate": continue

                killCount = convert_to_int(data["killCount"])
                checks = []
                if data["checks"]["smartbombs"]: checks.append("Smartbombs")
                if data["checks"]["dictors"]: checks.append("Dictors")
                if data["checks"]["hictors"]: checks.append("Hictors")
                if len(checks) == 0:
                    warning = "[{} at {} gate]".format(killCount, gate)
                elif len(checks) == 1:
                    warning = "[{}, {} at {} gate]".format(checks[0], killCount, gate)
                else:
                    ships = ", ".join(checks[:-1])
                    ships = "and ".join([ships, checks[-1]])
                    warning = "[{}, {} at {} gate]".format(ships, killCount, gate)
                warningLine.append(warning)
            warnings[systemId] = ", ".join(warningLine)
        return warnings


def main():
    gatecheck = GateCheck(None)
    gatecheck.get_warnings(None, None)

if __name__ == "__main__":
    main()


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
