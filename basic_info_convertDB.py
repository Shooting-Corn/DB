import scipy.io
import csv
import pymysql

conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='shootingcorn', 
    db = 'movie_info',
    charset='utf8')

curs = conn.cursor()

conn.commit()

f = open('R_movie_info.csv','r')

csvReader = csv.reader(f)

for row in csvReader:
    movie_key = (row[0])
    title = (row[1])
    directors = (row[2])
    stars = (row[3])
    genre = (row[4])
    runtime = (row[5])
    grade = (row[6])
    synopsis = (row[7])
    violence_per = (row[8])
    violence = (row[9])
    nudity = (row[10])
    word = (row[11])
    alcohol = (row[12])

    ## movie_key,title,directors,stars,genre,runtime,grade,synopsis,violence,violence,nudity,word,alcohol

    ## 첫 줄은 Table 생성 & Column 지정
    if csvReader.line_num == 1:
        sql = f'''CREATE TABLE `Metadata` (
            `{movie_key}` char(10) Not NULL,
            `{title}` varchar(255) Not NULL,
            `{directors}` varchar(255),
            `{stars}` varchar(100),
            `{genre}` varchar(50),
            `{runtime}` char(10),
            `{grade}` char(10),
            `{synopsis}` longtext,
            `{violence_per}` char(10),
            `{violence}` int, 
            `{nudity}` int, 
            `{word}` int,
            `{alcohol}` varchar(50)
        );'''
        #curs.execute(sql)
    else:
        sql = """insert into Metadata (Movie_key, Title, Directors, Stars, Genre, Runtime, Grade, Synopsis, Violence_per, Violence, Nudity, Word, Alcohol) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        curs.execute(sql, (movie_key, title, directors, stars, genre, runtime, grade, synopsis, violence_per, violence, nudity, word, alcohol))



#db의 변화 저장

conn.commit()

    

f.close()

conn.close()