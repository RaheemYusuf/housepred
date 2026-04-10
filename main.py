from src.wineqltypred import logger
from src.wineqltypred.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wineqltypred.pipeline.data_ingestion_pipeline import STAGE_NAME
from src.wineqltypred.pipeline.data_validation_pipeline import run_data_validation_pipeline

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


#run data validation pipeline
run_data_validation_pipeline()
