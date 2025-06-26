# File Compression Web Application (Shrinko)

Aplikasi web sederhana untuk kompresi file (PDF, DOCX, Gambar, Video) yang dikembangkan menggunakan Python dan Flask. Proyek ini merupakan bagian dari tugas akhir mata kuliah Teknologi Multimedia.

---

## Daftar Isi
- [Deskripsi](#deskripsi)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Fitur](#fitur)
- [Struktur Folder](#struktur-folder)
- [Cara Instalasi & Menjalankan](#cara-instalasi--menjalankan)
- [Cara Penggunaan](#cara-penggunaan)
- [Tim Pengembang](#tim-pengembang)
- [Lisensi](#lisensi)

---

## Deskripsi
Aplikasi ini memudahkan pengguna untuk melakukan kompresi file PDF, dokumen Word (DOCX), gambar (JPG, JPEG, PNG), dan video (MP4) secara cepat dan efisien melalui antarmuka web yang user-friendly. Hasil kompresi dapat langsung diunduh.

---

## Teknologi yang Digunakan
- **Python 3.11+**
- **Flask**: Framework web utama
- **PyPDF2**: Kompresi file PDF
- **Pillow (PIL)**: Kompresi gambar
- **ffmpeg-python**: Kompresi video (memerlukan FFmpeg terinstal di sistem)
- **docx2pdf**: Konversi dan kompresi file DOCX ke PDF
- **Werkzeug**: Utilitas untuk upload file
- **Bootstrap 5**: Tampilan antarmuka
- **HTML5, CSS3**: Frontend

---

## Fitur
- Kompresi file PDF
- Kompresi gambar (JPG, JPEG, PNG)
- Kompresi video (MP4)
- Konversi dan kompresi file DOCX ke PDF
- Batas maksimal file upload: 100 MB
- Download hasil kompresi langsung dari web
- Antarmuka modern dan responsif

---

## Struktur Folder
```
app_kompresi_data/
├── app.py
├── compress/
│   ├── __init__.py
│   ├── docx_compressor.py
│   ├── image_compressor.py
│   ├── pdf_compressor.py
│   └── video_compressor.py
├── index.html
├── requirements.txt
├── static/
│   ├── compressed/   # Hasil file kompresi
│   ├── css/
│   │   └── style.css
│   └── uploads/      # File yang diupload user
├── templates/
│   ├── about.html
│   ├── download.html
│   └── upload.html
└── venv/             # Virtual environment (opsional)
```

---

## Cara Instalasi & Menjalankan

### 1. Prasyarat
- Python 3.11 atau lebih tinggi
- FFmpeg (untuk kompresi video)

### 2. Instalasi
```bash
# Clone repository (jika dari GitHub)
# git clone <repo-url>
# cd app_kompresi_data

# Buat dan aktifkan virtual environment
python -m venv venv
# Di Windows:
venv\Scripts\activate
# Di Linux/macOS:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Instal semua dependensi
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi
```bash
python app.py
```
Aplikasi akan berjalan di [http://localhost:5000](http://localhost:5000)

---

## Cara Penggunaan
1. Buka browser dan akses `http://localhost:5000`
2. Pilih file yang ingin dikompresi (PDF, DOCX, JPG, JPEG, PNG, MP4)
3. Klik **Upload and Compress**
4. Setelah proses selesai, unduh file hasil kompresi

> **Catatan:**
> - Maksimal ukuran file: 100 MB
> - Untuk kompresi video, pastikan FFmpeg sudah terinstal di sistem

---

## Tim Pengembang
- **Rasya Aditya Amelia Putra** (231240001385)
- **Reza Dwi Mahendra** (231240001370)

---

## Lisensi
Aplikasi ini dikembangkan untuk keperluan edukasi dan tugas akhir mata kuliah Teknologi Multimedia.

---

## Pengembangan Selanjutnya
Silakan tambahkan bagian analisis, hasil pengujian, studi pustaka, dan pembahasan lain sesuai kebutuhan laporan praktikum. 
