# Predicting Human Emotions Using AI from Brainwaves

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/scikit--learn-1.x-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative" />
  <img src="https://img.shields.io/badge/Model-XGBoost-blue?logo=xgboost" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit" />  
  <img src="https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter" />
</p>

---

## Overview
This project develops an **AI-powered system** that predicts **human emotions** — such as **happiness**, **sadness**, and **fear** — from **EEG brainwave signals** using advanced **machine learning algorithms**.  
By analyzing neural activity patterns, the system classifies emotions in **real time**, helping **healthcare professionals** understand the emotional states of patients — especially those **unable to communicate** — thus enhancing **emotional awareness** and **patient-centered care**.

Multiple models were trained and compared:

- **Random Forest:** 72.5%  
- **AdaBoost:** 43.2%  
- **LightGBM:** 94.4%  
- **XGBoost (Final Model):** **96.3%**

The **XGBoost model** achieved the **highest accuracy of 96.3%**, with balanced performance across all emotion classes:  
**Precision = 0.96 | Recall = 0.96 | F1-Score = 0.96 | Accuracy = 96.3%**

---

## Features

- Real-time EEG signal processing and classification  
- Machine learning model based on XGBoost  
- Data preprocessing, cleaning, and visualization pipeline  
- Flask-based web interface for live emotion prediction  
- Modular, reproducible structure based on Cookiecutter Data Science  

---

## Project Structure

```bash
predicting-human-emotions-using-AI-from-brainwaves/
├── LICENSE
├── README.md
├── data
│   ├── raw/                # Original unprocessed EEG data
│   ├── interim/            # Intermediate transformed data
│   ├── processed/          # Final training and testing datasets
│       ├── train_dataset.csv
│       ├── real_world_test.csv
│       └── eeg_emotion_dataset.csv
│
├── models/                 # Trained ML models (e.g., XGBoost)
│   └── xgboost_model.pkl
│
├── notebooks/              # Jupyter Notebooks for exploration
│   └── eeg_final.ipynb
│
├── references/             # Dataset sources and documentation
│   └── data_source.txt
│
├── Deployment/             # Flask app and backend logic
│   └── app.py
│
├── reports/                # Generated reports and visualizations
│   └── figures/
│
├── requirements.txt        # Python dependencies
├── pyproject.toml
└── setup.cfg
```

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python ≥ 3.9  
- Pip ≥ 22.0  
- Jupyter Notebook  
- Dependencies listed in `requirements.txt`  

### Installation

```bash
# Clone repository
git clone https://github.com/rohitkumyadav/predicting-human-emotions-using-AI-from-brainwaves.git

# Navigate to project
cd predicting-human-emotions-using-AI-from-brainwaves

# Install dependencies
pip install -r requirements.txt
```

### Usage

Run the web app:

```bash
cd Deployment
python app.py
```

Or explore the model via Jupyter Notebook:

```bash
jupyter notebook notebooks/eeg_final.ipynb
```

---

## Model Details

- **Algorithm:** XGBoost Classifier  
- **Input:** EEG brainwave features (alpha, beta, theta, gamma bands)  
- **Output:** Predicted emotional state  
- **Metrics:** Accuracy, F1-score, Confusion Matrix  
- **Explainability:** SHAP visualizations for feature importance  

---

## 🗺️ Roadmap

- [x] Data preprocessing and feature extraction  
- [x] Model training and testing  
- [x] Flask deployment  
- [ ] Integration with real-time EEG hardware  
- [ ] Live dashboard for emotion tracking  

---

## Contributing

We welcome contributions!

1. Fork the repository  
2. Create a branch: `git checkout -b feature-name`  
3. Commit your changes: `git commit -m "Added new feature"`  
4. Push to your fork: `git push origin feature-name`  
5. Open a Pull Request  

For detailed contribution steps, refer to `CONTRIBUTING.md`.

---

## License

Distributed under the [MIT License](LICENSE).  
Feel free to use and modify this project with attribution.

---

## Acknowledgments

- EEG Emotion Recognition dataset contributors  
- XGBoost and Scikit-learn open-source communities  
- Cookiecutter Data Science template  
- All contributors who supported this research  

---

<p align="center">
  <a href="#top"><img src="https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square" /></a>
</p>
