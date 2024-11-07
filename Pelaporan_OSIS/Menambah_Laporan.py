# import os
# from datetime import datetime

# def Menambah_Laporan(kegiatan, deskripsi, peserta, tujuan, anggaran, hasil, evaluasi, rekomendasi):
#     """
#     Fungsi untuk membuat laporan kegiatan OSIS dalam format file Markdown (.md).

#     Fungsi ini akan membuat folder berdasarkan tahun dan bulan saat ini, kemudian 
#     membuat file laporan dengan nama yang berdasarkan tanggal dan nama kegiatan. 
#     Laporan akan mencakup detail kegiatan seperti deskripsi, peserta, tujuan, anggaran, 
#     hasil, evaluasi, dan rekomendasi.

#     Args:
#         kegiatan (str): Nama kegiatan OSIS yang dilaporkan.
#         deskripsi (str): Deskripsi tentang kegiatan yang dilakukan.
#         peserta (str): Daftar peserta yang terlibat dalam kegiatan.
#         tujuan (str): Tujuan dari kegiatan yang dilaksanakan.
#         anggaran (str): Anggaran yang digunakan dalam kegiatan.
#         hasil (str): Hasil yang dicapai setelah kegiatan dilakukan.
#         evaluasi (str): Evaluasi kegiatan yang dilakukan.
#         rekomendasi (str): Rekomendasi untuk kegiatan di masa mendatang.

#     Returns:
#         None: Fungsi ini akan mencetak pesan yang menginformasikan lokasi file laporan yang berhasil dibuat.
    
#     Raises:
#         OSError: Jika terjadi masalah saat membuat folder atau file, misalnya masalah izin atau path yang tidak valid.
#     """
    
#     # Mendapatkan tanggal saat ini untuk laporan
#     today = datetime.today().strftime('%Y-%m-%d')
    
#     # Membuat folder laporan berdasarkan tahun dan bulan
#     folder_laporan = os.path.join('laporan', datetime.today().strftime('%Y'), today[:7])  # Tahun/Bulan
#     os.makedirs(folder_laporan, exist_ok=True)
    
#     # Membuat nama file laporan berdasarkan kegiatan
#     file_laporan = os.path.join(folder_laporan, f"{today}_{kegiatan.replace(' ', '_')}.md")
    
#     # Menulis isi laporan ke dalam file markdown
#     with open(file_laporan, 'w') as file:
#         file.write(f"# Laporan Kegiatan OSIS: {kegiatan}\n")
#         file.write(f"**Tanggal Kegiatan:** {today}\n\n")
#         file.write(f"**Deskripsi Kegiatan:** {deskripsi}\n\n")
#         file.write(f"**Peserta Kegiatan:** {peserta}\n\n")
#         file.write(f"**Tujuan Kegiatan:** {tujuan}\n\n")
#         file.write(f"**Anggaran dan Pembiayaan:** {anggaran}\n\n")
#         file.write(f"**Hasil Kegiatan:** {hasil}\n\n")
#         file.write(f"**Evaluasi:** {evaluasi}\n\n")
#         file.write(f"**Rekomendasi:** {rekomendasi}\n")
    
#     print(f"Laporan berhasil dibuat di {file_laporan}")









# import os
# from datetime import datetime

# def Menambah_Laporan(kegiatan, deskripsi, peserta, tujuan, anggaran, hasil, evaluasi, rekomendasi):
#     """
#     Fungsi untuk membuat laporan kegiatan OSIS dalam format file Markdown (.md).

#     Fungsi ini akan membuat folder berdasarkan tahun dan bulan saat ini, kemudian 
#     membuat file laporan dengan nama yang berdasarkan tanggal dan nama kegiatan. 
#     Laporan akan mencakup detail kegiatan seperti deskripsi, peserta, tujuan, anggaran, 
#     hasil, evaluasi, dan rekomendasi.

#     Args:
#         kegiatan (str): Nama kegiatan OSIS yang dilaporkan.
#         deskripsi (str): Deskripsi tentang kegiatan yang dilakukan.
#         peserta (str): Daftar peserta yang terlibat dalam kegiatan.
#         tujuan (str): Tujuan dari kegiatan yang dilaksanakan.
#         anggaran (str): Anggaran yang digunakan dalam kegiatan.
#         hasil (str): Hasil yang dicapai setelah kegiatan dilakukan.
#         evaluasi (str): Evaluasi kegiatan yang dilakukan.
#         rekomendasi (str): Rekomendasi untuk kegiatan di masa mendatang.

#     Returns:
#         None: Fungsi ini akan mencetak pesan yang menginformasikan lokasi file laporan yang berhasil dibuat.
    
#     Raises:
#         OSError: Jika terjadi masalah saat membuat folder atau file, misalnya masalah izin atau path yang tidak valid.
#     """
    
#     # Mendapatkan tanggal saat ini untuk laporan
#     today = datetime.today().strftime('%Y-%m-%d')
    
#     # Membuat folder laporan berdasarkan tahun dan bulan
#     folder_laporan = os.path.join('laporan', datetime.today().strftime('%Y'), today[:7])  # Tahun/Bulan
#     os.makedirs(folder_laporan, exist_ok=True)
    
#     # Membuat nama file laporan berdasarkan kegiatan
#     file_laporan = os.path.join(folder_laporan, f"{today}_{kegiatan.replace(' ', '_')}.md")
    
