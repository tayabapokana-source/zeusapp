import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Awal Jendela Web
st.set_page_config(page_title="Gates of Olympus 1000 - Web Edition", page_icon="🎰", layout="centered")

st.title("🎰 Zeus 1000 Simulator (Web Clone)")
st.write("Mode Developer: Di-setting Pasti Pecah Perkalian X1000!")

# ==============================================================================
# MENYUNTIKKAN GAME HTML5 & JAVASCRIPT KE DALAM STREAMLIT
# ==============================================================================
html5_game_code = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: #110924;
            color: white;
            font-family: 'Arial', sans-serif;
            text-align: center;
            margin: 0;
            padding: 10px;
        }
        .game-container {
            max-width: 500px;
            margin: auto;
            background: radial-gradient(circle, #251242 0%, #0f061d 100%);
            border: 4px solid #ffd700;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 0 30px #00e6ff;
        }
        .header-panel {
            display: flex;
            justify-content: space-between;
            font-weight: bold;
            color: #ffd700;
            font-size: 18px;
            margin-bottom: 15px;
        }
        .slot-machine {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
            background: rgba(0, 0, 0, 0.5);
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #572d8c;
        }
        .reel {
            width: 90px;
            height: 100px;
            background-color: #2e1c4e;
            border: 3px solid #00e6ff;
            border-radius: 10px;
            font-size: 55px;
            line-height: 100px;
            text-align: center;
            transition: all 0.1s ease;
        }
        .zeus-status {
            font-size: 20px;
            font-weight: bold;
            color: #00e6ff;
            height: 30px;
            margin: 15px 0;
            text-shadow: 0 0 10px #00e6ff;
        }
        .multiplier-badge {
            display: inline-block;
            background: linear-gradient(45deg, #ff007f, #7f00ff);
            color: white;
            padding: 10px 20px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 20px;
            border: 2px solid #ffd700;
            box-shadow: 0 0 15px #ff007f;
            display: none;
            animation: pulse 1s infinite;
        }
        .spin-button {
            background: linear-gradient(180deg, #ffd700 0%, #b8860b 100%);
            color: black;
            border: none;
            padding: 15px 40px;
            font-size: 22px;
            font-weight: bold;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            width: 100%;
        }
        .spin-button:active {
            transform: scale(0.98);
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>

<div class="game-container">
    <div class="header-panel">
        <div id="saldo-display">SALDO: Pk 50,000</div>
        <div id="win-display" style="color: #50ff64;">WIN: Pk 0</div>
    </div>

    <!-- Tampilan Visual Gulungan Game -->
    <div class="slot-machine">
        <div id="reel1" class="reel">👑</div>
        <div id="reel2" class="reel">👑</div>
        <div id="reel3" class="reel">👑</div>
    </div>

    <div id="zeus-text" class="zeus-status">⚡ Kakek Zeus Bersiap Menyambar... ⚡</div>
    
    <div id="multiplier" class="multiplier-badge">⚡ X1000 ⚡</div>
    
    <br><br>
    <button class="spin-button" onclick="startSpin()">⚡ SPIN (CHEAT MODE) ⚡</button>
</div>

<script>
    let saldo = 50000;
    const simbols = ["👑", "⏳", "💍", "🔮"];

    function startSpin() {
        if (saldo < 1000) {
            alert("Saldo Demo Habis!");
            return;
        }

        saldo -= 1000;
        document.getElementById("saldo-display").innerText = "SALDO: Pk " + saldo.toLocaleString();
        document.getElementById("multiplier").style.display = "none";
        document.getElementById("win-display").innerText = "WIN: Pk 0";
        document.getElementById("zeus-text").innerText = "⚡ Gulungan Berputar... ⚡";

        // Efek Animasi Acak Cepat (Simulasi Spin Nyata)
        let count = 0;
        let interval = setInterval(() => {
            document.getElementById("reel1").innerText = simbols[Math.floor(Math.random() * simbols.length)];
            document.getElementById("reel2").innerText = simbols[Math.floor(Math.random() * simbols.length)];
            document.getElementById("reel3").innerText = simbols[Math.floor(Math.random() * simbols.length)];
            count++;
            
            if (count > 10) {
                clearInterval(interval);
                triggerJackpot(); // Jalankan settingan mutlak menang
            }
        }, 80);
    }

    function triggerJackpot() {
        // KUNCI SETTINGAN: Memaksa gambar selalu Mahkota Emas Kembar 3 (Simbol Tertinggi)
        document.getElementById("reel1").innerText = "👑";
        document.getElementById("reel2").innerText = "👑";
        document.getElementById("reel3").innerText = "👑";

        // Memunculkan sambaran petir pengali X1000 mutlak
        document.getElementById("zeus-text").innerText = "⚡ PETIR SENSASIONAL X1000 TURUN! ⚡";
        document.getElementById("multiplier").style.display = "inline-block";

        // Hitung skor fiktif kemenangan besar
        let menang = 5000 * 1000; 
        saldo += menang;

        document.getElementById("saldo-display").innerText = "SALDO: Pk " + saldo.toLocaleString();
        document.getElementById("win-display").innerText = "WIN: Pk " + menang.toLocaleString();
    }
</script>

</body>
</html>
"""

# Menyematkan (Embed) komponen HTML5 interaktif ke halaman Streamlit
# Menggunakan ukuran tinggi 480 piksel agar pas di layar PC dan HP pacar/temanmu
components.html(html5_game_code, height=480)

st.write("---")
st.caption("Klik tombol SPIN di atas, sistem Javascript akan mensimulasikan putaran acak lalu menguncinya ke kemenangan mutlak X1000.")
