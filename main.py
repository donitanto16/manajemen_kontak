"Program manajemen kontak"

class kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong")
            return 1

    def menambah_kontak(self):
        # menambah kontak
        nama = input("Masukan nama kontak yang baru: ")
        HP = input("Masukan nomor HP kontak yang baru: ")
        email = input("Masukan email kontak yang baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil di tambahkan!")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukan nomor kontak yang akan di hapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak yang dimaksud sudah dihapus")

kontak_kantor = kontak()
kontak_keluarga = kontak()

while True:
    print("\n Menu kontak")
    print("1. Melihat semua kontak")
    print("2. Menambah kontak baru")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukan pilihan menu kontak(1,2,3 atau 4): ")

    if pilihan == '1':
       kontak_kantor.melihat_kontak()

    elif pilihan == '2':
       kontak_kantor.menambah_kontak()


    elif pilihan == '3':
       kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("anda memasukan pilihan yang salah")
