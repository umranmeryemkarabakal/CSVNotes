import pandas as pd

def write_lists_to_csv(list1, list2, list3, csv_filename):
    data_table = list(zip(list1, list2, list3))

    df = pd.DataFrame(data_table, columns=["list1", "list2", "list3"]) # veri çerçevesini oluştur

    df.to_csv(csv_filename, index=False)

list1 = ["A1", "A2", "A3"]
list2 = ["B1", "B2", "B3"]
list3 = ["C1", "C2", "C3"]


# Her bir listeyi ayrı bir CSV dosyasına yazdır
write_lists_to_csv(list1, list2, list3, "data1.csv")

