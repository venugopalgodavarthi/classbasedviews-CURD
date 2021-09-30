from django.urls import path
from product import views
urlpatterns=[
    path("home/",views.home, name="home"),
    path("create/",views.viewcreate.as_view(),name="create"),
    path("details/",views.viewlist.as_view(),name="details"),
    path("update/<pk>/",views.viewupdate.as_view(),name="update"),
    path("delete/<pk>/",views.viewdelete.as_view(),name="delete"),
]