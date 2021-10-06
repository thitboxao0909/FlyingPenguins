from django.shortcuts import redirect, render
from django.http import HttpResponse
from extract import extracte
import os


def showHTML(self):

    return redirect('extracted')
    HttpResponse("Loading")


def extracted(self, *args, **kwargs):
    path = '../../runs/detect/exp/labels/'
    pdf_path = '../../../../media/pdfs/'
    home_path = '../../'
    run_path = './'
    os.chdir(path)
    for file in os.listdir():
        print("this is a file in " + file)

    extracte.run(run_path, pdf_path)
    os.chdir(home_path)
    return HttpResponse("done")

# Create your views here.
