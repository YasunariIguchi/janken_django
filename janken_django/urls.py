from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('janken/', include('janken.urls')),
    path('', RedirectView.as_view(url='/janken/')),  # ルートURLから/janken/へリダイレクト
]