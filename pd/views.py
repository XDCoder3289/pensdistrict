from django.shortcuts import render
from django.http import HttpResponse
from pd.models import Post
from pd.models import Category
from pd.models import PenInPost

def index(request):
    context_dict = {}
    # Latest Posts
    categories = Category.objects.all()[:3]
    posts = Post.objects.all()[:3]
    # Posts for Best
    posts_for_best = Post.objects.all()[3:6]
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
    context_dict['categories'] = categories
    context_dict['posts'] = posts
    context_dict['best'] = posts_for_best
    context_dict['premium'] = posts_for_premium
    context_dict['fountains'] = posts_for_fountains
    context_dict['quills'] = posts_for_quills
    return render(request, 'index.html', context=context_dict)

def cat_page(request, cat_slug_name):
    context_dict = {}
    try:
        categories = Category.objects.all()
        category = Category.objects.get(slug=cat_slug_name)
        posts = Post.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['posts'] = posts
        context_dict['categories'] = categories
    except:
        context_dict['not_found'] = "Sorry, the page does not exist"
    return render(request, 'categories.html', context=context_dict)


def posts(request, cat_slug_name, post_slug_name):
    context_dict = {}
    try:
        direct_post = Post.objects.get(slug=post_slug_name)
        pens_in_post = PenInPost.objects.filter(pen_is_in=direct_post)
        category = Category.objects.all()
        context_dict['categories'] = category
        context_dict['post'] = direct_post
        context_dict['pens'] = pens_in_post
        context_dict['test'] = 'test'
    except:
        context_dict['fourofour'] = 'Sorry, the page you were looking was not found'

    return render(request, 'post.html', context=context_dict)
