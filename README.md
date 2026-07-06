# Antrian Rumah Sakit — Priority Queue System

Aplikasi desktop manajemen antrian pasien rumah sakit berbasis Python Tkinter dengan sistem prioritas menggunakan **heap queue (heapq)**.

## Fitur

- **Tambah Pasien** — Input nama dan tingkat prioritas (Kritis, Serius, Ringan, Umum)
- **Prioritas Otomatis** — Pasien dengan prioritas lebih tinggi (Kritis) dipanggil lebih dulu
- **Cari Pasien** — Pencarian berdasarkan nama dalam antrian
- **Panggil Pasien** — Memanggil pasien berikutnya berdasarkan prioritas
- **Cegah Duplikat** — Konfirmasi jika nama dan prioritas sudah ada, tawarkan ubah prioritas
- **Kode Warna** — Setiap prioritas memiliki warna berbeda di daftar antrian

## Prioritas & Warna

| Prioritas | Nilai | Warna |
|---|---|---|
| Kritis | 1 | Merah (#CD0027) |
| Serius | 2 | Kuning (#FFE001) |
| Ringan | 3 | Hijau (#89B524) |
| Umum | 4 | Putih (#FFFFFF) |

## Cara Menjalankan

```bash
python "hospital queue.py"
```

## Teknologi

- **Python** — tkinter, heapq
