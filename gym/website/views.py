from django.shortcuts import render
from .models import BannerImage, Introduction, Program, Counter,CounterImage, Coaches, Testimony,TestimonyImage, Packages, BlogSingle, Appointment, Gallery, Comment, Schedule, Contact, Process
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import datetime


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.all()
        context['introduction'] = Introduction.objects.last()
        context['process'] = Process.objects.all()
        context['program'] = Program.objects.all()
        context['counter'] = Counter.objects.last()
        context['counter_image'] = CounterImage.objects.last()
        context['coaches'] = Coaches.objects.all()
        context['testimony_image'] = TestimonyImage.objects.last()
        context['testimony'] = Testimony.objects.all()
        context['packages'] = Packages.objects.all()
        context['blog_single'] = BlogSingle.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['appointment'] = Appointment.objects.last()

        return context

class ProgramView(TemplateView):
    template_name = 'program.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProgramView,self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        context['program'] = Program.objects.all()
        context['packages'] = Packages.objects.all()
        context['gallery'] = Gallery.objects.all()

        return context

class CoachesView(TemplateView):
    template_name = 'coaches.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CoachesView, self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        context['coaches'] = Coaches.objects.all()
        context['gallery'] = Gallery.objects.all()
        
        return context

class ScheduleView(TemplateView):
    template_name = 'schedule.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        context['schedule'] = Schedule.objects.last()

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        context['introduction'] = Introduction.objects.last()
        context['gallery'] = Gallery.objects.all()
        context['testimony_image'] = TestimonyImage.objects.last()
        context['testimony'] = Testimony.objects.all()
        context['counter_image'] = CounterImage.objects.last()
        context['counter'] = Counter.objects.last()

        return context


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context= super(BlogView, self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        context['blog_single'] = BlogSingle.objects.all()

        return context


class BlogSingleView(TemplateView):
    template_name = 'blogSingle.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogSingleView, self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        blog_single = BlogSingle.objects.get(id=kwargs.get('pk'))
        blog_single.views += 1
        blog_single.save()
        context['blog_single'] = blog_single
        context['blog_single'] = BlogSingle.objects.get(id=kwargs.get('pk'))
        context['comment'] = Comment.objects.filter(blog_id=kwargs.get('pk'))
        context['popular'] = BlogSingle.objects.filter(views__gte=1)

        return context

class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryView,self).get_context_data(**kwargs)
        context['banner_image'] = BannerImage.objects.last()
        context['gallery'] = Gallery.objects.all()

        return context


def contactview(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        description = request.POST.get("description")

        Contact.objects.create(name=name, email=email, subject=subject, description=description)

        return HttpResponseRedirect('/')
    else:
        banner_image = BannerImage.objects.last()
        return render(request, 'contact.html', {'banner_image': banner_image})        

def commentview(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        description = request.POST.get("description")
        blog = BlogSingle.objects.get(pk=kwargs.get('pk'))
        Comment.objects.create(name=name, email=email, description=description, blog=blog)
        print(kwargs.get('pk'))

        return HttpResponseRedirect('/blog/'+ str(kwargs.get('pk')))
    else:
        banner_image = BannerImage.objects.last()
        return render(request,'blogSingle.html',{'banner_image':banner_image})


def appointmentview(request, *args, **kwargs):
    if request.method == 'POST':
        F_name = request.POST.get("F_name")
        L_name = request.POST.get("L_name") 
        date = request.POST.get("date")
        date = datetime.strptime(date,"%m/%d/%Y").date()
        time = request.POST.get("time")
        phone_no = request.POST.get("phone_no")
        message = request.POST.get("message")
        Appointment.objects.create(F_name=F_name, L_name=L_name, date=date, time=time ,phone_no=phone_no, message= message)

        return HttpResponseRedirect('/')
    else:
        banner_image = BannerImage.objects.last()
        return render(request, 'index.html', {'banner_image':banner_image})