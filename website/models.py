from django.db import models

class Prato(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Prato")
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço (R$)")
    categoria = models.CharField(
        max_length=50, 
        verbose_name="Categoria", 
        help_text="Ex: Pizza, Lanche, Hambúrguer, Bebida, Vinho, Sobremesa, Porção..."
    )
    # Upload de imagem do próprio computador
    imagem = models.ImageField(upload_to='pratos/', blank=True, null=True, verbose_name="Foto do Computador")
    # Link da web como opção secundária
    imagem_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="OU URL da Imagem na Web")
    ativo = models.BooleanField(default=True, verbose_name="Exibir no Cardápio?")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Prato"
        verbose_name_plural = "Pratos do Cardápio"
        ordering = ['nome']

    def get_imagem(self):
        """Retorna a foto do computador se existir; caso contrário, a URL web."""
        if self.imagem:
            return self.imagem.url
        if self.imagem_url:
            return self.imagem_url
        return "https://via.placeholder.com/600x400?text=Sem+Foto"

    def __str__(self):
        return f"{self.nome} ({self.categoria})"