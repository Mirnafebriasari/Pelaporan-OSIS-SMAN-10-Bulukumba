import subprocess
import sys
import os
from datetime import datetime

def buat_laporan_osisi_dengan_foto(nama_file, judul_laporan, deskripsi, daftar_foto, posisi_foto=(100, 500), jarak_foto=160):
    """
    Fungsi untuk membuat laporan OSIS dalam bentuk PDF dengan beberapa gambar yang disisipkan.
    Jika pustaka reportlab belum terinstal, akan menginstalnya secara otomatis.

    :param nama_file: Nama file PDF output (misal: 'laporan_osis.pdf')
    :param judul_laporan: Judul laporan OSIS
    :param deskripsi: Deskripsi atau teks laporan
    :param daftar_foto: List of paths ke file foto yang akan disisipkan (contoh: ['foto1.jpg', 'foto2.jpg'])
    :param posisi_foto: Posisi (x, y) untuk menempatkan foto pertama (default: (100, 500))
    :param jarak_foto: Jarak vertikal antar foto (default: 160)
    """
    # Memastikan direktori untuk menyimpan file PDF ada
    output_dir = os.path.dirname(nama_file)  # Direktori dari path nama_file
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Membuat direktori jika belum ada
        print(f"Direktori {output_dir} berhasil dibuat.")

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

    # Menambahkan foto-foto dari daftar_foto
    y_position = posisi_foto[1]  # Posisi y pertama untuk foto pertama
    for foto_path in daftar_foto:
        try:
            # Memastikan foto_path adalah string yang valid
            if isinstance(foto_path, str):
                c.drawImage(foto_path, posisi_foto[0], y_position, width=200, height=150)
                y_position -= jarak_foto  # Menggeser posisi y untuk foto berikutnya
            else:
                print(f"Error: {foto_path} bukan path yang valid.")
        except Exception as e:
            print(f"Error saat menambahkan gambar {foto_path}: {e}")

    # Menambahkan tanggal pembuatan laporan
    tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, 50, f"Disusun pada: {tanggal}")

    # Menyimpan PDF
    try:
        c.save()
        print(f"Laporan telah disimpan sebagai {nama_file}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan PDF: {e}")
