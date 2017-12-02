# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi


class Database(object):
    """Database class"""

    def __init__(self):
        super(Database, self).__init__()

        self.dbpool = adbapi.ConnectionPool(
            "sqlite3", "../vagas.sqlite3", check_same_thread=False,
            timeout=60)

    def close(self):
        self.dbpool.close()

    def create_table(self):
        query_str = "create table if not exists vagas "
        query_str += "(id integer AUTOINCREMENT primary key, latitude real, longitude real, "
        query_str += "positive integer, negative integer "
        query_str += "unique(latitude,longitude,positive, negative));"

        return self.dbpool.runQuery(query_str)


    def add_vaga(self, lat, lon):

        param = (lat,lon)
        query_str = "insert or ignore into vagas values (null,?,?,null,null)"

        return self.twisted_dbpool.runQuery(query_str,param)


    def vaga_positiva(self,lat,lon):

        param = (lat,lon)
        #param = (lat,lon,)
        query_str = "select distinct positivo from vagas where "
        query_str += "latitude = ? and longitude = ?"
        
        positivo_atual = self.twisted_dbpool.runQuery(query_str,param)

        param = (lat,lon,positivo_atual+1)
        query_str = "insert or ignore into vagas values (null,?,?,?,null)"

        return self.twisted_dbpool.runQuery(query_str,param)


    def vaga_negativa(self,lat,lon):

        param = (lat,lon)
        #param = (lat,lon,)
        query_str = "select distinct negativo from vagas where "
        query_str += "latitude = ? and longitude = ?"
        
        negativo_atual = self.twisted_dbpool.runQuery(query_str,param)

        param = (lat,lon,negativo_atual+1)
        query_str = "insert or ignore into vagas values (null,?,?,null,?)"

        return self.twisted_dbpool.runQuery(query_str,param)

    def todas_vagas(self):

        query_str = "select * from vagas"

        return self.twisted_dbpool.runQuery(query_str)