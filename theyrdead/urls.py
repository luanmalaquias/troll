from django.urls.conf import path
from site.theyrdead.views import *

urlpatterns = [
    path('', index, name="index-tad"),
    path('logout/', logoutUser, name="logout"),
]
