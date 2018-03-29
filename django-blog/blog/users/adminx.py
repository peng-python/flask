#coding=utf-8
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title='博客后台管理系统'
    site_footer='版权所有'

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)