from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import os


def test_vue(request):
    return render(request, 'vue_app/test.html')


folder_path1 = "runs/detect/exp/"
folder_path3 = "labels/"
folder_path2 = "../../../../media/pdfs/"
home_path = "../../"


def delete_file(request):
    if os.path.exists(folder_path1):
        os.chdir(folder_path1)
        for file in os.listdir():
            if file.endswith(".txt"):
                os.remove(file)
            if file.endswith(".pdf"):
                os.remove(file)
            if file.endswith(".csv"):
                os.remove(file)
            if file.endswith(".jpg"):
                os.remove(file)
    else:
        print("File not found" + folder_path1)

    return redirect('/deletefile1')


def delete_file1(request):
    if os.path.exists(folder_path3):
        os.chdir(folder_path3)
        for file in os.listdir():
            if file.endswith(".txt"):
                os.remove(file)
            if file.endswith(".pdf"):
                os.remove(file)
            if file.endswith(".csv"):
                os.remove(file)
            if file.endswith(".jpg"):
                os.remove(file)
    else:
        print("File not found" + folder_path1)

    return redirect('/deletefile2')


def delete_file2(request):
    if os.path.exists(folder_path2):
        os.chdir(folder_path2)
        for file in os.listdir():
            if file.endswith(".txt"):
                os.remove(file)
            if file.endswith(".pdf"):
                os.remove(file)
            if file.endswith(".csv"):
                os.remove(file)
            if file.endswith(".jpg"):
                os.remove(file)
    else:
        print("File not found" + folder_path2)

    return redirect('/myview')


def my_view(request):

    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('/polls/')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)
