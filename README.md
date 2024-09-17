# LinkedIn Jobs Scraper

Ini adalah proyek Python untuk mengumpulkan data pekerjaan dari LinkedIn menggunakan pustaka `linkedin-jobs-scraper` dan Selenium.

## Prerequisites

Sebelum memulai, pastikan Anda memiliki Python dan pip terinstal di sistem Anda. Jika belum, Anda dapat mengunduh Python dari [python.org](https://www.python.org/downloads/) dan mengikuti petunjuk instalasi untuk sistem operasi Anda.

## Langkah-langkah Instalasi

### 1. Clone Repositori

Clone repositori ini dari GitHub dengan perintah berikut:

<pre>git clone https://github.com/LuthfiAjax/linkedin-jobs-scrapping.git</pre>

### 2. Masuk ke Direktori Proyek

Masuk ke direktori proyek yang telah Anda clone:

<pre>cd linkedin-jobs-scrapping</pre>

### 3. Buat dan Aktifkan Lingkungan Virtual

Buat lingkungan virtual baru untuk proyek ini:

<pre>python -m venv myenv</pre>

Aktifkan lingkungan virtual:

- **Untuk macOS/Linux:**

<pre>source myenv/bin/activate</pre>

- **Untuk Windows:**

<pre>myenv\Scripts\activate</pre>

### 4. Instalasi Dependensi

Instal semua dependensi yang diperlukan dengan menggunakan `pip`:

<pre>pip install -r requirements.txt</pre>

### 5. Konfigurasi dan Menjalankan Scraper

Sebelum menjalankan scraper, pastikan Anda sudah mengatur `linkedin_scraper.py` sesuai kebutuhan Anda. Kemudian, jalankan file Python untuk memulai scraping:

<pre>python linkedin_scraper.py</pre>

## Penjelasan

- `linkedin_scraper.py` adalah file utama yang menjalankan proses scraping. Pastikan untuk mengonfigurasi pengaturan di dalamnya sesuai kebutuhan.

## Troubleshooting

Jika Anda mengalami masalah saat menjalankan scraper, pastikan:

1. Lingkungan virtual Anda aktif.
2. Semua dependensi telah terinstal dengan benar.
3. Versi Python dan pip sesuai dengan yang diperlukan oleh proyek.

Jika Anda masih mengalami kesulitan, periksa log kesalahan untuk informasi lebih lanjut atau kunjungi [issues di GitHub](https://github.com/LuthfiAjax/linkedin-jobs-scrapping/issues) untuk bantuan.
