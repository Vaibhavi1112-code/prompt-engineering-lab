
# Exploring Few-Shot Prompting for Automating Requirement Analysis in Software Development

## 1-Liner Description
This project explores how Few-Shot Prompting can enhance the automation of requirement analysis in software development by improving the accuracy and relevance of AI-generated responses.

**Authors**  
Vaibhavi Panchal  
Academic Supervisor: Dr. Fernando Koch

## Research Question
How can Few-Shot Prompting be leveraged to improve AI-driven requirement analysis in software development?  
By providing contextual examples, we aim to enhance AI’s ability to generate structured and accurate responses for both short and long queries.

---

## 1️⃣ Background

### What is already known?
- Traditional AI models struggle with unstructured requirement gathering and often produce incomplete or irrelevant responses.
- Existing AI tools assist in requirement analysis but lack contextual understanding for complex queries.
- Few-Shot Prompting has shown promise in improving AI-generated responses by providing contextual examples.

### What is this research exploring?
- We use Few-Shot Prompting to improve the accuracy and structure of AI-driven requirement analysis.
- We build a pipeline that integrates contextual examples to guide AI models in answering both short and long queries.
- We analyze how contextual examples influence the relevance and completeness of AI-generated responses.

### Implications for Practice
- Automates the extraction of functional & non-functional requirements.
- Optimizes requirement analysis by reducing manual effort and improving AI response quality.
- Enhances our understanding of Few-Shot Prompting in software development.

---

## 2️⃣ Research Method
This research employs Few-Shot Prompting by providing the AI model (Llama3) with predefined examples.  
We experiment with context length, prediction length, and prompt variations (short vs. long).  
Evaluation focuses on accuracy, completeness, and response structure in automated requirement analysis.

---

## 3️⃣ Results

| Query Type       | AI Response Quality                       | Avg Processing Time |
|------------------|-------------------------------------------|---------------------|
| **Short Queries** | More accurate & structured                | 7.11s               |
| **Long Queries**  | Well-explained & contextually relevant    | 5.35s               |
| **Zero-Shot Prompting** | Less structured, more generic         |3.95s               |

**Key Finding**: Few-Shot Prompting significantly improves AI response quality, particularly for complex, long-form queries.

---

## 4️⃣ Further Research

### 🔍 Next Steps:
- Implement **Chain-of-Thought (CoT)** reasoning for deeper requirement analysis.
- Automate the **Few-Shot Example Generation** to reduce manual effort.
- Expand experiments using **real-world software development datasets**.

---

## 5️⃣ Installation & Usage

### 🔧 Prerequisites
- Install **Python 3.8+**

### Install dependencies:
```bash
pip install -r requirements.txt

