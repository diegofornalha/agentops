"""
Exemplo de uso do sistema Multi-Agent com Gemini
"""

import os
from dotenv import load_dotenv
from core import MultiAgentSystem
from rich.console import Console
from rich.panel import Panel

# Carregar variáveis de ambiente
load_dotenv()

def main():
    # Inicializar console para output formatado
    console = Console()
    
    # Criar instância do sistema multi-agent
    system = MultiAgentSystem()
    
    # Tópico para análise
    topic = "O futuro da programação com IA"
    
    console.print(Panel.fit("🤖 Iniciando análise multi-agent", title="Sistema Multi-Agent"))
    
    try:
        # Processar o tópico
        results = system.process(topic)
        
        # Exibir resultados
        console.print("\n[bold cyan]📚 Pesquisa Inicial:[/]")
        console.print(results['research'])
        
        console.print("\n[bold yellow]🔍 Análise Crítica:[/]")
        console.print(results['criticism'])
        
        console.print("\n[bold green]✨ Conteúdo Melhorado:[/]")
        console.print(results['improved'])
        
        console.print("\n[bold magenta]📊 Síntese Final:[/]")
        console.print(results['synthesis'])
        
    except Exception as e:
        console.print(f"[bold red]❌ Erro:[/] {str(e)}")
    
    console.print(Panel.fit("✅ Análise concluída", title="Sistema Multi-Agent"))

if __name__ == "__main__":
    main() 