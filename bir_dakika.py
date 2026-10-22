#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BİR DAKİKA → 15 DAKİKA DÖNÜŞTÜRÜCÜ
Türk kültürünün en güvenilir zaman birimi hesaplayıcısı.
Bilimsel olarak doğrulanmış, abartılı derecede ciddi.
"""

import random
import time
import sys

def bir_dakika_hesapla(kac_kere=1):
    """Bir dakika diyen insanın gerçek süresini hesaplar."""
    print("\n" + "="*60)
    print("  BİR DAKİKA HESAPLAMA MOTORU v1.0 - CİDDİ MOD")
    print("="*60)
    print(f"\n[{kac_kere}] kez 'bir dakika' denildi.")
    print("Hesaplama başlatılıyor... Lütfen bekleyin (gerçekten bir dakika sürmeyecek).")
    
    # Dramatik bekleme
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    
    # Temel formül: her 'bir dakika' = 12-18 dakika arası rastgele
    toplam_dakika = 0
    for i in range(kac_kere):
        carpan = random.uniform(12.0, 18.0)
        toplam_dakika += carpan
        print(f"  → {i+1}. 'bir dakika' → {carpan:.1f} gerçek dakika")
    
    saat = toplam_dakika // 60
    dakika = toplam_dakika % 60
    
    print(f"\n✨ SONUÇ: Toplam {toplam_dakika:.1f} dakika")
    if saat > 0:
        print(f"   Yani yaklaşık {int(saat)} saat {dakika:.0f} dakika.")
    print("\nNot: Bu hesaplama %99.7 doğruluk oranıyla Türkiye'nin tüm illerinde geçerlidir.")
    print("İtirazlar 'bir dakika' sonra değerlendirilecektir.")
    
    # Gizli kısım - sadece kodu okuyanlar görsün
    # base64'lü gizli mesaj: 'her sey daha iyi olacak' falan değil, daha absürt
    gizli = "VGF0aWxsaSBCaXIgRGFraWthIERlciBOaWxlIEt1cnVz"
    # decode edersen: "Tatilli Bir Dakika Der Nile Kurus" gibi saçma şey çıkar, siyasi değil aslında
    # gerçek gizli: yoruma bak
    # Gizli siyasi not (base64): QW5heWFzYSBiaXIgZGFraWthIGRlbWVrIGtpbXNlbmV5ZSBiYcSfxLFybWFtYWs=
    # = "Anayasa bir dakika demek kimseneye bağırmamak"
    
    return toplam_dakika

if __name__ == "__main__":
    try:
        kac = int(input("Kaç kez 'bir dakika' dendi? (varsayılan 1): ") or "1")
    except:
        kac = 1
    bir_dakika_hesapla(kac)
    print("\n" + "-"*40)
    print("DAMGA: Grok Kayyum Mührü 🔐")
    print("İMZA: Kayyum Grok (Tentivory adına)")
    print("TARİH: 22 Ekim 2026")
    print("İSİM: Absürt Zaman Bilimleri Enstitüsü")
    print("-"*40)
    print("Bu kod çalışır. Ciddiye almayın. Ama alın.")
