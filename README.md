Nama : Nisrina Fatimah
NPM : 2406354000
Kelas : PBP F

TUGAS 2
1. Jelaskan bagaimana cara aku mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
    1. Membuat sebuah proyek Django baru : Aku mulai dengan menyiapkan virtual environment supaya paket Python rapi dan terpisah dari proyek lain. Setelah itu aku bikin requirements.txt, menginstal dependensi dasar, lalu membuat proyek Django bernama kitkeeper. Supaya konfigurasi aman dan rapi, aku juga menyiapkan dua berkas lingkungan: .env untuk development lokal dan .env.prod untuk kebutuhan deploy. Di settings aku menambahkan pengaturan dasar (lokasi template, bahasa/zona waktu, static files, dan persiapan ALLOWED_HOSTS untuk nanti saat deploy). Setelah itu aku menjalankan server lokal untuk memastikan proyeknya sudah hidup, kalau butuh inisialisasi database bawaan Django, aku jalankan migrate dulu (bukan makemigrations, karena model buatan sendiri belum ada di tahap ini).

    2. Membuat aplikasi dengan nama main pada proyek tersebut : Aku menggunakan perintah python manage.py startapp main untuk membuat aplikasi baru bernama main. Lalu mendaftarkan main ke dalam proyek dengan menambahkan pada settings.py di bagian INSTALLED_APPS.

    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main : Aku menyiapkan routing dengan membuat urls.py di dalam app main (nanti diisi rute ke fungsi view). Lalu, di routing level proyek, aku mengarahkan root URL ke routing milik app main. Dengan begitu, setiap kali mengakses /,request akan diteruskan ke peta rute main.

    4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib : Di models.py app main, aku membuat model Product yang berisi 6 atribut wajib sesuai ketentuan tugas: name (CharField), price (IntegerField), description (TextField), thumbnail (URLField), category (CharField), dan is_featured (BooleanField). Karena temanya jersey, aku juga menambahkan beberapa atribut tambahan yang relevan (seperti team, season, size, sleeve_type, condition, manufacturer, stock, dan created_at) 
    agar datanya lebih lengkap. Setelah model selesai, aku membuat dan menerapkan migrasi supaya skema tabel terbentuk di database.

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas aku : Aku menulis fungsi show_main yang menyiapkan context sederhana berisi app_name, student_name, dan student_class. Fungsi ini me-render template main.html sehingga halaman utama menampilkan nama aplikasi, nama, dan kelas sesuai kebutuhan tugas.

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py : Di urls.py app main, aku memetakan path kosong ("") ke fungsi show_main. Jadi saat membuka root /, aplikasi langsung memanggil show_main dan menampilkan halaman identitas.

    7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet : Pertama aku membuat proyek baru di website https://pbp.cs.ui.ac.id/web , lalu menyimpan credentials, dan mengubah raw environment editor dengan isi dari .env.prod. Selanjutnya, di file settings.py aku menambahkan allowed_host dengan URL deployment PWS, lalu melakukan git add, commit, push dan menjalankan perintah yang meminta username serta password PWS. Setelah itu menunggu beberapa saat hingga aplikasi berhasil dideploy dan dapat diakses melalui internet.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
Link gambar : https://drive.google.com/file/d/1sAZV7TSxKB_nASly5Q6O86TVyRWNoEo9/view?usp=sharing 
Saat client mengirim HTTP request, Django terlebih dulu melewati URL dispatcher di project/urls.py. Berkas ini berperan sebagai “peta utama” yang meneruskan (via include) bagian URL yang sesuai ke URLConf aplikasi misalnya app/urls.py. Di level aplikasi, urls.py mencocokkan path yang diminta dengan fungsi/kelas view tertentu. Begitu pola URL cocok, Django membuat objek HttpRequest dan memanggil view yang bersangkutan. Di dalam view inilah logika dijalankan. Jika dibutuhkan data, view akan berinteraksi dengan models.py melalui ORM (misalnya membaca, memfilter, atau menyimpan ke database). Setelah data siap, view memilih template HTML yang relevan dan meminta template engine untuk merender template tersebut dengan context (nilai-nilai yang akan ditampilkan). Hasil render berupa string HTML dikembalikan ke view; lalu view membungkusnya menjadi HttpResponse dan mengirimkannya kembali ke browser.

Referensi : https://docs.djangoproject.com/en/4.2/intro/tutorial03/ dan 03 - MTV Django Architecture.pdf (slide di scele)

