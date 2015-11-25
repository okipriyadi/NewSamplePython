"""
PEMILIHAN
simbol "|" disebut juga alternasi atau pemilihan. Dapat dibaca sebagai “atau”. 
Gunanya untuk memilih satu dari dua atau lebih alternatif yang kita sediakan. 
Beberapa contoh:

aku|kamu,                 cocok dengan aku atau kamu, tapi tidak dengan dia;
apel|anggur|pisang,       cocok dengan salah satu dari apel, anggur, atau pisang, tapi tidak dengan jambu karena itu tidak ada dalam daftar pilihan.

============================================================================================================
PENGELOMPOKAN

"(" dan ")" berguna untuk mengelompokkan, persis seperti tanda kurung dalam operasi matematika. 
Umumnya dipakai bersama karakter meta lain. Contoh:

satria (baja hitam|pembela kebenaran) akan cocok dengan “satria baja hitam” atau “satria pembela kebenaran”. Regex ini berbunyi sebagai berikut: “deretan huruf ‘satria’ diikuti spasi dan diikuti ‘baja hitam’ atau ‘pembela kebenaran’.

============================================================================================================
Set karakter

"[" dan "]" mengapit sebuah set karakter. Pada dasarnya berguna untuk memberi pilihan juga, 
sama seperti |, namun memiliki perbedaan pilihannya berupa huruf dan memiliki sintaks 
rentang dan negasi. Sintaks rentang adalah [m-n] dan akan cocok dengan karakter mulai 
dari m hingga n. Sintaks negasi adalah [^m] dan akan cocok dengan semua karakter kecuali m. 
Berikut beberapa contoh set.


bat[aoiu]k, cocok dengan batak, batok, batik, atau batuk.
bat(a|i|o|u)k, sama dengan sebelumnya, namun menggunakan |.
[0-9], cocok dengan angka 0 hingga 9.
[A-EG-Z], cocok dengan semua huruf besar kecuali F.
[0-9][0-9], cocok dengan `00’ hingga ‘99’ (100 kombinasi).
[012][0-9], cocok dengan ‘00’ hingga ‘29’ (30 kombinasi)
[012][0-9]|30, cocok dengan ‘00’ hingga ‘29’ atau ‘30’ (30 plus 1 kombinasi)
sem([ui]|bilan), cocok dengan semi, semu, atau sembilan. Tidak cocok dengan semibilan, semubilan, maupun semuibilan.
Opsional

============================================================================================================
?

Arti ? di regex berbeda dengan di wildcard. Di regex, ? berarti huruf atau kelompok 
di kiri bersifat opsional. Dapat juga dibaca sebagai “boleh ada atau boleh tidak.” 
Beberapa contoh:

silah?kan, cocok dengan silakan atau silahkan.
(silah)?kan, cocok dengan silahkan atau dengan kan saja.
advi([sc]es?|sory), cocok dengan advice, advise, advices, advises, atau advisory. 
Regex ini berbunyi “empat huruf advi diikuti dengan salah satu dari: a) huruf s atau c 
yang diikuti e dan boleh diikuti s; atau b) deretan huruf sory.”

============================================================================================================
Titik

Titik atau dot adalah lambang yang cocok dengan semua karakter TUNGGAL. 
Beberapa contoh:

bat.k cocok dengan batak, batok, dan juga batbk, bat+k, bat8k, dsb. Namun tidak cocok dengan batrak (karena tr adalah dua karakter) atau batk (nol karakter).
bat.?k sama seperti sebelumnya, namun cocok pula dengan batk (nol karakter) karena titik diikuti oleh tanda opsional.
b...k cocok dengan lebih banyak lagi string, mulai dari batak, buruk, bilik, dan semua potongan string yang terdiri dari 5 karakter, diawali dengan b dan diakhiri dengan k.
============================================================================================================
Nol-Atau-Lebih, Satu-Atau-Lebih

Kalau tanda optional ? bisa dibilang sebagai “nol-atau-satu”, maka 
* melambangkan “nol-atau-lebih” dan 
+ melambangkan “satu-atau-lebih” dari karakter atau kelompok yang berada tepat di kiri tanda tersebut. Beberapa contoh:

[0-9]+, cocok dengan deretan angka.
.+, cocok dengan satu atau lebih karakter apa pun, atau cocok dengan string yang “tidak kosong”.
.*, cocok dengan nol atau lebih karakter apa pun, atau cocok dengan string apa saja, termasuk juga yang kosong.
h?(ah|eh)+!*, berbunyi “boleh diawali huruf h, terdiri dari deretan ah atau eh, dan boleh diakhiri dengan deretan tanda seru.” Cocok dengan string seperti eh, hahahah!, atau ehehahehah!!!. Tidak cocok dengan string seperti haha, hhah!, maupun h!.
============================================================================================================
Jangkar

^ dan $ masing-masing dapat disebut sebagai “harus di awal” dan “harus di akhir.” 
Mengapa disebut jangkar? Kedua karakter ini tidak melambangkan karakter mereka sendiri, 
ingat, keduanya adalah karakter meta. Bahkan ^ dan $ di sini tidak melambangkan karakter 
apapun, melainkan mensyaratkan posisi atau penambatan pola ke string yang ingin dicocokkan.
Itulah sebabnya pasangan karakter meta ini disebut anchor, atau jangkar. Beberapa contoh:

456 cocok dengan 456, 456789, maupun 123456 karena ketiganya mengandung pola tersebut.
^456 cocok dengan 456, 456789, namun tidak cocok dengan 123456.
^456$ hanya cocok dengan 456, tidak dengan 456789 maupun 123456.
Pola seperti [0-9][0-9] dan pola-pola lain di contoh sebelumnya bersifat tidak terjangkar 
karena tidak diberi ^ maupun $. Jadi di mana pun pola tersebut ditemukan di 
dalam string—di awal, tengah, maupun ujung akhir—tetap akan cocok.
Sementara jika sebuah pola terjangkar, maka hanya cocok di awal atau di akhir atau awal
-dan-akhir, bergantung pada jenis jangkar yang diberikan pada pola.


"""