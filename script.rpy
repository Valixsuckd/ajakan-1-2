# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image ruang_tamu_arman = "images/1.png"
image dapur_arman = "images/2.png"
image ruang_tamu_uztad = "images/3.png"
image ruang_kelas = "images/4.png"
image kampus = "images/5.png"
image masjid = "images/6.png"
image atap_markas = "images/7.png"
image ruang_rapat_rahasia = "images/8.png"
image aula_utama_markas_teroris = "images/9.png"
image lorong_markas_teroris = "images/10.png"
image hutan = "images/11.png"
image sungai_dalam_hutan = "images/12.png"
image meja_diskusi_markas_teroris = "images/13.png"
image garasi_markas_teroris = "images/14.png"
image dalam_mobil = "images/15.png"
image dermaga = "images/16.png"
image ruang_pengadilan = "images/17.png"
image dalam_penjara = "images/18.png"
image ruang_interogasi = "images/19.png"
image kantor_hotel = "images/22.png"
image kantin_siang_ramai = "images/25.png"
# Declare characters
define ar = Character("Arman")
define ay = Character("Ayah")
define ib = Character("Ibu")
define na = Character("Naomi")
define po = Character("Polisi")
define vi = Character("Victor")
define bu = Character("Budi")
define ri = Character("Rizal")
define ni = Character("Ibu-ibu")
define nb = Character("Bapak-bapak")
define ra = Character("Raksa")
define ja = Character("Jarwo")

# Mulai Permainan
label start:
    # SCENE 1: Pengenalan Keluarga Arman
    scene ruang_tamu_arman with fade
    ar "Ayah, Ibu, besok Arman mulai kuliah!"
    ay "Selamat ya nak. Kamu sudah keterima di ITW, kampus impianmu. Ayah bangga sama kamu."
    ib "Selamat, sayang. Nak Arman memang hebat. Bunda bangga sama kamu."
    ar "Makasih ya, Ayah, Ibu. Arman masuk ITW juga berkat support Ayah dan Ibu."
    ar "Insya Allah, besok sudah mulai masuk. Mohon doanya ya, Ayah."
    ay "Tentu, nak. Ayah selalu mendoakan yang terbaik untukmu. Semoga lancar dan sukses, juga selalu dalam lindungan Allah SWT."

    # SCENE 2: Pengenalan Arman
    scene kampus with dissolve
    ar "Namaku Arman. Alhamdulillah aku masuk ITW, kampus yang sudah aku idamkan sejak SMA. Aku sangat menyukai teknologi, matematika, dan coding. Itu yang membuatku ingin masuk ITW."

    # SCENE 3: Pengenalan Naomi
    scene ruang_kelas with fade
    ar "Hmm, mungkin hanya isu saja..."
    na "Arman!"
    ar "Naomi?"
    show arman happy at left with dissolve
    show naomi happy at right with dissolve
    na "Arman, bener Arman kan?"
    ar "Naomi kan?"
    na "Benar! Arman ingat nggak? Aku teman masa kecil kamu!"
    ar "Iya, Naomi."
    na "Arman, kita makan bareng, yuk?"

    menu:
        "Maaf Naomi, mungkin lain kali.":
            jump scene_4
        "Boleh, tidak masalah Naomi.":
            jump scene_5

label scene_4:
    # SCENE 4: Huru-Hara Hotel Imperial
    scene ruang_tamu_arman with fade
    ay "Apa salahku ya Allah??"
    ib "Ayah, sudah Ayah. Tenang dulu."

    play sound "telephone_ring.mp3"
    ay "Halo?"
    scene ruang_interogasi with fade
    po "Selamat siang, ini dengan Bapak Agus, benar? Kami dari kepolisian menerima laporan bahwa perusahaan Bapak, Hotel Imperial, terlibat kasus pencucian uang, penyalahgunaan izin, dan penggelapan dana sejak 2015."
    scene ruang_tamu_arman with dissolve
    ay "Itu tuduhan palsu, Pak! Mohon cek surat laporannya terlebih dahulu. Kalau tidak, saya akan melaporkan balik atas pencemaran nama baik!"
    scene ruang_interogasi with fade
    po "Silakan, Pak Agus. Namun, kami memiliki bukti konkret. Kami akan melakukan investigasi lebih lanjut terhadap hotel Anda."
    play sound "phone_hangup.mp3"
    scene ruang_tamu_arman with dissolve
    ay "SIAL!!"
    jump scene_6

label scene_5:
    # SCENE 5: Bersama Naomi di Kantin
    scene kantin_siang_ramai with fade
    na "Arman, kenapa terlihat murung? Apa ada masalah?"
    ar "Uhhh, nggak Naomi. Nggak apa-apa."
    na "Arman, nggak usah bohong deh. Kamu kelihatan berbeda dari biasanya."
    ar "Ya sebenarnya ada sih... Tapi aku nggak yakin apakah ini hoax atau fakta."
    na "Memangnya kenapa, Arman?"
    ar "Hotel Ayahku dituduh melakukan pencucian uang dan banyak tanggapan buruk dari masyarakat. Aku nggak tahu apa yang harus kulakukan."
    na "Astaghfirullah, Arman. Aku berdoa semoga semuanya segera selesai. Kalau ada yang bisa kubantu, kasih tahu aku ya."
    ar "Terima kasih, Naomi."
    

