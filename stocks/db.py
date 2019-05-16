#coding:utf-8              #由于.py文件是utf-8的，所以必须有这一句
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from DBUtils.PooledDB import PooledDB


class ai_conn():
    def __init__(self,poolsize,host,user,passwd,db,port,dbchar):
        self.poolsize = poolsize
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.pool = None
        self.conn = None
        self.dbchar = dbchar
    def create_pool(self):
        self.pool = PooledDB(MySQLdb,self.poolsize,host=self.host,user=self.user,passwd=self.passwd,charset=self.dbchar,db=self.db,port=self.port)

    def get_data(self,sql):
        conn = self.pool.connection()
        cur = conn.cursor()
        r = cur.execute(sql)
        r = cur.fetchall()
        cur.close()
        conn.close()
        return r

    def get_data_result(self,sql):
        try:
            conn = self.pool.connection()
            cur = conn.cursor()
            r = cur.execute(sql)
            r = cur.fetchall()
            cur.close()
            conn.close()
        except Exception as e:
            conn.rollback()
            conn.close()
            return False,str(e)
        return True,r

    def transaction(self,sql):
        conn = self.pool.connection()
        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            conn.close()
            return False,str(e)
        conn.close()
        return True,"Success"

    def transaction1(self,sql1,sql2):
        conn = self.pool.connection()
        try:
            cur = conn.cursor()
            cur.execute(sql1)
            cur.execute(sql2)
            conn.commit()
        except Exception as e:
            conn.rollback()
            conn.close()
            return False,str(e)
        conn.close()
        return True,"Success"
