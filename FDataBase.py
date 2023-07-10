import sqlite3
import time
import math

class FDataBase():
    def __init__(self, db):
        self.__db=db
        self.__cur=db.cursor()

    def get_menu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения из базы данных")
        return []

    def get_post(self, id_post):
        sql = f"SELECT title, text FROM posts WHERE id ={id_post} LIMIT 1"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res: return res
        except:
            print("Ошибка чтения из базы данных")
        return (False, False)

    def get_posts_announce(self):
        sql = f"SELECT id, title, text FROM posts ORDER BY time DESC"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения из базы данных")
        return []

    def add_post(self, title, text):
        try:
            tm =math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sql3.Error as e:
            print("Ошибка записи в базy данных"+str(e))
            return False
        return True
