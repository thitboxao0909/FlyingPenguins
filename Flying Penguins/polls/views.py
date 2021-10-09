from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import template
from polls import detect
from pdf2image import convert_from_path
import os


# def view(request):
#     return HttpResponse("Loading")

# delete file path


def detected(self, *args, **kwargs):

    t = template.Template("<html><body>loading</body></html>")
    c = template.Context({'now'})
    html = t.render(c)

    pdf_path = './'
    os.chdir(pdf_path)

    for file in os.listdir():
        print("this is a file in " + file)
        if file.endswith(".pdf"):
            file_path = f"{pdf_path}/{file}"
            print("this is file path: " + file_path)
            print("\nend file")
            images = convert_from_path(file_path)
            for i in range(len(images)):
                images[i].save('page' + str(i) + '.jpg', 'JPEG')

    detect.run()

    return redirect('/extract/')
