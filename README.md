# 🍽️ Renato's Bistrô - Backend & Aplicação Web

![Django Version](https://img.shields.io/badge/Django-6.0.7-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

Sistema backend e plataforma web para o **Renato's Bistrô**, responsável pelo gerenciamento de cardápio, reservas e interface institucional. Projetado para ser executado em ambiente *serverless* na Vercel com entrega eficiente de arquivos estáticos.

---

## 📸 Demonstração do Projeto

| Página Inicial | Cardápio | Painel Admin |
| :---: | :---: | :---: |
| ![Home](docs/screenshots/home.png) | ![Cardápio](docs/screenshots/cardapio.png) | ![Admin](docs/screenshots/admin.png) |

---

## 🛠️ Tecnologias Utilizadas

- **Framework Principal:** [Django 6.0](https://www.djangoproject.com/)
- **Linguagem:** Python
- **Servidor de Estáticos:** [WhiteNoise](https://whitenoise.readthedocs.io/)
- **Banco de Dados:** SQLite (Desenvolvimento / Leitura)
- **Hospedagem & Deploy:** [Vercel (Serverless Functions)](https://vercel.com/)

---

## ⚙️ Arquitetura de Deploy (Vercel)

A aplicação utiliza uma estrutura otimizada para execução em funções *Serverless* da Vercel:

- **WSGI Handler:** Configurado em `api/index.py` para adaptar o ciclo de requisição do Django ao ambiente serverless.
- **Arquivos Estáticos:** Gerenciados pelo **WhiteNoise** com geração automatizada via `collectstatic` durante a inicialização.

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10+ instalado
- Git instalado

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/renatos-bistro-backend.git](https://github.com/SEU-USUARIO/renatos-bistro-backend.git)
   cd renatos-bistro-backend