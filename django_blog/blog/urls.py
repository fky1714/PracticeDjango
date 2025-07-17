from django.urls import path
from . import views

# app_nameを設定することで、テンプレートなどからURLを逆引きする際に名前空間を利用できる
app_name = 'blog'

urlpatterns = [
    # path(URLパターン, ビュー関数, name=URLの名前)

    # 投稿一覧ページ
    # URL: /
    path('', views.PostListView.as_view(), name='post_list'),

    # 投稿詳細ページ
    # URL: /post/<int:pk>/  (例: /post/1/)
    # <int:pk> は、整数型のプライマリキー(pk)がURLに含まれることを示す
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # 新規投稿ページ
    # URL: /post/new/
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),

    # 投稿編集ページ
    # URL: /post/<int:pk>/edit/
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),

    # 投稿削除ページ
    # URL: /post/<int:pk>/delete/
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
