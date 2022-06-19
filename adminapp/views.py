from django.shortcuts import render, redirect, get_object_or_404
import csv
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from mainapp.forms import TemplateForm

from mainapp.models import Victim
from email_list.models import TemplateList, EmailList
from campaign.models import CampaignList
# Create your views here.

#
# @method_decorator(login_required(login_url="login"),name='dispatch')
# class Home(ListView):
#     model = Email
#     context_object_name = "emails"
#     template_name = 'panel/pages/home.html'
#     paginate_by = 25
#
#     def get_queryset(self):
#         query = self.request.GET.get("search")
#         if query:
#             return Email.objects.filter(
#                 Q(first_name__icontains=query) |
#                 Q(last_name__icontains=query) |
#                 Q(email__icontains=query) ,
#                 user=self.request.user
#             ).order_by("-id")
#         else:
#             return Email.objects.filter(user=self.request.user, activated=True).order_by('-id')

@login_required(login_url="login")
def Home(request):
    context = {}

    return render(request, 'panel/pages/adv.html', context)

@login_required(login_url='login')
def books(request):


    return render(request, 'panel/pages/all_books.html', context)


# @method_decorator(login_required(login_url="login"),name='dispatch')
# class LinkList(ListView):
#     model = Link
#     context_object_name = "links"
#     template_name = 'panel/pages/all_books.html'
#     paginate_by = 25
#
#     def get_queryset(self):
#         query = self.request.GET.get("search")
#         if query:
#             return Link.objects.filter(
#                 Q(title__icontains=query) |
#                 Q(description__icontains=query),
#                 user=self.request.user
#             ).order_by("-id")
#         else:
#             return Link.objects.filter(user=self.request.user).order_by('-id')



@login_required(login_url='login')
def add_book(request):
    # form = LinkForm(request.POST or None, request.FILES or None)
    #
    # if request.method == "POST":
    #     if form.is_valid():
    #         link = form.save(commit=False)
    #         link.user = request.user
    #         link.save()
    #         messages.success(request, 'Link is successfully added.')
    #
    # context = {
    #     'form':form
    # }
    return render(request, 'panel/pages/add.html')

@login_required(login_url='login')
def edit_book(request, id):
    # instance = Link.objects.filter(pk=id).last()
    # form = LinkForm(request.POST or None,request.FILES or None, instance=instance)
    # if request.method == "POST":
    #     form.save()
    #     messages.success(request, "Link is successfully updated.")
    #
    # context = {
    #     "form":form
    # }
    return render(request, 'panel/pages/edit.html', context)

@login_required(login_url='login')
def delete_book(request, id):
    # if request.method == "POST":
    #     link = Link.objects.filter(pk=id).last()
    #     link.delete()
    #     messages.success(request, 'Link is successfully added.')

    return redirect("adminapp:books")



@login_required(login_url='login')
def add_template(request):
    form = TemplateForm(request.POST or None)
    print(form.errors)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Link is successfully added.')
    context = {
         'form':form
     }

    return render(request, 'panel/template_app/add.html', context)



@login_required(login_url='login')
def edit_template(request, id):
    tl = TemplateList.objects.get(pk=id)

    form = TemplateForm(request.POST or None, instance=tl)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Link is successfully added.')

    context = {
        'form':form
    }
    return render(request, 'panel/template_app/edit.html', context)


@login_required(login_url='login')
def delete_template(request, id):
    if request.method == "POST":
        link = TemplateList.objects.get(pk=id)
        link.delete()
        messages.success(request, 'Link is successfully added.')

    return redirect("adminapp:books")



# -----------------------   ----------------------------------------


@method_decorator(login_required(login_url="login"),name='dispatch')
class List(ListView):
    model = EmailList
    context_object_name = "lists"
    template_name = 'panel/list/all.html'
    paginate_by = 25

    # def get_queryset(self):
    #     query = self.request.GET.get("search")
    #     if query:
    #         return List.objects.filter(
    #             #Q(title__icontains=query) |
    #             #Q(description__icontains=query),
    #             #user=self.request.user
    #         ).order_by("-id")
    #     else:
    #     return List.objects.filter(user=self.request.user).order_by('-id')


@login_required(login_url="login")
def edit_list(request, id):
    list = EmailList.objects.get(pk=id)

    context = {
        "list":list
    }
    return render(request, 'panel/list/edit.html', context)


# -------------------------- campaign ------------------------------------

@method_decorator(login_required(login_url="login"),name='dispatch')
class CList(ListView):
    model = CampaignList
    context_object_name = "clists"
    template_name = 'panel/campaign/all.html'
    paginate_by = 25



@login_required(login_url="login")
def edit_campaign(request, id):
    campaign = CampaignList.objects.get(pk=id)

    context = {
        "campaign":campaign,
    }
    return render(request, 'panel/list/edit.html', context)
