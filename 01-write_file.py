import csv

# Oluşturulacak CSV dosyasının adı
csv_file_name = 'example.csv'

# Veri kümesi (örnek veri)
dataset = [
    ['name', 'surname', 'age'],
    ['Emily', 'Brown', 25],
    ['John', 'Smith', 30],
    ['Sarah', 'Wiliams', 22]
]

# CSV dosyasını oluşturur ve yazma modunda açar
with open(csv_file_name, 'w', newline='') as csv_file:
    # CSV dosyasını yazmak için writer nesnesini oluşturur
    csv_writer = csv.writer(csv_file)

    # Veri kümesindeki her satırı CSV dosyasına yazar
    for line in dataset:
        csv_writer.writerow(line)

print(f' file {csv_file_name} created')