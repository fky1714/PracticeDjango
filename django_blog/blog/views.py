from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Create your views here.

class PostListView(ListView):
    """
    投稿の一覧を表示するビュー
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    # querysetをオーバーライドして、投稿を作成日時の降順で並び替える
    queryset = Post.objects.order_by('-created_at')

class PostDetailView(DetailView):
    """
    投稿の詳細を表示するビュー
    """
    model = Post
    template_name = 'blog/post_detail.html'
    # テンプレートに渡すオブジェクトの名前を指定
    # 指定しない場合は object という名前で渡される
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
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
        # フォームが保存される前に、投稿のauthorを現在ログインしているユーザーに設定
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    投稿を編集するビュー
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        """
        アクセスしているユーザーが投稿者本人か、スーパーユーザーであるかをチェック
        """
        post = self.get_object()
        return post.author == self.request.user or self.request.user.is_superuser

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    投稿を削除するビュー
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'post'

    def test_func(self):
        """
        アクセスしているユーザーが投稿者本人か、スーパーユーザーであるかをチェック
        """
        post = self.get_object()
        return post.author == self.request.user or self.request.user.is_superuser

class SignUpView(CreateView):
    """
    ユーザー登録（サインアップ）を行うビュー
    """
    form_class = UserCreationForm
    # 登録が成功したらログインページにリダイレクト
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'
