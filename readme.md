# Playwright Python Automation Framework

## 📌 Overview
This project is a scalable test automation framework built using Playwright and Pytest. It follows the Page Object Model (POM) design pattern and includes real-world features like reporting, failure handling, and security testing.

---

## 🚀 Features
- Page Object Model (POM)
- Data-driven testing using Pytest
- Parallel execution with pytest-xdist
- Pytest markers (smoke, regression, security)
- Screenshot capture on test failure
- HTML test reports
- Basic security test scenarios (SQL Injection & Brute-force simulation)

---

## 🛠 Tech Stack
- Python
- Playwright
- Pytest
- Pytest-HTML
- Pytest-xdist

---

## ▶️ How to Run Tests

Run all tests:
```bash
Run smoke tests:
```bash
python -m pytest -m smoke
```bash
Run regression tests:
```bash
python -m pytest -m regression
```bash
Run security tests:
```bash
python -m pytest -m security

📂 Project Structure
pages/         → Page Object classes  
tests/         → Test cases  
utils/         → Utility functions  
screenshots/   → Failure screenshots  
logs/          → Execution logs  

📊 Reporting
- HTML report generated after execution
- Screenshots attached for failed tests

🎯 Purpose
This project demonstrates practical automation skills including framework design, debugging support, and handling real-world scenarios.