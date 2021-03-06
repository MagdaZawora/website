from django.shortcuts import render, HttpResponse
from django.utils.timezone import now
from django.views import generic

from .models import Event, News, Project


class IndexView(generic.TemplateView):
    """
    Home page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        Show only future events
        """
        context = super().get_context_data(**kwargs)
        context['future_events'] = Event.objects.filter(
            ended_at__gt=now()
        ).order_by('started_at')
        return context


class EventsListView(generic.ListView):
    """
    All events on one site
    """
    model = Event

    def get_context_data(self, **kwargs):
        """
        Show only future events
        """
        context = super().get_context_data(**kwargs)
        context['future_events'] = context['object_list'].filter(
            ended_at__gt=now(),
        ).order_by('-started_at')
        context['past_events'] = context['object_list'].filter(
            ended_at__lte=now()
        ).order_by('-started_at')
        return context


class ProjectsListView(generic.ListView):
    model = Project


class MeetingsView(generic.TemplateView):
    """
    Meetings we are
    """
    template_name = 'meetings.html'


class MembersView(generic.TemplateView):
    """
    Information for members page
    """
    template_name = 'members.html'


class HistoryView(generic.TemplateView):
    """
    Our history page
    """
    template_name = 'history.html'


class PartnersView(generic.TemplateView):
    """
    Partners and Sponsors page
    """
    template_name = 'partners.html'


class ProjectsView(generic.TemplateView):
    """
    Projects list page
    """
    template_name = 'projects.html'


class ContactView(generic.TemplateView):
    """
    Contact page
    """
    template_name = 'contact.html'


class MicrobitView(generic.TemplateView):
    """
    Contact page
    """
    template_name = 'microbit.html'

class NewsView(generic.ListView):
    model = News
    template_name = 'plpug/news.html'


def agree_on_cookie_store(request):
    """
    Used by ajax to say agree for storing cookie
    :param request:
    :return: confirmation
    """
    request.session['isagree'] = True
    return HttpResponse("OK")
