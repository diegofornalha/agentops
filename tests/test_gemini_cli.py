import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
from gemini.cli import main, setup_environment, process_with_progress, display_results

class TestGeminiCLI(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = self.original_stdout
        self.held_output.close()

    @patch.dict('os.environ', {
        'AGENTOPS_API_KEY': 'test_key',
        'GEMINI_API_KEY': 'test_key'
    })
    @patch('gemini.cli.load_dotenv', return_value=True)
    def test_setup_environment_success(self, mock_load_dotenv):
        """Testa se o ambiente é configurado corretamente com as variáveis necessárias"""
        setup_environment()  # Não deve levantar exceção

    @patch.dict('os.environ', {}, clear=True)
    @patch('gemini.cli.load_dotenv', return_value=True)
    def test_setup_environment_failure(self, mock_load_dotenv):
        """Testa se o setup falha quando faltam variáveis de ambiente"""
        with self.assertRaises(SystemExit) as cm:
            setup_environment()
        self.assertEqual(cm.exception.code, 1)

    def test_process_with_progress_success(self):
        """Testa o processamento com barra de progresso"""
        with patch('gemini.cli.analyze_topic') as mock_analyze:
            mock_analyze.return_value = "Test result"
            result = process_with_progress(mock_analyze, "test topic", "Processing...")
            self.assertEqual(result, "Test result")

    def test_process_with_progress_error(self):
        """Testa o tratamento de erro durante o processamento"""
        with patch('gemini.cli.analyze_topic') as mock_analyze:
            mock_analyze.side_effect = Exception("Test error")
            with self.assertRaises(SystemExit) as cm:
                process_with_progress(mock_analyze, "test topic", "Processing...")
            self.assertEqual(cm.exception.code, 1)

    def test_display_results_complete(self):
        """Testa a exibição de resultados no modo completo"""
        results = {
            'research': 'Test research',
            'criticism': 'Test criticism',
            'improved': 'Test improved',
            'synthesis': 'Test synthesis'
        }
        display_results(results, "completo")
        output = self.held_output.getvalue()
        self.assertIn("Test research", output)
        self.assertIn("Test criticism", output)
        self.assertIn("Test improved", output)
        self.assertIn("Test synthesis", output)

    def test_display_results_simple(self):
        """Testa a exibição de resultados em modo simples"""
        results = "Test result"
        display_results(results, "sintese")
        output = self.held_output.getvalue()
        self.assertIn("Test result", output)

    @patch('sys.argv', ['cli.py', 'test topic', '--mode', 'completo'])
    @patch('gemini.cli.analyze_topic')
    @patch.dict('os.environ', {
        'AGENTOPS_API_KEY': 'test_key',
        'GEMINI_API_KEY': 'test_key'
    })
    def test_main_complete_mode(self, mock_analyze):
        """Testa a execução principal no modo completo"""
        mock_analyze.return_value = {
            'research': 'Test research',
            'criticism': 'Test criticism',
            'improved': 'Test improved',
            'synthesis': 'Test synthesis'
        }
        main()
        mock_analyze.assert_called_once_with('test topic')

    @patch('sys.argv', ['cli.py', 'test topic', '--mode', 'sintese'])
    @patch('gemini.cli.get_final_analysis')
    @patch.dict('os.environ', {
        'AGENTOPS_API_KEY': 'test_key',
        'GEMINI_API_KEY': 'test_key'
    })
    def test_main_synthesis_mode(self, mock_get_final):
        """Testa a execução principal no modo síntese"""
        mock_get_final.return_value = "Test synthesis"
        main()
        mock_get_final.assert_called_once_with('test topic')

if __name__ == '__main__':
    unittest.main() 