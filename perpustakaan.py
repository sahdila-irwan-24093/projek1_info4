class Buku:
    def __init__(self, kode, judul, penulis):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True


    def info(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.kode} | {self.judul} | {self.penulis} | {status}"

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            print(buku.info())

    def pinjam_buku(self, kode):
        for buku in self.daftar_buku:
            if buku.kode == kode and buku.tersedia:
                buku.tersedia = False
                print("Buku berhasil dipinjam")
                return
            print("Buku tidak tersedia atau kode salah")

# Program Utama
perpus = Perpustakaan()

# Data awal
perpus.tambah_buku(Buku("01", "Python Dasar", "Dila"))
perpus.tambah_buku(Buku("02", "PBO Python", "Zeel"))
perpus.tambah_buku(Buku("03", "Struktur Data", "Marsella"))

# Menu sederhana
while True:
    print("=== MENU PERPUSTAKAAN ===")
    print("1. Tampilkan Buku")
    print("2. Pinjam Buku")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        perpus.tampilkan_buku()
    elif pilihan == "2":
        kode = input("Masukkan kode buku: ")
        perpus.pinjam_buku(kode)
    elif pilihan == "3":
        print("Terima kasih")
        break
    else:
        print("Pilihan tidak valid")