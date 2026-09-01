# 🤖 AI Text Generator

A simple and interactive web-based **AI Text Generator** built using **Python, Streamlit, and Hugging Face Transformers**. The application allows users to enter a sentence or short prompt and generate AI-based text using a pretrained language model.

## 📌 About the Project

This project demonstrates how an AI language model can be integrated into a simple and user-friendly web application.

The application uses the **Qwen2.5-0.5B-Instruct** pretrained model from Hugging Face to generate text based on the user's input. **Streamlit** is used to create the interactive web interface.

This project was developed as a practical project to understand the basics of **Generative AI, Transformer models, and AI-powered web applications**.

## ✨ Features

* 📝 Simple text prompt input
* 🤖 AI-generated text
* ⚡ Interactive web interface
* 🔄 Generate different responses for different prompts
* 🎨 Customized Streamlit interface
* 🧠 Pretrained Transformer model
* 💾 Model caching for faster interaction
* 📱 Easy-to-use application

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Hugging Face Transformers**
* **PyTorch**
* **Qwen2.5-0.5B-Instruct**

## 🔄 How It Works

```text
User enters a prompt
        ↓
Streamlit receives the input
        ↓
AI language model processes the prompt
        ↓
The model generates text
        ↓
Generated text is displayed to the user
```

## 🧠 AI Model

This project uses the following pretrained model:

**Qwen/Qwen2.5-0.5B-Instruct**

The model is accessed through the Hugging Face Transformers library and is used for text generation based on the user's prompt.

## 📂 Project Structure

```text
AI-Text-Generator/
│
├── text_generator.py
└── README.md
```

## ⚙️ Installation

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Required Libraries

Open the terminal in the project folder and run:

```bash
pip install streamlit transformers torch
```

## ▶️ Run the Application

Run the following command in the terminal:

```bash
streamlit run text_generator.py
```

After running the command, Streamlit will provide a local URL where the application can be opened in a web browser.

Usually, it will be:

```text
http://localhost:8501
```

## 💡 Example

Enter a prompt such as:

```text
Artificial Intelligence is
```

The application will generate text based on the given prompt.

The generated response may vary between different runs because the model generates text dynamically.

## 🎯 What This Project Demonstrates

This project provides practical experience with:

* Generative AI concepts
* Transformer-based language models
* Hugging Face Transformers
* Pretrained AI models
* Text generation
* Python programming
* Streamlit web application development
* Integrating an AI model with a web interface

## ⚠️ Note

The generated text may sometimes be incomplete, repetitive, or inaccurate. The application is mainly intended for **learning, experimentation, and demonstration purposes**.

## 🚀 Future Improvements

The project can be enhanced in the future by adding:

* 🌡️ Temperature control
* 🔢 Maximum token control
* 🔄 Clear or reset option
* 📥 Download generated text
* 🕘 Prompt history
* 🤖 Multiple AI model selection
* 💬 Chat-style interface
* 🎨 Additional UI customization

## 👩‍💻 Developed By

**Lakshana V**

### 📌 Project

**AI Text Generator using Transformers and Streamlit**

---

⭐ **If you find this project useful, feel free to explore and learn from it!**
