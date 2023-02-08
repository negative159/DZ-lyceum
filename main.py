from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/list_prof/<text>')
def second(text):
    list_prof = ['Пилот', 'Доктор', 'Штурман']
    return render_template('index.html', list=list_prof, text=text)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    form = {'surname': 'Стив Джобс', 'name': 'Марк Цукерберг',
            'education': 'GLOBAL (10 LVL FaceIT)', 'profession': 'Охотник на монстров',
            'sex': 'Альфа', 'motivation': 'Поесть во Вкусно и Точка',
            'ready': 'Вы готовы дети? True'}
    return render_template('auto_answer.html', **form)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
