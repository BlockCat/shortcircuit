import requests
import logging
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
    def loadNetwork(self, list):
		query = ",".join(list)
        try:
            r = requests.get("http://eve-gatecheck.space/eve/get_kills.php?systems=" + query)
        except requests.exceptions.RequestException:
            logging.warning("Unable to connect to eve-gatecheck")
        else:
            if r.status_code == 200:
                return r.json()

        return {}

    def augment_map(self, solar_map, route):
        json = self.loadNetwork(route)

def main():
    bridgenetwork = BridgeNetwork(None)
    bridgenetwork.augment_map(None, None)

if __name__ == "__main__":
    main()