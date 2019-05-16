import config
import db
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from DBUtils.PooledDB import PooledDB

ai_conn = db.ai_conn(config.poolsize,config.host,config.user,config.passwd,config.db,config.port,config.dbchar)
ai_conn.create_pool()


def test():
    sql = """
    select 1
    """
    result = ai_conn.get_data(sql)
    l = []
    for i in result:
        d = {}
        d["src_name"] = i[0]
        l.append(d)
    return l

