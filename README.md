# Supernova Love - IVE & David Guetta Lyrics Print

Proyek ini adalah skrip Python sederhana yang menampilkan lirik lagu "Supernova Love" oleh IVE & David Guetta dengan efek animasi *typewriter* (mengetik teks satu per satu). Skrip ini juga menggunakan pewarnaan ANSI pada terminal untuk tampilan visual yang lebih estetik (warna ungu).

## 📌 Fitur Utama
- **Animasi Ketik (Typewriter Effect):** Lirik dicetak karakter demi karakter.
- **Kecepatan & Jeda Dinamis:** Kecepatan mengetik dan jeda antar-baris bervariasi mengikuti simulasi tempo lagu.
- **Warna Teks Kustom:** Menggunakan kode ANSI escape untuk mengubah warna lirik di terminal menjadi *Magenta / Ungu*.
- **Penanganan Interupsi Aman:** Menangani terminasi manual (Ctrl+C) secara mulus tanpa menampilkan pesan *error traceback* panjang.

## 🛠 Persyaratan Sistem (Prerequisite)
Pastikan Anda memiliki **Python 3.x** terinstal pada perangkat Anda. Library yang digunakan (`sys` dan `time`) adalah library bawaan standar Python, sehingga tidak perlu menginstal library eksternal berbayar atau tambahan apa pun.

## 🚀 Cara Menjalankan
Buka terminal dan arahkan *path* ke dalam folder proyek ini yang berisi file `lyrics.py`. Jalankan command berikut:

```bash
python lyrics.py
```

*Jika Anda ingin menghentikan script yang sedang berjalan, Anda dapat menekan `CTRL + C` di keyboard, dan animasi lirik akan dihentikan dengan aman.*

## 🔄 Alur Kerja Program (Mermaid Flowchart)

Berikut adalah ringkasan visual berupa diagram alur (flowchart) proses eksekusi kode `lyrics.py`:

```mermaid
graph TD
    A([Mulai Eksekusi]) --> B[Impor modul sys & time]
    B --> C{Pengecekan __name__ == '__main__'}
    C -- Ya --> D[Panggil fungsi cetak_lirik()]
    
    subgraph Proses Fungsi cetak_lirik()
        D --> E[Inisialisasi kode warna ANSI Ungu & List Lirik]
        E --> F[Print Header Lagu]
        F --> G[Tidur / Jeda 1 detik]
        G --> H{Apakah masih ada sisa lirik?}
        
        H -- Ya (Loop Baris) --> I[Ambil: teks, kecepatan_ketik, jeda_baris]
        I --> J{Sisa Karakter di baris ini?}
        
        J -- Ya (Loop Karakter) --> K[Print 1 karakter tanpa newline]
        K --> L[Flush Output Buffer stdout]
        L --> M[Jeda selama durasi kecepatan_ketik]
        M --> J
        
        J -- Tidak (Selesai Baris) --> N[Print newline]
        N --> O[Jeda selama durasi jeda_baris]
        O --> H
        
        H -- Tidak (Lirik Habis) --> P[Print Footer Tycami Tech & Reset Warna]
    end
    
    P --> Q([Program Selesai Eksekusi])
    
    subgraph Exception Handling
        R((KeyboardInterrupt Ctrl+C)) -.-> S[Catch Exception]
        S --> T[Print 'Paused.' dan matikan pewarnaan]
        T --> Q
    end
```

## 📜 Struktur Data Kode
Program ini mengatur lirik dan jedanya menggunakan kumpulan `tuple` dasar di dalam variabel `list`. 
Format strukturnya adalah sebagai berikut:
`("Rentetan Teks Lirik", delay_per_karakter_dalam_detik, delay_setelah_baris_selesai_dalam_detik)`

Contoh di kode: 
`("Never let me go", 0.15, 0.1)`

---
**Tycami Tech**
