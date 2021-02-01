import pymysql

conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='shootingcorn', 
    db = 'movie_info',
    charset='utf8')
cursor = conn.cursor()
col_info = "Kiss_scene"            ### change TABLE COLUMN NAME 
obj_info = "kiss scene"            ### change DARKNET OBJECT NAME  
col_sql = f"ALTER TABLE `Parasite` ADD `{col_info}` BOOL DEFAULT NULL;"
update_sql = f"UPDATE Parasite SET {col_info} = %s WHERE idx = %s;"
insert_sql = f"INSERT INTO Parasite (idx, {col_info}) VALUES (%s, %s)"
cursor.execute(col_sql)

f = open("parasite_test_results.txt", 'r')
flag = 0
file_list = []
lines = f.readlines()
sentence = ""
for line in lines:
    sentence += line
    if "Enter " in line:
        flag += 1
        if obj_info in sentence:
            file_list.append([flag, True])
            #cursor.execute(insert_sql, (flag, True))
            cursor.execute(update_sql, (True, flag))
        else:
            file_list.append([flag, False])
            #cursor.execute(insert_sql, (flag, False))
            cursor.execute(update_sql, (False, flag))
        sentence = ""

f.close()

conn.commit()
conn.close()