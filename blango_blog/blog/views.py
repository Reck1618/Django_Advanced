from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post
from blog.forms import CommentForm
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related('author')
    logger.info(f"Posts:{len(posts)}")
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_active:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)

                comment.creator = request.user
                comment.content_object = post
                comment.save()
                logger.info(f"Created comment on Post {post.pk} by {request.user}")
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request, 'blog/post-detail.html', {'post': post, 'comment_form': comment_form})

def get_ip(request):
    from django.http import HttpResponse
    return HttpResponse(request.META['REMOTE_ADDR'])

def post_table(request):
    return render(request, "blog/post-table.html")