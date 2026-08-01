#!/bin/bash

# Imprime mensagens para acompanhar o log na Vercel
echo "Building the project..."

# Instala as dependências
python3.9 -m pip install -r requirements.txt

# Executa o collectstatic para o WhiteNoise/estáticos funcionar
python3.9 manage.py collectstatic --noinput --clear

echo "Build complete!"