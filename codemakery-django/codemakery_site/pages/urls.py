from django.urls import path
from django.views.generic import TemplateView

from .views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),

]