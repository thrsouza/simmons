# Richards

Uma ferramenta de geração de documentação técnica baseada em transcrições de vídeos, utilizando IA para transformar
conhecimento verbal em documentação estruturada e clara.

## 📋 Sobre o Projeto

O Richards é um sistema baseado em CrewAI que utiliza múltiplos agentes especializados para processar transcrições de vídeos
técnicos e gerar documentação de alta qualidade. O projeto automatiza o processo de transformação de conhecimento tácito
(passado verbalmente) em documentação explícita e acessível.

## 🏗️ Arquitetura

O sistema é composto por 5 agentes especializados que trabalham em sequência:

1. **Analista de Conteúdo Técnico** - Extrai e estrutura tópicos principais
2. **Arquiteto de Software Sênior** - Valida e expande detalhes técnicos
3. **Redator Técnico** - Refina linguagem e estrutura para clareza
4. **Revisor** - Valida precisão técnica e compreensibilidade
5. **Publicador de Documentação** - Prepara e formata o material final

## 🚀 Instalação

### Pré-requisitos

- Python 3.12+
- UV (gerenciador de pacotes Python)

### Configuração

1. Clone o repositório:
```bash
git clone https://github.com/thrsouza/richards.git
cd richards
```

2. Instale as dependências:
```bash
uv sync
```

3. Configure as variáveis de ambiente:
```bash
cp .env.sample .env
# Edite o arquivo .env com sua chave da API OpenAI
```

## 💻 Uso

Execute o comando passando o arquivo de transcrição:

```bash
python main.py <caminho-para-arquivo-transcricao>
```

### Exemplo:
```bash
python main.py transcricao_video_tecnico.txt
```

O sistema irá:
1. Processar a transcrição através dos 5 agentes
2. Gerar documentação estruturada
3. Salvar o resultado como `output.md` no diretório atual

## 📁 Estrutura do Projeto

```
richards/
├── config/
│   ├── agents.yaml      # Configuração dos agentes
│   └── tasks.yaml       # Configuração das tarefas
├── knowledge/           # Base de conhecimento (arquivos de referência)
├── crew.py             # Definição da crew e agentes
├── main.py             # Ponto de entrada da aplicação
├── pyproject.toml      # Configuração do projeto
└── README.md
```

## ⚙️ Configuração

### Variáveis de Ambiente

- `OPENAI_API_KEY`: Sua chave da API OpenAI

### Base de Conhecimento

Adicione arquivos de referência na pasta `knowledge/` para enriquecer o contexto dos agentes durante o processamento.

## 🎯 Casos de Uso

- Transformar sessões de code review em documentação
- Converter explicações técnicas em guias estruturados
- Documentar decisões arquiteturais discutidas em reuniões
- Criar tutoriais a partir de demos e apresentações técnicas

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
