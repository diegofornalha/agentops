# AgentOps Documentation

Este é o repositório da documentação do AgentOps, utilizando Mintlify para gerar a documentação.

## 📁 Estrutura do Projeto

```
docs/
├── v1/                    # Documentação atual
│   ├── concepts/         # Conceitos fundamentais
│   ├── examples/         # Exemplos de uso
│   ├── integrations/     # Integrações com outras ferramentas
│   └── usage/           # Guias de uso
├── images/               # Imagens e recursos visuais
├── snippets/            # Trechos de código reutilizáveis
└── mint.json            # Configuração do Mintlify
```

## 🚀 Desenvolvimento Local

1. Instale o CLI do Mintlify:

```bash
npm i -g mintlify
```

2. Instale as dependências:

```bash
npm install
```

3. Execute o servidor de desenvolvimento:

```bash
mintlify dev
```

## 📝 Contribuindo

1. Atualize apenas os arquivos na pasta `v1/`
2. Coloque imagens em `images/`
3. Use snippets em `snippets/` para código reutilizável
4. Teste localmente antes de fazer commit

## 🔄 Deploy

O deploy é automático após push para a branch principal.

## 🔧 Troubleshooting

- Se `mintlify dev` não funcionar, execute `mintlify install`
- Se uma página carregar como 404, verifique se está no diretório com `mint.json`
- Para problemas com imagens, verifique os caminhos em `mint.json`
