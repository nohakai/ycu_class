from django.urls import path, include

from . import views



app_name="class"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('rule/', views.RuleView.as_view(), name="rule"),
    path('create/', views.Create_account.as_view(), name="create_account"),
    path('login/', views.Account_login.as_view(), name="login"),
    path('login/topic/', views.TopicView.as_view(), name="topic" ),
    path('login/topic/topic_1.html/', views.TopicList_1_1.as_view(), name="topic_1_1"),
    path('login/topic/topic_2.html/', views.TopicList_1_2.as_view(), name="topic_1_2"),
    path('login/topic/topic_3.html/', views.TopicList_1_3.as_view(), name="topic_1_3"),
    path('login/topic/topic_4.html/', views.TopicList_1_4.as_view(), name="topic_1_4"),
    path('login/topic/topic_5.html/', views.TopicList_1_5.as_view(), name="topic_1_5"),
    path('login/topic/topic_6.html/', views.TopicList_1_6.as_view(), name="topic_1_6"),
    path('login/topic/topic_1.html/<int:pk>/', views.detail_1_1, name="detail_1_1"),
    path('login/topic/topic_2.html/<int:pk>/', views.detail_1_2, name="detail_1_2"),
    path('login/topic/topic_3.html/<int:pk>/', views.detail_1_3, name="detail_1_3"),
    path('login/topic/topic_4.html/<int:pk>/', views.detail_1_4, name="detail_1_4"),
    path('login/topic/topic_5.html/<int:pk>/', views.detail_1_5, name="detail_1_5"),
    path('login/topic/topic_6.html/<int:pk>/', views.detail_1_6, name="detail_1_6"),
    path('login/topic/topic_1.html/<int:pk>/create/', views.CommentCreate_1.as_view(), name="comment_1"),
    path('login/topic/topic_2.html/<int:pk>/create/', views.CommentCreate_2.as_view(), name="comment_2"),
    path('login/topic/topic_3.html/<int:pk>/create/', views.CommentCreate_3.as_view(), name="comment_3"),
    path('login/topic/topic_4.html/<int:pk>/create/', views.CommentCreate_4.as_view(), name="comment_4"),
    path('login/topic/topic_5.html/<int:pk>/create/', views.CommentCreate_5.as_view(), name="comment_5"),
    path('login/topic/topic_6.html/<int:pk>/create/', views.CommentCreate_6.as_view(), name="comment_6"),
]
