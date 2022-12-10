from apps.models import Category, Post


def context_category(request):
    return {
        "categories": Category.objects.all(),
    }


def context_post(request):
    return {
        "feature_posts": Post.objects.filter(status='active').order_by('-created_at')[:3],
    }
