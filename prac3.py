import csv
# print(dir(csv))
with open('Book1.csv', 'r') as csv_obj:
    #    csv_reader = csv.reader(csv_obj)
    #    for ln in csv_reader:
    #        print(ln)

    csv_reader = csv.DictReader(csv_obj)
    with open('Book2.csv', 'w') as csv_write_obj:
        fieldnames = ['Emp ID', 'EName', 'EMail']
        csv_writer = csv.DictWriter(csv_write_obj, fieldnames=fieldnames, delimiter = ',')
        csv_writer.writeheader()
        for ln in csv_reader:
            csv_writer.writerow(ln)

        # for ln in csv_reader:
        #    print("{} {} {}".format(ln['Emp ID'], ln['EName'], ln['EMail']))
