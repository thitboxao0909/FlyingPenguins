from django.urls import path
from .views import delete_file1, my_view
from .views import delete_file, delete_file2, delete_file1

urlpatterns = [
    path('', delete_file, name='delete_file'),
    path('deletefile2', delete_file2, name='delete_file2'),
    path('deletefile1', delete_file1, name='delete_file1'),
    path('myview', my_view, name='my-view'),
]
