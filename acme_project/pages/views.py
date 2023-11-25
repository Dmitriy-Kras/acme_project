from birthday.models import Birthday
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Birthday.objects.count()
        return context
