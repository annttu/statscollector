import routes
import database

if __name__ == '__main__':
    database.DB.create_tables()
    routes.collector.run(debug=True, reloader=True)