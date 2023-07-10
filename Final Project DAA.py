##wow


import os
from getpass4 import getpass

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def printJenisBarang(jenis):
    jenis_barang = {
        1: "Pakaian",
        2: "Makanan",
        3: "Minuman",
        4: "Lainnya"
    }
    return jenis_barang.get(jenis, "Invalid")


def printDataBarang():
    clear_screen()
    print("Data Barang:")
    print("-" * 144)
    print("| {:<5s} | {:<20s} | {:<10s} | {:<15s} | {:<15s} | {:<15s} | {:<14s} | {:<10s} | {:<12s} |".format(
        "No.", "Nama barang", "Kode", "Tanggal Masuk", "Bulan masuk", "Tahun masuk", "Jumlah(pcs)", "Jenis", "Berat(Kg)"))
    print("-" * 144)
    for i in range(len(nambar)):
        jnsbrng = printJenisBarang(jnisbrng[i])
        print("| {:<5d} | {:<20s} | {:<10s} | {:<15s} | {:<15d} | {:<15s} | {:<14s} | {:<10s} | {:<12s} | ".format(
            i + 1, nambar[i], kode[i], tgglmsuk[i], blnmsuk[i], thnmsuk[i], jmlhbrng[i], jnsbrng, brtbrng[i]))
    print("-" * 144)
    print()


