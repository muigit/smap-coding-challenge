from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    def get(self, request):
        # ビュー内で使用するコンテキストデータを作成
        context = {
            'Hello': 'Hello',
            'World': 'World',
        }
        # テンプレートをレンダリングし、コンテキストデータを渡す
        return render(request, 'app/index.html', context)
