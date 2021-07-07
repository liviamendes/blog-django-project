from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post
from django.db.models import Q, Count, Case, When
from comments.forms import FormComment
from comments.models import Comment
from django.contrib import messages
from django.views import View


class PostIndexListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 9
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(published=True)
        qs = qs.annotate(
            comments_count=Count(
                Case(
                    When(comment__comment_published=True, then=1)
                )
            )
        )

        return qs


class PostSearch(PostIndexListView):
    template_name = 'posts/search_post.html'

    def get_queryset(self):
        qs = super().get_queryset()
        search_name = self.request.GET.get('search_name')

        if not search_name:
            return qs

        qs = qs.filter(
            Q(title__icontains=search_name) |
            Q(author__first_name__iexact=search_name) |
            Q(content__icontains=search_name) |
            Q(introduction__icontains=search_name) |
            Q(category__category_name__iexact=search_name)
        )

        return qs


class PostCategory(PostIndexListView):
    template_name = 'posts/post_category.html'

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(category__category_name__iexact=category)

        return qs


class PostDetailsUpdateView(View):
    template_name = 'posts/post_details.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, published=True)
        self.context = {
            'post': post,
            'comments': Comment.objects.filter(post_comment=post,
                                               comment_published=True),
            'form': FormComment(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.context['form']

        if not form.is_valid():
            return render(request, self.template_name, self.context)

        comment = form.save(commit=False)

        if request.user.is_authenticated:
            comment.usuario_comentario = request.user

        comment.post_comentario = self.context['post']
        comment.save()
        messages.success(request, 'Your comment has been submitted for review.')
        return redirect('post_details', pk=self.kwargs.get('pk'))
