from src.wineqltypred import logger
from src.wineqltypred.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wineqltypred.pipeline.data_ingestion_pipeline import STAGE_NAME

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e
