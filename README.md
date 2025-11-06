<h1 align="center">💼 Quotation Microservice (Python + OpenAI)</h1>

<p align="center">
  <b>FastAPI</b> • <b>Pydantic</b> • <b>Docker</b> • <b>pytest</b> • <b>Mock LLM</b>
</p>



## 📘 Overview

The **Quotation Microservice** is a lightweight, modular Python application that computes quotation totals and automatically generates professional email drafts in **English** and **Arabic**.  
It exposes a single REST endpoint: `POST /quote`, and operates entirely **locally** without API keys by using a **mock LLM**.

This project was developed as part of **Task 2** of the *AI Integration Engineer* assignment, following enterprise-grade coding, testing, and documentation standards.

---

## 🎯 Objectives

```text
1️⃣ Accept a quotation request (JSON) via POST /quote
2️⃣ Compute accurate line totals and grand total using decimal-safe math
3️⃣ Generate bilingual email drafts (EN / AR)
4️⃣ Provide automated tests and a Docker deployment option
5️⃣ Deliver fully validated OpenAPI documentation at /docs



## 🏗️ Architecture

```text
Quotation Microservice/
│
├─ app/
│   ├─ main.py           → FastAPI app and endpoint
│   ├─ models.py         → Pydantic data models (input validation)
│   ├─ logic.py          → Price calculation logic
│   └─ mock_llm.py       → Mock bilingual email generator
│
├─ tests/
│   └─ test_quote.py     → pytest unit tests
│
├─ Dockerfile
├─ requirements.txt
├─ screenshot/
├─ .gitignore
├─ technical_project_detail.pdf   → Detailed technical documentation
└─ README.md




## ⚙️ Setup Instructions (Local Run)

```bash
# 1️⃣ Clone and enter the project
git clone https://github.com/<your-username>/quotation-microservice-task2.git
cd quotation-microservice-task2

# 2️⃣ Create and activate virtual environment
python -m venv .venv
. .venv\Scripts\Activate.ps1    # (Windows PowerShell)

# Expected prompt:
# (.venv) PS C:\Users\anshs\Quotation Microservice>

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run FastAPI server
uvicorn app.main:app --reload --port 8000

# Expected output:
# INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO: Application startup complete.
# ✅ Server running locally

# 5️⃣ Access interactive API docs
# Open browser → http://127.0.0.1:8000/docs
# You'll see a FastAPI-generated Swagger page with endpoint: POST /quote




🧠 Key Technical Concepts

| Component        | Role                                | Technology              |
| ---------------- | ----------------------------------- | ----------------------- |
| FastAPI          | Web framework and OpenAPI docs      | `fastapi`, `uvicorn`    |
| Pydantic         | Schema validation and type checking | `BaseModel`, `EmailStr` |
| Decimal Math     | Precise currency calculation        | `decimal.Decimal`       |
| Mock LLM         | Generates EN/AR email drafts        | Pure Python             |
| Testing          | Logic validation                    | `pytest`                |
| Containerization | Deployment and portability          | `Dockerfile`            |




## 🔍 Error Handling and Validation

```text
Invalid email → 422 Unprocessable Entity
Missing fields → automatic Pydantic validation error
Type mismatch (e.g., string instead of float) → 422 error
Server exceptions → logged via FastAPI’s default middleware



## 🧪 Testing Summary

| **Test**                 | **Description**                                         | **Result**     |
|---------------------------|---------------------------------------------------------|----------------|
| `test_calc_line_total()`  | Verifies formula `10 * (1 + 0.1) * 2 = 22`              | ✅ Passed       |
| `test_build_quote()`      | Ensures grand total of multiple items is accurate       | ✅ Passed       |

All tests executed with **pytest** and returned expected outputs.




## 📦 Dependencies

```text
fastapi
uvicorn
pydantic[email]
pytest



🧱 Dockerfile Preview

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV MOCK_LLM=true
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



💡 Design Decisions & Rationale

| Design Choice            | Reason                                              |
| ------------------------ | --------------------------------------------------- |
| FastAPI                  | Modern async framework with automatic OpenAPI docs. |
| Pydantic                 | Strong data validation and clear error messages.    |
| Decimal instead of float | Avoids currency rounding errors.                    |
| Mock LLM                 | Local testing without API keys.                     |
| Docker                   | Portable environment across machines.               |
| pytest                   | Lightweight and industry-standard testing tool.     |



📈 Performance Snapshot (Local Run)

| Metric          | Observation       |
| --------------- | ----------------- |
| Startup Time    | ~120 ms           |
| Request Latency | ~150 ms avg       |
| Memory Usage    | ~130 MB (Docker)  |
| Throughput      | ≈ 25 requests/sec |



## 📚 Repository Maintenance Checklist

```text
✅ .venv excluded from GitHub (.gitignore configured)
✅ pytest tests passing before push
✅ README kept up-to-date with working examples
✅ Commit messages follow semantic versioning style
✅ Docker build verified (docker build . completes without error)



🚀 Final Summary

| Feature              | Status                    |
| -------------------- | ------------------------- |
| POST /quote endpoint | ✅ Implemented             |
| Input Validation     | ✅ Pydantic                |
| Decimal Computation  | ✅ Accurate                |
| Email Drafts (EN/AR) | ✅ Generated               |
| Mock LLM Mode        | ✅ Enabled                 |
| Tests (Pytest)       | ✅ Passed                  |
| Docker Build         | ✅ Success                 |
| OpenAPI Docs         | ✅ Auto generated at /docs |



🙌 Author

Ansh Srivastava
AI Integration Engineer Candidate








