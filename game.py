import random
import time
import streamlit as st

# 1. Konfigurasi Awal Halaman Website
st.set_page_config(page_title="Gates of Olympus 1000 - Cheat Mode", page_icon="⚡", layout="centered")

# Menggunakan CSS kustom untuk mengubah warna latar belakang menjadi ungu kegelapan khas Zeus
st.markdown("""
    <style>
    .stApp {
        background-color: #140F23;
        color: #FFFFFF;
    }
    div.stButton > button:first-child {
        background-color: #00E6FF;
        color: #000000;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Judul Utama Website
st.title("🎰 Gates of Olympus 1000 ⚡")
st.subheader("Mode Cheat Developer: 100% Pasti Menang")
st.write("---")

# Inisialisasi data saldo awal menggunakan Session State agar tidak ter-reset saat tombol diklik
if "saldo" not in st.session_state:
    st.session_state.saldo = 50000

# 3. Menampilkan Papan Informasi Saldo Fiktif
st.metric(label="💰 SALDO DEMO CHEAT", value=f"Pk {st.session_state.saldo:,}")

# 4. Tombol Utama Pemutar Slot (Spin)
if st.button("⚡ KETIK UNTUK SAMBARAN PETIR ZEUS! ⚡"):
    st.session_state.saldo -= 1000 # Potong biaya taruhan fiktif
    
    # KUNCI LOGIKA CHEAT: Memaksa simbol selalu kembar tiga (Pasti Jackpot)
    simbol_terpilih = random.choice(["💍", "⏳", "👑"])
    
    # Menentukan skor dasar fiktif berdasarkan kelangkaan item
    if simbol_terpilih == "👑":
        skor_dasar = 5000
        nama_item = "MAHKOTA EMAS"
    elif simbol_terpilih == "⏳":
        skor_dasar = 3000
        nama_item = "JAM PASIR"
    else:
        skor_dasar = 1500
        nama_item = "CINCIN DEWA"

    # Membuat efek loading putaran slot seolah-olah berputar asli
    with st.spinner("Mengguncang gulungan Olympus..."):
        time.sleep(1)

    # Menampilkan hasil 3 gulungan kotak dengan simbol kembar secara visual di web
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.info(f"### {simbol_terpilih}")
    with kolom2:
        st.info(f"### {simbol_terpilih}")
    with kolom3:
        st.info(f"### {simbol_terpilih}")

    # KUNCI LOGIKA CHEAT 2: Memaksa Kakek Zeus mengeluarkan Petir Perkalian X1000 Mutlak!
    PERKALIAN_X = 1000
    total_kemenangan = skor_dasar * PERKALIAN_X
    st.session_state.saldo += total_kemenangan

    # Memicu efek animasi balon berhamburan di layar web karena menang besar!
    st.balloons()

    # Menampilkan pesan kemenangan besar dengan teks menyala
    st.success(f"### ⚡ KAKEK ZEUS ANGKAT TANGAN! PETIR X{PERKALIAN_X} PECAH! ⚡")
    st.write(f"Kombinasi 3 **{nama_item}** dikalikan dengan **X{PERKALIAN_X}**!")
    st.write(f"**Total Kemenangan:** +Pk {total_kemenangan:,} dimasukkan ke saldo fiktif!")
    
    # Tombol re-run otomatis untuk memperbarui nilai saldo di bagian atas layar
    st.rerun()

else:
    # Tampilan awal sebelum tombol diklik pertama kali
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1: st.info("### ❓")
    with kolom2: st.info("### ❓")
    with kolom3: st.info("### ❓")
    st.info("Silakan klik tombol biru di atas untuk memicu sambaran petir pengali X1000!")

st.write("---")
st.caption("Mode Simulator Offline & Web ini dibuat murni untuk hiburan koding sendiri di VS Code.")
