from django.urls import path, re_path

app_name = 'wagtailvideos'

def get_urlpatterns():
    # Import views inside the function to avoid circular import
    from wagtailvideos.views import multiple, videos
    
    return [
        path('add/', videos.add, name='add'),
        re_path(r'^usage/(\d+)/$', videos.usage, name='video_usage'),

        path('multiple/add/', multiple.add, name='add_multiple'),
        re_path(r'^multiple/(\d+)/delete/$', multiple.delete, name='delete_multiple'),
        re_path(r'^multiple/(\d+)/$', multiple.edit, name='edit_multiple'),

        re_path(r'^(\d+)/delete/$', videos.delete, name='delete'),
        re_path(r'^(\d+)/create_transcode/$', videos.create_transcode, name='create_transcode'),
        re_path(r'^(\d+)/$', videos.edit, name='edit'),
        path('', videos.index, name='index'),
    ]

urlpatterns = get_urlpatterns()