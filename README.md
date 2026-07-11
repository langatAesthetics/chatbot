# Python Intent-Based Chatbot

A simple educational chatbot built using Python to understand how traditional chatbots work internally without relying (LLMs) such as ChatGPT, Gemini, Claude, or Llama.

The chatbot uses a classic Natural Language Processing (NLP) pipeline consisting of tokenization, stemming, pattern matching, intent detection, and response generation.

---

## Features

* Command-line chatbot interface
* Intent-based architecture
* Dynamic intent loading from `intents.json`
* Tokenization of user input
* Stemming using the Porter Stemmer algorithm
* Pattern matching for intent detection
* Multiple responses per intent
* Modular and scalable project structure

---

## Current Chatbot Architecture

```
User Input → Tokenization → Stemming → Pattern Matching → Intent Detection → Response
```

---

## Example Intents

The chatbot currently supports:

* Greetings
* Goodbyes
* "How are you?" conversations

Example interactions:

```text
You: hello
Bot: Hello! How can I help you today?
---


## Installed Packages

### NLTK

Used for Natural Language Processing tasks such as stemming.

```bash
pip install nltk
```

### Colorama

Used for improving terminal output formatting and color support.

```bash
pip install colorama
```

---

## Python Concepts Covered

* Functions
* Classes and Objects
* JSON Parsing
* File Handling
* List Comprehensions
* Modular Programming
* Virtual Environments
* Dependency Management

---

## NLP Concepts Covered

* Natural Language Processing (NLP)
* Intent Recognition
* Tokenization
* Stemming
* Pattern Matching
* Response Selection

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd python-chatbot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Chatbot

Start the chatbot using:

```bash
python main.py
```

Exit the chatbot by typing:

```text
exit
```

---

## Future Improvements

* Bag of Words (BoW)
* Machine Learning Intent Classification
* Model Persistence
* Context Awareness
* REST API using FastAPI
* Database Integration
* Website Integration using React or Django

---

## Learning Objective

The purpose of this project is not only to build a chatbot but also to understand the internal mechanisms behind conversational systems and Natural Language Processing.

By building each component from scratch, the project provides a solid foundation for future work in machine learning, AI, and intelligent assistants.

---
