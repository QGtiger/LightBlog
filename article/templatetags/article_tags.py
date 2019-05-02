from django import template
from django.db.models import Count
from article.models import ArticlePost
from django.conf import settings
import redis
register = template.Library()
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.article_post.count()


@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by('-created')[:n]
    return {"latest_articles": latest_articles}


@register.simple_tag
def most_commented_articles(n=5):
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:n]


@register.inclusion_tag('article/list/most_views.html')
def most_views():
    length = r.zcard('article_ranking')
    article_ranking = r.zrange("article_ranking", 0, length, desc=True)[:5]
    article_ranking_ids = [int(id) for id in article_ranking]
    most_viewed = list(ArticlePost.objects.filter(id__in=article_ranking_ids))
    most_viewed.sort(key=lambda x: article_ranking_ids.index(x.id))
    return {'most_viewed': most_viewed}
