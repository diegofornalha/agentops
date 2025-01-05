import os
from dotenv import load_dotenv
import google.generativeai as genai
import agentops
from core import MultiAgentSystem

load_dotenv()

# Configurar Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def analyze_examples():
    system = MultiAgentSystem()
    topic = """
    Analise a pasta examples do projeto e determine:
    1. Quais exemplos devem ser mantidos considerando que agora temos um sistema multi-agent isolado
    2. Como reorganizar os exemplos mantidos
    3. Quais pastas podem ser removidas com segurança
    4. Como estruturar os novos exemplos do sistema multi-agent
    """
    
    results = system.process(topic)
    return results

if __name__ == "__main__":
    results = analyze_examples()
    print("\nAnálise do ResearcherAgent:")
    print(results['research'])
    print("\nCríticas do CriticAgent:")
    print(results['criticism'])
    print("\nMelhorias do ImproverAgent:")
    print(results['improved'])
    print("\nSíntese Final:")
    print(results['synthesis']) 