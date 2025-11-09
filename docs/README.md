# Predicting Human Emotions Using AI from Brainwaves

<p align="center">
  <img src="readmeai/assets/logos/purple.svg" width="30%" alt="Project Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/scikit--learn-1.x-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative" />
  <img src="https://img.shields.io/badge/Model-XGBoost-blue?logo=xgboost" />
  <img src="https://img.shields.io/badge/Framework-Flask-lightgrey?logo=flask" />
  <img src="https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter" />
</p>

---

## 🧠 Overview

This project aims to design an **AI-powered system** that predicts emotional states—such as **happiness**, **sadness**, and **fear**—from **EEG brainwave signals**.  
By analyzing neural activity patterns and applying advanced **machine learning algorithms**, the system can accurately classify emotions in real time.

The goal is to assist **healthcare professionals** in understanding patients’ emotional conditions, especially those unable to communicate, thus enhancing **emotional awareness** and **patient-centered care**.

---

## 🚀 Features

- Real-time EEG signal processing and classification  
- Machine learning model based on XGBoost  
- Data preprocessing, cleaning, and visualization pipeline  
- Flask-based web interface for live emotion prediction  
- Modular, reproducible structure based on Cookiecutter Data Science  

---

## 🧩 Project Structure

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

## ⚙️ Getting Started

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

## 🧪 Model Details

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

## 🤝 Contributing

We welcome contributions!

1. Fork the repository  
2. Create a branch: `git checkout -b feature-name`  
3. Commit your changes: `git commit -m "Added new feature"`  
4. Push to your fork: `git push origin feature-name`  
5. Open a Pull Request  

For detailed contribution steps, refer to `CONTRIBUTING.md`.

---

## 📜 License

Distributed under the [MIT License](LICENSE).  
Feel free to use and modify this project with attribution.

---

## 🙏 Acknowledgments

- EEG Emotion Recognition dataset contributors  
- XGBoost and Scikit-learn open-source communities  
- Cookiecutter Data Science template  
- All contributors who supported this research  

---

<p align="center">
  <a href="#top"><img src="https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square" /></a>
</p>
