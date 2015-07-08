from bottle import app, run, HTTPError, request, BaseRequest
import database
import hashlib
import logging

logger = logging.getLogger("Server")

collector = app()
BaseRequest.MEMFILE_MAX = 1024 * 1024

def ok(message):
    return {"status": "ok", "message": message}


def fail(message):
    return {"status": "error", "message": message}


def create_password(password):
    return "$1$%s" % hashlib.sha512(password.encode("utf-8")).hexdigest()


@collector.get("/")
def callback():
    return ok("Noting to see here!")


@collector.post("/api/import/")
def callback():
    if "key" not in request.query:
        raise HTTPError(status=401, message="Permission denied")
    key = request.query['key']

    # get key from database

    crypted_key = create_password(key)

    s = database.DB.get_session()


    print(crypted_key)
    client = s.query(database.Clients).filter(database.Clients.key==crypted_key).all()
    if len(client) == 0:
        raise HTTPError(status=401, message="Permission denied")

    print(client)
    client = client[0]


    data = request.json
    if data is None:
        logger.error("Didn't receive any data")
        raise HTTPError(status=400, message="Data missing")
    for x, t in {'tcp': database.TCPTable, 'udp': database.UDPTable}.items():
        if x in data:
            for i in data[x]:
                value = t()
                value.client = client.id
                value.elevation = i['elevation']
                value.lat = i['lat']
                value.lon = i['lon']
                value.speed = i['speed']
                value.status = i['status']
                value.timestamp = i['timestamp']
                value.value = i['value']
                if i['lat'] and i['lon']:
                    value.the_geom = 'POINT(%f %f)' % (float(i['lon']), float(i['lat']))
                s.add(value)
        else:
            logger.error("%s not found from data" % x)
    s.commit()

    return ok("statistics saved")
    #raise HTTPError(status=500, body=fail("Failed to save data"))

