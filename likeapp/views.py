from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        if LikeRecord.objects.filter(user=user, article=article).exists():
            messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            LikeRecord(user=user, article=article).save()
            article.like = article.like + 1
            article.save()

            messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영 되었습니다.')


            return super(LikeArticleView, self).get(self, *args, **kwargs)