import os
import google.generativeai as genai
from dotenv import load_dotenv

class MultiAgentSystem:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY não encontrada no ambiente")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
        self.agents = {
            'researcher': self._create_researcher(),
            'critic': self._create_critic(),
            'improver': self._create_improver(),
            'synthesizer': self._create_synthesizer()
        }
        
    def _create_researcher(self):
        return self.model.start_chat(history=[
            {"role": "user", "parts": ["Você é um pesquisador especializado. Seu objetivo é realizar pesquisas profundas e detalhadas sobre tópicos específicos."]},
            {"role": "model", "parts": ["""Entendi. Como pesquisador especializado, vou focar em:
1. Análise profunda do tópico
2. Coleta de informações relevantes
3. Identificação de tendências e padrões
4. Contextualização do assunto
5. Apresentação de dados e evidências"""]}
        ])
    
    def _create_critic(self):
        return self.model.start_chat(history=[
            {"role": "user", "parts": ["Você é um crítico analítico. Seu objetivo é analisar criticamente o conteúdo, identificando pontos fortes e fracos."]},
            {"role": "model", "parts": ["""Entendi. Como crítico analítico, vou focar em:
1. Análise objetiva do conteúdo
2. Identificação de inconsistências
3. Avaliação da qualidade das informações
4. Sugestões de melhorias
5. Feedback construtivo"""]}
        ])
    
    def _create_improver(self):
        return self.model.start_chat(history=[
            {"role": "user", "parts": ["Você é um especialista em melhorias. Seu objetivo é aperfeiçoar o conteúdo com base nas críticas recebidas."]},
            {"role": "model", "parts": ["""Entendi. Como especialista em melhorias, vou focar em:
1. Implementação de sugestões
2. Refinamento do conteúdo
3. Clareza e objetividade
4. Estruturação lógica
5. Enriquecimento com exemplos"""]}
        ])
    
    def _create_synthesizer(self):
        return self.model.start_chat(history=[
            {"role": "user", "parts": ["Você é um sintetizador de informações. Seu objetivo é criar uma síntese clara e concisa do conteúdo final."]},
            {"role": "model", "parts": ["""Entendi. Como sintetizador, vou focar em:
1. Consolidação das informações
2. Destaque dos pontos principais
3. Organização coerente
4. Clareza na comunicação
5. Conclusões relevantes"""]}
        ])
    
    def process(self, topic):
        # Fase 1: Pesquisa
        research_response = self.agents['researcher'].send_message(
            f"Realize uma pesquisa detalhada sobre: {topic}"
        )
        research = research_response.text
        
        # Fase 2: Crítica
        critic_response = self.agents['critic'].send_message(
            f"Analise criticamente esta pesquisa:\n\n{research}"
        )
        criticism = critic_response.text
        
        # Fase 3: Melhoria
        improver_response = self.agents['improver'].send_message(
            f"Melhore este conteúdo com base nas críticas:\n\nPesquisa:\n{research}\n\nCríticas:\n{criticism}"
        )
        improved = improver_response.text
        
        # Fase 4: Síntese
        synthesizer_response = self.agents['synthesizer'].send_message(
            f"Sintetize todo o processo:\n\nPesquisa inicial:\n{research}\n\nCríticas:\n{criticism}\n\nMelhorias:\n{improved}"
        )
        synthesis = synthesizer_response.text
        
        return {
            'research': research,
            'criticism': criticism,
            'improved': improved,
            'synthesis': synthesis
        } 