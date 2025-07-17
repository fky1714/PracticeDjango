from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    管理サイトでのPostモデルの表示をカスタマイズするクラス
    """
    # 一覧画面に表示するフィールド
    list_display = ('title', 'created_at', 'updated_at')
    # 検索ボックスで検索対象とするフィールド
    search_fields = ('title', 'content')
    # フィルタリングに使用するフィールド
    list_filter = ('created_at', 'updated_at')
    # 日付で絞り込むためのナビゲーション
    date_hierarchy = 'created_at'
