import mysql.connector
import os
import getpass

def tambah(db, i):
  n = input("Masukan nama: ")
  a = input("Masukan alamat: ")
  val = (n,a,i)
  cursor = db.cursor()
  sql = "INSERT INTO customers (name, address, iduser) VALUES (%s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))

def show(db):
  cursor = db.cursor()
  sql = "SELECT * FROM customers"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def update(db, i):
  cursor = db.cursor()
  show(db)
  customer_id = input("pilih id customer> ")
  n = input("Nama baru: ")
  a = input("Alamat baru: ")
  sql = "UPDATE customers SET name=%s, address=%s, iduser=%s WHERE customer_id=%s"
  val = (n, a, i, customer_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete(db):
  cursor = db.cursor()
  show(db)
  customer_id = input("pilih id customer> ")
  sql = "DELETE FROM customers WHERE customer_id=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def cari(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  if cursor.rowcount < 1:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def login(db, i, p):
    cursor = db.cursor()
    print("LOGIN")
    val = (i, p)
    sql = "SELECT * FROM user WHERE iduser= %s AND pasw=%s"
    cursor.execute(sql, val)
    results = cursor.fetchall()
    if cursor.rowcount < 1:
      print("login gagal!")
      main()
    else:
      for data in results:
        print ("login as ", i)

def main():
  db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="daftardb"
  )
  i = input("userID: ")
  p = getpass.getpass("password: ")
  login(db, i, p)
  loop = 'true'
  while (loop == 'true'):
    print("------------------------------------------------------------------------------")
    print("  1.Insert     2.Tampilkan     3.Update      4.Hapus     5.Cari      0.Keluar ")
    print("------------------------------------------------------------------------------")
    print("login ID:%s" %i)
    menu = input("Pilih menu>  ")

    #clear screen
    os.system("cls")
    if menu == "1":
      tambah(db, i)
    elif menu == "2":
      show(db)
    elif menu == "3":
      update(db, i)
    elif menu == "4":
      delete(db)
    elif menu == "5":
      cari(db)
    elif menu == "0":
      exit() 
    else:
      print("Menu salah!")
if __name__ == "__main__":
  main()

  
