from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    投稿を作成・編集するためのフォーム
    """
    class Meta:
        # このフォームがどのモデルを元にしているかを指定
        model = Post
        # フォームに表示するフィールドを指定
        fields = ('title', 'content')
        # フォームのウィジェットをカスタマイズ
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'タイトルを入力してください'}),
            'content': forms.Textarea(attrs={'placeholder': '本文を入力してください'}),
        }
        # フィールドのラベルをカスタマイズ
        labels = {
            'title': 'ブログタイトル',
            'content': 'ブログ本文',
        }
