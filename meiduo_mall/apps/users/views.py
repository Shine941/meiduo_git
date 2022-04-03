

from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.users.models import User
import re
from django.http import JsonResponse
class UsernameCountView(View):
    def get(self, request, username):
        # 接收用户名；对这个用户名进行判断
        if not re.match('[a-zA-Z0-9_-]{5,20}', username):
            return JsonResponse({'code': 200, 'errmsg': '用户名不满足需求'})
        # 根据用户名查询数据库；
        count = User.objects.filter(username=username).count()
        # 返回响应
        return JsonResponse({'code':0, 'count': count, 'errmsg': 'ok'})
