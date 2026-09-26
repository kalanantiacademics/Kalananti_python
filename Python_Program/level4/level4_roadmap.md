# 🗺️ Roadmap Level 4 — Python OOP (Planet Visionara)
> Per-sesi: tujuan, bukti paham, dan dependency konsep sebelumnya

---

## 🧱 UNIT 1 — OOP Foundations (M1–M4)
> Fondasi dari nol. Tidak pakai konsep dari meeting sebelumnya (kecuali bekal Level 3).

---

### 🔵 Meeting 1 — Class & Object

**Goal:** Siswa paham bahwa **class = cetakan, object = benda yang jadi.**

**Bekal yang dipakai:** —  
*(ini sesi pertama, cukup ingat syntax Python dasar dari L3)*

**Konsep yang diajarkan:**
- Apa itu class (`class Hewan:`)
- Cara bikin object dari class (`kuda = Hewan()`)
- Bedanya class vs object

**Bukti Paham — Project Mini:**
> 🐾 **Kebun Binatang** — Bikin 2 class (`Hewan`, `Kandang`) dan buat 4 object berbeda, print semuanya.

```python
class Hewan:
    pass

singa = Hewan()
harimau = Hewan()
print(singa)
print(harimau)
```

**Tanda siswa BELUM paham:** Nulis `Hewan` tanpa `()` saat bikin object, atau bingung kenapa dua object punya "alamat" berbeda.

---

### 🔵 Meeting 2 — Attributes & Methods

**Goal:** Siswa paham bahwa **object punya data (attribute) dan bisa melakukan sesuatu (method).**

**Bekal yang dipakai:**
- ✅ M1: Bisa bikin class dan object

**Konsep yang diajarkan:**
- Attribute: `hewan.nama = "Singa"`
- Method: `def suara(self):`
- `self` = "diri sendiri" si object
- Dot notation: `hewan.suara()`

**Bukti Paham — Project Mini:**
> 🐣 **Tamagotchi** — Object dengan attribute `nama`, `lapar`. Method `makan()` yang ngurangin nilai lapar dan print statusnya.

```python
class Tamagotchi:
    def makan(self):
        self.lapar -= 2
        print(f"{self.nama} makan! Lapar: {self.lapar}")

pichu = Tamagotchi()
pichu.nama = "Pichu"
pichu.lapar = 10
pichu.makan()
pichu.makan()
```

**Tanda siswa BELUM paham:** Lupa nulis `self` di parameter method, atau panggil method pakai `()` tapi di `command=` tidak pakai `()` → ini bedain nanti di M4.

---

### 🔵 Meeting 3 — Constructor `__init__`

**Goal:** Siswa paham bahwa **data awal object bisa langsung diisi saat object dibuat**, bukan diisi manual satu-satu.

**Bekal yang dipakai:**
- ✅ M1: Class & object
- ✅ M2: Attribute, method, self

**Konsep yang diajarkan:**
- `def __init__(self, nama, saldo):`
- `self.nama = nama` — mindahin argument ke attribute
- Default value
- List of objects (`[AkunBank("Andi", 500), AkunBank("Budi", 300)]`)

**Bukti Paham — Project Mini:**
> 🏦 **Sistem Bank Sederhana** — Bikin class `AkunBank` dengan constructor, method `setor()`, dan simpan 2–3 object di dalam list.

```python
class AkunBank:
    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self.saldo = saldo_awal

    def setor(self, jumlah):
        self.saldo += jumlah

akun1 = AkunBank("Andi", 500000)
akun2 = AkunBank("Budi", 300000)
akun1.setor(200000)
print(akun1.saldo)  # 700000
```

**Tanda siswa BELUM paham:** Nulis `_init_` (satu underscore), atau tidak paham kenapa `self.nama = nama` perlu ada dua nama.

---

### 🔵 Meeting 4 — OOP in GUI

**Goal:** Siswa bisa **gabungin OOP (M1–M3) dengan CustomTkinter (Level 3)** — bikin GUI dalam bentuk class.

**Bekal yang dipakai:**
- ✅ M1: Class & object
- ✅ M2: Method & self
- ✅ M3: Constructor `__init__`
- ✅ Level 3: `ctk.CTk`, Label, Button, Entry, `pack()`/`grid()`, event `command`

**Konsep yang diajarkan:**
- `class App(ctk.CTk):` — class yang "mewarisi" window
- `super().__init__()` — inisialisasi window-nya dulu
- Widget jadi attribute: `self.label = ctk.CTkLabel(...)`
- Button command ke method: `command=self.klik` (tanpa kurung!)

