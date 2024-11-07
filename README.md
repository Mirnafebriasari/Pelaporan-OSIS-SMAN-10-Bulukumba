# Pelaporan-OSIS-SMAN-10-Bulukumba
cara penggunaan di google colab
pip install git+https://github.com/Mirnafebriasari/Pelaporan-OSIS-SMAN-10-Bulukumba.git
import Pelaporan_OSIS as O
O.pilih fungsi yang mana diinginkan(ikuti aturan inputnya)

Pelaporan OSIS adalah suatu bentuk sistem atau proses yang dilakukan oleh organisasi siswa intra sekolah (OSIS) untuk melaporkan kegiatan, pencapaian, atau laporan keuangan yang terkait dengan kegiatan yang dilaksanakan oleh OSIS di sekolah. Pelaporan ini bertujuan untuk memberikan informasi yang jelas dan transparan kepada pihak terkait, seperti kepala sekolah, guru pembimbing OSIS, dan anggota OSIS itu sendiri.

Tujuan Pelaporan OSIS:
Transparansi: Agar semua kegiatan dan anggaran yang digunakan oleh OSIS diketahui dan dipahami oleh semua pihak, termasuk pengelola sekolah, anggota OSIS, serta pihak lainnya yang berwenang.
Evaluasi dan Perbaikan: Dengan adanya pelaporan, kegiatan yang telah dilakukan bisa dievaluasi. Apa yang sudah berhasil dan apa yang perlu diperbaiki bisa ditinjau berdasarkan laporan yang disusun.
Pertanggungjawaban: Pelaporan OSIS juga menjadi sarana bagi pengurus OSIS untuk bertanggung jawab atas segala kegiatan yang telah dilakukan, baik itu dalam bentuk keuangan, acara, atau proyek lainnya.
Dokumentasi: Pelaporan merupakan dokumentasi yang bisa digunakan sebagai referensi atau arsip kegiatan yang pernah dilaksanakan oleh OSIS. Ini sangat penting untuk perencanaan kegiatan di masa mendatang.

berikut modul proyek ini:
# 1. Menambahkan_Laporan
Menambahkan Laporan dalam konteks OSIS atau organisasi lainnya biasanya merujuk pada proses menambahkan data atau informasi baru ke dalam sistem pelaporan, entah itu laporan kegiatan, laporan keuangan, atau laporan lainnya. Proses ini biasanya dilakukan untuk mencatat perkembangan atau hasil dari suatu kegiatan atau proyek yang telah dilakukan oleh OSIS (Organisasi Siswa Intra Sekolah). Tujuan dari menambahkan laporan adalah untuk memastikan bahwa setiap kegiatan yang telah dilaksanakan tercatat dengan baik, sehingga bisa dievaluasi, dipertanggungjawabkan, dan menjadi arsip yang berguna di masa mendatang.

Cara penggunaan
- kegiatan (str): Nama kegiatan OSIS yang dilaporkan.
- deskripsi (str): Deskripsi tentang kegiatan yang dilakukan.
- peserta (str): Daftar peserta yang terlibat dalam kegiatan.
- tujuan (str): Tujuan dari kegiatan yang dilaksanakan.
- anggaran (str): Anggaran yang digunakan dalam kegiatan.
- hasil (str): Hasil yang dicapai setelah kegiatan dilakukan.
- evaluasi (str): Evaluasi kegiatan yang dilakukan.
- rekomendasi (str): Rekomendasi untuk kegiatan di masa mendatang.

Contoh Input
O.Menambah_Laporan("membersihkan", "mebersihkan seluruh halaman sekolah", "seluruh ekstrakurikuler", "agar sekolah bersih","tidak ada", 'sekolah menjadi bersih', "melihat kembali kebersihan sekolah", "rajin membersihkan")


# 2. Menampilkan_Daftar_Laporan
Menampilkan_Daftar_Laporan kemungkinan besar merujuk pada fungsi atau fitur dalam sistem pelaporan yang digunakan untuk menampilkan daftar laporan yang telah disusun oleh OSIS atau organisasi lainnya. Fitur ini memungkinkan pengguna untuk melihat ringkasan atau daftar dari laporan yang telah ada, baik itu laporan kegiatan, laporan keuangan, atau laporan lainnya. Biasanya, fitur ini digunakan untuk memudahkan akses dan pemantauan terhadap laporan-laporan yang telah dibuat sebelumnya.

Cara Penggunaan 
- tahun (str, optional): Tahun untuk memfilter laporan. Defaultnya None, yang berarti semua tahun.
- bulan (str, optional): Bulan untuk memfilter laporan. Defaultnya None, yang berarti semua bulan.

Contoh Input
O.Menampilkan_Daftar_Laporan(None, None)

# 3. Mengupdate_Laporan
Mengupdate_Laporan adalah fungsi atau tindakan yang digunakan untuk memperbarui atau mengubah informasi dalam laporan yang sudah ada di dalam sistem pelaporan. Fungsi ini biasanya digunakan ketika ada perubahan dalam detail laporan yang sudah dibuat, misalnya perubahan pada tanggal, anggaran, deskripsi, atau informasi lain yang perlu diperbarui.

Cara Penggunaan 
- file_path (str): Path ke file laporan yang akan diupdate.
- deskripsi (str, optional): Deskripsi kegiatan yang akan diperbarui. Defaultnya None.
- peserta (str, optional): Daftar peserta kegiatan yang akan diperbarui. Defaultnya None.
- tujuan (str, optional): Tujuan kegiatan yang akan diperbarui. Defaultnya None.
- anggaran (str, optional): Anggaran dan pembiayaan kegiatan yang akan diperbarui. Defaultnya None.
- hasil (str, optional): Hasil kegiatan yang akan diperbarui. Defaultnya None.
- evaluasi (str, optional): Evaluasi kegiatan yang akan diperbarui. Defaultnya None.
- rekomendasi (str, optional): Rekomendasi untuk kegiatan yang akan diperbarui. Defaultnya None.

Contoh Input
O.Mengupdate_Laporan("laporan/2024/2024-11/2024-11-07_membersihkan.md","Membersihkan lingkungan sekolah SMAN 10 Bulukumba", "seluruh siswa SMAN 10 Bulukumba", "untuk meningkatkan jiwa lingkungan bersihnya","tidak ada","sekolah menjadi bersih","melihat ulang sekolah","jangan buang sampah sembarangan")

# 4. Menghapus_Daftar_Laporan

Menghapus_Daftar_Laporan adalah sebuah fungsi atau tindakan yang digunakan untuk menghapus laporan yang sudah ada dalam sistem pelaporan. Dalam konteks OSIS atau organisasi lainnya, fungsi ini digunakan untuk menghapus laporan yang tidak relevan, sudah kadaluarsa, atau tidak lagi dibutuhkan. Menghapus laporan ini penting untuk menjaga sistem tetap terorganisir dan mencegah penumpukan data yang tidak perlu.

Cara Penggunaan
-  file_path (str): Path ke file laporan yang ingin dihapus.

Contoh Input
O.Menghapus_Laporan("laporan/2024/2024-11/2024-11-07_membersihkan.md") 
