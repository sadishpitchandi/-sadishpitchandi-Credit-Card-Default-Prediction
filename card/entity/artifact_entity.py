from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",
[ "train_file_path", "test_file_path", "is_ingested", "message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])


ModelTrainerArtifact = namedtuple("ModelTrainerArtifact", ["is_trained", "message", "trained_model_file_path",
                                                           "train_rmse", "test_rmse", "train_accuracy", "test_accuracy",
                                                           "model_accuracy"])

ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact", ["is_model_accepted", "evaluated_model_path"])

