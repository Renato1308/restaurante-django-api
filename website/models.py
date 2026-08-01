from django.db import models


class Prato(models.Model):
    CATEGORIA_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Prato Principal', 'Prato Principal'),
        ('Massa', 'Massa'),
        ('Lanche', 'Lanche / Hambúrguer'),
        ('Pizza', 'Pizza'),
        ('Porção', 'Porção'),
        ('Bebida', 'Bebida'),
        ('Vinho', 'Vinho'),
        ('Sobremesa', 'Sobremesa'),
        ('Outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Prato")
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Preço (R$)"
    )
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIA_CHOICES,
        default='Prato Principal',
        verbose_name="Categoria",
        help_text="Selecione a categoria para os filtros do cardápio",
    )

    # Upload de imagem (requer Cloudinary ou S3 na Vercel)
    imagem = models.ImageField(
        upload_to='pratos/',
        blank=True,
        null=True,
        verbose_name="Foto do Computador",
    )

    # Link da web como fallback perfeito
    imagem_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="OU URL da Imagem na Web",
    )

    ativo = models.BooleanField(
        default=True, verbose_name="Exibir no Cardápio?"
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Prato"
        verbose_name_plural = "Pratos do Cardápio"
        ordering = ['categoria', 'nome']

    @property
    def get_imagem(self):
        """Retorna a foto enviada; caso contrário, a URL web ou o placeholder."""
        if self.imagem:
            try:
                return self.imagem.url
            except ValueError:
                pass
        if self.imagem_url:
            return self.imagem_url
        return "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&auto=format&fit=crop&q=80"

    def __str__(self):
        return f"{self.nome} - R$ {self.preco} ({self.categoria})"