def cariBarang():
    clear_screen()
    print("Menu Pencarian Barang:")
    print("1. Cari berdasarkan Kode barang")
    print("2. Cari berdasarkan Tanggal masuk barang")
    print("3. Cari berdasarkan Bulan masuk barang")
    print("4. Cari berdasarkan Tahun masuk barang")
    print("0. Batal")
    print()

    pilihan_cari = input("Pilih opsi pencarian: ")
    print()

    if pilihan_cari == "1":
        search_kode = input("Masukkan kode barang yang ingin dicari: ")
        print()
        found = False
        clear_screen()
        print("Hasil Pencarian:")
        print("-" * 144)
        print("| {:<5s} | {:<20s} | {:<10s} | {:<15s} | {:<15} | {:<15s} | {:<14s} | {:<10s} | {:<12s} |".format(
            "No.", "Nama barang", "Kode", "Tanggal Masuk", "Bulan masuk", "Tahun masuk", "Jumlah(pcs)", "Jenis", "Berat(Kg)"))
        print("-" * 144)
        for i in range(len(kode)):
            if search_kode.lower() in kode[i].lower():
                jnsbrng = printJenisBarang(jnisbrng[i])
                print("| {:<5d} | {:<20s} | {:<10s} | {:<15s} | {:<15d} | {:<15s} | {:<14s} | {:<10s} | {:<12s} | ".format(
                    i + 1, nambar[i], kode[i], tgglmsuk[i], blnmsuk[i], thnmsuk[i], jmlhbrng[i], jnsbrng, brtbrng[i]))
                found = True
        print("-" * 144)
        if not found:
            print("Tidak ada barang dengan kode yang sesuai.")
        print()

    elif pilihan_cari == "2":
        search_tanggal = input("Masukkan tanggal masuk barang yang ingin dicari: ")
        print()
        found = False
        clear_screen()
        print("Hasil Pencarian:")
        print("-" * 144)
        print("| {:<5s} | {:<20s} | {:<10s} | {:<15s} | {:<15s} | {:<15s} | {:<14s} | {:<10s} | {:<12s} |".format(
            "No.", "Nama barang", "Kode", "Tanggal Masuk", "Bulan masuk", "Tahun masuk", "Jumlah(pcs)", "Jenis", "Berat(Kg)"))
        print("-" * 144)
        for i in range(len(tgglmsuk)):
            if search_tanggal == tgglmsuk[i]:
                jnsbrng = printJenisBarang(jnisbrng[i])
                print("| {:<5d} | {:<20s} | {:<10s} | {:<15s} | {:<15d} | {:<15s} | {:<14s} | {:<10s} | {:<12s} | ".format(
                    i + 1, nambar[i], kode[i], tgglmsuk[i], blnmsuk[i], thnmsuk[i], jmlhbrng[i], jnsbrng, brtbrng[i]))
                found = True
        print("-" * 144)
        if not found:
            print("Tidak ada barang dengan tanggal masuk yang sesuai.")
        print()

    elif pilihan_cari == "3":
        search_bulan = int(input("Masukkan bulan masuk barang yang ingin dicari (1-12): "))
        print()
        found = False
        clear_screen()
        print("Hasil Pencarian:")
        print("-" * 144)
        print("| {:<5s} | {:<20s} | {:<10s} | {:<15s} | {:<15s} | {:<15s} | {:<14s} | {:<10s} | {:<12s} |".format(
            "No.", "Nama barang", "Kode", "Tanggal Masuk", "Bulan masuk", "Tahun masuk", "Jumlah(pcs)", "Jenis", "Berat(Kg)"))
        print("-" * 144)
        for i in range(len(blnmsuk)):
            if search_bulan == blnmsuk[i]:
                jnsbrng = printJenisBarang(jnisbrng[i])
                print("| {:<5d} | {:<20s} | {:<10s} | {:<15s} | {:<15d} | {:<15s} | {:<14s} | {:<10s} | {:<12s} | ".format(
                    i + 1, nambar[i], kode[i], tgglmsuk[i], blnmsuk[i], thnmsuk[i], jmlhbrng[i], jnsbrng, brtbrng[i]))
                found = True
        print("-" * 144)
        if not found:
            print("Tidak ada barang dengan bulan masuk yang sesuai.")
        print()

    elif pilihan_cari == "4":
        search_tahun = input("Masukkan tahun masuk barang yang ingin dicari: ")
        print()
        found = False
        clear_screen()
        print("Hasil Pencarian:")
        print("-" * 144)
        print("| {:<5s} | {:<20s} | {:<10s} | {:<15s} | {:<15s} | {:<15s} | {:<14s} | {:<10s} | {:<12s} |".format(
            "No.", "Nama barang", "Kode", "Tanggal Masuk", "Bulan masuk", "Tahun masuk", "Jumlah(pcs)", "Jenis", "Berat(Kg)"))
        print("-" * 144)
        for i in range(len(thnmsuk)):
            if search_tahun == thnmsuk[i]:
                jnsbrng = printJenisBarang(jnisbrng[i])
                print("| {:<5d} | {:<20s} | {:<10s} | {:<15s} | {:<15d} | {:<15s} | {:<14s} | {:<10s} | {:<12s} | ".format(
                    i + 1, nambar[i], kode[i], tgglmsuk[i], blnmsuk[i], thnmsuk[i], jmlhbrng[i], jnsbrng, brtbrng[i]))
                found = True
        print("-" * 144)
        if not found:
            print("Tidak ada barang dengan tahun masuk yang sesuai.")
        print()

    elif pilihan_cari == "0":
        return

    else:
        print("Pilihan tidak valid!")
        print()


def simpanDataTabel():
    clear_screen()
    print("Cetak Data barang")
    nama_file = input("Masukkan nama file (tanpa ekstensi): ")
    nama_file += ".txt"

    try:
                with open(nama_file, "w") as file:
                    file.write("Data Barang:\n")
                    file.write("-" * 144)
                    file.write("\n")
                    file.write("| {:<5s} | {:<20s} | {:<10s} | {:<15s} | {:<15s} | {:<15} | {:<14s} | {:<10s} | {:<12s} |\n".format(
                        "No.", "Nama barang", "Kode", "Tanggal Masuk", "Bulan masuk", "Tahun masuk", "Jumlah(pcs)", "Jenis", "Berat(Kg)"))
                    file.write("-" * 144)
                    file.write("\n")
                    for i in range(len(nambar)):
                        jnsbrng = printJenisBarang(jnisbrng[i])
                        file.write("| {:<5d} | {:<20s} | {:<10s} | {:<15s} | {:<15d} | {:<15s} | {:<14s} | {:<10s} | {:<12s} |\n".format(
                            i + 1, nambar[i], kode[i], tgglmsuk[i], blnmsuk[i], thnmsuk[i], jmlhbrng[i], jnsbrng, brtbrng[i]))
                    file.write("-" * 144)
                    file.write("\n")
                print("Data barang telah disimpan ke dalam file {}.".format(nama_file))
                print()

    except IOError:
                print("Terjadi kesalahan saat menyimpan data.")
                print()

    
