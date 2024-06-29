import csv

csv_file_name = 'test.csv'

with open(csv_file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Header'ı atlar (varsayılan olarak ilk satır okunur)
    next(csv_reader, None)

    for line in csv_reader:
        # Her bir hücreyi integer'a çevirir
        data = [int(hucre) for hucre in line]

        sum_numbers = sum(data)
        product = 1
        for number in data:
            product *= number

        print("sum:", sum_numbers)
        print("product:", product)

"""
çıktı:
ilk satır: 36+20+5 Toplam: 61 36.20.5 Çarpım: 3600
ikinci satır 34+22+10 Toplam: 66 34,22,10 Çarpım: 7480
"""