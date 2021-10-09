from os.path import isfile, join
from os import listdir
import tabula
import os

# path = '/Users/apple/Desktop/django/final/final1/final/runs/detect/exp5/labels'
# pdf_path = '/Users/apple/Desktop/django/final/final1/final/media/pdfs'

# os.chdir(path)

# read txt file


def getNo(files):
    print(files)
    x = files.split("e")
    no = x[1].split(".")
    print(no[0])
    a = int(no[0])
    return a


# onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
# print(onlyfiles)
# for file in onlyfiles:
#     no = getNo(file)
#     print("\n"+no)


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
        d = data.split("\n")
        print(d)
        return d


# data = []
# for file in os.listdir():
#     if file.endswith(".txt"):
#         file_path = f"{path}/{file}"
#         data.append(read_text_file(file_path))


# for i in data[1]:
#     if i != "":
#         j = i.split(" ")
#         print(j)


def delete_file(folder_path):
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
    else:
        print("File not found")


def run(path, pdf_path):
    os.chdir(path)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    data = []
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            data.append(read_text_file(file_path))

    count = 0
    os.chdir(pdf_path)
    for files in onlyfiles:
        if files.endswith(".txt"):
            no = getNo(files)
            table = 0
            for i in data[count]:
                if i != "":
                    j = i.split(" ")
                    print(j)

                    # get data from file
                    point_x = float(j[1])
                    point_y = float(j[2])
                    width = float(j[3])
                    height = float(j[4])

                    # get the coordinators
                    top = (point_y - 0.5*height)*100
                    bottom = (point_y + 0.5*height)*100
                    left = (point_x - 0.5*width)*100
                    right = (point_x + 0.5*width)*100

                    print(top)

                    for file in os.listdir():
                        real_file = "./"
                        if file.endswith(".pdf"):
                            file_path = f"{real_file}/{file}"
                            # read and extract table
                            df = tabula.read_pdf(file_path, pages=no, area=[
                                top, left, bottom, right], relative_area=True)

                            no2 = str(table)
                            no1 = str(no)
                            tabula.convert_into(file_path, f"{real_file}/data-"+no1+"-"+no2+".csv", output_format='csv', pages=no, area=[
                                top, left, bottom, right], relative_area=True)
                    table = table + 1
        count = count + 1
    #     # Read pdf into list of DataFrame
    #     df = tabula.read_pdf("test.pdf", pages='all')

    #     # convert PDF into CSV file
    #     tabula.convert_into("test.pdf", "output.csv",
    #                         output_format="csv", pages='all')

    # # convert all PDFs in a directory
    # tabula.convert_into_by_batch(
    #     "input_directory", output_format='csv', pages='all')
