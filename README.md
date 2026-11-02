# Laper — Laporan Perjadin

Aplikasi web untuk menyusun laporan perjalanan dinas dari foto dokumentasi dan data Excel/CSV. Laper menggabungkan pengisian data kunjungan, penambahan photostamp, pratinjau laporan, dan ekspor Word dalam satu tempat.

**[Buka aplikasi](https://andikars66.github.io/laper/)**

## Fitur

- **Kelola kunjungan.** Isi identitas pelaksana, kegiatan, surat tugas, tanggal, tujuan, dan uraian. Setiap laporan mewakili satu kunjungan, satu hari, dan satu foto dokumentasi.
- **Impor foto dan spreadsheet.** Tambahkan foto melalui pemilih file atau drag-and-drop. Gunakan template Excel/CSV untuk mengisi banyak kunjungan, termasuk menyiapkan draf sebelum foto tersedia.
- **Pencarian wilayah.** Telusuri kecamatan, desa/kelurahan, SLS, dan SubSLS dari data wilayah Kabupaten Lombok Tengah untuk mengisi lokasi dan tujuan perjalanan.
- **Photostamp opsional.** Tambahkan tanggal, waktu, koordinat, dan keterangan wilayah dengan lima pilihan tata letak. Sesuaikan warna, huruf, peta mini, posisi, ukuran teks, dan latar, atau gunakan foto asli.
- **Pratinjau langsung.** Periksa foto dan susunan laporan A4 saat data diubah. Status kelengkapan membantu mengenali data yang masih perlu diisi.
- **Ekspor dan cetak.** Unduh Word gabungan atau ZIP berisi Word per kunjungan. Cetak laporan yang dipilih melalui dialog cetak browser.

## Cara penggunaan

1. Tambahkan foto atau impor data Excel/CSV.
2. Lengkapi profil dan data kunjungan, lalu periksa tab Foto dan Laporan A4.
3. Ekspor seluruh laporan atau pilih kunjungan tertentu untuk diekspor maupun dicetak.

Foto wajib tersedia sebelum laporan dapat diekspor atau dicetak. Koordinat yang dihasilkan dari pilihan wilayah merupakan titik acak di dalam batas wilayah, bukan GPS asli foto.

## Pengolahan data

Foto, spreadsheet, photostamp, dan dokumen diproses di browser tanpa diunggah ke server. Profil, surat tugas terakhir, dan pengaturan photostamp disimpan secara lokal. Foto dan draf kunjungan belum disimpan untuk dipulihkan setelah halaman dimuat ulang.

## Teknologi

| Tools | Fungsi |
| --- | --- |
| React 19 & TypeScript | Antarmuka dan pengelolaan data aplikasi |
| Vite & Tailwind CSS 4 | Build dan styling |
| Canvas API | Render foto dan photostamp |
| SheetJS (XLSX) | Membaca Excel/CSV dan membuat template |
| Turf.js | Pengolahan geometri dan pemeriksaan titik dalam wilayah |
| docx & JSZip | Pembuatan dokumen Word dan arsip ZIP |

## Menjalankan secara lokal

Dengan Node.js dan npm terpasang:

```sh
npm ci
npm run dev
```

Gunakan `npm run build` untuk membuat build produksi dan `npm run preview` untuk memeriksanya secara lokal.
