from advanced_filters.views import GetFieldChoices
try:
    from django.urls import path
    urlpatterns = [
        path('field_choices/<model>/<field_name>/',
            GetFieldChoices.as_view(),
            name='afilters_get_field_choices'),

        # only to allow building dynamically
        path('field_choices/',
            GetFieldChoices.as_view(),
            name='afilters_get_field_choices'),
    ]
except ImportError:
    from django.urls import re_path
    urlpatterns = [
        re_path(r'^field_choices/(?P<model>.+)/(?P<field_name>.+)/?',
                GetFieldChoices.as_view(),
                name='afilters_get_field_choices'),

        # only to allow building dynamically
        re_path(r'^field_choices/$',
                GetFieldChoices.as_view(),
                name='afilters_get_field_choices'),
    ]