**Bukti Paham — Project Mini:**
> 🖱️ **Counter App** atau **To-Do List** berbasis class — Window OOP, tombol + method, state berubah saat klik.

```python
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.label = ctk.CTkLabel(self, text="0")
        self.label.pack()
        ctk.CTkButton(self, text="+", command=self.tambah).pack()

    def tambah(self):
        self.count += 1
        self.label.configure(text=str(self.count))
```

**Tanda siswa BELUM paham:** Nulis `command=self.tambah()` (ada kurung — langsung jalan saat startup), atau widget tidak disimpan sebagai `self` sehingga method lain tidak bisa aksesnya.

> ⚠️ **INI SESI PALING KRITIS** — M4 adalah titik koneksi OOP + GUI. Kalau siswa bingung di sini, sesi 5–8 akan berat.

---

## ⚙️ UNIT 2 — Advanced Logic (M5–M8)
> Setiap sesi **wajib pakai konsep dari sesi sebelumnya**. Dependency makin tebal.

---

### 🟠 Meeting 5 — Inheritance (Pewarisan)

**Goal:** Siswa paham bahwa **class bisa "nurunin" kemampuan ke class lain** tanpa nulis ulang.

**Bekal yang dipakai:**
- ✅ M1–M3: Class, attribute, method, constructor
- ✅ M4: `App(ctk.CTk)` — ini sudah pakai inheritance! Tinggal formalisasi konsepnya.

**Konsep yang diajarkan:**
- `class Minuman(Menu):` — child class
- Warisan otomatis: method parent bisa langsung dipanggil dari child
- `super().__init__(nama, harga)` — panggil constructor parent dari child
- Override: child nulis ulang method yang sama dengan behavior beda

**Bukti Paham — Project Mini:**
> 🎵 **Hierarki Alat Musik** — Class `AlatMusik` sebagai parent, `Gitar` dan `Drum` sebagai child. Tiap child punya method `suara()` yang berbeda (override).

```python
class AlatMusik:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("...")

class Gitar(AlatMusik):
    def suara(self):
        print(f"{self.nama}: Jreng jreng!")

class Drum(AlatMusik):
    def suara(self):
        print(f"{self.nama}: Dug dug!")
```

**Tanda siswa BELUM paham:** Bingung kenapa perlu `super().__init__()` di child, atau mengira inheritance = copy-paste kode.

---

### 🟠 Meeting 6 — Multi-Window Logic

**Goal:** Siswa bisa **navigasi antar halaman dalam satu aplikasi** tanpa bikin window baru.

**Bekal yang dipakai:**
- ✅ M4: GUI berbasis class, `self`, widget sebagai attribute
- ✅ M5: Inheritance — `CTkFrame` dan `CTkToplevel` adalah child dari class Tkinter

**Konsep yang diajarkan:**
- Aturan 1 root (`ctk.CTk` cukup satu)
- Frame switching: `frame.pack_forget()` → `frame_lain.pack()`
- `CTkToplevel` untuk pop-up/dialog
- Guard: `if self.popup is None or not self.popup.winfo_exists():`

**Bukti Paham — Project Mini:**
> 🔐 **Login → Dashboard** — Halaman login dengan form, tombol Login yang ganti ke halaman dashboard. Tombol Logout balikin ke login. Plus 1 pop-up konfirmasi.

```python
def ke_dashboard(self):
    self.frame_login.pack_forget()
    self.frame_dashboard.pack(fill="both", expand=True)

def ke_login(self):
    self.frame_dashboard.pack_forget()
    self.frame_login.pack(fill="both", expand=True)
```

**Tanda siswa BELUM paham:** Bikin `ctk.CTk()` lagi untuk halaman baru (root ganda), atau pop-up bisa dibuka tak terbatas.

---

### 🟠 Meeting 7 — Class Interaction (Model–View)

**Goal:** Siswa paham bahwa **data/logika (model) harus dipisah dari GUI (view)** dan keduanya berkomunikasi.

**Bekal yang dipakai:**
- ✅ M1–M3: Class model (AkunBank, dsb.)
- ✅ M4: GUI class
- ✅ M6: Navigasi multi-window
- **PERTAMA KALI** dua class bekerja sama dalam satu app

**Konsep yang diajarkan:**
- Composition: `self.akun = AkunBank()` — App *punya* Akun
- Event flow: `klik tombol → method GUI → method model → update tampilan`
- State ownership: data tinggal di model, bukan di widget

**Bukti Paham — Project Mini:**
> 🏧 **ATM App** atau **Voting App** — Ada class `AkunBank`/`Kandidat` (model) dan class `ATMApp`/`VotingApp` (view). Tombol di GUI memanggil method model, hasilnya tampil di Label.

```python
# Model
class AkunBank:
    def __init__(self):
        self.saldo = 0
    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah

# View (GUI)
class ATMApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.akun = AkunBank()  # composition!

    def lakukan_setor(self):
        self.akun.setor(int(self.entry.get()))
        self.label_saldo.configure(text=str(self.akun.saldo))
```

**Tanda siswa BELUM paham:** Nyimpan saldo di variable GUI, bukan di object model. Atau nulis `self.sistem = SistemBuku` tanpa kurung (simpan class, bukan instance).

---

### 🟠 Meeting 8 — Modular Coding

**Goal:** Siswa bisa **pecah satu file besar jadi 3 file terpisah** (`model.py`, `view.py`, `main.py`) dan jalankan dari `main.py`.

**Bekal yang dipakai:**
- ✅ M7: Model dan View sudah terpisah *secara logika* — sekarang pisah *secara file*
- ✅ Semua konsep M1–M7 digabung dalam satu arsitektur

**Konsep yang diajarkan:**
- `from model import AkunBank`
- Dependency direction: `model` tidak tahu `view`, `view` boleh pakai `model`, `main` rakit semuanya
- Circular import (bahayanya)
- `if __name__ == '__main__':` sebagai entry point

**Bukti Paham — Project Mini:**
> 📁 **Aplikasi 3-file** — Siswa memecah project ATM/Voting dari M7 menjadi 3 file terpisah. Jalankan hanya `main.py`.

```
📁 project/
├── model.py    ← class AkunBank
├── view.py     ← class ATMApp
└── main.py     ← import + jalankan app
```

**Tanda siswa BELUM paham:** `ModuleNotFoundError` karena salah nama file atau folder, atau bikin circular import (model import view).

---

## 🏗️ UNIT 3 — Final Project (M9–M12)

| Meeting | Fokus | Deliverable |
|---------|-------|-------------|
| **M9** | Plan — Problem, user, 3 MVP, class diagram | Blueprint disetujui guru |
| **M10** | Build — Bikin class model + GUI, hubungkan 1 flow end-to-end | Window jalan + 1 tombol bekerja |
| **M11** | Test — QA test cases, debugging, polish UI, siap presentasi | App presentation-ready + PPT 5–7 slide |
| **M12** | Showcase — Demo + jelaskan class structure, Q&A | Presentasi live / backup demo |

---

## 🔗 Peta Dependency Antar Sesi

```
M1 ──────────────────────────────────────────────────────────┐
      M2 (pakai M1) ──────────────────────────────────────┐  │
            M3 (pakai M1+M2) ──────────────────────────┐  │  │
                  M4 (pakai M1+M2+M3+Level3 GUI) ────┐  │  │  │
                        M5 (pakai M1–M3, hook M4) ─┐ │  │  │  │
                              M6 (pakai M4+M5) ──┐ │ │  │  │  │
                                    M7 (pakai SEMUA M1–M6) ─┐
                                          M8 (rakit M1–M7 jadi 3 file)
                                                   ↓
                                            M9–M12: FINAL PROJECT
```

### Sesi mana yang paling "bergantung ke belakang"?

| Sesi | Wajib paham dulu | Resiko kalau skip |
|------|-----------------|-------------------|
| M4 | M1+M2+M3+L3 GUI | Tidak bisa bikin GUI OOP sama sekali |
| M7 | M1–M6 semua | Tidak paham model-view, final project berantakan |
| M8 | M7 | Tidak bisa modularisasi → final project jadi 1 file 500 baris |

---

## 🎯 Summary: "Anak ini udah paham belum?"

| Sesi | Cek 1 kalimat ini |
|------|------------------|
| M1 | "Bikin 2 object berbeda dari 1 class" ✓ |
| M2 | "Panggil method yang ubah attribute, pakai dot notation" ✓ |
| M3 | "Bikin 3 object dengan data awal berbeda pakai constructor" ✓ |
| M4 | "Bikin window OOP, widget sebagai self, button ke method" ✓ |
| M5 | "Child class pakai method parent + override 1 method" ✓ |
| M6 | "Pindah antara 2 halaman tanpa bikin root baru" ✓ |
| M7 | "Tombol GUI → method model → state berubah → tampilan update" ✓ |
| M8 | "Jalankan main.py yang import dari model.py dan view.py" ✓ |
