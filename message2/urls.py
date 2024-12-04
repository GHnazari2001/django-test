from django.urls import path
from .views import MessageView



urlpatterns = [
  #  path('admin/', admin.site.urls),
   path("",MessageView.as_view(),name="View"),
  # path("",message_view,name="demo")
]

