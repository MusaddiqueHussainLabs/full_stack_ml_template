# Full-Stack ML Template

This project template is designed to streamline the development process for end-to-end machine learning applications. It encompasses various components, from data processing and modeling to deployment, providing a structured framework for building robust machine learning solutions.

## Creating Project Structure

To generate the Full-Stack ML Template structure automatically, follow these steps:

### Using `template.py`

1. **Clone Repository:** Clone this repository to your local machine.

2. **Run `template.py`:** Execute the `template.py` script to create the project structure.

    ```bash
    python template.py
    ```

    This script initializes the entire project structure with predefined directories and essential files.

3. **Customization:**
    - Modify `params.yaml` and `schema.yaml` to align with your project requirements.
    - Add or modify scripts within the structured directories to build, train, and deploy models.

## Project Structure Overview

### Directories

- **.github/workflows/**
  - *Description:* GitHub Actions workflows configuration.
- **data/**
  - **raw/**
    - *Description:* Raw data storage and data loading modules.
  - **processed/**
    - *Description:* Processed data storage and related scripts.
- **model_artifacts/**
  - **trained_models/**
    - *Description:* Trained models storage.
  - **evaluation_metrics/**
    - *Description:* Storage for model evaluation metrics.
- **notebooks/**
  - *Description:* Jupyter notebooks for exploratory analysis, data preprocessing, and model training.
- **references/**
  - *Description:* External references and resources.
- **reports/**
  - *Description:* Storage for project reports.

### Files

- **logs/app.log**
  - *Description:* Application logs.
- **src/**
  - **[project_name]/**
    - **core/**
      - *Description:* Core project configurations and constants.
    - **data/**
      - *Description:* Data processing and validation modules.
    - **modeling/**
      - *Description:* Model training, evaluation, and prediction scripts.
    - **pipelines/**
      - *Description:* Data and model pipelines.
    - **schemas/**
      - *Description:* Schemas for configurations and data validation.
    - **visualization/**
      - *Description:* Visualization utilities.
    - **utils/**
      - *Description:* Helper functions.

### Additional Files

- **params.yaml:** Configuration parameters.
- **schema.yaml:** Data schema definitions.
- **main.py:** Entry point for the application.
- **Dockerfile:** Docker container configuration.
- **requirements.txt:** Project dependencies.
- **setup.py:** Project setup and installation script.