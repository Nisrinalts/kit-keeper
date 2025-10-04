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
Data delivery itu penting banget karena dia jembatan antara backend (server, database, logika) dengan frontend (tampilan, interaksi user). Tanpa data delivery yang baik, aplikasi web bakal statis, gak interaktif, dan gak bisa ngasih pengalaman personal ke user. Dengan data delivery, backend bisa ngirim data dinamis (misalnya daftar produk, profil user, hasil pencarian) ke frontend secara real-time atau sesuai kebutuhan. Ini bikin aplikasi terasa hidup, responsif, dan relevan buat user. Selain itu, data delivery juga memungkinkan sinkronisasi data antar user (misalnya notifikasi chat), integrasi dengan layanan eksternal (misalnya pembayaran online), dan optimasi performa (misalnya lazy loading). Singkatnya, data delivery itu fondasi buat bikin aplikasi web modern yang engaging, fungsional, dan scalable

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut aku, keduanya sama sama baik. Tergantung dengan kebutuhan kita saja. 
JSON (lebih populer karena):
    - Lebih ringkas & human readable (key-value)
    - Pemetaan tipe data langsung ke struktur bahasa pemrograman (objek, list, number, bool)
    - Native di JavaScript -> parsing cepat (JSON.parse) dan dukungan luas di browser/API modern
    - Payload biasanya lebih kecil -> lebih hemat bandwidth
XML cocok kalau:
    - Dokumen butuh markup kaya (atribut, mixed content) atau transformasi dengan XSLT/XPath
    - Validasi ketat dengan XSD/DTD & namespaces yang kompleks
Untuk API modern, JSON biasanya default karena ringkas dan dukungan luas. XML masih relevan untuk kasus dokumen/legacy/validasi & transformasi kompleks

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() melakukan validasi server-side:
- Menjalankan built in validators per field (wajib/opsional, panjang, format, pilihan/choices, dll)
- Menjalankan clean_<field>() dan clean() (validasi lintas field)
- Mengisi form.cleaned_data jika valid, jika tidak, mengisi form.errors untuk ditampilkan ke user
Kenapa perlu?
- Keamanan & integritas data: user bisa mematikan JS/ubah HTML -> hanya server side validation yang bisa dipercaya
- UX lebih baik: error jelas pada field yang salah
- Mencegah data kotor masuk DB

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- CSRF (Cross-Site Request Forgery) = serangan di mana penyerang “menumpang” cookie sesi user untuk mengirim POST ke situs kamu dari domain lain tanpa sepengetahuan user
- Django memitigasi dengan token unik per sesi/permintaan. Saat submit form, token harus cocok -> jika tidak, request ditolak
- Tanpa CSRF token, penyerang bisa menaruh form tersembunyi/auto-submit di situs berbahaya yang menembak endpoint kamu (mis. create, delete, transfer, change password) memakai cookie user -> state berubah tanpa consent.