def hapusDataBarang():
    clear_screen()
    print("Hapus Data Barang:")
    printDataBarang()
    data_index = input("Masukkan nomor data yang ingin dihapus (0 untuk batal): ")
    print()

    if data_index == "0":
        print("Penghapusan data dibatalkan.")
        print()
    else:
        data_index = int(data_index) - 1
        if 0 <= data_index < len(nambar):
            del nambar[data_index]
            del kode[data_index]
            del tgglmsuk[data_index]
            del blnmsuk[data_index]
            del thnmsuk[data_index]
            del jmlhbrng[data_index]
            del jnisbrng[data_index]
            del brtbrng[data_index]
            print("Data barang telah dihapus.")
            print()
        else:
            print("Nomor data tidak valid.")
            print()


def printMainMenu():
    clear_screen()
    print("+=========================================+")
    print("|                Menu Awal                |")
    print("+=========================================+")
    print("| Options:                                |")
    print("|    1. Admin                             |")
    print("|    2. Keeper                            |")
    print("|    0. Exit                              |")
    print("+=========================================+")


def printInitialMenu(role):
    clear_screen()
    print("+=========================================+")
    print("|               Menu Utama                |")
    print("+=========================================+")
    print("| Options:                                |")
    if role == "admin":
        print("|    1. Input Data Barang                 |")
        print("|    2. Tampilkan Data Barang             |")
        print("|    3. Edit Data Barang                  |")
        print("|    4. Pencarian Barang                  |")
        print("|    5. Hapus Data Barang                 |")
        print("|    6. Cetak Data Barang                 |")
        print("|    0. Logout                            |")
        print("+=========================================+")       
    elif role == "keeper":          
        print("|    1. Tampilkan Data Barang             |")
        print("|    2. Pencarian Barang                  |")
        print("|    3. Cetak Data Barang                 |")
        print("|    0. Logout                            |")
        print("+=========================================+")


nambar = []
kode = []
tgglmsuk = []
blnmsuk = []
thnmsuk = []
jmlhbrng = []
jnisbrng = []
brtbrng = []

is_logged_in = False
role = ""

