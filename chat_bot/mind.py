# gerencia o contexto da conversa e chama a API do google.
# importacoes
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys

# Chama load_dotenv
load_dotenv()
chave_api = os.getenv('GEMINI_API_KEY')
if not chave_api:
    raise ValueError('Chave API nao encontrada no arquivo .env!')
    sys.exit(1)

# conf da api
genai.configure(api_key=chave_api)


class Vikir_mind:
    def __init__(self):
        self.instrucao_sistema = """
        Seu nome e Vikir, uma IA assistente avancada.
        Sua personalidade e prestativa, inteligente e levemente sarcastica.
        deve responder de forma clara e objetiva.
        """

        self.config_geracao = {
            'temperature': 0.7, # para criatividade (0.0 a 1.0)
            'top_p': 0.95,
            'top_k': 64,
            'max_output_tokens': 8192,
        }

        self.modelo = genai.GenerativeModel(
            model_name='gemini-3.5-flash-lite',
            generation_config = self.config_geracao,
            system_instruction = self.instrucao_sistema
        )
        self.chat = self.modelo.start_chat(history=[])

    def pensar(self, usuario_mensagem):
        # o objetivo e receber a mensagem do usuario e mandar para a API.
        if usuario_mensagem == None: # valida o input
            return ''

        # Envia para o chat da gemini
        try:
            resposta_bruta = self.chat.send_message(usuario_mensagem)

            if hasattr(resposta_bruta, 'text'):
                texto_resposta = resposta_bruta.text
            else:
                # Montar o texto a partir dos parts (quando a resposta
                # vem em varios blocos)
                parte_texto = []
                for parte in resposta_bruta.parts:
                    parte_texto.append(parte.text)
                texto_resposta = ''.join(parte_texto)

        # Tratamento de falha
        except Exception as e:
            print(f'Ocorreu um erro ao chamar a API!')
            return f'Vikir: deu um erro inesperado. Tenta de novo em instantes.'

        # Garantir que a resposta e um texto limpo

        if texto_resposta == None:
            return ''

        return texto_resposta
