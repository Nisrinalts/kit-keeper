Nama : Nisrina Fatimah
NPM : 2406354000
Kelas : PBP F

TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
    1. Membuat sebuah proyek Django baru : Aku mulai dengan menyiapkan virtual environment supaya paket Python rapi dan terpisah dari proyek lain. Setelah itu aku bikin requirements.txt, menginstal dependensi dasar, lalu membuat proyek Django bernama kitkeeper. Supaya konfigurasi aman dan rapi, aku juga menyiapkan dua berkas lingkungan: .env untuk development lokal dan .env.prod untuk kebutuhan deploy. Di settings aku menambahkan pengaturan dasar (lokasi template, bahasa/zona waktu, static files, dan persiapan ALLOWED_HOSTS untuk nanti saat deploy). Setelah itu aku menjalankan server lokal untuk memastikan proyeknya sudah hidup, kalau butuh inisialisasi database bawaan Django, aku jalankan migrate dulu (bukan makemigrations, karena model buatan sendiri belum ada di tahap ini).

    2. Membuat aplikasi dengan nama main pada proyek tersebut : Aku menyiapkan routing level app dengan membuat urls.py di dalam app main (nanti diisi rute ke fungsi view). Lalu, di routing level proyek, aku mengarahkan root URL ke routing milik app main. Dengan begitu, setiap kali mengakses /, request akan diteruskan ke peta rute main.

    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main : Aku menyiapkan routing dengan membuat urls.py di dalam app main (nanti diisi rute ke fungsi view). Lalu, di routing level proyek, aku mengarahkan root URL ke routing milik app main. Dengan begitu, setiap kali mengakses /, request akan diteruskan ke peta rute main.

    4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib : Di models.py app main, aku membuat model Product yang berisi 6 atribut wajib sesuai ketentuan tugas:
    name (CharField), price (IntegerField), description (TextField), thumbnail (URLField), category (CharField), dan is_featured (BooleanField).
    Karena temanya jersey, aku juga menambahkan beberapa atribut tambahan yang relevan (seperti team, season, size, sleeve_type, condition, manufacturer, stock, dan created_at) agar datanya lebih lengkap. Setelah model selesai, aku membuat dan menerapkan migrasi supaya skema tabel terbentuk di database.

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu : Aku menulis fungsi show_main yang menyiapkan context sederhana berisi app_name, student_name, dan student_class. Fungsi ini me-render template main.html sehingga halaman utama menampilkan nama aplikasi, nama, dan kelas sesuai kebutuhan tugas.

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py : Di urls.py app main, aku memetakan path kosong ("") ke fungsi show_main. Jadi saat membuka root /, aplikasi langsung memanggil show_main dan menampilkan halaman identitas.

    7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet : Pertama aku membuat proyek baru di website https://pbp.cs.ui.ac.id/web , lalu menyimpan credentials, dan mengubah raw environment editor dengan isi dari .env.prod. Selanjutnya, di file settings.py aku menambahkan allowed_host dengan URL deployment PWS, lalu melakukan git add, commit, push dan menjalankan perintah yang meminta username serta password PWS. Setelah itu menunggu beberapa saat hingga aplikasi berhasil dideploy dan dapat diakses melalui internet.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
A[Client / Browser] -> B[project/urls.py] : meneruskan semua request dari domain ke “aplikasi” (app) tertentu
B -> C[main/urls.py] : memetakan sebuah path ke fungsi di views.py, kalau path-nya kosong ("", alias halaman depan), panggil fungsi show_main 
C -> D[views.py (show_main)] : menerima request, menyiapkan data (context), lalu merender template HTML
D ->|render + data context| E[templates/main.html] : menerima context dari view dan menampilkan jadi HTML
E -> F[Response HTML ke Browser]


3. Jelaskan peran settings.py dalam proyek Django! 
settings.py itu pusat pengaturan proyek. Django baca file ini saat server jalan, lalu semua bagian aplikasi (URL, view, model, template, static) kerja sesuai pengaturan di sini. Di sini aku mengaktifkan app main, mengatur lokasi template supaya main.html bisa dirender, serta menyiapkan setelan production (DEBUG, ALLOWED_HOSTS, dan WhiteNoise) agar aman saat deploy ke PWS. Singkatnya, semua perilaku global proyek dari database sampai static files diatur lewat settings.py


4. Bagaimana cara kerja migrasi database di Django?
Di Django, aku mengubah models.py, lalu makemigrations membuat skrip perubahan schema, dan migrate mengeksekusinya ke database jadi struktur sehingga akan selalu mengikuti model Product yang aku definisikan. Kapan harus migrasi? Setiap kali kita mengubah apapun di models.py (nambah field, rename, ganti tipe, dll.) Dengan begitu, struktur selalu mengikuti definisi Product yang aku tulis, baik di lokal maupun di PWS


5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 
Django dipilih sebagai permulaan karena arsitektur MVT nya jelas, fiturnya sudah siap pakai, ORM+migrasi ramah pemula, dan pengaturan settings/deploy yang mendidik, semua hal penting untuk belajar bikin aplikasi web beneran dari nol


6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? 
Hmm tidak ada kak yay makasih ya keep it up hehe
