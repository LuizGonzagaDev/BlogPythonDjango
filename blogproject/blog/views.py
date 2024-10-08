from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts_list = Post.objects.all().order_by('-created_at')  # Lista de todos os posts
    
    # Defina o número de posts por página
    paginator = Paginator(posts_list, 5)  # Exibe 5 posts por página

    # Obtém o número da página a partir da URL (padrão é 1)
    page_number = request.GET.get('page')
    
    # Obtém os posts da página atual
    page_obj = paginator.get_page(page_number)
    
    # Passa o objeto da página para o template
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

