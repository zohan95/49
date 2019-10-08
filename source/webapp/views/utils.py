from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views import View
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


class UpdateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = self.model.objects.get(pk=pk)
        form = self.form_class(instance=obj)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.pkey = pk
        obj = self.model.objects.get(pk=pk)
        form = self.form_class(data=request.POST, instance=obj)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = {'form': form, 'pk': self.pkey}
        return render(self.request, self.template_name, context)

    def get_redirect_url(self):
        return self.redirect_url


class DeleteView(View):
    template_name = None
    model = None
    redirect_url = ''
    confirmation = True

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = self.model.objects.get(pk=pk)
        if self.confirmation:
            context = {'type': obj}
            return render(request, self.template_name, context)
        else:
            try:
                obj.delete()
            except ProtectedError:
                return render(request, 'error_page.html')
            return redirect(self.get_redirect_url())

    def post(self, request, *args, **kwargs):
        obj = self.model.objects.get(pk=kwargs.get('pk'))
        try:
            obj.delete()
        except ProtectedError:
            return render(request, 'error_page.html')
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return self.redirect_url
