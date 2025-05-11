from article import Article
import sqlite3
class Database:
    SCHEMA = "schema.sql"
    DATABASE = "database.db"
    """""
    """""
    """""
    """""
    @staticmethod
    def execute(sql, params=()):
        # ПОДКЛЮЧАЕМСЯ К БАЗЕ ДАННЫХ
        connection = sqlite3.connect(Database.DATABASE)

        # получаем курсор
        cursor = connection.cursor()

        # выполнение скрипта для базы данных
        cursor.execute(sql, params)

        # фиксируем измнения в бвзе данных
        connection.commit()
    """""
    """""
    """""
    """""
    @staticmethod
    def select(sql, params=()):
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execute(sql, params)

        raw_articles = cursor.fetchall()

        articles = []
        for id, title, content, photo in raw_articles:
            article = Article(title, content, photo, id)
            articles.append(article) 
        return articles
    """""
    """""
    """""
    """""
    @staticmethod
    def create_table():

        with open(Database.SCHEMA) as schema_file:
            Database.execute(schema_file.read())
    """""
    """""
    """""
    """""
    @staticmethod
    def save(article:Article): #Нужна проверка на наличие такой же статьи
        if Database.find_article_by_title(article.title) is not None:
            return False
        Database.execute("INSERT INTO articles (title, content, photo) VALUES (?, ?, ?)",
                       [article.title, article.content, article.photo])
        return True
    """""
    """""
    """""
    """""
    @staticmethod
    def find_articles_by_id(id):
        articles = Database.select("SELECT * FROM articles WHERE id = ?", [id])
        if not articles:
            return None
        return articles[0]
    """""
    """""
    """""
    """""
    @staticmethod
    def delete_article_by_id(id):
        article = Database.find_articles_by_id(id)
        if article is None:
            return False
        
        Database.execute("DELETE FROM articles WHERE id = ?", [id])
        return True

    @staticmethod
    def update_article(id, title, content, photo):
        article = Database.find_articles_by_id(id)
        if article is None:
            return False
        
        Database.execute("UPDATE articles SET title = ?, content = ?, photo = ? WHERE id = ?",
                        [title, content, photo, id])
        return True

    

    @staticmethod
    def get_all_articles():
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM articles")
        raw_articles = cursor.fetchall()
        articles = []
        for id, title, content, photo in raw_articles:
            article = Article(title, content, photo, id)
            articles.append(article) 
        return articles
    
    @staticmethod
    def find_article_by_title(title):
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM articles WHERE title = ?", [title])
        articles = cursor.fetchall()

        if len(articles) == 0:
            return None
        
        id, title, content, photo = articles[0]
        article = Article(title, content, photo, id)
        return article
