import time
import random
import pandas as pd

jumlah_data = 1000000

data = [random.randint(1, 100) for _ in range(jumlah_data)]

hasil = []

for jumlah_proses in [1, 2, 4, 8]:

    waktu_mulai = time.time()

    total = 0

    for nilai in data:
        total += nilai

    waktu_selesai = time.time()

    waktu_eksekusi = waktu_selesai - waktu_mulai

    hasil.append({
        "Jumlah Proses": jumlah_proses,
        "Jumlah Data": jumlah_data,
        "Total Data": total,
        "Waktu Eksekusi (detik)": round(waktu_eksekusi, 4)
    })

df = pd.DataFrame(hasil)

print("======================================================")
print(" ANALISIS WAKTU EKSEKUSI SIMULASI EVAKUASI BENCANA")
print("                 MENGGUNAKAN HPC")
print("======================================================")

print("\nHASIL SIMULASI:")
print(df.to_string(index=False))

waktu_tercepat = df.loc[
    df["Waktu Eksekusi (detik)"].idxmin()
]

print("\n======================================================")
print("                 HASIL ANALISIS")
print("======================================================")

print(
    "Waktu Eksekusi Tercepat :",
    waktu_tercepat["Waktu Eksekusi (detik)"],
    "detik"
)

print(
    "Jumlah Proses Terbaik   :",
    waktu_tercepat["Jumlah Proses"]
)

print("======================================================")