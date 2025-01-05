"""
Exemplo de uso da API simplificada do sistema Multi-Agent
"""

from api import (
    analyze_topic,
    get_final_analysis,
    get_detailed_research,
    get_improved_content
)
from rich.console import Console
from rich.table import Table

console = Console()

def demonstrate_api():
    # Criar tabela para resultados
    table = Table(title="🤖 Demonstração da API Multi-Agent")
    table.add_column("Função", style="cyan")
    table.add_column("Resultado", style="green")
    
    # Tópico para análise
    topic = "Impacto da IA na educação"
    
    try:
        # Análise completa
        console.print("\n[bold]1. Análise Completa[/]")
        results = analyze_topic(topic)
        for key, value in results.items():
            table.add_row(f"analyze_topic[{key}]", value[:100] + "...")
        
        # Apenas síntese
        console.print("\n[bold]2. Apenas Síntese[/]")
        synthesis = get_final_analysis(topic)
        table.add_row("get_final_analysis", synthesis[:100] + "...")
        
        # Pesquisa detalhada
        console.print("\n[bold]3. Pesquisa Detalhada[/]")
        research = get_detailed_research(topic)
        for key, value in research.items():
            table.add_row(f"get_detailed_research[{key}]", value[:100] + "...")
        
        # Conteúdo melhorado
        console.print("\n[bold]4. Conteúdo Melhorado[/]")
        improved = get_improved_content(topic)
        table.add_row("get_improved_content", improved[:100] + "...")
        
        # Exibir resultados
        console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]❌ Erro:[/] {str(e)}")

if __name__ == "__main__":
    demonstrate_api() 