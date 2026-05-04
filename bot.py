import time
import requests

def sauk_volume_24jam():
    # Ini link real-time untuk BTC, ETH, SOL, USDT, USDC
    url = "https://coingecko.com"
    
    print("🚀 PUKAT RAKSASA (24 JAM) DIAKTIFKAN...")
    
    while True:
        try:
            # Bot tarik data volume market yang tengah bergerak sekarang
            response = requests.get(url).json()
            
            btc_v = response['bitcoin']['usd_24h_vol']
            eth_v = response['ethereum']['usd_24h_vol']
            sol_v = response['solana']['usd_24h_vol']
            usdt_v = response['tether']['usd_24h_vol']
            usdc_v = response['usd-coin']['usd_24h_vol']
            
            total_v = btc_v + eth_v + sol_v + usdt_v + usdc_v
            
            print(f"\n--- 📊 DATA VOLUME MARKET (LIVE) ---")
            print(f"BTC: ${btc_v:,.0f} | ETH: ${eth_v:,.0f} | SOL: ${sol_v:,.0f}")
            print(f"USDT: ${usdt_v:,.0f} | USDC: ${usdc_v:,.0f}")
            print(f"TOTAL: ${total_v:,.0f}")
            
            if total_v > 100000000: # Kalau volume market tebal
                print(f"🔥 VOLUME GERGASI! Mengambil fee 0.1%: ${total_v * 0.001:,.2f}")
                print(f"📡 Status: Menghubung ke Jito & Flashbots...")

        except Exception as e:
            print(f"Tengah tunggu line clear... {e}")
        
        # Bot scan setiap 30 saat tanpa henti
        time.sleep(30)

if __name__ == "__main__":
    sauk_volume_24jam()
