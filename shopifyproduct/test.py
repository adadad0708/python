import re
import csv


def extract_BDt(input_file):
    file = open(input_file, 'r')
    new_file = open('BDtList.txt', 'w')
    for line in file:
        if "BDt;" in line:
            new_file.write(line)
    file.close()
    new_file.close()
    print('BDt is extracted')


def extract_name():
    file = open('BDtList.txt', 'r')
    with open('NameList.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerow(["Name"])
        for line in file:
            Name = re.findall(r"NAm(.+?);",line)
            writer.writerow(Name)
    print('Name is extracted')
    file.close()


if __name__ == '__main__':
    data_file = 'C:\\Python36\\TestCode\\ExtractName\\Test.tip'
    print('**********Start***********')
    extract_BDt(data_file)
    extract_name()
    print('**********Done***********')