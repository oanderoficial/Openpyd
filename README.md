# Openpyd

# Assistente IA Especializado em Python

**Openpyd** é uma aplicação web de chat inteligente que utiliza IA para auxiliar desenvolvedores Python. O projeto integra o modelo GPT-5-mini através da API Requesty, oferecendo respostas especializadas, exemplos de código e suporte ao desenvolvimento.

## Funcionalidades

- **Chat Inteligente**: Conversas contextuais 
- **Especialização Python**: Respostas otimizadas para desenvolvimento Python
- **Interface Moderna**: Design responsivo com tema moderno
- **Syntax Highlighting**: Destaque de código com Prism.js
- **API RESTful**: Backend robusto com FastAPI
- **Deploy Simplificado**: Configurado para Render

 **Teste aqui:** https://openpyd.onrender.com

<img width="2450" height="1832" alt="image" src="https://github.com/user-attachments/assets/013dc574-b202-40da-89d4-6d48237610ad" />

<img width="2450" height="1832" alt="image" src="https://github.com/user-attachments/assets/2b9b238c-feb1-4757-b2b4-f18036724eeb" />

<img width="2450" height="1832" alt="image" src="https://github.com/user-attachments/assets/4fe4ba46-4fd3-4c94-bebc-6a4a61cfcc12" />

## Tecnologias e Arquitetura

### Backend
- **FastAPI**: Framework web moderno e rápido para Python
- **Uvicorn**: Servidor ASGI de alta performance
- **Pydantic**: Validação de dados e serialização
- **OpenAI SDK**: Integração com APIs de IA
- **Python-dotenv**: Gerenciamento de variáveis de ambiente

### Frontend
- **HTML5/CSS3**: Interface responsiva e moderna
- **JavaScript ES6+**: Funcionalidades interativas
- **Prism.js**: Syntax highlighting para código
- **Font Awesome**: Ícones vetoriais
- **Google Fonts**: Tipografia Inter

### Integração IA
- **Requesty API**: Roteador compatível com OpenAI
- **GPT-5-mini**: Modelo de linguagem otimizado
- **Contexto Especializado**: Prompts específicos para Python

## Função das Bibliotecas Principais

### FastAPI
- **Propósito**: Framework web principal do backend
- **Funcionalidades**: 
  - Criação de endpoints REST
  - Validação automática de dados
  - Documentação automática (Swagger)
  - Suporte nativo a async/await
  - Middleware CORS para integração frontend

### Uvicorn
- **Propósito**: Servidor ASGI para executar a aplicação FastAPI
- **Funcionalidades**:
  - Alta performance com suporte assíncrono
  - Hot reload durante desenvolvimento
  - Compatibilidade com deploy em produção

### Python-dotenv
- **Propósito**: Gerenciamento seguro de variáveis de ambiente
- **Funcionalidades**:
  - Carregamento de configurações do arquivo .env
  - Separação entre configuração e código
  - Segurança para chaves de API

### OpenAI
- **Propósito**: SDK oficial para integração com APIs de IA
- **Funcionalidades**:
  - Comunicação com modelos de linguagem
  - Compatibilidade com Requesty (OpenAI-compatible)
  - Gerenciamento de conversas e contexto
  - Streaming de respostas (se necessário)

## Instalação e Configuração

### Pré-requisitos
- Python 3.13+
- Poetry (recomendado) ou pip
- Conta na Requesty para API key

### Instalação

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd Openpyd_priv
```

2. **Instale as dependências**:
```bash
# Com Poetry (recomendado)
poetry install

# Ou com pip
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**:
```bash
# Crie o arquivo .env na raiz do projeto
echo "REQUESTY_API_KEY=sua_chave_aqui" > .env
```

4. **Execute a aplicação**:
```bash
# Com Poetry
poetry run uvicorn main:app --reload

# Ou diretamente
uvicorn main:app --reload
```

5. **Acesse a aplicação**:
   - Local: http://localhost:8000
   - A interface web será carregada automaticamente

## Deploy

### Render
O projeto está configurado para deploy automático no Render:

- **Frontend + Backend**: Servidos pela mesma aplicação FastAPI
- **Variáveis de ambiente**: Configuradas no painel do Render
- **Build automático**: A partir do repositório Git

### Configurações necessárias no Render:

REQUESTY_API_KEY=sua_chave_da_requesty


## API Endpoints

### POST /chat
Endpoint principal para conversas com a IA.

**Request Body**:
```json
{
  "pergunta": "Como criar uma lista em Python?",
  "historico": [
    {"role": "user", "content": "Olá"},
    {"role": "assistant", "content": "Olá! Como posso ajudar?"}
  ]
}
```

**Response**:
```json
{
  "resposta": "Para criar uma lista em Python, você pode usar colchetes []..."
}
```

### GET /
Retorna a interface web (index.html).

## Segurança

- **API Keys**: Armazenadas em variáveis de ambiente
- **CORS**: Configurado para permitir origens necessárias
- **Validação**: Dados validados com Pydantic
- **Rate Limiting**: Implementado pela Requesty API

## Interface

- **Design Responsivo**: Funciona em desktop e mobile
- **Tema Moderno**: Tema novo recriado com um visual moderno.
- **Syntax Highlighting**: Código Python destacado automaticamente
- **Animações Suaves**: Transições e feedback visual
- **Glassmorphism**: Efeitos visuais modernos

## Links Úteis

- **Aplicação**: https://openpyd.onrender.com/
- **Requesty Dashboard**: https://app.requesty.ai/
- **Render Dashboard**: https://dashboard.render.com
- **FastAPI Docs**: Disponível em `/docs` quando executando localmente


## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT no arquivo LICENSE.

##  Autor

**Anderson B Silva (Ander)**
- GitHub: [@oanderoficial](https://github.com/oanderoficial)
- Email: andersoncomercial@pm.me

---

*Desenvolvido com ❤️ para a comunidade Python*