Best practice:
- Pasang {% csrf_token %} di setiap <form method="POST">
- Saat deploy (PWS), set CSRF_TRUSTED_ORIGINS ke domain

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID : 
    Di main/views.py aku membuat empat fungsi khusus data delivery. show_xml dan show_json mengambil seluruh objek Product dengan Product.objects.all() lalu men-serialize hasilnya menggunakan serializers.serialize("xml" | "json", queryset) dan mengembalikannya sebagai HttpResponse dengan content_type yang tepat. Untuk varian by-ID, aku menambahkan show_xml_by_id yang menggunakan Product.objects.filter(pk=id) agar tetap berupa QuerySet (aman untuk diserialisasi meskipun tidak ada hasil), serta show_json_by_id yang memakai Product.objects.get(pk=id) karena memang hanya satu objek; objek tunggal ini kubungkus ke dalam list sebelum diserialisasi. Pada show_json_by_id juga kutambahkan penanganan try/except Product.DoesNotExist supaya ketika UUID tidak ditemukan, view mengembalikan status 404 yang jelas. Seluruh fungsi ini bekerja di atas primary key UUID tanpa perlu konversi manual dari string karena Django sudah memetakan parameter URL <uuid:id> menjadi objek UUID di view
    b. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
    Di main/urls.py aku memetakan rute untuk seluruh endpoint data delivery dan memberi nama pada masing-masing path agar mudah dipanggil dari template. Khusus parameter ID, aku memakai converter <uuid:id> supaya URL sesuai dengan tipe primary key pada model. Hasilnya, endpoint yang tersedia adalah /xml/ dan /json/ untuk semua data, serta /xml/<uuid:id>/ dan /json/<uuid:id>/ untuk akses berdasarkan satu produk. Pada saat yang sama, rute halaman aplikasi juga kuatur: / untuk daftar produk (show_main), /add/ untuk form tambah (create_product), dan /detail/<uuid:id>/ untuk detail (show_product). Dengan susunan ini, baik konsumsi data mesin (XML/JSON) maupun navigasi HTML untuk pengguna berjalan selaras
    c. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
    Untuk menampilkan koleksi produk, fungsi show_main mengambil semua Product lalu merender templates/main.html. Di halaman ini setiap item divisualisasikan sebagai kartu kecil bernuansa pastel: sisi kiri menampilkan gambar thumbnail, sisi kanan berisi label “Product N” dan nama produk yang dipertegas, diikuti garis pemisah horizontal; bagian bawah kiri menampilkan “Category — Team” (dengan get_category_display agar label dari choices tampil rapi), sementara bagian bawah kanan ada tombol “Detail” yang ketika diklik mengarahkan pengguna ke halaman detail produk sesuai UUID. Di bagian atas halaman, terdapat tombol “+ Add Product” yang membawa pengguna ke halaman form. Ukuran kartu kuseragamkan lewat CSS (tinggi baris dan lebar kolom foto dikunci) agar tampilan list rapih dan konsisten
    d. Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
    Untuk pembuatan entri baru, aku membuat ProductForm (ModelForm) di main/forms.py yang memetakan field-field dari model Product. View create_product menangani dua alur: pada GET ia merender templates/create_product.html yang berisi {{ form.as_p }} dan {% csrf_token %}; pada POST ia memvalidasi input lewat form.is_valid(), lalu memanggil form.save() ketika data sah, dan akhirnya melakukan redirect('main:show_main') agar pengguna kembali ke daftar dan melihat item baru mereka. Karena beberapa field, seperti category, size, dan sleeve_type—didefinisikan sebagai choices pada model, input di halaman form otomatis menjadi dropdown sehingga konsisten dengan pilihan yang sudah ditentukan (mis. Jersey; XXS–XXL; None/Short/Long)
    e. Membuat halaman yang menampilkan detail dari setiap data objek model.
    Halaman detail dihasilkan oleh show_product yang memanggil get_object_or_404(Product, pk=id) sehingga jika UUID tidak valid atau data tidak ada, pengguna akan mendapat 404 yang tepat. Template templates/product_detail.html menata informasi dalam dua kolom: bagian kiri berisi teks (nama produk, harga, kategori, ukuran, jenis sleeve, dan atribut relevan lainnya), sementara bagian kanan menyajikan foto di dalam photo card terpisah. Untuk menampilkan label yang ramah pengguna pada field bertipe choices, aku menggunakan helper {{ product.get_<field>_display }} sehingga, misalnya, “short” ditampilkan sebagai “Short Sleeve”. Khusus halaman detail, gaya container aku override menjadi putih agar isi lebih fokus, sementara halaman daftar tetap memakai latar gradient sesuai tema

LINK DRIVE FOTO : https://drive.google.com/drive/folders/1QkHMYRa5oEKPHRdwSnfnErx-qviH7hZr?usp=sharing 

