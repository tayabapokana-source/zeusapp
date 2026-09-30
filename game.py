import pygame
import sys
import random

pygame.init()

# 1. Sesuaikan resolusi layar agar pas dengan aspek rasio gambar asli
LEBAR_LAYAR = 1000
TINGGI_LAYAR = 800
layar = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR))
pygame.display.set_caption("Gates of Olympus 1000 - Custom Developer Mode")

# 2. LOAD ASET GAMBAR ASLI (Pastikan file gambar ini sudah ada di foldermu)
try:
    img_background = pygame.image.load("bg_olympus.png")
    img_zeus = pygame.image.load("zeus_character.png")
    img_tombol_spin = pygame.image.load("tombol_spin.png")
    
    # Load gambar simbol-simbol asli
    img_mahkota = pygame.image.load("sym_mahkota.png")
    img_jam_pasir = pygame.image.load("sym_jampasir.png")
    img_cincin = pygame.image.load("sym_cincin.png")
except:
    print("Tips: Untuk hasil sama persis, siapkan file gambar .png asli di folder kodinganmu!")

# 3. SETTINGAN CHEAT: Matriks Grid 6x5 Pasti Menang
# Game asli menggunakan grid 6 kolom x 5 baris. Kita setting agar semuanya berisi Mahkota (Maksimal Win)
grid_pasti_menang = [
    ["👑", "👑", "👑", "👑", "👑", "👑"],
    ["👑", "👑", "👑", "👑", "👑", "👑"],
    ["👑", "👑", "👑", "👑", "👑", "👑"],
    ["👑", "👑", "👑", "👑", "👑", "👑"],
    ["👑", "👑", "👑", "👑", "👑", "👑"]
]

font_hud = pygame.font.SysFont("Arial", 24, bold=True)
saldo_fiktif = 100000
win_fiktif = 0

# ==============================================================================
# GAME LOOP
# ==============================================================================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Logika ketika tombol SPASI ditekan: Saldo berkurang, dan langsung set WIN meledak
                saldo_fiktif -= 2000
                win_fiktif = 2000 * 1000 # Menang Perkalian X1000 fiktif
                saldo_fiktif += win_fiktif

    # --- PROSES MENGGAMBAR VISUAL PERSIS SEPERTI DI GAMBAR ---
    # 1. Tempel Gambar Background Istana Langit
    try: layar.blit(img_background, (0, 0))
    except: layar.fill((25, 15, 40)) # Jika gambar belum ada, pakai warna dasar ungu

    # 2. Tempel Gambar Karakter Kakek Zeus di Sebelah Kanan
    try: layar.blit(img_zeus, (800, 200))
    except: pygame.draw.rect(layar, (0, 230, 255), (820, 250, 150, 300))

    # 3. Menggambar Grid 6x5 Mengikuti Isi Matriks Jalur Cheat
    for baris in range(5):
        for kolom in range(6):
            posisi_x = 180 + (kolom * 100) # Jarak antar kolom simbol
            posisi_y = 180 + (baris * 90)   # Jarak antar baris simbol
            
            # Tempel gambar simbol asli berdasarkan hasil acak/cheat
            try:
                layar.blit(img_mahkota, (posisi_x, posisi_y))
            except:
                # Jika file gambar belum ada, render teks emoji sementara di koordinat tersebut
                font_emoji = pygame.font.SysFont("Segoe UI Emoji", 45)
                txt_simbol = font_emoji.render(grid_pasti_menang[baris][kolom], True, (255,255,255))
                layar.blit(txt_simbol, (posisi_x, posisi_y))

    # 4. Gambar Panel Informasi Angka Kredit & Taruhan di bagian bawah
    txt_kredit = font_hud.render(f"KREDIT Rp {saldo_fiktif:,}.00", True, (255, 255, 255))
    txt_win = font_hud.render(f"KEMENANGAN: Rp {win_fiktif:,}.00", True, (80, 255, 100))
    layar.blit(txt_kredit, (200, 700))
    layar.blit(txt_win, (200, 660))

    # 5. Tempel Gambar Tombol Putar Melingkar di Pojok Kanan Bawah
    try: layar.blit(img_tombol_spin, (800, 650))
    except: pygame.draw.circle(layar, (255, 215, 0), (850, 700), 40)

    pygame.display.update()
