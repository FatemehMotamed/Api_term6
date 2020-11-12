
from django.conf.urls import url
from django.urls import path

from invoices import views
urlpatterns = [
    path('invoices/', views.invoice_list),
    path('invoices/<int:x>', views.invoice_detail)
]