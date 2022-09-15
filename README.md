1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

Untuk urls.py berfungsi untuk meminta request terhadap URL router, pada kode ini digunakan urlpatterns sebagai variable

Untuk views.py dia akan menjadi tempat urlpatterns akan dipanggil, yang dimana views akan mengirim semua data data yang sudah terintegrate kepada models.py

Sehingga ketika semua terkoneksi, HTML akan mengirimkan kepada orang yang mengakses URL tersebut 

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kenapa perlu untuk menggunakan virtual event adalah agar alamat yang kita ingin gapai dalam bentuk virtual environment, karena ada beberapa kemungkinan client/users yang mengakses environment tersebut datang dari versi django yang berbeda, sehingga kita dapat aman untuk mengaksesnya,

tetap bisa karena, tetapi ada chances untuk terjadi konflik karena ada dependencies ketika misalnya pada versi yang berbeda dsb

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

a. saya memulai dengan mengisi data yang dibutuhkan pada views.py, tujuannya agar kita bisa mengakses misalnys list_barang dapat diakses dari data_barang_katalog, dan nama & NPM
b. dilanjutkan dengan mengisi routing urls.py dengan apa yang ingin ditunjukkan, dan memasukkan project_django juga
c.pada katalog.html kita memindahkan data data yang sudah di simpan dengan syntax html seperti pada lab 01
d. lalu karena saya lab0 belum selesai, saya membuat herokuapp dan melakukan proses deploy
