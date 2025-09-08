Nama : Nisrina Fatimah
NPM : 2406354000
Kelas : PBP F

TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
    1. Membuat sebuah proyek Django baru : Bikin virtual environment, bikin file requirements.txt dan nambahin beberapa dependencies, install recuirements.txt, terus bikin proyek django baru pake perintah django-admin startproject kitkeeper. Lalu selanjutnya bikin file .env (untuk development lokal) dan .env.prod (untuk production deployment), memodifikasi settings untuk menambahkan variable dan allowed host agar memberikan akses ke host lokal, lalu terakhir dijalankan server dengan sebelumnya make migrations dulu 
    2. Membuat aplikasi dengan nama main pada proyek tersebut : menggunakan perintah python manage.py startapp main untuk membuat aplikasi baru bernama main. Lalu mendaftarkan main ke dalam proyek dengan menambahkan pada settings.py

    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main : Pertama membuat file urls.py pada aplikasi main, lalu menamhahkan isi urls.py unutk show_main. Selanjutnya menambahkan routing pada urls.py proyek utama untuk mengarahkan semua request ke aplikasi main. 

    4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib : name (CharField, max_length=100), price (IntegerField), description (TextField) : Membuat model Product pada models.py aplikasi main dengan atribut name, price, dan description. Lalu melakukan migrasi database dengan perintah makemigrations dan migrate agar model Product tercipta di database. Selain itu aku juga menambahkan beberapa atribut tambahan yang relevan dengan proyek saya seperti team (tim), season (musim, mis. “2024/25”), size (S/M/L/XL), sleeve_type (short/long), condition (new/used/like new), manufacturer (brand), stock (stok), created_at (timestamp otomatis). 

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu : membuat fungsi show_main yang akan menerima parameter request, lalu merender template HTML main.html dengan context yang berisi nama aplikasi, nama, dan kelas saya. Membuat file main.html pada folder templates di dalam aplikasi main, lalu menambahkan kode HTML untuk menampilkan informasi yang diinginkan.

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py : menambahkan path kosong ("") pada urls.py aplikasi main yang memetakan ke fungsi show_main di views.py.

    7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet : membuat proyek baru di website https://pbp.cs.ui.ac.id/web , menyimpan credentials, lalu mengubah raw environment editor dengan isi dari .env.prod. Lalu selanjutnya, di settings.py menambahkan allowed_host dengan URL deployment PWS, lalu melakukan git add, commit, push dan menjalankan perintah yang meminta username serta password PWS. Setelah itu menunggu beberapa saat hingga aplikasi berhasil dideploy dan dapat diakses melalui internet.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
A[Client / Browser] -> B[project/urls.py] : nerusin semua request dari domain ke “aplikasi” (app) tertentu
B -> C[main/urls.py] : memetakan sebuah path ke fungsi di views.py, kalau path-nya kosong ("", alias halaman depan), panggil fungsi show_main 
C -> D[views.py (show_main)] : menerima request, menyiapkan data (context), lalu merender template HTML
D ->|render + data context| E[templates/main.html] : menerima context dari view dan menampilkan jadi HTML
E -> F[Response HTML ke Browser]

3. Jelaskan peran settings.py dalam proyek Django! 
settings.py itu pusat pengaturan proyek. Django baca file ini saat server jalan, lalu semua bagian aplikasi (URL, view, model, template, static) kerja sesuai pengaturan di sini. Di sini aku mengaktifkan app main, mengatur lokasi template supaya main.html bisa dirender, serta menyiapkan setelan production (DEBUG, ALLOWED_HOSTS, dan WhiteNoise) agar aman saat deploy ke PWS. Singkatnya, semua perilaku global proyek dari database sampai static files diatur lewat settings.py

4. Bagaimana cara kerja migrasi database di Django?
Di Django, aku mengubah models.py, lalu makemigrations membuat skrip perubahan schema, dan migrate mengeksekusinya ke database jadi struktur  selalu mengikuti model Product yang aku definisikan. Kapan harus migrasi? Setiap kali kita mengubah apapun di models.py (nambah field, rename, ganti tipe, dll.) Dengan begitu, struktur selalu mengikuti definisi Product yang aku tulis, baik di lokal maupun di PWS

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 
Django dipilih sebagai permulaan karena arsitektur MVT nya jelas, fiturnya sudah siap pakai, ORM+migrasi ramah pemula, dan pengaturan settings/deploy yang mendidik, semua hal penting untuk belajar bikin aplikasi web beneran dari nol

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? 
Hmm tidak ada kak yay makasih ya keep it up hehe
