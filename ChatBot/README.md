# Console-Based Chatbot using Transformers

## Overview

This project is a console-based chatbot built using a pre-trained transformer model from Hugging Face.
The chatbot communicates with users in natural language and generates dynamic responses.

---

## Features

* Natural language conversation
* Uses a pre-trained transformer model
* Maintains conversation context
* Continuous interaction loop
* Exit command support (`exit` or `quit`)

---

## Technologies Used

* Python
* Hugging Face Transformers
* PyTorch

---

## Model Used

This project uses the DialoGPT-medium model:

* Designed for conversational AI
* Based on transformer architecture
* Generates human-like responses

---

## Installation

```bash
pip install transformers torch
```

---

## How to Run

1. Open terminal or Jupyter Notebook
2. Run the Python script
3. Start chatting with the bot

Example:

```
You: Hello
Chatbot: Hi! How can I help you today?
```

---

## How It Works

1. User enters input
2. Input is tokenized into numerical format
3. Model processes the input using transformer architecture
4. Response is generated using text generation
5. Output is decoded and displayed

---

## Concepts Used

* Transformer Architecture
* Natural Language Processing (NLP)
* Tokenization
* Text Generation
* Context Handling

---

## Limitations

* May generate incorrect or random responses
* Does not have real-time knowledge
* Limited long-term memory

---

## Future Improvements

* Add web interface (Gradio)
* Improve memory handling
* Use larger or fine-tuned models

---

