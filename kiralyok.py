from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',password='mysql',host='127.0.0.1', database='kiralyok')

cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)

print("3. feladat")
cursor.execute("SELECT nev, ragnev FROM uralkodo WHERE ragnev IS NOT NULL AND ragnev <> '' ORDER BY szul")
for uralkodo in cursor:
    print(uralkodo) 

print("4. feladat")
cursor.execute("SELECT u.nev FROM uralkodo u JOIN hivatal h ON u.azon = h.uralkodo_az WHERE h.koronazas IS NOT NULL AND h.koronazas > h.mettol;")
for uralkodo in cursor:
    print(uralkodo)

print("5. feladat")
cursor.execute("SELECT COUNT(DISTINCT h.uralkodo_az) FROM hivatal h WHERE h.mettol <= 1700 AND h.meddig >= 1601;")
for uralkodo in cursor:
    print(uralkodo)

print("6. feladat")
cursor.execute("SELECT u.nev, MAX(h.meddig - h.mettol) AS ev FROM uralkodo u JOIN hivatal h ON u.azon = h.uralkodo_az GROUP BY u.nev ORDER BY ev DESC LIMIT 1;")
for uralkodo in cursor:
    print(uralkodo)

print("7. feladat")
cursor.execute("SELECT u.nev, (h.mettol - u.szul) AS eletkor FROM uralkodo u JOIN hivatal h ON u.azon = h.uralkodo_az WHERE (h.mettol - u.szul) < 15 ORDER BY eletkor;")
for uralkodo in cursor:
    print(uralkodo)

print("8. feladat")
cursor.execute("SELECT u.nev, SUM(h.meddig - h.mettol) AS osszes_ev FROM uralkodo u JOIN hivatal h ON u.azon = h.uralkodo_az GROUP BY u.nev HAVING COUNT(h.azon) > 1;")
for uralkodo in cursor:
    print(uralkodo)

print("9. feladat")
cursor.execute("SELECT uh.nev, COUNT(DISTINCT u.azon) AS uralkodok_szama FROM uralkodohaz uh JOIN uralkodo u ON uh.azon = u.uhaz_az GROUP BY uh.nev ORDER BY uralkodok_szama DESC;")
for uralkodo in cursor:
    print(uralkodo)













cnx.close()
