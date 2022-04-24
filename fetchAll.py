import pymysql.cursors

connection = pymysql.connect(host='sesac-db------------amazonaws.com',
                             user='-----',
                             password='---------',
                             database='SesacMovies',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        sql = "SELECT id, title, poster FROM movies"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            print(f'{item["id"]} - {item["title"]} - {item["poster"]}')
