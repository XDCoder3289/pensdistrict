from django.shortcuts import render
from django.http import HttpResponse
from pd.models import Post
from pd.models import Category
from pd.models import PenInPost

def index(request):
    context_dict = {}
    cat_for_nav = Category.objects.all()
    # Latest Posts
    categories = Category.objects.all()[:3]
    posts = Post.objects.all()[:3]
    # Posts for Top Picks
    cat_for_top = Category.objects.get(pen_category='Top Picks')
    posts_for_best = Post.objects.filter(category=cat_for_top)[:3]
    # Premium Pens
    cat_for_premium = Category.objects.get(pen_category='Premium Pens')
    posts_for_premium = Post.objects.filter(category=cat_for_premium)[:3]
    # Fountain Pens
    fountain_pens = Category.objects.get(pen_category='Fountain Pens')
    posts_for_fountains = Post.objects.filter(category=fountain_pens)[:3]
    # Quills
    quill_pens = Category.objects.get(pen_category='Quills')
    posts_for_quills = Post.objects.filter(category=quill_pens)[:3]

    # context_dict
    context_dict['category_nav'] = cat_for_nav
    context_dict['categories'] = categories
    context_dict['posts'] = posts
    context_dict['best'] = posts_for_best
    context_dict['premium'] = posts_for_premium
    context_dict['fountains'] = posts_for_fountains
    context_dict['quills'] = posts_for_quills
    context_dict['cat_premium'] = cat_for_premium
    context_dict['cat_fountain'] = fountain_pens
    context_dict['cat_quill'] = quill_pens
    return render(request, 'index.html', context=context_dict)

def cat_page(request, cat_slug_name):
    context_dict = {}
    try:
        categories = Category.objects.all()
        category = Category.objects.get(slug=cat_slug_name)
        posts = Post.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['posts'] = posts
        context_dict['category_nav'] = categories
    except:
        context_dict['not_found'] = "Sorry, the page does not exist"
    return render(request, 'categories.html', context=context_dict)


def posts(request, cat_slug_name, post_slug_name):
    context_dict = {}
    try:
        direct_post = Post.objects.get(slug=post_slug_name)
        pens_in_post = PenInPost.objects.filter(pen_is_in=direct_post)
        category = Category.objects.all()
        side_nav_posts = Post.objects.exclude(post_name=direct_post)[:5]
        context_dict['category_nav'] = category
        context_dict['post'] = direct_post
        context_dict['pens'] = pens_in_post
        context_dict['sidenav_posts'] = side_nav_posts
    except:
        context_dict['fourofour'] = 'Sorry, the page you were looking was not found'

    return render(request, 'post.html', context=context_dict)

def about(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['category_nav'] = categories
    return render(request, 'about.html', context=context_dict)

def privacy(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['category_nav'] = categories
    return render(request, 'privacy.html', context=context_dict)


def contact(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['category_nav'] = categories
    return render(request, 'contact.html', context=context_dict)

def search(request):
    search = request.GET['query']
    posts = Post.objects.filter(post_name__contains=search)
    context_dict = {}
    categories = Category.objects.all()
    context_dict['search_posts'] = posts
    context_dict['category_nav'] = categories
    context_dict['query'] = search
    return render(request, 'search.html', context=context_dict)

def sitemap(request):
    posts = Post.objects.all()
    context_dict = {}
    context_dict['posts'] = posts
    return render(request, 'sitemap.xml', context=context_dict)
