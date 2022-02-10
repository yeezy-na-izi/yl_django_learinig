import sqlite3

name = input()
invisibility = int(input())
column = input()

database = sqlite3.connect(name)
cursor = database.cursor()
ans = cursor.execute(f'SELECT p.name, d.{column} FROM demiguisse d join places p on d.place_id=p.id '
                     f'where d.invisibility >= {invisibility} order by d.invisibility desc, p.name asc')
for i in ans:
    print(*i)