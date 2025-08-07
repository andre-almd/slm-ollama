# Use a imagem base do Ubuntu
FROM ubuntu:22.04
 
# Evitar prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive
 
# Atualizar pacotes, instalar dependências, Ollama e criar diretórios
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL https://ollama.ai/install.sh | sh \
    && mkdir -p /root/.ollama
 
# Expor porta padrão do Ollama
EXPOSE 11434
 
# Script de inicialização
RUN echo '#!/bin/bash\n\
# Iniciar Ollama em background\n\
ollama serve &\n\
\n\
# Aguardar o serviço inicializar\n\
sleep 10\n\
\n\
# Baixar o modelo Gemma3:1b\n\
ollama pull gemma3:1b\n\
ollama pull llama3.2:1b\n\
\n\
# Manter o container rodando\n\
wait' > /start.sh && chmod +x /start.sh
 
# Comando padrão
CMD ["/start.sh"]
