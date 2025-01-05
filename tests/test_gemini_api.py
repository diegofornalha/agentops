import unittest
from unittest.mock import patch, MagicMock
from gemini.api import (
    analyze_topic,
    get_final_analysis,
    get_detailed_research,
    get_improved_content
)

class TestGeminiAPI(unittest.TestCase):
    def setUp(self):
        self.mock_results = {
            'research': 'Test research',
            'criticism': 'Test criticism',
            'improved': 'Test improved',
            'synthesis': 'Test synthesis'
        }
        self.patcher = patch('gemini.api.MultiAgentSystem')
        self.mock_system = self.patcher.start()
        self.mock_instance = MagicMock()
        self.mock_instance.process.return_value = self.mock_results
        self.mock_system.return_value = self.mock_instance

    def tearDown(self):
        self.patcher.stop()

    def test_analyze_topic(self):
        """Testa a análise completa de um tópico"""
        result = analyze_topic("test topic")
        self.mock_system.assert_called_once()
        self.mock_instance.process.assert_called_once_with("test topic")
        self.assertEqual(result, self.mock_results)

    def test_get_final_analysis(self):
        """Testa a obtenção apenas da síntese final"""
        result = get_final_analysis("test topic")
        self.mock_system.assert_called_once()
        self.mock_instance.process.assert_called_once_with("test topic")
        self.assertEqual(result, self.mock_results['synthesis'])

    def test_get_detailed_research(self):
        """Testa a obtenção da pesquisa detalhada com críticas"""
        result = get_detailed_research("test topic")
        self.mock_system.assert_called_once()
        self.mock_instance.process.assert_called_once_with("test topic")
        self.assertEqual(result, {
            'research': self.mock_results['research'],
            'criticism': self.mock_results['criticism']
        })

    def test_get_improved_content(self):
        """Testa a obtenção do conteúdo melhorado"""
        result = get_improved_content("test topic")
        self.mock_system.assert_called_once()
        self.mock_instance.process.assert_called_once_with("test topic")
        self.assertEqual(result, self.mock_results['improved'])

if __name__ == '__main__':
    unittest.main() 