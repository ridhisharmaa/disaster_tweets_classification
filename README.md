# 🌍 Disaster Tweets Classification using Machine Learning

An end-to-end Machine Learning project that classifies tweets as **Disaster** or **Not Disaster** using Natural Language Processing (NLP) techniques and a trained classification pipeline.

---

## 🚀 Project Overview

Social media platforms like Twitter become crucial sources of information during natural disasters. However, not every tweet mentioning words like "fire", "flood", or "earthquake" actually refers to a real disaster.

This project builds an NLP-based classification system that automatically determines whether a tweet is related to a real disaster or not.

---

## ✨ Features

- Text preprocessing and cleaning
- NLP feature engineering
- Machine Learning classification pipeline
- REST API built using FastAPI
- Trained model serialization using Joblib
- End-to-end inference pipeline

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Joblib
- FastAPI
- Uvicorn

---

## 📂 Project Structure

```text
disaster_tweets_classification/
│
├── app.py                     # FastAPI application
├── preprocess.py             # Text preprocessing functions
├── requirements.txt
├── .gitignore
│
├── dataset/
│   ├── train.csv
│   ├── test.csv
│   ├── sample_submission.csv
│   └── disaster_tweets_processed.csv
│
├── model/
│   └── disaster_pipeline.pkl
│
└── notebooks/
    ├── eda.ipynb
    ├── preprocessing.ipynb
    └── word2vec.ipynb
```

---

## 🔍 NLP Pipeline

### Text Preprocessing
- Lowercasing
- URL removal
- Username handling
- Punctuation removal
- Stopword removal
- Tokenization
- Lemmatization

### Feature Engineering
- TF-IDF Vectorization
- Word Embeddings (Word2Vec experiments)

### Machine Learning Models Explored
- Logistic Regression
- Naive Bayes
- Support Vector Machine (SVM)

---

## 📊 Dataset

Dataset used:

**Kaggle - Natural Language Processing with Disaster Tweets**

The dataset contains tweets labeled as:

- `1` → Disaster Tweet
- `0` → Not a Disaster Tweet

---



---

⭐ If you found this project useful, consider giving it a star!
