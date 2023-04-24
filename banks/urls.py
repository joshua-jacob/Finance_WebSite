from django.urls import path
from .views import Home,t_pnb,t_hdfc,form_pnb,form_hdfc,table_pnb,table_hdfc,Submit_pnb,Submit_hdfc
urlpatterns = [
    path("", Home, name="home"),
    path("pnb",t_pnb,name="transactions_pnb"),
    path("hdfc",t_hdfc,name="transactions_hdfc"),
    path("pnb/form",form_pnb,name="form_pnb"),
    path("hdfc/form",form_hdfc,name="form_hdfc"),
    path("hdfc/table",table_hdfc,name="table_hdfc"),
    path("pnb/table",table_pnb,name="table_pnb"),
    path("pnb/form/submit",Submit_pnb,name="Submit_pnb"),
    path("hdfc/form/submit",Submit_hdfc,name="Submit_hdfc"),


]
