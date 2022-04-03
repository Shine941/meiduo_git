from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.users.models import User
from django.http import JsonResponse
class UsernameCountView(View):
    def get(self, request, username):
        # 接收用户名；
        # 根据用户名查询数据库；
        count=User.objects.filter(username=username).count()
        # 返回响应
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})
