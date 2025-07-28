from datetime import datetime

print("=== Penghitung Hari Menuju Ulang Tahun + Umur ===")
nama = input("Masukkan nama kamu: ")
tanggal_input = input("Masukkan tanggal lahir kamu (format: DD-MM-YYYY): ")

try:
    tanggal_lahir = datetime.strptime(tanggal_input, "%d-%m-%Y")
    hari_ini = datetime.now()
    tahun_ini = hari_ini.year

    # Umur saat ini
    umur = tahun_ini - tanggal_lahir.year
    ulang_tahun_tahun_ini = tanggal_lahir.replace(year=tahun_ini)

    # Kalau ulang tahun belum terjadi tahun ini, umur belum bertambah
    if hari_ini < ulang_tahun_tahun_ini:
        umur -= 1

    # Cek ulang tahun berikutnya
    if hari_ini > ulang_tahun_tahun_ini:
        ulang_tahun_berikutnya = ulang_tahun_tahun_ini.replace(year=tahun_ini + 1)
    else:
        ulang_tahun_berikutnya = ulang_tahun_tahun_ini

    selisih_hari = (ulang_tahun_berikutnya - hari_ini).days

    print(f"\nHalo {nama}!")
    print(f"Umur kamu sekarang: {umur} tahun")

    if selisih_hari == 0:
        print(f"🎉 Selamat ulang tahun yang ke-{umur + 1}, {nama}! Semoga harimu menyenangkan! 🥳")
    else:
        tanggal_format = ulang_tahun_berikutnya.strftime("%d %B %Y")
        print(f"Ulang tahunmu berikutnya dalam {selisih_hari} hari lagi ({tanggal_format}) 🎂")

except ValueError:
    print("⚠️ Format tanggal salah! Gunakan format: DD-MM-YYYY (contoh: 28-07-2000)")
