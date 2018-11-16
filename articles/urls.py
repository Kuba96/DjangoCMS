from django.contrib import admin
from django.urls import path
from articles.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('show_all/', articles),
    path('<int:id>/', article),
]