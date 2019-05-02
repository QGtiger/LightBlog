from django.shortcuts import render,get_object_or_404,HttpResponse
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import ArticlePost,Comment
from comment.models import Comment_reply
from django.conf import settings
import json
import redis

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


def article_titles(request):
    length = r.zcard('article_ranking')
    article_ranking = r.zrange("article_ranking", 0, length, desc=True)[:5]
    article_ranking_ids = [int(id) for id in article_ranking]
    most_viewed = list(ArticlePost.objects.filter(id__in=article_ranking_ids))
    most_viewed.sort(key=lambda x: article_ranking_ids.index(x.id))
    return render(request,'article/article_titles.html',locals())


def article_page(request):
    article_titles = ArticlePost.objects.all()
    paginator = Paginator(article_titles, 8)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    articles_json = []
    for i in range(len(articles)):
        articles_json.append({'id':articles[i].id,'author':articles[i].author.username,'title':articles[i].title,'updated':articles[i].updated.strftime("%Y-%m-%d %H:%M:%S"),'body':articles[i].body[:70],'users_like':articles[i].users_like.count()})
    #return HttpResponse(serializers.serialize("json",articles))
    return HttpResponse(json.dumps({'static':200,'data':articles_json,'page_num':paginator.num_pages}))


@csrf_exempt
def article_content(request, article_id):
    if request.method == 'POST':
        if request.user.username == "":
            return HttpResponse(json.dumps({'code': 502, 'tips':'What are u doing now??'}))
        comment = request.POST.get('comment','')
        try:
            user = request.user
            article = get_object_or_404(ArticlePost, id=article_id)
            C = Comment(article=article,commentator=user,body=comment)
            C.save()
            comment_info = {'commentator':user.username,'id': C.id, 'body': C.body, 'created': C.created.strftime("%Y-%m-%d %H:%M:%S")}
            return HttpResponse(json.dumps({"code":200,"tips":"感谢您的评论", 'comment_info':comment_info}))
        except:
            return HttpResponse(json.dumps({"code":501, "tips":"评论系统出现错误"}))
    else:
        article = get_object_or_404(ArticlePost, id=article_id)
        total_views = r.incr("article:{}:views".format(article_id))
        r.zincrby('article_ranking', 1, article_id)
        return render(request, "article/article_content.html", locals())


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def comment_like(request):
    user = request.user
    comment_id = request.POST.get("id","")
    action = request.POST.get("action","")
    if comment_id and action:
        try:
            comment = Comment.objects.get(id=comment_id)
            if action == 'like':
                comment.comment_like.add(user)
                num = comment.comment_like.count()
                return HttpResponse(json.dumps({'static':200, 'support_num':num}))
            else:
                comment.comment_like.remove(user)
                num = comment.comment_like.count()
                return HttpResponse(json.dumps({'static':201, 'support_num':num}))
        except:
            return HttpResponse(json.dumps({'static':500,'tips':'系统错误,重新尝试'}))

@csrf_exempt
@require_POST
def comment_delete(request):
    comment_id = request.POST['id']
    comment = Comment.objects.get(id=comment_id)
    try:
        if request.user == comment.commentator:
            comment.delete()
            return HttpResponse(json.dumps({'static':201, 'tips':'评论已删除'}))
        else:
            return HttpResponse(json.dumps({'static':502, 'tips':"You don't have permission.."}))
    except:
        return HttpResponse(json.dumps({'static':500, 'tips':'Something Error...'}))


def init_data(data):
    items = data.comment_reply.all()[:2]
    list_data = []
    for item in items:
        if item.reply_type == 0:
            list_data.append({'from': item.comment_user.username,'to':data.commentator.username , 'id': item.id, 'body': item.body,
                            'created': item.created.strftime("%Y-%m-%d %H:%M:%S")})
        else:
            to_id = item.reply_comment
            list_data.append(
                {'from': item.comment_user.username, 'to': Comment_reply.objects.get(id=to_id).comment_user.username, 'id': item.id, 'body': item.body,
                 'created': item.created.strftime("%Y-%m-%d %H:%M:%S")})
    return list_data


def comment_page(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    comments_all = article.comments.all()
    paginator = Paginator(comments_all,6)
    page = request.GET['page']
    try:
        current_page = paginator.page(page)
        comments = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        comments = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        comments = current_page.object_list
    comments_list=[]
    for item in comments:
        comments_list.append({'id':item.id ,'commentator': item.commentator.username,'comment_reply':init_data(item) ,'created': item.created.strftime("%Y-%m-%d %H:%M:%S"), 'comment_like': item.comment_like.count(), 'body': item.body})
    return HttpResponse(json.dumps({'code':200, 'res': comments_list, 'page_num': paginator.num_pages}))