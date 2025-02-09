import numpy as np  # Mengimpor pustaka NumPy untuk operasi matriks dan pembuatan angka acak
import matplotlib.pyplot as plt  # Mengimpor Matplotlib untuk menampilkan dan menyimpan gambar

"""
Program ini bertujuan untuk menghasilkan kumpulan angka acak yang disusun dalam format tes Kraeplin, kemudian menyimpannya sebagai gambar dengan kualitas tinggi. Tes Kraeplin sering digunakan dalam psikotes untuk mengukur konsentrasi dan daya tahan seseorang dalam menyelesaikan tugas berulang. Dengan program ini, pengguna bisa dengan mudah membuat dan menyimpan tampilan tes tanpa harus menyusunnya secara manual.

Cara kerja program ini cukup sederhana. Pertama, ia membuat matriks berisi angka acak dari 0 hingga 9 dengan ukuran 30x30 menggunakan NumPy. Setelah matriks terbentuk, program akan menampilkannya sebagai gambar tanpa garis pembatas menggunakan Matplotlib. Supaya hasilnya terlihat lebih rapi, angka-angka dalam matriks ditampilkan dengan penyesuaian posisi dan ukuran font. Terakhir, gambar disimpan dalam format PNG dengan resolusi tinggi (dpi=600), memastikan hasilnya tetap jelas dan tajam saat dicetak atau digunakan dalam presentasi.

Dengan adanya program ini, siapa pun yang ingin membuat latihan atau simulasi tes Kraeplin bisa melakukannya dengan cepat dan efisien. Pengguna hanya perlu menjalankan skrip Python ini, dan secara otomatis akan mendapatkan gambar tes dalam format PNG. Jika ingin mengubah ukuran matriks atau meningkatkan kualitas gambar, cukup menyesuaikan parameter yang tersedia di dalam kode.
"""

# Fungsi untuk membuat matriks angka acak
def generate_kraeplin_matrix(rows=30, cols=30):
    """Membuat matriks berisi angka acak antara 0 hingga 9 dengan ukuran rows x cols"""
    return np.random.randint(0, 10, size=(rows, cols))  # Menghasilkan matriks angka acak berukuran 30x30

# Fungsi untuk menampilkan matriks sebagai gambar tanpa garis tabel dengan kualitas tinggi
def save_matrix_as_image(matrix, filename="kraeplin_test.png"):
    """Menyimpan matriks angka dalam format gambar dengan resolusi tinggi"""
    fig, ax = plt.subplots(figsize=(15, 15), dpi=600)  # Membuat canvas gambar dengan ukuran 15x15 inci dan resolusi tinggi (600 dpi)
    ax.set_xticks([])  # Menghapus garis pembatas sumbu X
    ax.set_yticks([])  # Menghapus garis pembatas sumbu Y
    ax.axis('off')  # Menonaktifkan tampilan sumbu agar hanya angka yang terlihat
    
    # Menampilkan angka-angka dalam matriks ke dalam gambar
    for i in range(matrix.shape[0]):  # Looping melalui setiap baris
        for j in range(matrix.shape[1]):  # Looping melalui setiap kolom
            ax.text(j, -i, str(matrix[i, j]), ha='center', va='center', fontsize=16)  # Menampilkan angka dengan posisi dan ukuran font tertentu
    
    plt.xlim(-0.5, matrix.shape[1] - 0.5)  # Mengatur batas tampilan sumbu X
    plt.ylim(-matrix.shape[0] + 0.5, 0.5)  # Mengatur batas tampilan sumbu Y
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1, dpi=600)  # Menyimpan gambar dengan batas rapat dan resolusi tinggi
    plt.close()  # Menutup gambar untuk menghemat memori
    print(f"Tes Kraeplin berhasil disimpan sebagai {filename}")  # Menampilkan pesan konfirmasi penyimpanan

if __name__ == "__main__":  # Menjalankan program utama jika file dieksekusi secara langsung
    matrix = generate_kraeplin_matrix()  # Membuat matriks angka acak
    output_filename = "kraeplin_test.png"  # Menentukan nama file output
    save_matrix_as_image(matrix, output_filename)  # Menyimpan matriks dalam bentuk gambar
