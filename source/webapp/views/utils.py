from django.views.generic import TemplateView


class DetailView(TemplateView):
    model = None
    context_key = 'objects'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.model.objects.get(pk=pk)
        return context


class ListView(TemplateView):
    model = None
    context_key = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.model.objects.all()
        return context

