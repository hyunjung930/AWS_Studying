import pymysql.cursors

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
        for item in result:
            print(f'{item["id"]} - {item["title"]} - {item["poster"]}')