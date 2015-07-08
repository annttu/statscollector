import routes
import database

if __name__ == '__main__':
    database.DB.create_tables()
    routes.collector.run(host=configuration.address, port=configuration.port, debug=configuration.debug, reloader=configuration.debug)