from apps.models import Category, Post


def context_category(request):
    return {
        "categories": Category.objects.all(),
    }


def context_post(request):
    return {
        "feature_posts": Post.active.all()[:3],
    }
