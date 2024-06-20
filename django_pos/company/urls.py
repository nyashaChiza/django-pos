from django.urls import path

from .views import CompanyView, index, branches, invoice_design, CompanyCreateView

app_name = "company"
urlpatterns = [
    path("", CompanyView.as_view(), name="company"),
    path("create/", CompanyCreateView.as_view(), name="company_create"),
    path("<int:id>/", CompanyView.as_view(), name="company_id"),
    path("settings/", view=index, name="settings"),
    path("branches/", view=branches, name="branches"),
    path("invoice-design/", view=invoice_design, name="invoice_design"),
]
