from posts.views import PostList, PostCreate, PostDetail
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('new/', PostCreate.as_view(), name='post_create'),
    path('posts/<pk>/', PostDetail.as_view(), name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)