from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """
    ブログ投稿を表すモデル
    """
    # 投稿のタイトル
    # CharFieldは文字列を格納するためのフィールド
    # max_lengthは最大文字数を指定
    title = models.CharField(
        'タイトル',
        max_length=200
    )

    # 投稿の内容
    # TextFieldは長いテキストを格納するためのフィールド
    content = models.TextField('本文')

    # 著者
    # Djangoの標準Userモデルと ForeignKey で紐付ける
    # on_delete=models.CASCADE は、ユーザーが削除されたらそのユーザーの投稿も削除する設定
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    # 作成日時
    # DateTimeFieldは日時を格納するためのフィールド
    # auto_now_add=Trueを指定すると、データが作成された日時が自動的に保存される
    created_at = models.DateTimeField(
        '作成日',
        auto_now_add=True
    )

    # 更新日時
    # auto_now=Trueを指定すると、データが更新された日時が自動的に保存される
    updated_at = models.DateTimeField(
        '更新日',
        auto_now=True
    )

    def __str__(self):
        """
        このモデルのインスタンスが文字列として参照されたときに、
        投稿のタイトルを返すように設定
        Djangoの管理サイトなどで役立ちます
        """
        return self.title
