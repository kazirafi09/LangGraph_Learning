# LangGraph Learning

A comprehensive collection of Jupyter notebooks and experiments focused on learning and mastering **LangGraph** for building stateful, multi-agent LLM workflows.

## 🚀 Project Overview

This repository serves as a learning journey through LangGraph, progressing from basic LLM interactions to complex, iterative, and parallel workflows. Each notebook represents a specific concept or project, providing hands-on examples of how to orchestrate LLMs for sophisticated tasks.

## 📚 Key Topics Covered

The notebooks are organized to build knowledge incrementally:

### Foundations
- **LLM Basics**: Basic calls and prompt engineering (`06_02_llm_call.ipynb`).
- **Simple Logic**: Implementing basic calculations via LLMs (`06_01_bmi_calc.ipynb`).
- **Structured Output**: Leveraging LLMs to generate data in a specific format (`Separates/model_with_structured_output.ipynb`).

### Workflow Orchestration
- **Content Generation**: Building a blog generation pipeline (`06_03_blog_gen.ipynb`).
- **Parallel Workflows**: Executing multiple nodes concurrently to improve efficiency (`07_parallel_workflow.ipynb`).
- **Conditional Routing**: Implementing decision-making logic to route workflows dynamically (`08_conditional_workflows.ipynb`).
- **Iterative Workflows**: Creating loops and feedback cycles for refinement (`09_Iterative_workflow.ipynb`).

### Advanced Concepts & Applications
- **Chatbot Implementation**: Building a full-fledged conversational agent (`10_chatbot.ipynb`).
- **State Management**: Practicing with LangGraph reducers to manage complex states (`Separates/reducer_prac.ipynb`).

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.10+
- Jupyter Notebook or JupyterLab

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/LangGraph_Learning.git
   cd LangGraph_Learning
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

4. Set up your API Keys:
   Create a `.env` file in the root directory and add your LLM provider keys:
   ```env
   OPENAI_API_KEY=your_api_key_here
   # Or other providers as used in the notebooks
   ```

## 📂 Repository Structure

```text
.
├── 06_01_bmi_calc.ipynb           # BMI calculation with LLM
├── 06_02_llm_call.ipynb           # LLM call fundamentals
├── 06_03_blog_gen.ipynb           # Blog generation workflow
├── 07_parallel_workflow.ipynb     # Parallel execution patterns
├── 08_conditional_workflows.ipynb # Conditional routing logic
├── 09_Iterative_workflow.ipynb   # Looping and iterative patterns
├── 10_chatbot.ipynb               # End-to-end chatbot implementation
├── Separates/                     # Specialized practice notebooks
│   ├── model_with_structured_output.ipynb
│   └── reducer_prac.ipynb
└── requirement.txt                # Project dependencies
```

## 🎯 Learning Goals

- Understand the core concepts of LangGraph (Nodes, Edges, State).
- Build workflows that are more than just linear chains.
- Master state management and complex routing in AI agents.
- Implement real-world patterns like parallel processing and iterative refinement.
