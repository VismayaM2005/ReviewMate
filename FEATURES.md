# FEATURES.md

# ReviewMate — AI-Powered Company-Specific Code Interview Evaluator

## Project Vision

ReviewMate is an AI-powered platform that evaluates coding interview solutions using company-specific hiring standards.

Instead of providing generic code reviews, ReviewMate simulates how different companies such as Google, Amazon, Microsoft, Meta, Oracle, and Goldman Sachs would assess a candidate's solution.

The system generates structured feedback, scores, hiring recommendations, improvement suggestions, and interview follow-up questions based on the selected company's engineering culture and expectations.

---

# Phase 1 — Minimum Viable Product (MVP)

The following features define the initial production-ready release.

## 1. Code Submission

Users can paste code directly into the application.

### Requirements

* Multi-line code editor
* Supports large code blocks
* No language validation required
* Syntax highlighting (optional)

---

## 2. Programming Language Selection

Supported languages:

* Python
* Java
* C++
* JavaScript
* TypeScript
* Go
* SQL
* Other

The selected language is used to customize the AI evaluation prompt.

---

## 3. Company Persona Selection

### Built-In Personas

* Google
* Amazon
* Microsoft
* Meta
* Oracle
* Goldman Sachs

Each persona uses a dedicated evaluation rubric.

---

## 4. Custom Company Mode

Users may enter any company name.

Example:

NVIDIA
Netflix
Airbnb
Uber
Salesforce

For unknown companies, the system dynamically generates an evaluation rubric before reviewing the submitted code.

---

## 5. AI Code Evaluation

The platform analyzes:

* Problem-solving approach
* Algorithm efficiency
* Code quality
* Readability
* Maintainability
* Edge-case handling
* Production readiness

---

## 6. Hiring Recommendation

Every evaluation produces:

### Verdict

* HIRE
* NO HIRE

### Overall Score

Range:

0–100

### Evaluation Summary

* Strengths
* Weaknesses
* Complexity Analysis
* Final Recommendation

---

## 7. Evaluation History

All reviews are stored in MongoDB.

Stored information:

* Company
* Programming language
* Submitted code
* Score
* Verdict
* Timestamp

Users can revisit previous evaluations.

---

# Phase 2 — Enhanced Evaluation Engine

## 8. Company-Specific Scoring Rubrics

### Google

Focus Areas:

* Data structures
* Algorithms
* Time complexity
* Space complexity
* Clean coding practices

### Amazon

Focus Areas:

* Scalability
* Reliability
* Production readiness
* Operational excellence

### Microsoft

Focus Areas:

* Readability
* Maintainability
* Object-oriented design
* Collaboration readiness

### Meta

Focus Areas:

* Performance
* Systems thinking
* Optimization
* Speed of execution

### Oracle

Focus Areas:

* Enterprise coding standards
* Java best practices
* SQL efficiency
* Database interaction

### Goldman Sachs

Focus Areas:

* Correctness
* Reliability
* Risk reduction
* Financial-grade software quality

---

## 9. Detailed Score Breakdown

Evaluation dimensions:

* Algorithm Design
* Code Quality
* Scalability
* Maintainability
* Testing & Reliability

Example:

Algorithm Design: 90/100
Code Quality: 84/100
Scalability: 78/100
Testing & Reliability: 72/100

Overall: 83/100

---

## 10. Advanced Evaluation Dashboard

Users can:

* Filter reviews
* Sort reviews
* Search past evaluations
* Compare performance across companies

---

# Phase 3 — Interview Preparation Features

## 11. Follow-Up Interview Questions

The AI generates likely interviewer questions based on the submitted solution.

Example:

* How would you optimize memory usage?
* What edge cases did you consider?
* How would this scale to millions of users?

---

## 12. Improvement Recommendations

The system identifies specific actions that would increase the candidate's score.

Example:

* Replace nested loops with a hash map
* Add input validation
* Improve error handling

---

## 13. PDF Report Export

Users can download a complete interview evaluation report.

Contents:

* Company persona
* Score breakdown
* Verdict
* Strengths
* Weaknesses
* Follow-up questions
* Improvement recommendations

---

# Phase 4 — Advanced Features

## 14. Multi-Company Comparison

Evaluate a single solution against multiple companies simultaneously.

Example:

Google → HIRE
Amazon → HIRE
Meta → NO HIRE
Oracle → HIRE

---

## 15. Candidate Performance Analytics

Track:

* Average score
* Best-performing company
* Improvement trends
* Historical performance

---

## 16. Voice Interview Simulation

Future enhancement.

Features:

* AI-generated interview questions
* Voice input
* Communication scoring
* Technical response evaluation

---

# Technical Architecture

## Frontend

* Next.js
* React
* Tailwind CSS
* Shadcn UI
* Monaco Editor

## Backend

* FastAPI
* Python

## AI Layer

* Claude API
* Prompt-engineered company personas

## Database

* MongoDB Atlas

## Deployment

Frontend:

* Vercel

Backend:

* Render

Database:

* MongoDB Atlas

---

# MVP Scope Lock

The first release will include only:

* Code submission
* Language selection
* Company selection
* Custom company support
* AI evaluation
* Hire / No Hire verdict
* MongoDB persistence
* Evaluation history

All other features are considered future enhancements.
