import serial
import csv

serial_port = serial.Serial('COMx', baudrate=9600)
file_name = 'received_data.csv'

with open(file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    try:
        while True:
            # Seri porttan bir satır okur
            line = serial_port.readline().decode('utf-8').strip()

            # Satırı CSV dosyasına yazar
            csv_writer.writerow(line.split(','))
            print(line)

            # Verilerin anında dosyaya yazılmasını sağlar
            csv_file.flush()
    except KeyboardInterrupt:
        print("Reading stopped by user.")
    finally:
        serial_port.close()