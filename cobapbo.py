import sqlite3
import pathlib

class data:
    def __init__(self):
        #database = str(pathlib.Path().absolute())+"\cobapbo.db"
        self.connector = sqlite3.connect(r"C:\Users\irzap\Downloads\cobapbo (1)\cobapbo\cobapbo.db")
        self.cursor = self.connector.cursor()

    def executeQuery(self, query, retval=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.connector.commit()
        if retval:
            return all_results

class pengguna(data):

    def __init__(self):
        data.__init__(self)
        self.user_id = None
        self.username = None
        self.password = None

    def masuk(self, username, password):
        query = 'SELECT user_id, username, password FROM user_data \
            where username=\'%s\' and password=\'%s\''
        query = query % (username, password)
        masuk = self.executeQuery(query, True)
        status = False

        for i in range(0,len(masuk)):
            if username == masuk[i][1] and password == masuk[i][2]:
                status = True
                self.user_id = masuk[i][0]
                self.username = masuk[i][1]
                self.password = masuk[i][2]
                print("berhasil masuk!")
                print(f"selamat datang {self.username}")
        if status == False:
            print("data tidak ditemukan")
    
    def daftar(self, username, password):
        query = 'INSERT INTO user_data (username, password) \
            VALUES (\'%s\', \'%s\')'
        query = query % (username, password)
        self.executeQuery(query)
        query = 'SELECT user_id, username, password FROM user_data where username=\'%s\' and password=\'%s\' '
        query = query % (username, password)
        masuk = self.executeQuery(query, True)

        for i in range(0, len(masuk)):
            if username == masuk[i][1] and password == masuk[i][2]:
                self.user_id = masuk[i][0]
            self.username
            self.password
            print("akun berhasil dibuat!")

u = pengguna()
total = 0
while True:
    print('''
    1. login
    2. register
    3. pilih jasa
    4. checkout
    5. exit program''')
    menu = input()
    
    if menu == "1":
        username = str(input("masukan username: "))
        password = str(input("masukan password: "))
        u.masuk(username, password)
    
    elif menu == "2":
        username = str(input("masukan username: "))
        password = str(input("masukan password: "))
        u.daftar(username, password)
    
    elif menu == "3":
        if u.username == None:
            print("silahkan Login / Register terlebih dahulu")
        
        else:
            print('''
            pilih jasa kami:
            1. dokter hewan
            2. salon hewan''')
            pilihjasa = input()
        
            if pilihjasa == "1":
                jenishewan = str(input("masukan jenis hewan (kucing/anjing): "))
                berat = int(input("masukan berat badan hewan (Kilogram): "))
                jenismakanan = str(input("masukan jenis makanan hewan (wetfood/dryfood): "))
                umur = int(input("masukan umur hewan (Tahun): "))
                kondisi = str(input("dekripsikan kondisi hewan tersebut : "))
            
            elif pilihjasa == "2":
                jenishewan = str(input("masukan jenis hewan (kucing/anjing): "))
                berat = int(input("masukan berat badan hewan: "))
                jenismakanan = str(input("masukan jenis makanan hewan (wetfood/dryfood): "))
                umur = int(input("masukan umur hewan: "))

    elif menu == "4":
        if u.username == None:
            print("silahkan Login / Register terlebih dahulu")
        elif pilihjasa == "1":
            if jenishewan == "kucing":
                total += 150_000
                print("total checkout anda adalah: ")
                print((str(total)), " Ribu Rupiah")
            elif jenishewan == "anjing":
                total += 170_000
                print("total checkout anda adalah: ")
                print((str(total)), " Ribu Rupiah")
            else:
                print("error")
        
        elif pilihjasa == "2":
            if jenishewan == "kucing":
                total += 200_000
                print("total checkout anda adalah: ")
                print((str(total)), " Ribu Rupiah")
            elif jenishewan == "anjing":
                total += 250_000
                print("total checkout anda adalah: ")
                print((str(total)), " Ribu Rupiah")
            else:
                print("error")

    elif menu == "5":
        print("selamat tinggal!")
        break
