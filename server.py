from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def ruwiki():
    return render_template('ruwiki.html')

@app.route('/sonic')
def sonic_article():
    text_article="""Ёж Со́ник яп.(ソニック・ザ・ヘッジホッグСоникку дза Хэдзихоггу,англ. Sonic the Hedgehog)— главный персонаж серии видеоигр Sonic the Hedgehog от компании,а также созданных на её основе комиксов,мультсериалов и полнометражных фильмов.Соник — синий антропоморфный ёж, созданный художником Наото Осимой,программистом Юдзи Накой и дизайнером Хирокадзу Ясухарой. Во времяразработки было предложено множество образов главного героя будущейигры, но разработчики остановились на ёжике синего цвета. Своё имяСоник получил за способность бегать на сверхзвуковых скоростях(англ. sonic — «звуковой; со скоростью звука»).Геймплей за Соника в большинстве игр серии Sonic the Hedgehogзаключается в быстром прохождении уровней и битвах с врагами, дляатаки которых Соник сворачивается в шар во время прыжка. Немаловажнуюроль для Соника играют золотые кольца, служащие ему в качестве защиты.Главным антагонистом героя является доктор Эггман, который хочет захватитьмир и построить свою империю «Эггманленд».После выхода одноимённой игры с его участием Соник быстро стал популярным вовсём мире и положил начало крупной медиафраншизе. Персонаж стал талисманом компании Sega,которым остаётся и сейчас, сменив Алекса Кидда, бывшего неофициальным маскотом компании до 1990года.На ноябрь 2014 года было продано свыше 150 миллионов экземпляров игр серии о Сонике[4]. Помимокомпьютерных игр,ёж Соник является главным героем комиксов, книг, ряда мультсериалов и полнометражных аниме ифильмов."""

    article_image_title="Ёж Соник"
    title_article="Ёж Соник"
    article_image_path="static/sonic.png"
    return render_template('article.html', title_article=title_article,
                           article_image_title=article_image_title,
                            text_article=text_article,
                            article_image_path=article_image_path)

@app.route('/naklz')
def naklz_article():
    text_article="""Ехидна Наклз[2] (яп. ナックルズ・ザ・エキドゥナ Наккурудзу дза Экидуна, англ. Knuckles the Echidna) — персонаж видеоигр, телешоу и комиксов серии Sonic the Hedgehog. Его прозвища — «Knuckie», «Rad Red», «Red Storm», «Knux», и «Knucklehead». Создан Такаси Юдой. Первое появление — игра Sonic the Hedgehog 3"""
    article_image_title="Ехидна Наклз"
    title_article="Ехидна Наклз"
    article_image_path="static/Naklz.png"
    return render_template('article.html', title_article=title_article,
                           article_image_title=article_image_title,
                            text_article=text_article,
                            article_image_path=article_image_path)

@app.route('/hello')
def hello():
    return "Hello world!"

@app.route("/max")
def find_max():
    a = int(request.args["a"])
    b = int(request.args["b"])

    if a > b:
        return f"<h1> максимум это число а: {a}</h1>"
    else:
        return f"<h1> максимум это число b: {b}</h1>"
    
@app.route("/base")
def base():
    return render_template("base.html", title="Китайский новый год")

if __name__ == '__main__':
    app.run(debug=True)
