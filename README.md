# Sistema Multi-Agent com Gemini

Sistema especializado de múltiplos agentes usando Google Gemini e AgentOps para análise avançada de tópicos.

## Arquitetura

O sistema é composto por quatro agentes especializados:

1. **ResearcherAgent**: Realiza pesquisas profundas sobre um tópico
2. **CriticAgent**: Analisa criticamente o conteúdo produzido
3. **ImproverAgent**: Melhora o conteúdo baseado nas críticas
4. **SynthesizerAgent**: Sintetiza todas as informações em uma conclusão final

## Instalação

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows

# Instalar dependências
pip install -e .
```

## Configuração

Crie um arquivo `.env` com suas chaves de API:

```env
AGENTOPS_API_KEY=sua_chave_agentops
GEMINI_API_KEY=sua_chave_gemini
```

## Uso

### Uso Básico

```python
from gemini import MultiAgentSystem

# Criar instância do sistema
system = MultiAgentSystem()

# Processar um tópico
results = system.process("Seu tópico aqui")

# Acessar resultados
research = results['research']      # Pesquisa inicial
criticism = results['criticism']    # Análise crítica
improved = results['improved']      # Versão melhorada
synthesis = results['synthesis']    # Síntese final
```

### API Simplificada

```python
from gemini import (
    analyze_topic,           # Análise completa
    get_final_analysis,      # Apenas síntese
    get_detailed_research,   # Pesquisa e críticas
    get_improved_content     # Conteúdo melhorado
)

# Obter apenas a síntese final
synthesis = get_final_analysis("Seu tópico")

# Obter pesquisa detalhada com críticas
research = get_detailed_research("Seu tópico")

# Obter conteúdo melhorado
improved = get_improved_content("Seu tópico")
```

## Monitoramento

O sistema é integrado com o AgentOps, permitindo:

- Rastreamento de todas as ações dos agentes
- Monitoramento de performance
- Detecção e registro de erros
- Análise de custos

## Exemplos

### Análise de Tecnologia

```python
results = analyze_topic("Inteligência Artificial Quântica")
```

### Pesquisa de Mercado

```python
research = get_detailed_research("Tendências em Blockchain")
```

### Síntese de Informações

```python
summary = get_final_analysis("Impacto da IA na Medicina")
```

## Melhores Práticas

1. **Tópicos Claros**: Forneça tópicos específicos e bem definidos
2. **Contexto**: Quanto mais contexto, melhores os resultados
3. **Monitoramento**: Use o dashboard do AgentOps para acompanhar o desempenho
4. **Tratamento de Erros**: Sempre implemente tratamento de erros adequado
5. **Cache**: Considere implementar cache para resultados frequentes

## Limitações

- Requer chaves API válidas (AgentOps e Gemini)
- Processamento sequencial dos agentes
- Dependência de conexão com internet
- Custos associados ao uso das APIs
