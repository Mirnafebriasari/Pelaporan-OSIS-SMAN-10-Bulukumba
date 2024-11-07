import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def Dokumentasi(nama_file, judul_laporan, deskripsi, foto_path, posisi_foto=(100, 500)):
    """
    Fungsi untuk membuat laporan OSIS dalam bentuk PDF dengan gambar yang disisipkan.

    :param nama_file: Nama file PDF output (misal: 'laporan_osis.pdf')
    :param judul_laporan: Judul laporan OSIS
    :param deskripsi: Deskripsi atau teks laporan
    :param foto_path: Path ke file foto yang akan disisipkan
    :param posisi_foto: Posisi (x, y) untuk menempatkan foto pada halaman
    """
    # Membuat canvas (halaman PDF)
    c = canvas.Canvas(nama_file, pagesize=letter)
    
    # Mengatur font untuk judul
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, judul_laporan)
    
    # Mengatur font untuk deskripsi
    c.setFont("Helvetica", 12)
    c.drawString(100, 730, deskripsi)
    
    # Menambahkan gambar (foto)
    try:
        c.drawImage(foto_path, posisi_foto[0], posisi_foto[1], width=200, height=150)
    except Exception as e:
        print(f"Error saat menambahkan gambar: {e}")
    
    # Menambahkan tanggal pembuatan laporan
    tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, 50, f"Disusun pada: {tanggal}")
    
    # Menyimpan PDF
    c.save()
    print(f"Laporan telah disimpan sebagai {nama_file}")

# Contoh penggunaan
foto_path = "path_ke_foto.jpg"  # Ganti dengan path file foto yang ingin disisipkan
buat_laporan_osisi_dengan_foto("laporan_osis_dengan_foto.pdf", 
                               "Laporan Kegiatan OSIS Bulan Oktober", 
                               "Laporan ini berisi dokumentasi kegiatan OSIS bulan Oktober, termasuk foto kegiatan.", 
                               foto_path)
