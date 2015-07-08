database_username = "statscollector"
database_password = "changeme"
database_hostname = "localhost"
database_database = "statscollector"

address = "127.0.0.1"
port = 8080
debug = False


try:
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
    from local_config import *
except ImportError:
    print("Cannot import local settings")