while True:
    if not is_logged_in:
        printMainMenu()
        pilihan = input("Masukkan pilihan: ")
        print()

        if pilihan == "1":
           username = input("Masukkan username: ")
           password = getpass("Masukkan password: ")

           if username == "admin" and password == "admin":
               is_logged_in = True
               role = "admin"
               print("Login berhasil sebagai Admin.")
               input("Tekan Enter untuk melanjutkan...")
           else:
               print("Username atau password salah. Silakan coba lagi.")
               input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "2":
            username = input("Masukkan username: ")
            password = getpass("Masukkan password: ")

            if username == "keeper" and password == "keeper":
               is_logged_in = True
               role = "keeper"
               print("Login berhasil sebagai Keeper.")
               input("Tekan Enter untuk melanjutkan...")
            else:    
               print("Username atau password salah. Silakan coba lagi.")
               input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "0":
            print("Terima kasih! Sampai jumpa lagi.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    else:
        printInitialMenu(role)
        pilihan_menu_awal = input("Masukkan pilihan: ")
        print()

        if role == "admin":
            if pilihan_menu_awal == "1":
                os.system('cls')
                print("Input Data Barang")
                nama_barang = input("Masukkan nama barang: ")
                kode_barang = input("Masukkan kode barang: ")
                tanggal_masuk = input("Masukkan tanggal masuk barang: ")
                
                while True:
                    bulan_masuk = input("Masukkan Bulan masuk barang (1-12): ")
                    if bulan_masuk.isdigit() and 1 <= int(bulan_masuk) <= 12:
                       blnmsuk.append(int(bulan_masuk))
                       break
                    else: 
                       print("Input tidak valid. Mohon masukkan angka antara 1 sampai 12.")
                
                tahun_masuk = input("Masukkan tahun masuk barang: ")
                jumlah_barang = input("Masukkan jumlah barang: ")
                jenis_barang = int(input("Masukkan jenis barang (1. Pakaian, 2. Makanan, 3. Minuman, 4. Lainnya): "))
                berat_barang = input("Masukkan berat barang: ")

                nambar.append(nama_barang)
                kode.append(kode_barang)
                tgglmsuk.append(tanggal_masuk)
                blnmsuk.append(bulan_masuk)
                thnmsuk.append(tahun_masuk)
                jmlhbrng.append(jumlah_barang)
                jnisbrng.append(jenis_barang)
                brtbrng.append(berat_barang)
                

                print("Data barang berhasil diinput.")
                input("Tekan Enter untuk melanjutkan...")

            elif pilihan_menu_awal == "2":
                printDataBarang()
                input("Tekan Enter untuk melanjutkan...")

            elif pilihan_menu_awal == "3":
                print("Edit Data Barang:")
                printDataBarang()
                data_index = input("Masukkan nomor data yang ingin diedit (0 untuk batal): ")
                print()

                if data_index == "0":
                    print("Pengeditan data dibatalkan.")
                    print()
                else:
                    data_index = int(data_index) - 1
                    if 0 <= data_index < len(nambar):
                        print("Masukkan data baru:")
                        nama_barang = input("Nama barang: ")
                        kode_barang = input("Kode barang: ")
                        tanggal_masuk = input("Tanggal masuk barang: ")
                        
                        while True:
                            bulan_masuk = input("Masukkan Bulan masuk barang (1-12): ")
                            if bulan_masuk.isdigit() and 1 <= int(bulan_masuk) <= 12:
                                blnmsuk.append(int(bulan_masuk))
                                break
                            else: 
                                print("Input tidak valid. Mohon masukkan angka antara 1 sampai 12.")
                        
                        tahun_masuk = input("Tahun masuk barang: ")
                        jumlah_barang = input("Jumlah barang: ")
                        jenis_barang = int(input("Jenis barang (1. Pakaian, 2. Makanan, 3. Minuman, 4. Lainnya): "))
                        berat_barang = input("Berat barang: ")

                        nambar[data_index] = nama_barang
                        kode[data_index] = kode_barang
                        tgglmsuk[data_index] = tanggal_masuk
                        blnmsuk[data_index] = bulan_masuk
                        thnmsuk[data_index] = tahun_masuk
                        jmlhbrng[data_index] = jumlah_barang
                        jnisbrng[data_index] = jenis_barang
                        brtbrng[data_index] = berat_barang

                        print("Data barang telah diperbarui.")
                        input("Tekan Enter untuk melanjutkan...")
                    else:
                        print("Nomor data tidak valid.")
                        input("Tekan Enter untuk melanjutkan...")

            elif pilihan_menu_awal == "4":
                cariBarang()
                input("Tekan Enter untuk melanjutkan...")

            elif pilihan_menu_awal == "5":
                hapusDataBarang()
                input("Tekan Enter untuk melanjutkan...")
            
            elif pilihan_menu_awal == "6":
                simpanDataTabel()
                input("Tekan Enter untuk melanjutkan...")

            elif pilihan_menu_awal == "0":
                is_logged_in = False
                role = ""
                print("Anda berhasil logout.")
                input("Tekan Enter untuk melanjutkan...")

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("Tekan Enter untuk melanjutkan...")

        elif role == "keeper":
            if pilihan_menu_awal == "1":
                printDataBarang()
                input("Tekan Enter untuk melanjutkan...")

            elif pilihan_menu_awal == "2":
                cariBarang()
                input("Tekan Enter untuk melanjutkan...")
            
            elif pilihan_menu_awal == "3":
                simpanDataTabel()
                input("Tekan Enter untuk melanjutkan...")

            elif pilihan_menu_awal == "0":
                is_logged_in = False
                role = ""
                print("Anda berhasil logout.")
                input("Tekan Enter untuk melanjutkan...")

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("Tekan Enter untuk melanjutkan...")
