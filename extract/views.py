from django.shortcuts import redirect, render
from django.http import HttpResponse
from extract import extracte
# from .models import Document
# from .forms import DocumentForm
import os
import zipfile
import io
from django.conf import settings


def showHTML(self):
    return redirect('extracted')


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
        d = data.split("\n")
        print(d)
        return d


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
    # return HttpResponse("done")
    return redirect('show')
    # return render(self, 'result.html')


def show(request):
    return render(request, 'output.html')


def getfiles(request):

    # fix
    home_path = './'
    pdf_path = '../../../../media/pdfs/'
    os.chdir(pdf_path)

    filenames = []
    for file in os.listdir():
        if file.endswith(".csv"):
            file_path = f"./{file}"
            filenames.append(read_text_file(file_path))

    # filenames = ["/tmp/file1.csv", "/tmp/file2.csv"]

    zip_subdir = "csvoutputs"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = io.StringIO.StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type="application/csvzip")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp


# def download(request):
#     # print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
#     # message = 'Upload as many files as you want!'
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile=request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return render(request, 'index.html')
#         else:
#             message = 'The form is not valid. Fix the following error:'
#     else:
#         form = DocumentForm()  # An empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form
#     context = {'documents': documents, 'form': form, 'message': message}

#     return render(request, 'index.html', context)
