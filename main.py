"Program manajemen kontak"

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong")
        return 1

def menambah_kontak():
    # menambah kontak
    nama = input("Masukan nama kontak yang baru: ")
    HP = input("Masukan nomor HP kontak yang baru: ")
    email = input("Masukan email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil di tambahkan!")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukan nomor kontak yang akan di hapus: "))
        del kontak[i_hapus - 1]
        print("Kontak yang dimaksud sudah dihapus")


kontak1 = {'nama' : "Andi", 'HP' : '12332121', 'email' : 'Andy@python.com'}
kontak2 = {'nama' : "Ani", 'HP' : '12332122', 'email' : 'Ani@python.com'}
kontak = [kontak1,kontak2]

while True:
    print("\n Menu kontak")
    print("1. Melihat semua kontak")
    print("2. Menambah kontak baru")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukan pilihan menu kontak(1,2,3 atau 4): ")

    if pilihan == '1':
        melihat_kontak()

    elif pilihan == '2':
       menambah_kontak()


    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        break
    else:
        print("anda memasukan pilihan yang salah")
