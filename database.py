from article import Article
import sqlite3

class Database:
    articles = []

    SCHEMA = "schema.sql"
    DATABASE = "database.db"

    @staticmethod
    def execute(sql, params=()):
        # ПОДКЛЮЧАЕМСЯ К БАЗЕ ДАННЫХ
        connection = sqlite3.connect(Database.DATABASE)

        # получаем курсор
        cursor = connection.cursor()

        # выполнение скрипта для базы данных
        cursor.execut(sql, params)

        # фиксируем измнения в бвзе данных
        connection.commit()



    @staticmethod
    def create_table():

        with open(Database.SCHEMA) as schema_file:
            Database.execute(schema_file.read())


    @staticmethod
    def save(article:Article): #Нужна проверка на наличие такой же статьи
        if Database.find_article_by_title(article.tirle) is not None:
            return False
        Database.execute("INSERT INTO articles VALUE (?, ?, ?)",
                       [article.title, article.content, article.photo])
        return True
    
    @staticmethod
    def get_all_articles():
        return Database.articles
    
    @staticmethod
    def find_article_by_title(title):
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execut("SELECT * FROM articles WHERE title = ?", [title])
        articles = cursor.fetchall()

        if len(articles) == 0:
            return None
        
        article = Article(
            articles[0][0],
            articles[0][1],
            articles[0][2],
            articles[0][3])
        return article
