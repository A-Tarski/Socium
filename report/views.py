from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from . import models, forms
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from plate.models import Vehicle_plate
from django.core.paginator import Paginator
# Create your views here.

# class AuthorRequiredMixin(object):
#     def get_queryset(self):
#        qs = super().get_queryset()
#        return qs.filter(user=self.request.user)
#
# class ReportOwner(AuthorRequiredMixin):
#     model = models.Report

class CreateReport(LoginRequiredMixin, CreateView):
    login_url = 'base:login'
    # fields = ('header', 'description','video_link_report', 'image_report',)
    form_class = forms.ReportForm
    model = models.Report
    template_name = 'report/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        clean_plate = form.cleaned_data['plate_nubmer'].upper()
        plate_qs = Vehicle_plate.objects.filter(plate_nubmer=clean_plate)
        if len(plate_qs) > 0:
            self.object.vehicle_plate = plate_qs[0]
        else:
            # create new vehicle plate next_page_number
            new_plate = Vehicle_plate(plate_nubmer=clean_plate, created_by=self.request.user)
            new_plate.save()
            self.object.vehicle_plate = new_plate
            # need add check if such user exist than add user_link
        self.object.save()
        return super().form_valid(form)

def report_detail(request, pk):
    comment_form = forms.CommentForm(request.POST or None)
    like_form = forms.LikeForm(request.POST or None)
    report = models.Report.objects.get(pk=pk)
    comment_list = models.Comment.objects.filter(report=report)
    if request.method == "POST":
        print("POST method")
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.report = report
            comment.save()
            return HttpResponseRedirect(reverse('report:detail', kwargs={'pk':pk}))
        if like_form.is_valid():
            like = like_form.save(commit=False)
            like.user = request.user
            like.report = report
            like.save()
            return HttpResponseRedirect(reverse('report:detail', kwargs={'pk':pk}))
    context = {
        'comment_form': comment_form,
        'like_form': like_form,
        'report': report,
        'comment_list': comment_list,
    }
    return render(request, 'report/report_detail.html', context)


class DetailReport(DetailView):
    model = models.Report

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test']='testText'
        return context

class DeleteReport(DeleteView):
    model = models.Report
    success_url = reverse_lazy('base:index')

    def get_queryset(self):
       qs = super().get_queryset()
       return qs.filter(user=self.request.user)

    def delete(self, *args, **kwargs):
        messages.error(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)

# class ListReport(ListView):
#     model=models.Report
#     paginate_by = 10
    # queryset = models.Report.objects.order_by('-header')[:2]

def list_page(request):
    report_list = models.Report.objects.all()
    paginator = Paginator(report_list, 25)
    page = request.GET.get('page')
    reports = paginator.get_page(page)
    context = {
        'report_list': reports,
    }
    return render(request, 'report/report_list.html', context)

def deleteLike(user, side):
    try:
        like = models.Like.objects.get(user=user, side=side)
        like.delete()
    except models.Like.DoesNotExist:
        pass

@login_required
def add_like(request, pk):
    report = models.Report.objects.get(pk=pk)
    try:
        like = models.Like.objects.get(user=request.user, side=True)
        like.delete()
    except models.Like.DoesNotExist:
        deleteLike(request.user, False)
        like = models.Like.objects.create(user=request.user, report=report, side=True)
        like.save()
    return HttpResponseRedirect(reverse('report:detail', kwargs={'pk':pk}))

@login_required
def add_unlike(request, pk):
    report = models.Report.objects.get(pk=pk)
    try:
        like = models.Like.objects.get(user=request.user, side=False)
        like.delete()
    except models.Like.DoesNotExist:
        deleteLike(request.user, True)
        like = models.Like.objects.create(user=request.user, report=report, side=False)
        like.save()
    return HttpResponseRedirect(reverse('report:detail', kwargs={'pk':pk}))
