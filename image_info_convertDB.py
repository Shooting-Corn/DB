import pymysql

conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='shootingcorn', 
    db = 'movie_info',
    charset='utf8')
cursor = conn.cursor()
col_info = "poster"            ### change TABLE COLUMN NAME 
obj_info = "kiss scene"            ### change DARKNET OBJECT NAME  
col_sql = f"ALTER TABLE `Metadata` ADD `{col_info}` LONGTEXT DEFAULT NULL;"
update_sql = f"UPDATE Metadata SET {col_info} = %s WHERE row_num = %s;"
insert_sql = f"INSERT INTO Metadata (idx, {col_info}) VALUES (%s, %s)"
#cursor.execute(col_sql)
#cursor.execute("ALTER TABLE movie_info.Metadata ADD COLUMN row_num INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;")
f = open("Raw_movie_info/nonR_img.txt", 'r')
flag = 400      ## modify!!

lines = f.readlines()

for line in lines:
    flag+=1
    cursor.execute(update_sql, (line, flag))

f.close()

conn.commit()
conn.close()