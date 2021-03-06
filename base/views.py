from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from . import forms
from . import models
from report.models import Report, Comment, Like

# Create your views here.

def fullUserCreateForm(request):
    userAdditionalForm = forms.UserAdditionalInfo(request.POST or None, request.FILES or None)
    userCreateForm = forms.UserCreating(request.POST or None)
    if request.method == "POST":
        if userAdditionalForm.is_valid() and userCreateForm.is_valid():
            userMain = userCreateForm.save()
            userAdditional = userAdditionalForm.save(commit=False)
            userAdditional.user = userMain
            userAdditional.save()
            request.session["isJustRegistered"] = True
            return HttpResponseRedirect(reverse('base:login'))
    context = {'userAdditionalForm': userAdditionalForm,
               'userCreateForm': userCreateForm,}
    return render(request, 'registration/sign_up.html', context)

def userUpdateForm(request, username):
    if request.method == "POST":
        userAdditionalForm = forms.UserAdditionalInfo(request.POST, instance=request.user)
        userCreateForm = forms.UserCreating(request.POST, instance=request.user.userinformation)
        if userAdditionalForm.is_valid() and userCreateForm.is_valid():
            userMain = userCreateForm.save()
            userAdditional = userAdditionalForm.save(commit=False)
            userAdditional.user = userMain
            userAdditional.save()
            return HttpResponseRedirect(reverse('base:personal', kwargs={'username':request.user.username}))
    else:
        userAdditionalForm = forms.UserAdditionalInfo(instance=request.user.userinformation)
        userCreateForm = forms.UserCreating(instance=request.user)

    context = {'userAdditionalForm': userAdditionalForm,
               'userCreateForm': userCreateForm,}

    return render(request, 'registration/user_edit.html', context)


class UserUpdateView(UpdateView):
    model = models.UserInformation
    form_class = forms.UserUpdateForm
    slug_field = 'user__username'

# class UserCreateView(CreateView):
#     form_class = forms.UserCreating
#     template_name = 'registration/registration.html'
#     success_url = reverse_lazy('base:login')
#     def form_valid(self, form):
#         self.request.session["isJustRegistered"] = True
#         return super().form_valid(form)


class UserLoginView(LoginView):

    def get_context_data(self, **kwargs):
        if 'isJustRegistered' in self.request.session:
            kwargs['isJustRegistered'] = self.request.session["isJustRegistered"]
            del self.request.session["isJustRegistered"]
        return super().get_context_data(**kwargs)


def userPage(request, username):
    user = User.objects.get(username=username)
    report_list = Report.objects.filter(user=user)
    context = {
        'user': user,
        'report_list': report_list,
    }
    return render(request, 'base/personal.html', context)

def user_page_comments(request, username):
    # user = request.user
    user = User.objects.get(username=username)
    comments_list = Comment.objects.filter(user=user)
    context = {
        'user': user,
        'comments_list': comments_list,
    }
    return render(request, 'base/personal.html', context)

def user_page_likes(request, username):
    user = User.objects.get(username=username)
    likes_list = Like.objects.filter(user=user)
    report_list = [like.report for like in likes_list]
    context = {
        'user': user,
        'report_list': report_list,
    }
    return render(request, 'base/personal.html', context)
