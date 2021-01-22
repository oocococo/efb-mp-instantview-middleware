import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class dbManager:
    def __init__(self,dbname: str,username: str,password: str='',hostname: str='192.168.1.50'):
        self.conn = psycopg2.connect("dbname={dbname} user={username} password={password} host={hostname}".format(dbname=dbname,hostname=hostname,password=password,username=username))
        self.cur = self.conn.cursor()
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    @staticmethod
    def dbinit(dbname: str): # return 0 if db exists, return 1 if create new db
        res=0
        conn = psycopg2.connect("user=postgres password=''")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
        cur = conn.cursor()
        # Detect exists db
        sqlDetectDatabase = "SELECT 1 FROM pg_database WHERE datname = '"+dbname+"' ;"
        cur.execute(sqlDetectDatabase)
        if cur.fetchone()[0] != 1:
            sqlCreateDatabase = "create database "+dbname+";"
            cur.execute(sqlCreateDatabase)
            res=1
        cur.close()
        conn.close()
        return res
        
