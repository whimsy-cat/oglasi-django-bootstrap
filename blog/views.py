from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from blog.models import Article, ArticleCategory
from django.core.paginator import Paginator

def article_list(request):
    promoted_listings = Listing.objects.all().order_by('?')[:6]
    
    category = request.GET.get('category')
    categories = ArticleCategory.objects.all()
    if category:
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.all()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "promoted_listings": promoted_listings,
        "articles": page_obj,
        "selected_category": category,
        "categories": categories
    }

    return render(request, 'blog/blog_list.html', context)


def article_detail(request, pk):
    promoted_listings = Listing.objects.all().order_by('?')[:6]
    article = get_object_or_404(Article, pk=pk)    
    categories = ArticleCategory.objects.all()
    
    context = {
        "promoted_listings": promoted_listings,
        "categories": categories,
        "article": article
    }

    return render(request, 'blog/blog_page.html', context)