# 📊 Twitter Sentiment Analysis

##  Overview
This project performs sentiment analysis on Twitter data to classify text as positive, negative, or neutral using NLP and machine learning techniques.

---

##  Pipeline
Raw Data → Preprocessing → TF-IDF → Model Training → Evaluation

---

##  Feature Engineering
Text data is converted into numerical form using **TF-IDF with n-grams (1,2)**, which captures both individual words and word combinations like *“not good”* for better sentiment understanding.

---

## 📊 Model Comparison

| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression | ~0.84    |
| Decision Tree       | ~0.77    |
| Naive Bayes         | ~0.69    |

---

##  Conclusion
Logistic Regression performed best due to its ability to handle high-dimensional TF-IDF features effectively. Using n-grams improved the model’s understanding of context, especially for negation-based sentences.