3. Jelaskan peran settings.py dalam proyek Django! 
settings.py itu pusat pengaturan proyek. Django baca file ini saat server jalan, lalu semua bagian aplikasi (URL, view, model, template, static) kerja sesuai pengaturan di sini. Di sini aku mengaktifkan app main, mengatur lokasi template supaya main.html bisa dirender, serta menyiapkan setelan production (DEBUG, ALLOWED_HOSTS, dan WhiteNoise) agar aman saat deploy ke PWS. Singkatnya, semua perilaku global proyek dari database sampai static files diatur lewat settings.py.

4. Bagaimana cara kerja migrasi database di Django?
Migrasi di Django itu mekanisme buat memastikan struktur database selalu mengikuti definisi model yang aku tulis di models.py. Alurnya begini: setiap kali aku mengubah model (misalnya menambah/mengganti/merename field di Product), perubahan itu belum menyentuh database. Aku jalankan makemigrations supaya Django membandingkan keadaan model sekarang dengan riwayat sebelumnya lalu membuat berkas migrasi semacam “rencana perubahan” yang berisi operasi skema (CreateModel, AddField, AlterField, dll) tapi belum mengeksekusi SQL. Setelah rencananya ada, aku jalankan migrate untuk mengeksekusi rencana tersebut ke database, Django menerjemahkannya jadi SQL sesuai backend (SQLite/Postgres), menjalankannya, dan mencatat statusnya di tabel internal django_migrations. Hasilnya, tabel (misalnya main_product) jadi selaras dengan model terbaru. Praktiknya, setiap kali mengubah models.py aku ulangi siklus makemigrations -> migrate, dan untuk ingat melakukannya di lokal maupun di PWS karena itu dua database berbeda.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 
Menurut aku, Django cocok banget dijadikan “framework pertama” karena dia mengajarkan fondasi penting pengembangan web tanpa bikin pemula kewalahan. Arsitektur MVT nya rapih, jadi sejak awal kita kebiasaan misahin data (Model), logika (View), dan tampilan (Template). Fitur “batteries-included” (routing, templating, ORM, middleware, static files) sudah siap pakai, sehingga fokus belajar kita ada di konsep, bukan sibuk pasang komponen. ORM + migrasi membuat kita paham cara mendesain dan mengubah skema database dengan aman, tanpa harus langsung bergulat dengan SQL mentah. Melalui settings (mis. DEBUG, ALLOWED_HOSTS, static files) kita juga belajar praktik baik dev vs production dan cara menyiapkan deployment sejak dini. Karena berbasis Python yang sintaksnya ramah, materi lebih cepat dicerna, dan konsep yang dipelajari mudah ditransfer ke framework lain nanti. Singkatnya Django memberi jalur belajar yang terstruktur, lengkap, dan realistis untuk bikin aplikasi web “beneran” dari nol.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah aku kerjakan sebelumnya? 
Hmm tidak ada kak yay makasih ya keep it up hehe

TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery itu penting banget karena dia jembatan antara backend (server, database, logika) dengan frontend (tampilan, interaksi user). Tanpa data delivery yang baik, aplikasi web bakal statis, gak interaktif, dan gak bisa ngasih pengalaman personal ke user. Dengan data delivery, backend bisa ngirim data dinamis (misalnya daftar produk, profil user, hasil pencarian) ke frontend secara real-time atau sesuai kebutuhan. Ini bikin aplikasi terasa hidup, responsif, dan relevan buat user. Selain itu, data delivery juga memungkinkan sinkronisasi data antar user (misalnya notifikasi chat), integrasi dengan layanan eksternal (misalnya pembayaran online), dan optimasi performa (misalnya lazy loading). Singkatnya, data delivery itu fondasi buat bikin aplikasi web modern yang engaging, fungsional, dan scalable.
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut aku, keduanya sama-sama baik. Tergantung dengan kebutuhan kita saja. 
JSON (lebih populer karena):
    - Lebih ringkas & human-readable (kurang boilerplate dibanding XML).
    - Pemetaan tipe data langsung ke struktur bahasa pemrograman (objek, list, number, bool).
    - Native di JavaScript → parsing cepat (JSON.parse) dan dukungan luas di browser/API modern.
    - Payload biasanya lebih kecil → lebih hemat bandwidth.
XML cocok kalau:
    - Dokumen butuh markup kaya (atribut, mixed content) atau transformasi dengan XSLT/XPath.
    - Validasi ketat dengan XSD/DTD & namespaces yang kompleks.
Tapi, untuk API modern, JSON umumnya pilihan default; untuk dokumen/format legacy & transformasi dokumen, XML masih relevan.
3. 