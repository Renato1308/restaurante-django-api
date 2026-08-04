from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render

from .models import Prato


def index(request):
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário do HTML
        nome = request.POST.get('nome', '').strip()
        email_cliente = request.POST.get('email', '').strip()
        assunto_cliente = request.POST.get('assunto', '').strip() or 'Mensagem do Formulário de Contato'
        mensagem = request.POST.get('mensagem', '').strip()

        # Monta o corpo do e-mail que você vai receber
        assunto = f'[Restaurante Contato] {assunto_cliente} - {nome}'
        corpo = (
            f'Você recebeu uma nova mensagem pelo site:\n\n'
            f'Nome: {nome}\n'
            f'E-mail: {email_cliente}\n\n'
            f'Mensagem:\n{mensagem}'
        )

        # Destinatário seguro (Usa RECIPIENT_ADDRESS, ou EMAIL_HOST_USER se não existir)
        destino = getattr(settings, 'RECIPIENT_ADDRESS', getattr(settings, 'EMAIL_HOST_USER', None))

        try:
            # Envio seguro utilizando EmailMessage para permitir reply_to (responder direto ao cliente)
            email = EmailMessage(
                subject=assunto,
                body=corpo,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[destino],
                reply_to=[email_cliente] if email_cliente else None,
            )
            email.send(fail_silently=False)

            messages.success(
                request, 'Sua mensagem foi enviada com sucesso! Em breve retornaremos.'
            )
        except Exception as e:
            # Log do erro no console da Render para facilitar o debug se necessário
            print(f"Erro ao enviar e-mail via SMTP: {e}")
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