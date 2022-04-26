from flask import Flask, render_template, request
import pymysql.cursors


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/movies", methods=['POST'])
def insert_movie():
    connection = pymysql.connect(host='sesac-db---------------------------amazonaws.com',
                             user='-----',
                             password='---------',
                             database='SesacMovies',
                             cursorclass=pymysql.cursors.DictCursor)
    title = request.form['title']
    poster = request.form['poster']
    print(f'title: {title}, poster: {poster}')

    with connection:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO movies (title, poster) VALUES (%s, %s)'
            cursor.execute(sql, (title, poster))
        connection.commit()            

    return f'title: {title}, poster: {poster}'

@app.route("/new-movie")
def show_movie_form():
    return render_template('upload.html')


@app.route("/movies", methods=["GET"])
def show_movies():
    connection = pymysql.connect(host='sesac-db--------------------------amazonaws.com',
                             user='-----',
                             password='---------',
                             database='SesacMovies',
                             cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT id, title, poster FROM movies"
            cursor.execute(sql)
            result = cursor.fetchall()
            response = ""
            for item in result:
                response += f'<li><img src="{item["poster"]}" height="50"/>{item["title"]}</li>'
            return f'''
                    <html>
                    <body>
                    <ul>{response}</ul>
                    </body>
                    </html>'''


