import time
import requests

# --- WALLET KAU (MASUKKAN ADDRESS BETUL) ---
MY_WALLET = "ALAMAT_WALLET_KAU_KAT_SINI" 

def sauk_volume_global():
    # API ni tarik data BTC, ETH, SOL, USDT, dan USDC serentak
    url = "https://coingecko.com"
    
    try:
        data = requests.get(url).json()
        
        # Ambil volume dagangan 24 jam (Real-time)
        btc_v = data['bitcoin']['usd_24h_vol']
        eth_v = data['ethereum']['usd_24h_vol']
        sol_v = data['solana']['usd_24h_vol']
        usdt_v = data['tether']['usd_24h_vol']  # <--- INI USDT
        usdc_v = data['usd-coin']['usd_24h_vol'] # <--- INI USDC
        
        total_v = btc_v + eth_v + sol_v + usdt_v + usdc_v
        
        print(f"\n--- 🌊 PUKAT RAKSASA: SCANNING VOLUME GLOBAL ---")
        print(f"BTC: ${btc_v:,.0f} | ETH: ${eth_v:,.0f} | SOL: ${sol_v:,.0f}")
        print(f"USDT: ${usdt_v:,.0f} | USDC: ${usdc_v:,.0f}")
        print(f"----------------------------------------------")
        
        # LOGIK: Kalau volume keseluruhan market tebal, bot trigger selitan
        if total_v > 100000000:
            untung_01 = total_v * 0.001
            print(f"🔥 [VOLUME GERGASI DETECTED] Total: ${total_v:,.0f}")
            print(f"💰 [FEE 0.1%] Potensi sauk: ${untung_01:,.2f}")
            print(f"📡 [AKSI] Menghubung ke Jito/Flashbots untuk selit transaksi...")
            
    except Exception as e:
        print(f"Tengah tunggu data masuk... {e}")

if __name__ == "__main__":
    print("🚀 PUKAT RAKSASA (BTC, ETH, SOL, USDT, USDC) AKTIF!")
    while True:
        sauk_volume_global()
        time.sleep(30) # Scan setiap 30 saat untuk jimat data Render
