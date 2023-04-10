from ReadCsv.views import  CreateUserProfilesView

from django.urls import path

urlpatterns = [
    path('', CreateUserProfilesView.as_view())
]