#     # Menulis isi laporan ke dalam file markdown
#     with open(file_laporan, 'w') as file:
#         # Menulis header laporan
#         file.write(f"# Laporan Kegiatan OSIS: {kegiatan}\n")
#         file.write(f"**Tanggal Kegiatan:** {today}\n\n")
        
#         # Menulis bagian deskripsi kegiatan
#         file.write(f"## Deskripsi Kegiatan\n")
#         file.write(f"{deskripsi}\n\n")
        
#         # Menulis bagian peserta kegiatan
#         file.write(f"## Peserta Kegiatan\n")
#         file.write(f"{peserta}\n\n")
        
#         # Menulis bagian tujuan kegiatan
#         file.write(f"## Tujuan Kegiatan\n")
#         file.write(f"{tujuan}\n\n")
        
#         # Menulis bagian anggaran
#         file.write(f"## Anggaran dan Pembiayaan\n")
#         file.write(f"{anggaran}\n\n")
        
#         # Menulis bagian hasil kegiatan
#         file.write(f"## Hasil Kegiatan\n")
#         file.write(f"{hasil}\n\n")
        
#         # Menulis bagian evaluasi kegiatan
#         file.write(f"## Evaluasi\n")
#         file.write(f"{evaluasi}\n\n")
        
#         # Menulis bagian rekomendasi
#         file.write(f"## Rekomendasi\n")
#         file.write(f"{rekomendasi}\n\n")
        
#         # Garis horizontal sebagai pemisah
#         file.write("\n---\n")
#         file.write(f"Laporan dibuat oleh: OSIS\n")
    
#     print(f"Laporan berhasil dibuat di {file_laporan}")








import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def Menambah_Laporan_Tabel(kegiatan, deskripsi, peserta, tujuan, anggaran, hasil, evaluasi, rekomendasi, file_name="laporan_osis.pdf"):
    """
    Fungsi untuk membuat laporan kegiatan OSIS dalam format PDF dengan output berbentuk tabel saja.

    Fungsi ini akan membuat file PDF hanya berisi tabel yang mencakup detail kegiatan seperti deskripsi, peserta, tujuan, anggaran,
    hasil, evaluasi, dan rekomendasi, serta tempat untuk tanda tangan di bagian bawah.

    Args:
        kegiatan (str): Nama kegiatan OSIS yang dilaporkan.
        deskripsi (str): Deskripsi tentang kegiatan yang dilakukan.
        peserta (str): Daftar peserta yang terlibat dalam kegiatan.
        tujuan (str): Tujuan dari kegiatan yang dilaksanakan.
        anggaran (str): Anggaran yang digunakan dalam kegiatan.
        hasil (str): Hasil yang dicapai setelah kegiatan dilakukan.
        evaluasi (str): Evaluasi kegiatan yang dilakukan.
        rekomendasi (str): Rekomendasi untuk kegiatan di masa mendatang.
        file_name (str): Nama file PDF yang akan disimpan (default: "laporan_osis.pdf").

    Returns:
        None: Fungsi ini akan mencetak pesan yang menginformasikan lokasi file laporan yang berhasil dibuat.
    """
    # Mendapatkan tanggal saat ini untuk laporan
    today = datetime.today().strftime('%Y-%m-%d')

    # Membuat folder laporan berdasarkan tahun dan bulan
    folder_laporan = os.path.join('laporan', datetime.today().strftime('%Y'), today[:7])  # Tahun/Bulan
    os.makedirs(folder_laporan, exist_ok=True)

    # Membuat nama file laporan berdasarkan kegiatan
    file_laporan = os.path.join(folder_laporan, f"{today}_{kegiatan.replace(' ', '_')}.pdf")

    # Membuat dokumen PDF
    doc = SimpleDocTemplate(file_laporan, pagesize=letter)
    content = []

    # Membuat tabel data laporan kegiatan
    data = [
        ["No", "Nama Kegiatan", "Deskripsi", "Peserta", "Tujuan", "Anggaran", "Hasil", "Evaluasi", "Rekomendasi"],
        ["1", kegiatan, deskripsi, peserta, tujuan, anggaran, hasil, evaluasi, rekomendasi]
    ]

    # Membuat tabel
    table = Table(data)

    # Menambahkan style pada tabel
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header tabel berwarna abu-abu
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Warna teks header putih
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Semua teks di dalam tabel diatur ke tengah
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Font header tabel tebal
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Menambahkan garis pada tabel
        ('SIZE', (0, 0), (-1, -1), 10),  # Ukuran font di seluruh tabel
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Jarak bawah header
        ('TOPPADDING', (0, 0), (-1, 0), 12),  # Jarak atas header
    ]))

    # Menambahkan tabel ke konten
    content.append(table)

    # Menambahkan Spacer agar ada jarak sebelum tanda tangan
    content.append(Spacer(1, 24))

    # Menambahkan tempat untuk tanda tangan
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']

    # Menambahkan keterangan tanda tangan
    tanda_tangan = Paragraph("""
    Diketahui oleh,<br/>
    Ketua OSIS<br/><br/>
    __________________________<br/>
    Nama Ketua OSIS
    """, normal_style)

    # Menambahkan keterangan tanda tangan ke konten
    content.append(tanda_tangan)

    # Menyusun dan menyimpan PDF
    doc.build(content)
    print(f"Laporan berhasil dibuat di {file_laporan}")

