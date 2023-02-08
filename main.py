from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/list_prof/<text>')
def second(text):
    list_prof = ['Пилот', 'Доктор', 'Штурман']
    return render_template('index.html', list=list_prof, text=text)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
