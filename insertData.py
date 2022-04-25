import pymysql.cursors

connection = pymysql.connect(host='sesac-db---------------amazonaws.com',
                             user='sesac',
                             password='-------',
                             database='SesacMovies',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO movies (title, poster) VALUES (%s, %s)'
        cursor.execute(sql, ('공기살인', 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85780/85780_320.jpg'))
    connection.commit()
