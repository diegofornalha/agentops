import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure o Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def analyze_files(files_content):
    prompt = f"""
    Analise os seguintes arquivos e diretórios do projeto AgentOps e determine quais podem ser removidos:

    {files_content}

    Considere:
    1. Funcionalidade essencial para o projeto
    2. Dependências entre arquivos
    3. Impacto na estrutura do projeto
    4. Uso atual dos recursos
    
    Forneça uma lista detalhada do que pode ser removido e por quê.
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    files_to_analyze = {
        'llms': 'Diretório com providers e tracker.py',
        'partners': 'Diretório com integrações de terceiros',
        'exceptions.py': 'Definições de exceções customizadas',
        '__init__.py': 'Arquivo principal de inicialização',
        'client.py': 'Cliente principal do AgentOps',
        'cli.py': 'Interface de linha de comando',
        'config.py': 'Configurações do sistema',
        'decorators.py': 'Decoradores para tracking',
        'descriptor.py': 'Descritores para propriedades',
        'enums.py': 'Enumerações do sistema',
        'event.py': 'Classes de eventos',
        'helpers.py': 'Funções auxiliares',
        'host_env.py': 'Informações do ambiente',
        'http_client.py': 'Cliente HTTP',
        'log_config.py': 'Configuração de logs',
        'meta_client.py': 'Metaclasse do cliente',
        'session.py': 'Gerenciamento de sessões',
        'singleton.py': 'Implementação do padrão Singleton',
        'time_travel.py': 'Funcionalidade de time travel'
    }

    analysis = analyze_files(files_to_analyze)
    print("\nAnálise do Gemini:")
    print(analysis)

if __name__ == "__main__":
    main() 