from opensky_api import OpenSkyApi
import mysql.connector
import time

# from Main import user, password
while True:
    api = OpenSkyApi()
    user = 'Sergei'
    password = 'programmlife4775'

    cnx = mysql.connector.connect(user=user, password=password,
                                  host='127.0.0.1',
                                  database='opensky')

    cursor = cnx.cursor()

    '''Отбор всех воздушных средств'''
    states = api.get_states()
    for s in states.states:
        query = ("REPLACE INTO table1 (icao24, callsign, origin_country, category) "
                 "VALUES (%s, %s, %s, %s)")
        cursor.execute(query, (s.icao24, s.callsign, s.origin_country, s.category))


    cnx.commit()

    # cursor.close()
    cnx.close()
    time.sleep(600)