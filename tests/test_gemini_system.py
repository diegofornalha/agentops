import unittest
from unittest.mock import patch, MagicMock
from gemini.core import MultiAgentSystem

class TestMultiAgentSystem(unittest.TestCase):
    @patch('gemini.core.genai')
    def setUp(self, mock_genai):
        self.mock_model = MagicMock()
        mock_genai.GenerativeModel.return_value = self.mock_model
        with patch.dict('os.environ', {'GEMINI_API_KEY': 'test_key'}):
            self.system = MultiAgentSystem()

    def test_initialization(self):
        """Testa se o sistema é inicializado corretamente com todos os agentes"""
        self.assertIn('researcher', self.system.agents)
        self.assertIn('critic', self.system.agents)
        self.assertIn('improver', self.system.agents)
        self.assertIn('synthesizer', self.system.agents)

    @patch.dict('os.environ', {'GEMINI_API_KEY': 'test_key'})
    def test_api_key_validation(self):
        """Testa se o sistema valida corretamente a chave API"""
        with patch('gemini.core.genai') as mock_genai:
            mock_model = MagicMock()
            mock_genai.GenerativeModel.return_value = mock_model
            system = MultiAgentSystem()
            self.assertIsNotNone(system)

    @patch.dict('os.environ', {}, clear=True)
    @patch('gemini.core.load_dotenv', return_value=True)
    def test_missing_api_key(self, mock_load_dotenv):
        """Testa se o sistema levanta erro quando falta a chave API"""
        with patch('gemini.core.genai') as mock_genai:
            with self.assertRaises(ValueError) as cm:
                MultiAgentSystem()
            self.assertEqual(str(cm.exception), "GEMINI_API_KEY não encontrada no ambiente")

    def test_process_flow(self):
        """Testa o fluxo completo de processamento"""
        # Mock das respostas dos agentes
        mock_response = MagicMock()
        mock_response.text = "Test response"
        self.mock_model.start_chat().send_message.return_value = mock_response

        topic = "test topic"
        result = self.system.process(topic)

        self.assertIn('research', result)
        self.assertIn('criticism', result)
        self.assertIn('improved', result)
        self.assertIn('synthesis', result)

        # Verifica se cada agente foi chamado
        self.assertEqual(result['research'], "Test response")
        self.assertEqual(result['criticism'], "Test response")
        self.assertEqual(result['improved'], "Test response")
        self.assertEqual(result['synthesis'], "Test response")

if __name__ == '__main__':
    unittest.main() 