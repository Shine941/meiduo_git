from django.urls import path
from apps.users.views import UsernameCountView
urlpattens={
    # 判断用户名是否重复
    path('usernames/<username>/count/', UsernameCountView.as_view()),
}