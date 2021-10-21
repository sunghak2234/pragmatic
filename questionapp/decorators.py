from django.http import HttpResponseForbidden
from articleapp.models import Article
from questionapp.models import Question


def question_ownership_required(func):
    def decorated(request, *args, **kwargs):
        quesion = Question.objects.get(pk=kwargs['pk'])
        if not quesion.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

