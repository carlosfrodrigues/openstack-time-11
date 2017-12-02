# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi


class Database(object):
    """Database class"""

    def __init__(self):
        super(Database, self).__init__()

        self.dbpool = adbapi.ConnectionPool(
            "sqlite3", "../vagas.sqlite3", check_same_thread=False,
            timeout=60)
        
        self.create_table()
        
    def close(self):
        self.dbpool.close()

    def create_table(self):
        query_str = "CREATE TABLE IF NOT EXISTS vagas \
                    (id INTEGER PRIMARY KEY, \
                    latitude real, \
                    longitude real, \
                    positive INTEGER, \
                    negative INTEGER, \
                    unique(latitude, longitude));"

        return self.dbpool.runQuery(query_str)
        


    def add_vaga(self, lat, lon):

        param = (lat,lon)
        query_str = "insert or ignore into vagas values (null,?,?,0,0)"

        return self.dbpool.runQuery(query_str,param)


    def consulta_positiva(self,lat,lon):

        param = (lat,lon)

        query_str = "select distinct positive from vagas where "
        query_str += "latitude = ? and longitude = ? limit 1"

        return self.dbpool.runQuery(query_str,param)

    def update_positivo(self,lat,lon,pos):

        param = (pos,lat,lon)
        print(pos)

        query_str = "update vagas set positive = ? where "
        query_str += "latitude = ? and longitude = ?"

        return self.dbpool.runQuery(query_str,param)




    def consulta_negativa(self,lat,lon):

        param = (lat,lon)

        query_str = "select distinct negative from vagas where "
        query_str += "latitude = ? and longitude = ? limit 1"

        return self.dbpool.runQuery(query_str,param)

    def update_negativo(self,lat,lon,neg):

        param = (neg,lat,lon)
        

        query_str = "update vagas set negative = ? where "
        query_str += "latitude = ? and longitude = ?"

        return self.dbpool.runQuery(query_str,param)




    def todas_vagas(self):

        query_str = "select * from vagas"

        return self.dbpool.runQuery(query_str)