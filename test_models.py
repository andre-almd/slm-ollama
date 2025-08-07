"""Script to test Ollama models running in docker container"""

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from utils.prompt import template


class PersonInfo(BaseModel):
    """Person info model"""
    name: str = Field(description="Name")
    age: int = Field(description="Age")
    profession: str = Field(description="Profession")
    hobby: str = Field(description="Hobby")


parser = PydanticOutputParser(pydantic_object=PersonInfo)

gemma_model = OllamaLLM(
    model="gemma3:1b", base_url="localhost:11434", temperature=0.7)
llama_model = OllamaLLM(
    model="llama3.2:1b", base_url="localhost:11434", temperature=0.7)

prompt = ChatPromptTemplate.from_template(template)

gemma_chain = prompt | gemma_model | parser
llama_chain = prompt | llama_model | parser


def test_json_parser(chain, tema: str):
    """Test JSON parser"""
    response = chain.invoke({"tema": tema})
    print("Resposta estruturada:")
    print(f"Nome: {response.name}")
    print(f"Idade: {response.age}")
    print(f"Profissão: {response.profession}")
    print(f"Hobby: {response.hobby}")
    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    try:
        print("🤖 Testando Ollama com gemma3:1b")
        test_json_parser(gemma_chain, "desenvolvedor de software")
        print("🤖 Testando Ollama com llama3.2:1b")
        test_json_parser(llama_chain, "artista digital")
        print("✅ Testes concluídos!")
    except Exception as e:
        print("❌ Erro ao testar modelos")
        print(e)