TUGAS 4
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya
    Django AuthenticationForm adalah form bawaan dari django.contrib.auth.forms untuk login yang menyediakan fields username dan password memvalidasi lewat aut backend dan apabila valid akan mengembalikan user yang bisa dipakai login(request, user)
    Kelebihannya yaitu siap pakai dan aman, terintegrasi session dan juga pesan error yang standard cocok untuk pemula. Kekurangannya yaitu keterbatasan yang hanya menyediakan username/password sehingga kalau butuh fields tambahan akan memerlukan custom form dan juga pesan error yang generik.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Autentikasi : verifikasi siapa kita(login). Di Django: authenticate() -> jika OK, login() menyimpan identitas ke session
    Otorisasi : verifikasi boleh akses apa. Di Django: pengecekan user.is_authenticated, @login_required, permission & groups (permission_required, user.has_perm()), serta pola kontrol akses lain

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Session
        Kelebihan : data sensitif disimpan di server, cookie di klien hanya menyimpan sessionid, bisa dicabut sisi server. Sehingga cocok untuk info user/login
        Kekurangan : ada beban penyimpanan di server, perlu skalabilitas (DB/cache) saat traffic besar
    Cookies
        Kelebihan : ringan, sederhana, bisa persisten(tetap ada setelah browser ditutup) sehingga cocok untuk preferensi ringan
        Kekurangan : kapasitas kecil, bisa dibaca/diutak atik klien, rawan dicuri lewat XSS, dan mudah “terlihat” di request sehingga jangan taruh data sensitif

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Tidak otomatis aman. Risiko umum: XSS (mencuri cookie), CSRF (menyalahgunakan session pengguna), sniffing saat non-HTTPS, dan salah konfigurasi.
    Django membantu :
        - CSRF protection aktif default (CsrfViewMiddleware) + {% csrf_token %} di form.
        - Escaping template bantu cegah XSS (tapi tetap harus sanitasi input)
        - Session cookie biasanya diberi HttpOnly (mengurangi akses JS) & SameSite (mitigasi CSRF) -> gunakan Secure pada HTTPS lewat SESSION_COOKIE_SECURE/CSRF_COOKIE_SECURE
    Sehingga, pakai cookie untuk hal ringan. Untuk autentikasi/identitas, simpan di session server-side dan pastikan flag keamanan diaktifkan

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya : Routing & view, Aku tambah tiga route di main/urls.py: /register/, /login/, dan /logout/.
    Di views.py: register(request): pakai UserCreationForm. Kalau valid -> form.save() -> tampilkan pesan sukses -> redirect ke /login/ (sengaja tidak auto-login supaya metrik last_login dicatat saat login beneran)
    login_user(request): pakai AuthenticationForm. Kalau valid -> login(request, user) -> bikin HttpResponseRedirect ke halaman utama -> set cookie last_login dengan timestamp sekarang -> return response.
    logout_user(request): panggil logout(request) -> hapus cookie last_login -> redirect ke /login/.
    Template, Aku buat login.html dan register.html yang simple, sudah ada {% csrf_token %} dan tanpa pemanggilan method ber argumen di template
    - Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal : Sesuai permintaan soal, aku membuat 2 akun langsung dari website PWS lewat halaman Register. Lalu login masing-masing akun dan menambahkan 3 produk per akun via tombol Add Product. Ini sekaligus menguji end-to-end flow: register -> login (cookie terset) -> create product (terkait user).
    - Menghubungkan model Product dengan User : 
    Di main/models.py aku tambahkan field: user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Lalu makemigrations + migrate.
    Di create_product, aku simpan pemilik produk:
    product = form.save(commit=False)
    product.user = request.user
    product.save()
    Aku juga punya filter “All / My Products” di show_main untuk memfilter berdasarkan request.user.
    Ini menerapkan relasi many-to-one (banyak product ke satu user).
    - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi : Di show_main(request) aku kirimkan ke context:
    "name": request.user.username,
    "last_login": request.COOKIES.get("last_login", "Never")
    Di main.html aku tampilkan bar kecil di bawah header:
    Welcome, {{ request.user.username }} • Last login: {{ last_login }}
    Semua view yang harus aman—show_main, create_product, show_product—aku beri @login_required agar non-logged user otomatis diarahkan ke /login


TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Dalam CSS ada konsep specificity atau tingkat kekuatan selector. Urutan prioritasnya seperti ini:
    1. Inline style (style="..." langsung di elemen HTML) akan selalu menang karena paling spesifik.
    2. Selector dengan ID (#id-name) lebih kuat daripada class.
    3. Selector dengan class, attribute, atau pseudo-class (misalnya .card, [type="text"], :hover) berada di bawah ID.
    4. Selector dengan element atau pseudo-element (h1, p, ::before) punya kekuatan paling lemah.
    5. Jika dua aturan punya tingkat spesifik yang sama, aturan yang dideklarasikan paling akhir akan dipakai.
Dengan kata lain: inline > id > class > element, dan posisi terakhir juga berpengaruh.
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design penting karena pengguna mengakses website dari perangkat yang sangat beragam: HP, tablet, maupun laptop/PC. Tanpa desain responsif, tampilan bisa berantakan, pengguna harus zoom in/out, tombol jadi kecil, dan pengalaman mereka jadi buruk. Manfaatnya antara lain yaitu User experience lebih baik, mudah digunakan di semua device, Aksesibilitas meningkat, tidak ada pengguna yang kesulitan membaca konten, dan juga Efisiensi: kita hanya butuh satu kode dasar, tanpa membuat versi berbeda untuk mobile/desktop.
- Contoh aplikasi yang sudah menerapkan responsive design: Tokopedia: di desktop produknya tampil 4–5 kolom, sedangkan di HP otomatis berubah jadi 1–2 kolom, tombol tetap nyaman untuk ditekan.
- Contoh aplikasi yang belum responsif:

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah ruang kosong di luar elemen, berguna untuk mengatur jarak antar elemen.
Border adalah garis tepi yang membungkus elemen, biasanya dipakai sebagai bingkai.
Padding adalah ruang kosong di dalam elemen, antara konten dengan border.
Contoh penggunaannya dalam web:
- Margin dipakai agar antar-kartu produk tidak berhimpitan.
- Border dipakai untuk memberi frame agar setiap kartu lebih jelas.
- Padding dipakai supaya teks di dalam tombol atau kartu tidak menempel ke tepi.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah sistem layout 1 dimensi, cocok untuk mengatur elemen secara horizontal atau vertikal. Misalnya: membuat navbar, menyusun tombol dalam satu baris, atau memposisikan elemen ke tengah halaman.
Grid Layout adalah sistem layout 2 dimensi, artinya bisa mengatur baris dan kolom sekaligus. Cocok dipakai untuk membuat galeri produk, dashboard, atau layout halaman yang kompleks.
Perbedaan utama:
- Kalau hanya perlu susunan linear (misalnya satu baris menu), gunakan Flexbox.
- Kalau perlu susunan kotak/galeri (misalnya daftar produk multi-kolom), gunakan Grid.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Menambahkan fitur edit & delete product
    - Aku membuat view baru untuk edit dan delete, lalu menghubungkannya dengan URL pattern baru.
    - Di halaman daftar produk dan halaman detail, aku menambahkan tombol "Edit" dan "Delete" supaya user bisa langsung melakukan aksi tersebut.
    - Untuk delete, aku tambahkan konfirmasi agar tidak terhapus tanpa sengaja.
    - Supaya aman, aku batasi hanya pemilik produk yang bisa melakukan edit dan delete.
2. Mengubah tampilan halaman (login, register, tambah, edit, detail produk)
    - Aku mengonversi desain lama yang masih pakai CSS biasa menjadi Tailwind CSS.
    - Semua ukuran, warna, dan posisi aku sesuaikan agar tampilannya menarik, tapi tetap konsisten di seluruh halaman.
    - Login & register aku buat dengan kartu sederhana di tengah layar, tombol dibuat lebih jelas, input diberi padding dan border yang halus.
    - Halaman detail produk aku ubah jadi dua kolom: bagian kiri menampilkan foto produk, bagian kanan menampilkan deskripsi, harga, serta tombol aksi.
3. Halaman daftar produk lebih menarik dan responsif
    - Aku menambahkan kondisi khusus: jika produk kosong, tampilkan ilustrasi gambar dan teks “Belum ada produk”.
    - Jika ada produk, tampilannya menggunakan card dengan desain baru, berbeda dari tutorial. Setiap card memuat foto produk, nama, harga, deskripsi singkat, serta tombol edit dan delete.
    - Layout daftar produk dibuat dengan CSS Grid sehingga jumlah kolom menyesuaikan ukuran layar: 1 kolom di HP, 2–3 kolom di tablet, dan 4 kolom di desktop.
4. Navbar responsif
    - Aku menambahkan navbar di base.html supaya muncul di semua halaman.
    - Di desktop, navbar tampil sebagai menu horizontal.
    - Di mobile, navbar berubah jadi menu burger yang bisa diklik untuk menampilkan daftar link.
    - Isi navbar meliputi link ke halaman utama, tambah produk, login/logout.
5. Responsif di seluruh halaman
    - Aku menggunakan breakpoint bawaan Tailwind (sm:, md:, lg:) untuk mengatur tampilan sesuai ukuran layar.
    - Semua halaman sudah aku uji di ukuran mobile, tablet, dan desktop supaya tetap nyaman dilihat.
Dengan alur ini, semua checklist dari tugas 5 berhasil aku implementasikan: ada fitur edit & delete, tampilan halaman yang dikustomisasi, daftar produk dengan kondisi empty dan non-empty, card produk dengan tombol aksi, dan navbar responsif.


TUGAS 6
1. Apa perbedaan antara synchronous request dan asynchronous request?
    Synchronous Request:
    - Blocking: Browser menunggu respons dari server sebelum melanjutkan
    - Halaman harus di-refresh untuk memperbarui konten
    - User tidak bisa berinteraksi dengan halaman selama request diproses
    - Contoh: Form submit tradisional yang me-reload halaman

    Asynchronous Request:
    - Non-blocking: Browser tetap bisa digunakan selama menunggu respons
    - Update konten tanpa reload halaman (partial update)
    - User bisa terus berinteraksi dengan halaman
    - Contoh: Like post di social media tanpa refresh halaman

2. Bagaimana AJAX bekerja di Django (alur request–response)?
    1. Client-side:
    - JavaScript membuat XMLHttpRequest/fetch ke URL Django
    - Request bisa membawa data (POST/PUT) atau hanya mengambil data (GET)
    - CSRF token disertakan untuk keamanan

    2. Server-side (Django):
    - View menerima request AJAX (dapat dideteksi dengan request.headers['X-Requested-With'])
    - Memproses data/query database sesuai kebutuhan
    - Mengembalikan response (biasanya JSON)
    
    3. Client-side lagi:
    - JavaScript menerima response
    - Memperbarui DOM sesuai data yang diterima
    - Menampilkan feedback ke user (success/error)

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
    1. User Experience:
    - Tidak ada page refresh yang mengganggu
    - Feedback instant ke user
    - Transisi lebih halus

    2. Performa:
    - Bandwidth lebih hemat (hanya transfer data yang diperlukan)
    - Server load berkurang (tidak perlu render full page)
    - Respons lebih cepat untuk update kecil

    3. Interaktivitas:
    - Real-time updates tanpa refresh
    - Multi-tasking (user bisa lakukan beberapa aksi sekaligus)
    - Validasi form instant

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
    1. CSRF Protection:
    - Sertakan CSRF token di setiap request
    - Gunakan {% csrf_token %} di template
    - Kirim token via headers: 'X-CSRFToken'

    2. Validasi:
    - Server-side validation tetap wajib
    - Sanitasi input untuk mencegah XSS
    - Rate limiting untuk mencegah brute force

    3. Best Practices:
    - Gunakan HTTPS
    - Jangan simpan data sensitif di localStorage/sessionStorage
    - Implementasi timeout untuk session
    - Enkripsi data sensitif sebelum dikirim

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
    1. Kecepatan & Responsivitas:
    - Update UI instan tanpa loading screen
    - Feedback langsung untuk aksi user
    - Mengurangi waktu tunggu

    2. Interaktivitas:
    - Form validation real-time
    - Auto-save
    - Live search/filter
    - Infinite scroll

    3. Seamless Experience:
    - Tidak ada interupsi navigasi
    - Background processing
    - Progress indicators untuk operasi panjang
    - Reduced cognitive load karena konteks tetap terjaga

    4. Mobile-Friendly:
    - Hemat bandwidth
    - Lebih responsif di koneksi lambat
    - Lebih baik untuk single page applications