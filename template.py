import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ml_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"data/__init__.py",
    f"data/raw/__init__.py",
    f"data/processed/__init__.py",
    f"data/interim/__init__.py",
    f"models/__init__.py",
    f"notebooks/exploratory_analysis.ipynb",
    f"notebooks/data_preprocessing.ipynb",
    f"notebooks/model_training.ipynb",
    f"references/.gitkeep",
    f"reports/__init__.py",
    f"reports/evaluation_metrics/__init__.py",
    f"reports/figures/.gitkeep",
    f"logs/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/core/__init__.py",
    f"src/{project_name}/core/config.yaml",
    f"src/{project_name}/core/config.py",
    f"src/{project_name}/core/constants.py",
    f"src/{project_name}/core/params.yaml",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/data/data_ingestion.py",
    f"src/{project_name}/data/data_preprocessing.py",
    f"src/{project_name}/data/data_transformation.py",
    f"src/{project_name}/data/data_validation.py",
    f"src/{project_name}/experiments/__init__.py",
    f"src/{project_name}/experiments/experiment_tracking.py",
    f"src/{project_name}/modeling/__init__.py",
    f"src/{project_name}/modeling/predict_model.py",
    f"src/{project_name}/modeling/train_model.py",
    f"src/{project_name}/modeling/evaluate_model.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/data_pipeline.py",
    f"src/{project_name}/pipelines/model_pipeline.py",
    f"src/{project_name}/schemas/__init__.py",
    f"src/{project_name}/schemas/config_schema.py",
    f"src/{project_name}/schemas/schema.yaml",
    f"src/{project_name}/visualization/__init__.py",
    f"src/{project_name}/visualization/plot_utils.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/helper_functions.py",
    f"src/{project_name}/utils/custom_exceptions.py",
    f"src/{project_name}/utils/output_generator.py",
    f"src/{project_name}/utils/custom_logging.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")