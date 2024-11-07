import os

def Menghapus_Laporan(file_path):
    """
    Fungsi untuk menghapus laporan kegiatan OSIS yang ada pada file tertentu.

    Fungsi ini akan memeriksa apakah file laporan yang diberikan ada. 
    Jika file ditemukan, maka file tersebut akan dihapus dari sistem.

    Args:
        file_path (str): Path ke file laporan yang ingin dihapus.

    Returns:
        None: Fungsi ini mencetak pesan keberhasilan jika file berhasil dihapus, atau pesan kesalahan jika file tidak ditemukan.
    
    Raises:
        OSError: Jika terjadi kesalahan saat mencoba menghapus file (misalnya, file tidak dapat dihapus karena alasan izin).
    """
    
    # Mengecek apakah file laporan ada
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Laporan {file_path} berhasil dihapus.")
    else:
        print("Laporan tidak ditemukan!")
