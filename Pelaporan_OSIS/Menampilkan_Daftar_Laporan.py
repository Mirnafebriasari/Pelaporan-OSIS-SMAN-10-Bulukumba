import os

def Menampilkan_Daftar_Laporan(tahun=None, bulan=None):
    """
    Fungsi untuk melihat daftar laporan kegiatan OSIS yang ada dalam folder tertentu.

    Fungsi ini akan mencari dan menampilkan daftar file laporan (.md) yang ada dalam folder 
    'laporan' yang bisa difilter berdasarkan tahun dan bulan. 
    Jika parameter `tahun` dan `bulan` tidak diberikan, maka fungsi akan menampilkan semua laporan.

    Args:
        tahun (str, optional): Tahun untuk memfilter laporan. Defaultnya None, yang berarti semua tahun.
        bulan (str, optional): Bulan untuk memfilter laporan. Defaultnya None, yang berarti semua bulan.

    Returns:
        None: Fungsi ini mencetak daftar file laporan yang ditemukan sesuai dengan filter yang diberikan.
    
    Raises:
        FileNotFoundError: Jika tidak ada laporan yang ditemukan sesuai filter yang diberikan.
    """
    
    folder_path = 'laporan'
    
    # Filter berdasarkan tahun dan bulan
    if tahun:
        folder_path = os.path.join(folder_path, tahun)
    if bulan:
        folder_path = os.path.join(folder_path, bulan)
    
    # Menampilkan semua laporan dalam folder yang dipilih
    laporan_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                laporan_files.append(os.path.join(root, file))
    
    if laporan_files:
        print("Daftar Laporan:")
        for laporan in laporan_files:
            print(f"- {laporan}")
    else:
        print("Tidak ada laporan ditemukan.")
