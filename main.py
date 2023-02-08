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


if __name__ == '__main__':
    app.run(port=8080, debug=True)
