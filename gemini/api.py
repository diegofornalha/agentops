from .core import MultiAgentSystem

def analyze_topic(topic):
    """Realiza uma análise completa do tópico."""
    system = MultiAgentSystem()
    return system.process(topic)

def get_final_analysis(topic):
    """Retorna apenas a síntese final do tópico."""
    results = analyze_topic(topic)
    return results['synthesis']

def get_detailed_research(topic):
    """Retorna a pesquisa detalhada com críticas."""
    results = analyze_topic(topic)
    return {
        'research': results['research'],
        'criticism': results['criticism']
    }

def get_improved_content(topic):
    """Retorna o conteúdo melhorado."""
    results = analyze_topic(topic)
    return results['improved'] 