
print("======= Latihan Dictionary =======")
print()
s={'Rapi': '08128809', 'Sutan': '08957716'}
print("Daftar Kontak :\n", s)
print()

#Menampilkan kontak
print("Menampilkan kontak Rapi :", s['Rapi'])
print("================================================================================")

#Menambah Kontak Baru
print("Menambah Kontak Baru\n")
print("Daftar Kontak sebelum ditambah :\n", s)
s['Yogi']='08122461';
print("Daftar Kontak setelah ditambah :\n", s)
print("================================================================================")

#Mengubah Kontak
print("Mengubah Kontak\n")
print("Daftar Kontak sebelum diubah :\n", s)
s['Sutan']='08956177';
print("Daftar Kontak setelah diubah :\n", s)
print("================================================================================")

#Menampilkan Semua Nama Kontak
print("Menampilkan Semua Nama Kontak :\n")
print(s.keys())
print("================================================================================")

#Menampilkan Semua Nomor Kontak
print("Menampilkan Semua Nomor Kontak :\n")
print(s.values())
print("================================================================================")

#Menampilkan Seluruh Daftar Kontak Beserta Nomor Telp
print("Daftar Kontak :\n")
print(s.items())
print("================================================================================")

#Menghapus Kontak Dina
print("Menghapus salah satu kontak\n")
print("Daftar Kontak sebelum dihapus :\n", s)
del s['Sutan'];
print("Daftar Kontak setelah dihapus :\n", s)