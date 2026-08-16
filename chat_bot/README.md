# Vikir — Assistente IA no Terminal

Bot de chat baseado em Google Gemini com interface no terminal usando Rich.
Feito por Phelpy. Projeto open-source para portfólio.

## Funcionalidades

- Chat interativo no terminal com uma IA configurada via Gemini
- Interface visual com **Rich** (banners, painéis, markdown, cores)
- Comandos de sessão: limpar histórico, ajudar, ver modelo, sair
- Sistema de "pensamento" encapsulado na classe `Vikir_mind`
- Configuração via `.env` (chave da API GMINI_CACHE_API_KEY_2)
- Respostas fatiadas e tratadas quando a API retorna múltiplos blocos

## Tecnologias

- Python 3.10+
- `google-generativeai` — cliente oficial Gemini
- `python-dotenv` — carregamento de variáveis de ambiente
- `rich` — terminal formatado

## Arquitetura

```
terminal.py          → loop de chat, comandos, interface Rich
mind.py              → classe Vikir_mind: configuração Gemini + método pensar()
requirements.txt     → dependências
.env (não commitado) → GEMINI_API_KEY
```

- **mind.py**: gerencia o modelo Gemini, instrução de sistema, histórico de chat e envio de mensagens.
- **terminal.py**: loop REPL com comandos (`/sair`, `/clear`, `/help`, `/model`, `/history`), renderização via Rich.

## Pré-requisitos

- Python 3.10+
- Conta no Google AI Studio com chave de API Gemini
- FFmpeg não é necessário para este projeto

## Instalação

```bash
# 1. Clone o repositório
git clone <url-do-repo>
cd chat_bot

# 2. Crie e ative ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/macOS

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# Edite .env com sua chave:
#   GEMINI_API_KEY=sua_chave_aqui
```

## Uso

```bash
python terminal.py
```

### Comandos

| Comando                     | Descrição                       |
|-----------------------------|---------------------------------|
| `/sair`, `/exit`, `/quit`   | Sair do chat                    |
| `/clear`, `/limpar`         | Limpar histórico da sessão      |
| `/help`, `/ajuda`, `/?`     | Mostrar lista de comandos       |
| `/model`                    | Mostrar modelo atual            |
| `/history`, `/historico`    | Mostrar tamanho do histórico    |

Digite qualquer mensagem para conversar com Vikir.

## Estrutura do projeto

```
chat_bot/
├── terminal.py       # Interface de terminal (Rich)
├── mind.py           # Motor de IA (Gemini)
├── requirements.txt  # Dependências Python
├── README.md         # Este arquivo
└── .env              # Variáveis de ambiente (não commitar)
```

## Roadmap

### Concluído
- [x] Classe Vikir_mind com Gemini
- [x] Terminal com Rich e comandos
- [x] Fatiamento de respostas múltiplas
- [x] Configuração via `.env`

### Em desenvolvimento
- [ ] Sistema de memória e contexto maior
- [ ] Persistência de histórico entre sessões
- [ ] Logs de sessão

## Status

EM DESENVOLVIMENTO ATIVO.

## Contribuição

Contribuições são bem-vindas.

1. Fork o repositório
2. Crie um branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Autor

Desenvolvido por Phelpy.

## Licença

MIT — veja o arquivo `LICENSE` para detalhes.

## Agradecimentos

- Google AI Studio pelo acesso ao Gemini
- Comunidade open-source Python
