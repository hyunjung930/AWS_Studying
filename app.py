import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from botocore.client import Config
import pymysql.cursors
import boto3

s3 = boto3.client('s3', config=Config(
    region_name = 'ap-northeast-2',
    signature_version='s3v4'))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
# print(app.config['UPLOAD_FOLDER'])

@app.route("/")
def hello_world():
    return "<p>Hello, Flask!</p>"

@app.route("/new-movie")
def show_movie_form():
    return render_template("upload.html")

@app.route("/movies", methods=['POST'])
def insert_movie():
    connection = pymysql.connect(host='sesac-db.cyll0mqkobhi.ap-northeast-2.rds.amazonaws.com',
                             user='sesac',
                             password='sesac2022',
                             database='SesacMovies',
                             cursorclass=pymysql.cursors.DictCursor)    

    title = request.form['title']
    # poster = request.form['poster']
    file = request.files['poster']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    print(filepath)

    response = s3.upload_file(filepath, 'sesac-sample', f'upload/{filename}',
        {'ContentType':'image/jpeg'})

    url = s3.generate_presigned_url('get_object',
        Params={
            'Bucket': 'sesac-sample',
            'Key': f'upload/{filename}'
        })
    print('generate_presigned_url ', url)

    with connection:
        with connection.cursor() as cursor:        
            sql = 'INSERT INTO movies (title, poster) VALUES (%s, %s)'
            cursor.execute(sql, (title, url))
        connection.commit()

    # return f'Insert Movie title: {title}, poster: {url}' 
    return redirect('/movies')

@app.route("/movies", methods=['GET'])
def show_movies():
    connection = pymysql.connect(host='sesac-db.cyll0mqkobhi.ap-northeast-2.rds.amazonaws.com',
                             user='sesac',
                             password='sesac2022',
                             database='SesacMovies',
                             cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT id, title, poster FROM movies"
            cursor.execute(sql)
            result = cursor.fetchall()
            response = ""
            for item in result:
                response += f'<li><img src="{item["poster"]}" height="60"/>{item["title"]}</li>'
                print(f'{item["id"]} - {item["title"]} - {item["poster"]}')                             

    return f'''
        <html>
        <body>
        <a href="/new-movie">새 영화 추가</a>
        <ul>
            {response}
        </ul>
        </body>
        </html>
    '''
