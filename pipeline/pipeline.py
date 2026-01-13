from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecomendationPipeline:
    def __init__(self,presist_dir = "chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")

            vector_builder =VectorStoreBuilder(csv_path="",persist_dir=presist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipeline Intialized Successfully...")

        except Exception as e:
            logger.error(f"Falied to initialize Pipeline {str(e)}")
            raise CustomException("Error during Pipeline initialization", e)

    def recommend(self,query:str):
        try:
            logger.info(f"Recived a query :{query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommandation generated succesfully...")

            return recommendation
        
        except Exception as e:
            logger.error(f"Falied to get recommandation {str(e)}")
            raise CustomException("Error during recommendation", e)




        