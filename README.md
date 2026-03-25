# 🧠 Nextdot AI Agent — Customer Support Pipeline

This project implements a mini AI agent that processes unstructured customer messages and generates structured, intelligent responses while explaining its reasoning.

Built as part of the Nextdot AI Engineering Internship assignment.

---

## 🚀 Features

- Intent classification (complaint / query / feedback / request)
- Sentiment detection (positive / neutral / negative / urgent)
- Structured information extraction:
  - Customer name
  - Issue type
  - Urgency level
  - Recommended action
- Context-aware reply generation with tone matching sentiment
- "Thinking out loud" reasoning (model explains its decisions)
- Robust JSON parsing and error handling
- Interactive CLI for real-time testing
- Model comparison capability
- Edge case handling (empty input, Hinglish, short messages)

---

## 🛠️ Tech Stack

- Python
- Groq API (LLaMA models)
- python-dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd nextdot-ai-agent