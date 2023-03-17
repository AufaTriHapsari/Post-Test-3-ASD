import os
from prettytable import PrettyTable
import datetime
from datetime import timedelta
import time

os.system('cls')

print("""
      ==========================================
                 Aufa Tri Hapsari
                   2209116031
              Program Reservation Hotel
      =========================================\n""")
time.sleep(3)
os.system("cls")


#class  node linked list
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
class nodeHotel:
    def __init__(self, roomtype, person , lokasi, Chekin, Chekout, tarif, nextHotel=None):
        self.roomtype = roomtype
        self.person = person
        self.lokasi = lokasi
        self.chekin = Chekin
        self.chekout = Chekout
        self.tarif = tarif
        self.nextHotel = nextHotel

    def __str__(self):
        return f"{self.roomtype} {self.person} {self.lokasi} {self.chekin} {self.chekout} {self.tarif}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def addhotel(self, roomtype, person, lokasi, chekin, chekout, tarif):
        if self.head == None:
            self.head = nodeHotel(roomtype, person, lokasi, chekin, chekout, tarif)
            self.tail = self.head
            self.history.append('Add')
        else:
            self.tail.nextHotel = nodeHotel(roomtype, person, lokasi, chekin, chekout, tarif)
            self.tail = self.tail.nextHotel
        self.history.append(('Add', (roomtype, person, lokasi, chekin, chekout, tarif)))

    def tampikanhotel(self):
        temp = self.head

        table = PrettyTable(['No.', 'kamar', 'person', 'lokasi', 'Waktu chekin', 'Waktu chekout', 'Harga'])
        number = 1
        while temp != None:
            table.title = 'Daftar reservasi hotel'
            table.add_row(
                [number, temp.roomtype, temp.person, temp.lokasi, temp.chekin, temp.chekout, temp.tarif])
            number += 1
            temp = temp.nextHotel
        print(table)

    def remove(self, number):
        temp = self.head
        prev = None
        count = 1
        while temp and count != number:
            prev = temp
            temp = temp.nextHotel
            count += 1

        if temp is None:
            return

        if prev is None:
            self.head = temp.nextHotel
            
        else:
            prev.nextHotel = temp.nextHotel
        self.history.append(
            ('Delete', (temp.roomtype, temp.person, temp.lokasi, temp.chekin, temp.chekout, temp.tarif)))

    def paginate(self, page, size):
        temp = self.head
        table = PrettyTable(['No.', 'Kamar', 'person', 'lokasi', 'Waktu chekin', 'Waktu chekout', 'Harga'])
        number = (page - 1) * size + 1
        table.title = f'Halaman {page}'
        count = 0
        while temp != None:
            if count >= (page - 1) * size and count < page * size:
                table.add_row([number, temp.roomtype, temp.person, temp.lokasi, temp.chekin, temp.chekout,
                               temp.tarif])
                number += 1
            count += 1
            temp = temp.nextHotel
        print(table)

    def historyAddDelete(self):
        table = PrettyTable(
            ['No.', 'Action', 'Kamar', 'person', 'lokasi', 'Waktu chekin', 'Waktu chekout', 'Harga'])
        number = 1
        for i in self.history:
            table.title = 'Riwayat Add/Delete'
            if i[0] == 'Add':
                table.add_row([number, i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]])
            elif i[0] == 'Delete':
                table.add_row([number, i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]])
            number += 1
        print(table)
        
       
def loginuser():
    while True:
        print()
        waktu = datetime.datetime.now() 
        print (waktu)
        import time
        
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("============== SELAMAT DATANG DI PROGRAM PEMESANAN  HOTEL ==============")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
        print("Silahkan Input Nama Pengguna Anda Untuk Melakukan Pemesanan!")
        print('''  
        ----------------------------------
        |           Menu Utama           |
        ----------------------------------    
        |     | No |   Menu              |
        |  >>>| 1. |   Login             |  
        |  >>>| 2. |   Exit              |  
        -----------------------------------
       ''')
        pilih = input ("Masukan menu yang diinginkan : ")
        print("Loading..")
        time.sleep(2)
        os.system("cls")
        
        if pilih == "1":
            os.system("cls")
            nama= input ("Silahkan masukan ursename anda : ")
            print("Data Anda sedang diproses....")
            time.sleep(3)
            os.system("cls")
            print("=========================lOGIN BERHASIL===========================\n")
            time.sleep(2)
            os.system("cls")
            print ("="*70)
            print ("\t       ===== Selamat Datang  Guest", nama,  "=====")
            main()
            
        elif pilih == "2":
            print("======================================================================================") 
            print("    ==================TERIMAKASIH SAMPAI JUMPA LAGI😊======================    ")
            print("======================================================================================")
            exit()
            
        else:
            print("Menu Tidak Tersedia")  
                  
