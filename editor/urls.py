from django.conf.urls import url
import views

urlpatterns = [
    url(r'^poses$', views.view_poses_all),
    url(r'^poses/(?P<pose_name>[a-zA-Z]+)/$', views.view_poses)
]

