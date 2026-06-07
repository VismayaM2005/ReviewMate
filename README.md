# AI Interview Evaluator

An AI-powered coding interview assessment platform that evaluates code using company-specific hiring personas.

## Features

- Company-specific evaluation (Google, Amazon, Microsoft, Meta, Oracle, Goldman Sachs)
- Custom company support
- Model selection
- Hire / No-Hire verdict
- Strengths and weaknesses analysis
- Time and space complexity evaluation
- MongoDB evaluation history
- FastAPI backend
- Next.js frontend

## Tech Stack

### Frontend
- Next.js
- React
- Tailwind CSS

### Backend
- FastAPI
- Python

### Database
- MongoDB

### AI
- CLōD API
- Meta Llama 3.3 70B Instruct

## Architecture

User Code
→ Company Persona Prompt
→ LLM Evaluation
→ Structured Parsing
→ MongoDB Storage
→ Frontend Visualization
