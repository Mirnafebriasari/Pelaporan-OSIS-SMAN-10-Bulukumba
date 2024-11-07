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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def Menambah_Laporan(kegiatan, deskripsi, peserta, tujuan, anggaran, hasil, evaluasi, rekomendasi, file_name="laporan_osis.pdf"):
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

    # Menulis header laporan
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading2']
    normal_style = styles['Normal']
    paragraph_style = styles['BodyText']

    # Menambahkan judul laporan
    title = Paragraph(f"<b>Laporan Kegiatan OSIS: {kegiatan}</b>", title_style)
    content.append(title)

    # Menambahkan tanggal laporan
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"**Tanggal Kegiatan:** {today}", normal_style))

    # Menambahkan deskripsi kegiatan
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"<b>Deskripsi Kegiatan</b>", heading_style))  # Judul tanpa ##
    content.append(Spacer(1, 6))
    content.append(Paragraph(deskripsi, paragraph_style))

    # Menambahkan peserta kegiatan
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"<b>Peserta Kegiatan</b>", heading_style))  # Judul tanpa ##
    content.append(Spacer(1, 6))
    content.append(Paragraph(peserta, paragraph_style))

    # Menambahkan tujuan kegiatan
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"<b>Tujuan Kegiatan</b>", heading_style))  # Judul tanpa ##
    content.append(Spacer(1, 6))
    content.append(Paragraph(tujuan, paragraph_style))

    # Menambahkan anggaran
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"<b>Anggaran dan Pembiayaan</b>", heading_style))  # Judul tanpa ##
    content.append(Spacer(1, 6))
    content.append(Paragraph(anggaran, paragraph_style))

    # Menambahkan hasil kegiatan
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"<b>Hasil Kegiatan</b>", heading_style))  # Judul tanpa ##
    content.append(Spacer(1, 6))
    content.append(Paragraph(hasil, paragraph_style))

    # Menambahkan evaluasi kegiatan
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"<b>Evaluasi</b>", heading_style))  # Judul tanpa ##
    content.append(Spacer(1, 6))
    content.append(Paragraph(evaluasi, paragraph_style))

    # Menambahkan rekomendasi
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"<b>Rekomendasi</b>", heading_style))  # Judul tanpa ##
    content.append(Spacer(1, 6))
    content.append(Paragraph(rekomendasi, paragraph_style))

    # Menambahkan tabel kegiatan
    content.append(Spacer(1, 12))
    table_data = [
        ["No", "Nama Kegiatan", "Tanggal", "Lokasi", "Deskripsi"],
        ["1", kegiatan, today, "Lokasi Kegiatan", deskripsi],  # Contoh data kegiatan
    ]
    
    # Membuat tabel dengan pengaturan kolom yang lebih lebar
    table = Table(table_data, colWidths=[1 * inch, 2 * inch, 1.5 * inch, 2 * inch, 3 * inch])  # Menyesuaikan lebar kolom

    # Styling tabel untuk memastikan teks terlihat dengan baik
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alignment tengah
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Font header
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Border grid untuk tabel
        ('SIZE', (0, 0), (-1, -1), 9),  # Ukuran font tabel
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding bawah pada header
        ('TOPPADDING', (0, 0), (-1, 0), 12),  # Padding atas pada header
        ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Padding kiri
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),  # Padding kanan
    ]))
    
    content.append(table)

    # Menambahkan tempat untuk tanda tangan
    content.append(Spacer(1, 24))
    tanda_tangan = Paragraph("""
    Diketahui oleh,<br/>
    Ketua OSIS<br/><br/>
    __________________________<br/>
    Nama Ketua OSIS
    """, normal_style)
    content.append(tanda_tangan)

    # Menyusun dan menyimpan PDF
    doc.build(content)
    print(f"Laporan berhasil dibuat di {file_laporan}")

