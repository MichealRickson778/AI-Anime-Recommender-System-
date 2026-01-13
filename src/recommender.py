from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriver, api_key:str, model_name:str):
        self.llm = ChatGroq(api_key=api_key,model_name=model_name,temperature=0)
        self.prompt = get_anime_prompt()
        self.retriver = retriver
        self.qa_chain = (
            self.prompt
            | self.llm
            | StrOutputParser()
            )
        
    def get_recommendation(self,query:str):
        docs = self.retriver.invoke(query)

        answer = self.qa_chain.invoke(
            {
                "context": docs,
                "question": query
            }
        )

        return {
        "answer": answer
        }