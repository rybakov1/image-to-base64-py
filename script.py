import psycopg2
import base64

connection = psycopg2.connect(database="database", user="user", password="password", host="host", port=port)

cursor = connection.cursor()
paths = []
base64Strings = []
id = 4

for path in paths:
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        base64Strings.append(encoded_string.decode('utf-8'))

answer_paths = ','.join(paths)
answer_base64 = ','.join(base64Strings)

cursor.execute("update object set path_to_image = %s where id = %s", (answer_paths, id))
cursor.execute("update object set base64 = %s where id = %s", (answer_base64, id))
connection.commit()
connection.close()