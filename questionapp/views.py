from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms import forms
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, FormView
from questionapp.decorators import question_ownership_required
from questionapp.forms import QuestionCreationForm, QuestionSearchForm
from questionapp.models import Question


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionCreationForm
    template_name = 'questions/create.html'

    # 게시글 작성자의 writer를 저장
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('questionapp:detail', kwargs={'pk': self.object.pk})


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'target_question'
    template_name = 'questions/detail.html'


class QuestionListView(ListView):
    model = Question
    context_object_name = 'question_list'
    template_name = 'questions/list.html'
    paginate_by = 30

    def get_queryset(self):
        article_list = Question.objects.order_by('-id')
        return article_list

    def get(self, *args, **kwargs):
        return super(QuestionListView, self).get(self, *args, **kwargs)

    # def search(request):
    #      question_list = Question.objects.order_by('-id')
    #      q = request.POST.get('q', "")
    #
    #      if q:
    #         question_list = question_list.filter(title__icontains=q)
    #         return render(request, 'questions/list.html', {'question_list': question_list, 'q': q})
    #      else:
    #          return render(request, 'questions/list.html')



@method_decorator(question_ownership_required, 'get')
@method_decorator(question_ownership_required, 'post')
class QuestionDeleteView(DeleteView):
    model = Question
    context_object_name = 'target_question'
    template_name = 'questions/delete.html'
    success_url = reverse_lazy('questionapp:list')


class SearchFormView(FormView):
    template_name = 'questions/search.html'
    form_class = QuestionSearchForm

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        question_list = Question.objects.all().filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) |
                                               Q(content__icontains=searchWord)).distinct()

        context = { }
        context['form'] = form
        context['search_term'] = searchWord
        context['question_list'] = question_list

        return render(self.request, self.template_name, context)
