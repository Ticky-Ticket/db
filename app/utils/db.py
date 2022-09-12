from config.db import Settings
import psycopg2
import psycopg2.extras

class Database : 
    def __init__(self) :
        self.s = Settings()
    
    def connect(self) :
        self.conn = psycopg2.connect(
            host = self.s.POSTGRES_SERVER, 
            database = self.s.POSTGRES_DB, 
            user = self.s.POSTGRES_USER, 
            password = self.s.POSTGRES_PASSWORD, 
            port = self.s.POSTGRES_PORT
        )
    
    def processor(self, res) : 
        l = []
        for i in res : 
            d = {}
            for j in i :
                d[j] = i.get(j)
            l.append(d)
        return l
    
    def execute(self, query : str, *args) :
        self.connect()
        curr = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        if len(args)==0 :
            curr.execute(query)     
        else : 
            curr.execute(query, args)
        self.conn.commit()
        self.conn.close()
    
    def fetch(self, query : str, *args) :
        self.connect()
        curr = self.conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        if len(args)==0 :
            curr.execute(query)     
        else : 
            curr.execute(query, args)
        try : 
            res = curr.fetchall()
            res = self.processor(res)
        except Exception as e: 
            print(e)
            res = None
        self.conn.commit()
        self.conn.close()
        return res