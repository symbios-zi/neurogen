from django.conf import settings
from django.urls import include, path  # For django versions from 2.0 and up
from . import views

urlpatterns = [
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/parse/', views.parse, name='parse'),
    path('create', views.create, name='create'),
    path('', views.list, name='list'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns