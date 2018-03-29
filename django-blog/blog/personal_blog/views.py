#coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator,PageNotAnInteger,EmptyPage

from models import ArticleModel,RecommendModel,SentenceModel,LabelModel,NoticeModel,ColumnModel
# Create your views here.


class IndexView(View):
    def get(self,request):
        articles=ArticleModel.objects.all().order_by('-id')
        recommend=RecommendModel.objects.last()
        hot_article=articles.order_by('-click_nums')[:5]
        sentence=SentenceModel.objects.last()
        notice=NoticeModel.objects.last()
        try:
            page=request.GET.get('page','1')
        except PageNotAnInteger:
            page=1
        p=Paginator(articles,5,request=request)
        article=p.page(page)
        context={'articles':article,'recommend':recommend,'hot_article':hot_article,'sentence':sentence,'notice':notice}
        return render(request,'blog/index.html',context)


def detail(request,article_id):
    hot_articles = ArticleModel.objects.all().order_by('-click_nums')
    article=hot_articles.get(id=int(article_id))
    taxonomy=LabelModel.objects.get(id=int(article.label.id))#获得分类名称
    relevant_article=taxonomy.articlemodel_set.all()[:5]#取出分类为taxonomy的所有文章
    hot_article=hot_articles[:5]
    sentence=SentenceModel.objects.last()
    notice=NoticeModel.objects.last()
    article.click_nums+=1
    article.save()
    context={'article':article,'hot_article':hot_article,'sentence':sentence,'relevant_article':relevant_article,
             'notice':notice}
    return render(request,'blog/detail.html',context)


def recommend(request,recommend_id):
    recommend=RecommendModel.objects.get(id=int(recommend_id))
    hot_article=ArticleModel.objects.all().order_by('-click_nums')[:5]
    sentence=SentenceModel.objects.last()
    notice=NoticeModel.objects.last()
    context={'recommend':recommend,'hot_article':hot_article,'sentence':sentence,'notice':notice}
    return render(request,'blog/recommend.html',context)


def list(request,column_id):
    column=ColumnModel.objects.get(id=int(column_id))
    articles=column.articlemodel_set.all().order_by('-id')
    p=int(column_id)
    hot_article=ArticleModel.objects.all().order_by('-click_nums')[:5]
    sentence=SentenceModel.objects.last()
    notice=NoticeModel.objects.last()
    try:
        page=request.GET.get('page','1')
    except PageNotAnInteger:
        page=1
    p=Paginator(articles,1,request=request)
    article=p.page(page)
    context={'articles':article,'p':p,'column':column,'hot_article':hot_article,'sentence':sentence,'notice':notice}
    return render(request,'blog/list.html',context)