database_username = "statscollector"
database_password = "changeme"
database_hostname = "localhost"
database_database = "statscollector"


try:
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
    import local_config
except ImportError:
    print("Cannot import local settings")