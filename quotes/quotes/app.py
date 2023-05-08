from flask import Flask, render_template
import psycopg2


app = Flask(__name__)


@app.route('/')
def index():
    connection = psycopg2.connect(
        host='127.0.0.1',
        port='5432',
        dbname='wiki_elf',
        user='postgres',
        password='4568579',
    )
    cursor = connection.cursor()

    cursor.execute('SELECT content, tags, author FROM quotes LIMIT 500')
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
