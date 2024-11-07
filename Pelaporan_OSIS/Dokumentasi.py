import subprocess
import sys
from datetime import datetime

def Dokumentasi(nama_file, judul_laporan, deskripsi, foto_path, posisi_foto=(100, 500)):
    """
    Fungsi untuk membuat laporan OSIS dalam bentuk PDF dengan gambar yang disisipkan.
    Jika pustaka reportlab belum terinstal, akan menginstalnya secara otomatis.

    :param nama_file: Nama file PDF output (misal: 'laporan_osis.pdf')
    :param judul_laporan: Judul laporan OSIS
    :param deskripsi: Deskripsi atau teks laporan
    :param foto_path: Path ke file foto yang akan disisipkan
    :param posisi_foto: Posisi (x, y) untuk menempatkan foto pada halaman
    """
    # Menginstal reportlab jika belum terinstal
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib import colors
    except ImportError:
        print("Pustaka 'reportlab' tidak ditemukan. Menginstalnya...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'reportlab'])
        # Setelah instalasi, coba impor kembali
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib import colors

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
