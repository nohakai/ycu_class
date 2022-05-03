from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from . forms import UserCreateForm, LoginForm
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView
from . import models
from django.shortcuts import redirect, get_object_or_404
from .forms import CommentForm_1,CommentForm_2,CommentForm_3,CommentForm_4,CommentForm_5,CommentForm_6
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'home.html'
    
    
class RuleView(generic.TemplateView):
    template_name = 'rule.html'


class TopicView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'top.html'
    login_url = '/login/'

    
    
#アカウント作成ビュー
class Create_account(CreateView):
    def post(self, request,*args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/login/topic/')
        return render(request, 'create.html', {'form': form,})
    
    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'create.html', {'form': form,})

create_account  = Create_account.as_view()
    
#ログインビュー
class Account_login(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('topic/')
        return render(request, 'login.html', {'form': form})
    
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})
    
account_login = Account_login.as_view()


#1年
class TopicList_1_1(generic.ListView):
    model = models.Topic_1_1
    
    context_object_name = "topic_list_1_1"
    
    template_name = "topic_1.html"
    
    
    
    
class TopicList_1_2(generic.ListView):
    model = models.Topic_1_2
    
    context_object_name = "topic_list_1_2"
    
    template_name = "topic_2.html"
    
#二年  
class TopicList_1_3(generic.ListView):
    model = models.Topic_1_3
    
    context_object_name = "topic_list_1_3"
    
    template_name = "topic_3.html"
    
    
class TopicList_1_4(generic.ListView):
    model = models.Topic_1_4
    
    context_object_name = "topic_list_1_4"
    
    template_name = "topic_4.html"

#3年
    
class TopicList_1_5(generic.ListView):
    model = models.Topic_1_5
    
    context_object_name = "topic_list_1_5"
    
    template_name = "topic_5.html"


class TopicList_1_6(generic.ListView):
    model = models.Topic_1_6
    
    context_object_name = "topic_list_1_6"
    
    template_name = "topic_6.html"
    
    
#授業詳細ビュー

#１年必修
def detail_1_1(request, pk):
    thread_1_1 = get_object_or_404(models.Topic_1_1, pk=pk)
    
    context = {
        "thread_1_1": thread_1_1,
        "comments_1_1": models.Class_1_1.objects.filter(target=thread_1_1.id)
    }
    return render(request, 'topic_detail_1_1.html', context)

#１年選択必修
def detail_1_2(request, pk):
    thread_1_2 = get_object_or_404(models.Topic_1_2, pk=pk)
    
    context = {
        "thread_1_2": thread_1_2,
        "comments_1_2": models.Class_1_2.objects.filter(target=thread_1_2.id)
    }
    return render(request, 'topic_detail_1_2.html', context)

#２年必修
def detail_1_3(request, pk):
    thread_1_3 = get_object_or_404(models.Topic_1_3, pk=pk)
    
    context = {
        "thread_1_3": thread_1_3,
        "comments_1_3": models.Class_1_3.objects.filter(target=thread_1_3.id)
    }
    return render(request, 'topic_detail_1_3.html', context)

#二年専門
def detail_1_4(request, pk):
    thread_1_4 = get_object_or_404(models.Topic_1_4, pk=pk)
    
    context = {
        "thread_1_4": thread_1_4,
        "comments_1_4": models.Class_1_4.objects.filter(target=thread_1_4.id)
    }
    return render(request, 'topic_detail_1_4.html', context)

#三年必修
def detail_1_5(request, pk):
    thread_1_5 = get_object_or_404(models.Topic_1_5, pk=pk)
    
    context = {
        "thread_1_5": thread_1_5,
        "comments_1_5": models.Class_1_5.objects.filter(target=thread_1_5.id)
    }
    return render(request, 'topic_detail_1_5.html', context)

#三年専門
def detail_1_6(request, pk):
    thread_1_6 = get_object_or_404(models.Topic_1_6, pk=pk)
    
    context = {
        "thread_1_6": thread_1_6,
        "comments_1_6": models.Class_1_6.objects.filter(target=thread_1_6.id)
    }
    return render(request, 'topic_detail_1_6.html', context)


#コメント
class CommentCreate_1(CreateView):
    template_name = 'comment_form.html'
    model = models.Class_1_1
    form_class = CommentForm_1
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic_1_1, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CommentCreate_2(CreateView):
    template_name = 'comment_form.html'
    model = models.Class_1_2
    form_class = CommentForm_2
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic_1_2, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.Topic_1_2, pk=self.kwargs['pk'])
        return context

class CommentCreate_3(CreateView):
    template_name = 'comment_form.html'
    model = models.Class_1_3
    form_class = CommentForm_3
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic_1_3, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.Topic_1_3, pk=self.kwargs['pk'])
        return context
    
class CommentCreate_4(CreateView):
    template_name = 'comment_form.html'
    model = models.Class_1_4
    form_class = CommentForm_4
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic_1_4, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.Topic_1_4, pk=self.kwargs['pk'])
        return context

class CommentCreate_5(CreateView):
    template_name = 'comment_form.html'
    model = models.Class_1_5
    form_class = CommentForm_5
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic_1_5, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.Topic_1_5, pk=self.kwargs['pk'])
        return context
    
class CommentCreate_6(CreateView):
    template_name = 'comment_form.html'
    model = models.Class_1_6
    form_class = CommentForm_6
    
    def form_valid(self,form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(models.Topic_1_6, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect("../", pk=post_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(models.Topic_1_6, pk=self.kwargs['pk'])
        return context