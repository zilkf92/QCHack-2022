from django.urls import path


from qpd_api import views


urlpatterns = [
    path("job", views.JobApiView.as_view()),
]
