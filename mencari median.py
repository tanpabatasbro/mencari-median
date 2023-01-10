import statistics

inputan = input("Masukkan Deret Angka (Pisahkan Dengan Tanda Koma (,)) :")
data = []

for bilangan in inputan.split(','):
    data.append(int(bilangan))
    
rerata = statistics.median(data)
print(f"Data -> {data}")
print(f"Median -> {rerata}")