def main():
    hotel = LinkedList()

    hotel.addhotel('Suite room', 'Dua', 'Jakarta', 'Senin, 13 Maret 2023 12:00', 'Selasa, 14 Maret 2023 06:50', 1200000)
    hotel.addhotel('Family room', 'Lima', 'Solo', 'Rabu, 11 Juni 2022 15:00', 'Jumat, 14 Juni 2023 09:30', 1500000)
    hotel.addhotel('Luxury room', 'Empat', 'Balikpapan', 'Senin, 13 Mei 2023 12:00', 'Kamis, 16  Mei 2023 06:50', 2300000)
    hotel.addhotel('Twins room', 'Empat', 'Jambi', 'Senin, 13 Maret 2023 05:00', 'Rabu, 15 Maret 2023 09:30', 2000000)
    hotel.addhotel('Family room', 'Lima', 'Magelang', 'Sabtu, 6 Maret 2023 12:00', 'Minggu, 7 Maret 2023 07:20', 1500000)
    hotel.addhotel('Standar room', 'Satu', 'Balikpapan', 'Minggu, 1 Febuari 2023 05:00', 'Senin, 2 Febuari 2023 06:50', 1000000)
    hotel.addhotel('Suite room', 'Dua', 'Balikpapan', 'Senin, 17 Juli 2023 09:00', 'Rabu, 19 Juli 2023 08:00', 1200000)
    hotel.addhotel('Suite room', 'Dua', 'Balikpapan', 'Minggu, 16 Desember 2022 05:00', 'Senin, 23 Desember 2022 06:00', 1200000)
    hotel.addhotel('Deluxe room', 'Tiga', 'Semarang', 'Sabtu, 17 Agustus 2023 12:00', 'Minggu, 18 Agustus 2023 08:30', 2100000)
    hotel.addhotel('Twins room', 'Empat', 'Bali', 'Kamis, 10 Oktober 2022 11:00', 'Sabtu 12 Oktober 2022 12:45', 2300000)
    hotel.addhotel('Family room', 'Enam', 'Makasar', 'Rabu, 10 Juli 2022 17:00', 'Jumat, 12 Juli 2022 10:30', 1500000)
    hotel.addhotel('Family room', 'Lima', 'Solo', 'Minggu, 21 September 2022 12:00', 'Senin, 22 September 2023 11:00', 1500000)

    while True:
        choice = int(input('''
            ==========================================
            |          M E N U   H O T E L           |
            ==========================================
            |   > 1. Tambah Pemesanan hotel          |
            |   > 2. Hapus pemesanan hotel           |
            |   > 3. Halaman pemesanan               |
            |   > 4. History Add/Delete              |
            |   > 5. Exit From Menu Hotel            |
            ==========================================
            Pilih nomor : '''))

        if choice == 1:
            roomtype = str(input('Pilih Jenis Kamar yang diinginkan : '))
            person = str(input('Pemasan untuk berapa orang? : '))
            lokasi = str(input('Mau nginep dimana?  : '))
            chekin = str(input('Chek in : '))
            chekout = str(input('Chek out : '))
            tarif = int(input('Harga : '))
            hotel.addhotel(roomtype, person, lokasi, chekin, chekout, tarif)
            print("Data Berhasil Ditambahkan")
            mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
            print("Back To Menu..")
            time.sleep(2)
            os.system("cls")

        elif choice == 2:
            hotel.tampikanhotel()
            number = int(input('Masukan Nomor Pemesenan Yang Ingin Dihapus : '))
            hotel.remove(number)
            print("Data Berhasil Dihapus")
            mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
            print("Back To Menu..")
            time.sleep(2)
            os.system("cls")

        elif choice == 3:
            hotel.paginate(1, 5)
            hal = str(input('Apakah ingin lanjut ke halaman berikutnya? (ya/no) : '))
            while hal == 'ya':
                page = int(input('Page : '))
                hotel.paginate(page, 5)
                hal = str(input('Apakah ingin lanjut ke halaman berikutnya? (ya/no) : '))
                
            else:
                mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
                print("Back To Menu..")
                time.sleep(2)
                os.system("cls")
                continue           

        elif choice == 4:
            hotel.historyAddDelete()
            mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
            print("Back To Menu..")
            time.sleep(2)
            os.system("cls")
            
        elif choice == 5:
          break

        else:
            print('Maaf, Pilihan tidak tersedia')


loginuser()
