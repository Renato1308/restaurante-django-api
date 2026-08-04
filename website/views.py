from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .models import Prato


def index(request):
  if request.method == 'POST':
    # Captura os dados enviados pelo formulário do HTML
    nome = request.POST.get('nome')
    email_cliente = request.POST.get('email')
    assunto_cliente = request.POST.get(
        'assunto', 'Mensagem do Formulário de Contato'
    )
    mensagem = request.POST.get('mensagem')

    # Monta o corpo do e-mail que você vai receber
    assunto = f'[Restaurante Contato] {assunto_cliente} - {nome}'
    corpo = (
        f'Você recebeu uma nova mensagem pelo site:\n\n'
        f'Nome: {nome}\n'
        f'E-mail: {email_cliente}\n\n'
        f'Mensagem:\n{mensagem}'
    )

    try:
      # Dispara o e-mail via SMTP do Gmail
      send_mail(
          assunto,
          corpo,
          settings.DEFAULT_FROM_EMAIL,
          [settings.RECIPIENT_ADDRESS],
          fail_silently=False,
      )
      messages.success(
          request, 'Sua mensagem foi enviada com sucesso! Em breve retornaremos.'
      )
    except Exception as e:
      # Exibe um aviso amigável caso ocorra algum erro na entrega
      messages.error(
          request,
          'Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente.',
      )

    return redirect('index')

  # Busca os pratos e categorias para exibir na página
  pratos = Prato.objects.filter(ativo=True)
  categorias = (
      Prato.objects.filter(ativo=True)
      .values_list('categoria', flat=True)
      .distinct()
  )

  context = {
      'pratos': pratos,
      'categorias': categorias,
  }
  return render(request, 'website/index.html', context)


# Alias 'home' para manter compatibilidade de rotas
home = index