label scene_6:
    # SCENE 6: Konflik di Rumah
    scene ruang_tamu_arman with fade
    ay "DASAR ANAK TIDAK TAHU DIRI!"
    ar "Maksud Ayah apa?"
    ay "Kenapa baru pulang jam segini? Pergi ke mana saja kamu? Main-main terus, kuliah tidak becus."
    ib "Arman, dari mana saja? Ibu tidak suka kamu pulang malam."
    ar "Ayah, Ibu! Jangan langsung tuduh! Aku habis kerja kelompok, bukan main-main."
    ay "Halah alasan! Kamu paling jago bikin alibi."
    ar "Ayah juga jago bikin alibi untuk menutupi masalah perusahaan Ayah yang busuk itu!"
    ay "Jaga ucapanmu, Arman!"
    ib "Sudah Arman. Besok kamu ikut pengajian saja, daripada nongkrong nggak jelas."

    menu:
        "Menolak ikut pengajian":
            jump scene_8
        "Mengalah untuk Ibu dan ikut pengajian":
            jump scene_9

label scene_8:
    # SCENE 8: Penolakan Pengajian
    scene masjid with fade
    ar "Ya Allah, kenapa aku mendapat cobaan berat seperti ini? Berilah petunjuk-Mu ya Allah."
    ar "Semoga dalang di balik fitnah ini segera terbalaskan."
    jump scene_10

label scene_9:
    # SCENE 9: Mengalah untuk Ibu
    scene kampus with fade
    ar "Notifikasi grup... Kerja kelompok dibatalkan? Ya sudah, lebih baik aku pulang."
    show naomi smiling
    na "Arman, kok sendirian di kampus?"
    ar "Naomi, terlihat buru-buru. Mau ke mana?"
    na "Aku mau ikut pengajian. Kamu tertarik ikut juga?"
    ar "Iya, aku mau lebih sering baca Alquran dan ikut ceramah ustadz."
    na "Bagus sekali! Nanti aku kenalkan teman-teman di sana."
    

label scene_10:
    # SCENE 10: Victor manipulatif terhadap Budi
    scene kantor_hotel with fade
    vi "Budi, kamu sangat berhutang budi pada Agus, bukan?"
    bu "Pak Agus orang baik. Tidak mungkin dia melakukan itu."
    vi "Jangan naif, Budi. Agus hanya memanfaatkanmu. Kalau kamu bergabung denganku, aku pastikan kamu aman."
    bu "... (terdiam)."

label scene_11:
    scene ruang_tamu_arman with fade
    play sound "door_knock.ogg"
    ib "Suami saya tidak bersalah! Kami dijebak!"
    po "Kami hanya menjalankan tugas. Bapak Agus dilaporkan atas tuduhan penggelapan uang."
    ay "Apa-apaan ini? Saya tidak bersalah!"
    po "Kami harus membawa Bapak untuk diinterogasi di kantor."
    play sound "dramatic_sound.ogg"

label scene_12:
    scene ruang_tamu_arman with fade
    ay "Arman, Ayah mau bicara. Perusahaan Ayah sedang banyak utang."
    ay "Maaf, bulan depan kamu harus menunggak uang kuliah. Untuk makan saja kita susah."
    ar "... (terdiam)."
    show subtitle "Ya Allah, keluarga kami telah kehilangan segalanya."

label scene_13:
    scene kampus with fade
    na "Arman, ada apa?"
    menu:
        "Menceritakan pada Naomi":
            jump scene_14
        "Memendam masalah":
            jump scene_15
                       
label scene_14:
    scene kampus
    ar "Naomi, aku tidak tahu harus bagaimana. Hotel Ayahku dituduh macam-macam."
    na "Astaghfirullah. Aku berdoa masalah ini segera selesai, Arman. Kalau butuh bantuan, kasih tahu aku ya."
    ar "Terima kasih, Naomi."
    jump scene_16

label scene_15:
    scene kampus
    ar "Ah, tidak apa-apa."
    na "Kalau ada apa-apa, kamu bisa cerita ke aku ya."

label scene_16:
    scene dapur_arman with fade
    ay "Aku tidak sanggup lagi hidup di dunia ini..."
    show subtitle "Ayah meninggalkan surat wasiat."
    show subtitle "Untuk Ibu: Siti, maafkan aku. Dunia ini tidak adil. Aku pamit."
    show subtitle "Untuk Arman: Ayah salah jalan. Patuhilah Ibu dan ikuti pengajian. Jangan seperti Ayah."

label scene_17:
    scene ruang_tamu_arman with fade
    ib "Arman, jangan lupa ikut pengajian."
    ar "Bu, sudah bu! Ayah sudah nggak ada!!"
    ib "... (kaget)."
    ar "Ibu, istighfar."
    ib "Arman, tolong dengarkan pesan Ayah. Ikutlah pengajian dan dengarkan ceramah ustadz."
    ar "Iya, Bu. Arman akan ikut pengajian."

label scene_18:
    scene masjid with fade
    ar "Aku ikut pengajian untuk menyenangkan Ibu, meski pikiranku penuh kebencian dan kesedihan."
    show shadow "rizal" with fade
    show subtitle "Rizal memperhatikan Arman dengan niat tertentu..."

