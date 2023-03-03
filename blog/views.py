from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from blog.models import Article, ArticleCategory
from django.core.paginator import Paginator

def blog_list(request):
    promoted_listings = Listing.objects.all().order_by('?')[:6]
    
    category = request.GET.get('category')
    categories = ArticleCategory.objects.filter(for_article_type="Blog")

    if category:
        articles = Article.objects.filter(article_type="Blog", category=category)
    else:
        articles = Article.objects.filter(article_type="Blog")

    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    articles_different = Article.objects.filter(article_type="News").order_by('-timestamp')[:3]

    context = {
        "promoted_listings": promoted_listings,
        "articles": page_obj,
        "articles_different": articles_different,
        "selected_category": category,
        "categories": categories
    }

    return render(request, 'blog/blog_list.html', context)


def blog_details(request, pk):
    promoted_listings = Listing.objects.all().order_by('?')[:3]
    article = get_object_or_404(Article, pk=pk)    
    categories = ArticleCategory.objects.filter(for_article_type="Blog")
    articles_different = Article.objects.filter(article_type="News").order_by('-timestamp')[:3]
    
    context = {
        "promoted_listings": promoted_listings,
        "categories": categories,
        "articles_different": articles_different,
        "article": article
    }

    return render(request, 'blog/blog_page.html', context)

def news_list(request):
    promoted_listings = Listing.objects.all().order_by('?')[:3]
    
    category = request.GET.get('category')
    categories = ArticleCategory.objects.filter(for_article_type="News")

    if category:
        articles = Article.objects.filter(article_type="News", category=category)
    else:
        articles = Article.objects.filter(article_type="News")
        
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    articles_different = Article.objects.filter(article_type="Blog").order_by('-timestamp')[:3]

    context = {
        "promoted_listings": promoted_listings,
        "articles": page_obj,
        "selected_category": category,
        "categories": categories,
        "articles_different": articles_different
    }

    return render(request, 'blog/blog_list.html', context)


def news_details(request, pk):
    promoted_listings = Listing.objects.all().order_by('?')[:3]
    article = get_object_or_404(Article, pk=pk)    
    categories = ArticleCategory.objects.filter(for_article_type="News")
    articles_different = Article.objects.filter(article_type="Blog").order_by('-timestamp')[:3]
    
    context = {
        "promoted_listings": promoted_listings,
        "categories": categories,
        "article": article,
        "articles_different": articles_different
    }

    return render(request, 'blog/blog_page.html', context)