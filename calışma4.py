tuketim = float(input("harcanan su miktarı (m3) girin: "))
toplam_fiyat = 0
if tuketım <= 10:
    toplam_fiyat = tuketim * 30
elif tuketim <= 20:
    # ilk 10 m3 için 30 tl, kalanı için 45 tl
    toplam_fiyat = (10 * 30) + ((tuketim - 10) * 45)
else:
    # ilk 10m3 için 30tl kalanı için 45 tl
    toplam_fiyat = (10 * 30) + (10 * 45) + ((tuketim - 20)* 70)
    print(f"toplam su faturası: {toplam_fiyat: .2f} tl")
             
