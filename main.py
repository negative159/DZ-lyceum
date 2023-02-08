from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adgqwayighoauishduiasbfaiu'


class AccessForm(FlaskForm):
    id_astronaut = StringField('Id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('Id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


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


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = AccessForm()
    return render_template('login.html', form=form)


@app.route('/distribution')
def distribution():
    passengers = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон бин']
    return render_template('distribution.html', passengers=passengers)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
