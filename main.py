"""
Ini adalah demo
"""


# percabangan
jumlah_botol_susu = 173
jumlah_telur = 1000
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} telur")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, ternyata cukup")

    if jumlah_telur == 0:
        print("budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
     print("budi tidak jadi membeli")

 print("budi pulang kerumah")
print("budi menyampaikan ke ibunya")