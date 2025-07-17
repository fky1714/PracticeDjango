from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
    """
    投稿の一覧を表示するビュー
    """
    # どのモデルのリストを表示するかを指定
    model = Post
    # どのテンプレートを使って表示するかを指定
    # 指定しない場合は <app_name>/<model_name>_list.html (blog/post_list.html) が自動的に使われる
    template_name = 'blog/post_list.html'
    # テンプレートに渡すオブジェクトのリストの名前を指定
    # 指定しない場合は object_list という名前で渡される
    context_object_name = 'posts'
    # 1ページに表示するオブジェクトの数を指定
    paginate_by = 5

class PostDetailView(DetailView):
    """
    投稿の詳細を表示するビュー
    """
    model = Post
    template_name = 'blog/post_detail.html'
    # テンプレートに渡すオブジェクトの名前を指定
    # 指定しない場合は object という名前で渡される
    context_object_name = 'post'

class PostCreateView(CreateView):
    """
    新しい投稿を作成するビュー
    """
    model = Post
    form_class = PostForm # fieldsの代わりにform_classを使用
    template_name = 'blog/post_form.html'
    # フォームの送信が成功した後のリダイレクト先を指定
    # reverse_lazyは、URLの逆引きを遅延評価で行う（プロジェクト起動時にURL解決を試みない）
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        """
        フォームのデータが有効だった場合の処理
        """
        # フォームのインスタンスに、現在ログインしているユーザーを紐付けるなどの処理をここで行うことが多い
        # 今回は特に処理は不要なので、親クラスのform_validをそのまま呼び出す
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    """
    投稿を編集するビュー
    """
    model = Post
    form_class = PostForm # fieldsの代わりにform_classを使用
    template_name = 'blog/post_form.html'
    # 編集対象のオブジェクトを特定するためのURLパラメータ名を指定
    # デフォルトは 'pk' なので、今回は省略可能
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:post_list')

class PostDeleteView(DeleteView):
    """
    投稿を削除するビュー
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'post'
