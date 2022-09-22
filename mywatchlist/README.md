1. **Jelaskan Perbedaan JSON, XML dan HTML**

Untuk dapat melihat diferensiasi diantara JSON XML & HTML adalah, dengan membayangkan JSON sebagai daging, XML sebagai pembantu proses transfer data (dalam konteks ini memudahkan), 
HTML sebagai surface atau kulit yang dimiliki. Pada dasarnya mereka saling terinterkorelasi satu sama lain dalam membentuk project yang diinginkan

![image](https://user-images.githubusercontent.com/88032633/191659007-628816ca-07c0-4ea5-b76d-04ca5534e7b1.png)

![image](https://user-images.githubusercontent.com/88032633/191659176-cb3ae811-f6a0-478d-a3f5-2f9a4d3f7462.png)

2. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform**

Untuk melihat bagaimana urgensi atau substansi dari data delivery adalah dengan memposisikan diri kita sebagai user, dimana seandainya kita berasumsi tidak ada data delivery
yang dapat terjadi adalah, user tidak akan bisa melihat data yang diharapkan dikarena data delivery tidak sampai kepada front-end itu sendiri. Bagaikan delivery pada gojek,
seandainya kita memesan gojek dan gojeknya tidak sampai kekita maka kita tidak akan menerima file/barang tersebut. 

4. **Jelaskan bagaimana cara kamu mengimplementasikan checklist diatas**

a. dimulai dengan menginisiasi django app pada CMD dengan menggunakan command "python manage.py startapp mywatchlist', sehingga ketika kita membuka file di Tugas2 kita akan
melihat folder baru bernama mywatchlist berisi dengan template template django yang sudah disiapkan, dan memasukkan 'mywatchlist' kedalam 'settings.py'

b.  membuat model 'mywatchlist' sesuai request dr soal seperti 'watched', 'title', dst.

c. Lakukan migrasi model kedatabase

d. membuat folder fixtures, yang dimana sesuai request soal ini kita perlu untuk membuat 10 data, sehingga tempat ini dipakai sebagai penyimpanan data yang kita inginkan

e. membuat fungsi mirip seperti lab 02 dengan implementasi yang tidak jauh berbeda

f. membuat routing urlpattern sesuai yang sudah pernah dipelajari

g. membuat mywatchlist.html, dimana disini struktur atau layer yang diinginkan untuk ditunjjukan akan muncul disini, dengan melakukan
proses validasi menggunakan test unit 'test.py' agar dapat melakukan uji URL router

h. Melakukan uji test dengan postman

j. Procfile dapat diubah dengan menambahkan loaddata initial_mmywatchlist_data.json, sehingga proses loaddata dapat berjalan dengan optimal, selesai dan cukup deploy!