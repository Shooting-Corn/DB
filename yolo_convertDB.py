import pymysql

conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='shootingcorn', 
    db = 'movie_info',
    charset='utf8')
cursor = conn.cursor()
table_info = "tt6751668"
cursor.execute(f"CREATE TABLE `{table_info}`(`idx` int NOT NULL);")

col_info = "Kiss_scene"            ### change TABLE COLUMN NAME 
obj_info = "kiss scene"            ### change DARKNET OBJECT NAME  
col_sql = f"ALTER TABLE `{table_info}` ADD `{col_info}` BOOL DEFAULT NULL;"
update_sql = f"UPDATE {table_info} SET {col_info} = %s WHERE idx = %s;"
insert_sql = f"INSERT INTO {table_info} (idx, {col_info}) VALUES (%s, %s)"
cursor.execute(col_sql)

f = open("Parasite/results_kiss.txt", 'r')
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
            cursor.execute(insert_sql, (flag, True))
            #cursor.execute(update_sql, (True, flag))
        else:
            file_list.append([flag, False])
            cursor.execute(insert_sql, (flag, False))
            #cursor.execute(update_sql, (False, flag))
        sentence = ""

f.close()

conn.commit()
conn.close()