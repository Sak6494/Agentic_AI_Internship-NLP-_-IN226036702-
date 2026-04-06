


# **BERT for POS Tagging and Chunking**

## **Overview**

This project demonstrates how to **build and fine-tune a transformer model (BERT/DistilBERT)** to perform **Part-of-Speech (POS) Tagging** and **Chunking (Phrase Detection)** using token classification techniques. The model predicts grammar-level tags for words (POS) and groups words into meaningful phrases (Chunking), enabling deeper understanding of sentence structure in Natural Language Processing (NLP).

---

## **Project Workflow**

The pipeline includes the following stages:

1. **Dataset Selection** – Using the CoNLL-2003 dataset to obtain tokens, POS tags, and chunk tags.
2. **Data Preprocessing** – Tokenizing sentences with a BERT tokenizer and aligning labels for subwords and special tokens.
3. **Model Setup** – Configuring `AutoModelForTokenClassification` with the correct number of labels and proper label mappings.
4. **Training** – Fine-tuning the BERT model using Hugging Face Trainer with defined learning rate, epochs, and batch size.
5. **Evaluation** – Measuring performance using metrics like Precision, Recall, and F1 via the seqeval metric.
6. **Inference** – Predicting POS and chunk tags on custom sentences.
7. **Comparison** – Analyzing the difference between POS tagging (word-level) and Chunking (phrase-level).

---

## **Key Learnings**

* Handling subwords and special tokens in transformer models
* Aligning token-level labels for NLP tasks
* Using Hugging Face Transformers for sequence labeling
* Evaluating NLP models using sequence-based metrics

---

## **References**

* [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)
* [CoNLL-2003 Dataset](https://www.clips.uantwerpen.be/conll2003/ner/)
* [Seqeval Metric](https://github.com/chakki-works/seqeval)

---
