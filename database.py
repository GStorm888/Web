from article import Article

class Database:
    articles = []

    @staticmethod
    def save(article:Article):
        Database.articles.append(article) #Нужна проверка на наличие такой же статтьи

    @staticmethod
    def get_all_articles():
        return Database.articles