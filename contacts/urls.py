from django.urls import path

from contacts import views

urlpatterns = [
    path("", views.index, name="contact_list"),
    path("add/", views.add, name="add_contact"),
    path("delete/<int:contact_id>/", views.delete, name="delete"),
    path("<int:contact_id>/", views.detail, name="contact_detail"),
    path("edit/<int:contact_id>/", views.edit, name="contact_edit"),
]
