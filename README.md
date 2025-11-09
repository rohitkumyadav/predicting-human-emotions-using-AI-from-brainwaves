# predicting human emotions using AI from brainwaves

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This project aims to design an intelligent system that predicts emotional states—such as happiness, sadness, and fear—from patients’ brainwave (EEG) signals. By analyzing neural patterns and applying machine learning algorithms, the system can accurately classify these emotions in real time. The objective is to assist healthcare professionals in understanding patients’ emotional conditions, especially for those who cannot easily communicate their feelings, thereby improving emotional awareness and patient-centered care

## Project Organization

```
├── LICENSE            <- Open-source license
├── README.md          <- Read about the project
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
|   |   |── train
|   |   |   |──train_dataset.csv <- training data
|   |   |── test
|   |   |   |──real_world_test.csv <- data to test 
|   |   |── eeg_emotion_dataset.csv  <- main csv file without train-test
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `eeg_final.ipynb`.
│
├── references         <- dataset link
|   |──data_source.txt
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── Deployment   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes predicting human emotions using AI from brainwaves a Python module
    │
    ├── app.py             <- Code to create features for modeling
    │
    ├── modeling                
```

--------

