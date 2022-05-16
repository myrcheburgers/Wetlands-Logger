from django.contrib import admin
from django.urls import path
# from tutorials import views as tutorials_views
from wetland_logger import views as wlv
from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#     #path('', tutorials_views.index, name='home'),
#     path('', tutorials_views.index.as_view(), name='home'),
#     path('api/tutorials/', tutorials_views.tutorial_list),
#     path('api/tutorials/<int:pk>/', tutorials_views.tutorial_detail),
#     path('api/tutorials/published/', tutorials_views.tutorial_list_published)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('users/', wlv.user_list),
    path('users/<int:pk>/', wlv.user_detail),
    path('projects/', wlv.project_list),
    path('projects/<int:pk>/', wlv.project_detail),
    #path('projects/<int:pk>/datapoints', wlv.datapoint_list), #show all datapoints for a specific project
    # path('datapoints/', wlv.datapoint_list),
    path('projects/<int:fk>/datapoints/', wlv.datapoint_list)
]