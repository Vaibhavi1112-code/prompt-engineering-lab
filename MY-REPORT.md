Exploring Few-Shot Prompting for Automating Requirement Analysis in Software Development
1-liner description of your project:
This project explores how Few-Shot Prompting can enhance the automation of requirement analysis in software development by improving the accuracy and relevance of AI-generated responses.

Authors: Vaibhavi Panchal
Academic Supervisor: Dr. Fernando Koch

Research Question
How can Few-Shot Prompting be leveraged to improve AI-driven requirement analysis in software development?
By providing contextual examples, we aim to improve AI’s ability to generate structured and accurate responses for both short and long queries.

Arguments
What is already known about this topic

Traditional AI models struggle with unstructured requirement gathering and often produce incomplete or irrelevant responses.
Existing AI tools can assist in requirement analysis but lack the contextual understanding required for complex queries.
Few-Shot Prompting has shown promise in improving the quality of AI responses by providing contextual examples.
What this research is exploring

We employ Few-Shot Prompting to improve the accuracy and structure of AI-driven requirement analysis.
We are building a pipeline that uses contextual examples to guide the AI model in answering short and long requirement-related queries.
We are exploring how providing contextual examples (short and long) influences the relevance and completeness of AI-generated responses.
Implications for practice

It will be easier to automate the extraction of both functional and non-functional requirements.
It will optimize requirement analysis by reducing the need for manual interpretation and improving the quality of AI responses.
We will better understand the role of Few-Shot Prompting in enhancing AI's ability to handle complex software development tasks.
Research Method
This research employs the Few-Shot Prompting technique, which involves providing the AI model (Llama3) with predefined examples of questions and answers. By adjusting parameters such as context length and prediction length, we experiment with different types of prompts (short vs. long) to evaluate the effectiveness of Few-Shot Prompting in improving requirement analysis automation.

Results
Short queries led to more accurate and structured AI-generated responses compared to zero-shot approaches, with an average processing time of 14.7 seconds.
Long queries resulted in well-explained, contextually relevant answers, with a slight increase in processing time to 15.2 seconds.
Few-Shot Prompting significantly improved the quality of responses, particularly for more complex, long-form queries.

Further Research
Implementing Chain-of-Thought (CoT) reasoning could help with more complex, step-by-step analysis of requirements.
Investigating automated Few-Shot example generation to reduce the manual effort in crafting contextual examples.
Expanding the research by incorporating real-world software development datasets to evaluate the generalizability of Few-Shot Prompting in practical scenarios.

