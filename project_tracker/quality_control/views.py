# from django.http import HttpResponse
# from django.views import View
from django.urls import reverse_lazy #, reverse
from .models import BugReport, FeatureRequest
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from .forms import BugReportForm, FeatureRequestForm

# def index(request):
#     bug_list_url = reverse('quality_control:bug_list')
#     feature_list_url = reverse('quality_control:feature_list')
#     html = f'''<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a></br>
#         <a href='{feature_list_url}'>Запросы на улучшение</a>'''
#     return HttpResponse(html)

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         bug_list_url = reverse('quality_control:bug_list')
#         feature_list_url = reverse('quality_control:feature_list')
#         html = f'''<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a></br>
#             <a href='{feature_list_url}'>Запросы на улучшение</a>'''
#         return HttpResponse(html)
    
def index(request):
    return render(request, 'quality_control/index.html')

# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
#     for bug in bugs:
#         bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> - {bug.status}</li>'
#     bugs_html += '</ul>'
#     return HttpResponse(bugs_html)

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'

# class BugDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug = self.object
#         response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
#         response_html += f'<p>Статус: {bug.status}</p>'
#         response_html += f'<p>Приоритет: {bug.priority}</p>'
#         project_detail_url = reverse('tasks:project_detail', kwargs={'project_id': bug.project.id})
#         response_html += f'<p>Проект: <a href="{project_detail_url}">{bug.project.name}</a></p>'
#         task_detail_url = reverse('tasks:task_detail', kwargs={'project_id': bug.project.id, 'task_id': bug.task.id})
#         response_html += f'<p>Задача: <a href="{task_detail_url}">{bug.task.name}</a></p>'
#         return HttpResponse(response_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bugreport': bug})

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     features_html = '<h1>Список запросов на улучшение</h1><ul>'
#     for feature in features:
#         features_html += f'<li><a href="{feature.id}/">{feature.title}</a> - {feature.status}</li>'
#     features_html += '</ul>'
#     return HttpResponse(features_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'

# class FeatureDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         feature = self.object
#         response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
#         response_html += f'<p>Статус: {feature.status}</p>'
#         response_html += f'<p>Приоритет: {feature.priority}</p>'
#         project_detail_url = reverse('tasks:project_detail', kwargs={'project_id': feature.project.id})
#         response_html += f'<p>Проект: <a href="{project_detail_url}">{feature.project.name}</a></p>'
#         task_detail_url = reverse('tasks:task_detail', kwargs={'project_id': feature.project.id, 'task_id': feature.task.id})
#         response_html += f'<p>Задача: <a href="{task_detail_url}">{feature.task.name}</a></p>'
#         return HttpResponse(response_html)

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'featurerequest': feature})

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'

# def bug_detail(request, bug_id):
#     return HttpResponse(f"<h1>Детали бага {bug_id}</h1>")

# def feature_id_detail(request, feature_id):
#     return HttpResponse(f"<h1>Детали улучшения {feature_id}</h1>")

def create_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bug_list')

def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:feature_list')

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    # success_url = reverse_lazy('quality_control:bug_list')

    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    # success_url = reverse_lazy('quality_control:feature_list')

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'feature_id': self.object.id})

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')

class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})
    
class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'feature_id': self.object.id})
