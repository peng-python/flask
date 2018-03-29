import xadmin
from models import ArticleModel,ColumnModel,LabelModel,RecommendModel,SentenceModel,NoticeModel


class ArticleAdmin(object):
    list_display=['title','content','column','source','click_nums','label','add_time']
    search_fields=['title','content','column','source','click_nums','label']
    list_filter=['title','content','column','source','click_nums','label','add_time']

    style_fields={"content":"ueditor"}


class ColumnAdmin(object):
    list_display=['name','isDelete','add_time']
    search_fields=['name','isDelete']
    list_filter=['name','isDelete','add_time']


class LabelAdmin(object):
    list_display=['name','isDelete','add_time']
    search_fields=['name','isDelete','add_time']
    list_filter=['name','isDelete','add_time']


class RecommendAdmin(object):
    list_display=['title','recommend','add_time']
    search_fields=['title','recommend']
    list_filter=['title','recommend','add_time']

    style_fields={'recommend':'ueditor'}


class SentenceAdmin(object):
    list_display=['content','add_time']
    search_fields=['content']
    list_filter=['content','add_time']


class NoticeAdmin(object):
    list_display=['title','content','add_time']
    search_fields=['title','content']
    list_filter=['title','content','add_time']


xadmin.site.register(ArticleModel,ArticleAdmin)
xadmin.site.register(ColumnModel,ColumnAdmin)
xadmin.site.register(LabelModel,LabelAdmin)
xadmin.site.register(RecommendModel,RecommendAdmin)
xadmin.site.register(SentenceModel,SentenceAdmin)
xadmin.site.register(NoticeModel,NoticeAdmin)