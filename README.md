# Teste de Modelos Ollama

Este projeto testa modelos de linguagem Ollama (Gemma e Llama) rodando em containers Docker.

## Pré-requisitos

- Docker
- Docker Compose
- Python 3.8+

## Como executar

### 1. Iniciar o container Ollama

```bash
# Construir e iniciar o container
docker-compose up -d --build

# Verificar se está rodando
docker-compose ps
```

### 2. Aguardar o download dos modelos

O container irá baixar automaticamente os modelos:
- `gemma3:1b`
- `llama3.2:1b`

Isso pode levar alguns minutos na primeira execução.

### 3. Instalar dependências Python

```bash
pip install langchain-ollama langchain-core pydantic
```

### 4. Executar os testes

```bash
python test_models.py
```

## O que o teste faz

O script `test_models.py`:
- Conecta aos modelos Ollama rodando no Docker
- Gera perfis fictícios de pessoas baseados em temas
- Parseia as respostas em JSON estruturado
- Exibe os resultados formatados

## Parar o container

```bash
docker-compose down
```

## Estrutura do projeto

```
.
├── docker-compose.yml    # Configuração do Docker
├── Dockerfile           # Imagem do container
├── test_models.py       # Script de teste
└── README.md           # Este arquivo
```

## Solução de problemas

- **Porta 11434 já em uso**: Pare outros serviços Ollama locais
- **Erro de conexão**: Aguarde o container inicializar completamente
- **Modelos não encontrados**: Verifique os logs com `docker-compose logs`
