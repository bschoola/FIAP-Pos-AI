
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.document_loaders import TextLoader
import os

def carregar_documentos(caminho_arquivo):
    loader = TextLoader(caminho_arquivo)
    documentos = loader.load()
    return documentos

def limpar_texto(texto):
    return texto.strip()

llm = Ollama(
    model= "llama2", ##  "llama3.2",
    num_gpu=0,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

prompt_sentimento = "Analise o sentimento do seguinte texto em português: {text}"
prompt_resumo = "Gere um resumo em português para o seguinte texto: {text}"

template_sentimento = PromptTemplate(input_variables=["text"], template=prompt_sentimento)
template_resumo = PromptTemplate(input_variables=["text"], template=prompt_resumo)

chain_sentimento = LLMChain(llm=llm, prompt=template_sentimento)
chain_resumo = LLMChain(llm=llm, prompt=template_resumo)

caminho_arquivo = os.path.join(os.path.dirname(__file__), "noticias.txt")

if not os.path.exists(caminho_arquivo):
    raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")

documentos = carregar_documentos(caminho_arquivo)

for doc in documentos:
    texto_limpo = limpar_texto(doc.page_content)

    resultado_sentimento = chain_sentimento.run({"text": texto_limpo})
    resultado_resumo = chain_resumo.run({"text": texto_limpo})

    print(f"Notícia: {texto_limpo}")
    print(f"Sentimento: {resultado_sentimento}")
    print(f"Resumo: {resultado_resumo}")
    print("-" * 50)

