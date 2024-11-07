import os

def Mengupdate_Laporan(file_path, deskripsi=None, peserta=None, tujuan=None, anggaran=None, hasil=None, evaluasi=None, rekomendasi=None):
    """
    Fungsi untuk memperbarui laporan kegiatan OSIS dalam file Markdown.

    Fungsi ini akan mencari dan mengganti nilai-nilai dalam file laporan berdasarkan parameter yang diberikan.
    Setiap parameter opsional yang diberikan akan menggantikan teks yang sesuai di dalam file laporan.

    Args:
        file_path (str): Path ke file laporan yang akan diupdate.
        deskripsi (str, optional): Deskripsi kegiatan yang akan diperbarui. Defaultnya None.
        peserta (str, optional): Daftar peserta kegiatan yang akan diperbarui. Defaultnya None.
        tujuan (str, optional): Tujuan kegiatan yang akan diperbarui. Defaultnya None.
        anggaran (str, optional): Anggaran dan pembiayaan kegiatan yang akan diperbarui. Defaultnya None.
        hasil (str, optional): Hasil kegiatan yang akan diperbarui. Defaultnya None.
        evaluasi (str, optional): Evaluasi kegiatan yang akan diperbarui. Defaultnya None.
        rekomendasi (str, optional): Rekomendasi untuk kegiatan yang akan diperbarui. Defaultnya None.

    Returns:
        None: Fungsi ini akan mencetak pesan keberhasilan jika laporan berhasil diupdate, atau pesan kesalahan jika file tidak ditemukan.
    
    Raises:
        FileNotFoundError: Jika file yang dimaksud tidak ditemukan.
    """
    
    # Mengecek apakah file laporan ada
    if not os.path.exists(file_path):
        print("Laporan tidak ditemukan!")
        return
    
    # Membaca konten file yang ada
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    # Menyunting konten file berdasarkan parameter yang diberikan
    if deskripsi:
        content = [line.replace("**Deskripsi Kegiatan:**", f"**Deskripsi Kegiatan:** {deskripsi}\n") if "**Deskripsi Kegiatan:**" in line else line for line in content]
    if peserta:
        content = [line.replace("**Peserta Kegiatan:**", f"**Peserta Kegiatan:** {peserta}\n") if "**Peserta Kegiatan:**" in line else line for line in content]
    if tujuan:
        content = [line.replace("**Tujuan Kegiatan:**", f"**Tujuan Kegiatan:** {tujuan}\n") if "**Tujuan Kegiatan:**" in line else line for line in content]
    if anggaran:
        content = [line.replace("**Anggaran dan Pembiayaan:**", f"**Anggaran dan Pembiayaan:** {anggaran}\n") if "**Anggaran dan Pembiayaan:**" in line else line for line in content]
    if hasil:
        content = [line.replace("**Hasil Kegiatan:**", f"**Hasil Kegiatan:** {hasil}\n") if "**Hasil Kegiatan:**" in line else line for line in content]
    if evaluasi:
        content = [line.replace("**Evaluasi:**", f"**Evaluasi:** {evaluasi}\n") if "**Evaluasi:**" in line else line for line in content]
    if rekomendasi:
        content = [line.replace("**Rekomendasi:**", f"**Rekomendasi:** {rekomendasi}\n") if "**Rekomendasi:**" in line else line for line in content]
    
    # Menyimpan kembali perubahan pada file
    with open(file_path, 'w') as file:
        file.writelines(content)
    
    print(f"Laporan di {file_path} berhasil diupdate.")
