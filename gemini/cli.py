#!/usr/bin/env python3
import os
import sys
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from dotenv import load_dotenv

from . import (
    MultiAgentSystem,
    analyze_topic,
    get_final_analysis,
    get_detailed_research,
    get_improved_content
)

console = Console()

def setup_environment():
    """Configura o ambiente carregando as variáveis necessárias."""
    load_dotenv()
    required_vars = ['AGENTOPS_API_KEY', 'GEMINI_API_KEY']
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        console.print(f"[red]Erro: Faltam as seguintes variáveis de ambiente: {', '.join(missing)}")
        sys.exit(1)

def process_with_progress(func, topic, description):
    """Executa uma função com barra de progresso."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task(description, total=None)
        try:
            result = func(topic)
            progress.update(task, completed=True)
            return result
        except Exception as e:
            progress.update(task, completed=True)
            console.print(f"[red]Erro durante o processamento: {str(e)}")
            sys.exit(1)

def display_results(results, mode):
    """Exibe os resultados formatados."""
    if mode == "completo":
        sections = {
            "Pesquisa": results.get('research', ''),
            "Críticas": results.get('criticism', ''),
            "Melhorias": results.get('improved', ''),
            "Síntese": results.get('synthesis', '')
        }
        for title, content in sections.items():
            console.print(Panel(content, title=title, border_style="blue"))
    else:
        console.print(Panel(str(results), title="Resultado", border_style="blue"))

def main():
    parser = argparse.ArgumentParser(description="CLI do Sistema Multi-Agent com Gemini")
    parser.add_argument("topic", help="Tópico para análise")
    parser.add_argument(
        "--mode",
        choices=["completo", "sintese", "pesquisa", "melhoria"],
        default="completo",
        help="Modo de análise"
    )
    
    args = parser.parse_args()
    setup_environment()
    
    console.print(f"[blue]Analisando tópico:[/blue] {args.topic}")
    console.print("[blue]Modo:[/blue] {args.mode}\n")
    
    try:
        if args.mode == "completo":
            results = process_with_progress(
                analyze_topic,
                args.topic,
                "Realizando análise completa..."
            )
        elif args.mode == "sintese":
            results = process_with_progress(
                get_final_analysis,
                args.topic,
                "Gerando síntese..."
            )
        elif args.mode == "pesquisa":
            results = process_with_progress(
                get_detailed_research,
                args.topic,
                "Realizando pesquisa detalhada..."
            )
        else:  # melhoria
            results = process_with_progress(
                get_improved_content,
                args.topic,
                "Gerando conteúdo melhorado..."
            )
        
        display_results(results, args.mode)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Operação cancelada pelo usuário.")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Erro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 