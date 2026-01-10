<h2>🏷️ Project Title</h2>
<p><b>AI-Driven Quotation Microservice (FastAPI + Decimal Finance Engine + Bilingual AI Email Generator)</b></p>

<h2>🧩 Project Overview</h2>
<p>
This project is a production-grade quotation computation and communication microservice designed for B2B sales, procurement, and CRM automation systems. 
It accepts structured quotation requests via a REST API, performs precise financial calculations using decimal-safe arithmetic, and generates professional bilingual (English & Arabic) quotation emails through a controlled AI abstraction layer.
</p>
<p>
The service is built using FastAPI and Pydantic, making it fully OpenAPI compliant, strongly typed, and enterprise-ready for integration with CRMs, ERP systems, and sales automation pipelines.
</p>

<h2>📑 Table of Contents</h2>
<ul>
<li>🏷️ Project Title</li>
<li>🧾 Executive Summary</li>
<li>📑 Table of Contents</li>
<li>🧩 Project Overview</li>
<li>🎯 Objectives & Goals</li>
<li>✅ Acceptance Criteria</li>
<li>💻 Prerequisites</li>
<li>⚙️ Installation & Setup</li>
<li>🔗 API Documentation</li>
<li>🖥️ UI / Frontend</li>
<li>🔢 Status Codes</li>
<li>🚀 Features</li>
<li>🧱 Tech Stack & Architecture</li>
<li>🛠️ Workflow & Implementation</li>
<li>🧪 Testing & Validation</li>
<li>🔍 Validation Summary</li>
<li>🧰 Verification Testing Tools</li>
<li>🧯 Troubleshooting & Debugging</li>
<li>🔒 Security & Secrets</li>
<li>☁️ Deployment</li>
<li>⚡ Quick-Start Cheat Sheet</li>
<li>🧾 Usage Notes</li>
<li>🧠 Performance & Optimization</li>
<li>🌟 Enhancements & Features</li>
<li>🧩 Maintenance & Future Work</li>
<li>🏆 Key Achievements</li>
<li>🧮 High-Level Architecture</li>
<li>🗂️ Project Structure</li>
<li>🧭 How to Demonstrate Live</li>
<li>💡 Summary, Closure & Compliance</li>
</ul>

<h2>🧩 Project Overview</h2>
<p>
This system exposes a REST API endpoint <b>POST /quote</b> that accepts a structured quotation request containing customer details and line items.
It performs decimal-safe pricing calculations, applies taxes, computes totals, and generates bilingual professional email drafts using a deterministic mock AI layer.
</p>

<h2>🎯 Objectives & Goals</h2>
<ul>
<li>Provide accurate financial calculations using decimal arithmetic</li>
<li>Generate professional quotation emails in English and Arabic</li>
<li>Expose a clean OpenAPI-compliant REST interface</li>
<li>Ensure validation, testing, and containerized deployment</li>
<li>Enable enterprise-ready extensibility for real LLM integration</li>
</ul>

<h2>✅ Acceptance Criteria</h2>
<table>
<tr><th>Criteria</th><th>Description</th></tr>
<tr><td>API Validity</td><td>POST /quote must accept and validate structured JSON</td></tr>
<tr><td>Accuracy</td><td>All totals must be decimal-safe and reproducible</td></tr>
<tr><td>Emails</td><td>Both English and Arabic drafts must be generated</td></tr>
<tr><td>Testing</td><td>All pytest tests must pass</td></tr>
<tr><td>Docs</td><td>Swagger docs must be available at /docs</td></tr>
</table>

<h2>💻 Prerequisites</h2>
<ul>
<li>Python 3.11+</li>
<li>pip</li>
<li>Docker (optional)</li>
<li>Postman or curl</li>
</ul>

<h2>⚙️ Installation & Setup</h2>
<ul>
<li>Create virtual environment</li>
<li>Install dependencies from requirements.txt</li>
<li>Run uvicorn app.main:app</li>
<li>Access http://127.0.0.1:8000/docs</li>
</ul>

<h2>🔗 API Documentation</h2>
<table>
<tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
<tr><td>POST</td><td>/quote</td><td>Accepts quotation JSON, returns totals and bilingual email drafts</td></tr>
</table>

<h2>🖥️ UI / Frontend</h2>
<p>
This microservice is API-first and UI-agnostic. The interactive Swagger UI at /docs serves as the reference interface for clients and testers.
</p>

<h2>🔢 Status Codes</h2>
<table>
<tr><th>Code</th><th>Meaning</th></tr>
<tr><td>200</td><td>Quotation generated successfully</td></tr>
<tr><td>422</td><td>Invalid input schema</td></tr>
<tr><td>500</td><td>Internal processing error</td></tr>
</table>

<h2>🚀 Features</h2>
<ul>
<li><b>Decimal-Safe Financial Engine</b> – Eliminates floating-point rounding errors for real-world pricing and taxation.</li>
<li><b>Multi-Item Quotation Processing</b> – Supports unlimited line items with quantity, unit price, and tax.</li>
<li><b>Bilingual AI Communication Layer</b> – Generates English and Arabic quotation emails using a deterministic AI engine.</li>
<li><b>Enterprise-Grade API Validation</b> – Uses Pydantic schemas to enforce strict data integrity.</li>
<li><b>OpenAPI / Swagger Interface</b> – Automatically generated interactive API documentation.</li>
<li><b>Mock LLM Abstraction</b> – Allows safe offline testing while keeping architecture ready for real OpenAI or Claude.</li>
<li><b>Dockerized Microservice</b> – Portable deployment across cloud, on-premise, or CI/CD pipelines.</li>
<li><b>Automated Testing Suite</b> – Financial correctness verified using Pytest.</li>
</ul>

<h2>🧱 Tech Stack & Architecture</h2>
<table>
<tr><th>Layer</th><th>Technology</th><th>Purpose</th></tr>
<tr><td>API Layer</td><td>FastAPI</td><td>High-performance REST API and OpenAPI generation</td></tr>
<tr><td>Validation</td><td>Pydantic</td><td>Strong typing, schema enforcement, email validation</td></tr>
<tr><td>Finance Engine</td><td>Decimal</td><td>Accurate currency and tax calculations</td></tr>
<tr><td>AI Layer</td><td>Mock LLM</td><td>Bilingual email generation engine</td></tr>
<tr><td>Testing</td><td>Pytest</td><td>Business logic verification</td></tr>
<tr><td>Deployment</td><td>Docker</td><td>Containerized execution</td></tr>
</table>

<pre>
Client
  |
  | POST /quote
  v
FastAPI Gateway
  |
  v
Pydantic Validation
  |
  v
Financial Engine (Decimal)
  |
  v
AI Draft Generator (Mock LLM)
  |
  v
Structured JSON Response
</pre>

<h2>🛠️ Workflow & Implementation</h2>
<ol>
<li>Client submits a quotation request with customer data and line items.</li>
<li>FastAPI validates all inputs using Pydantic models.</li>
<li>Each line item is processed using Decimal arithmetic to compute taxed totals.</li>
<li>The grand total is calculated from all validated line totals.</li>
<li>The Mock LLM engine generates professional quotation emails in English and Arabic.</li>
<li>The API returns a structured JSON response containing totals and both email drafts.</li>
</ol>

<h2>🧪 Testing & Validation</h2>
<table>
<tr><th>ID</th><th>Area</th><th>Command</th><th>Expected Output</th><th>Explanation</th></tr>
<tr><td>T1</td><td>Math</td><td>pytest</td><td>Pass</td><td>Verifies line and grand totals</td></tr>
<tr><td>T2</td><td>API</td><td>POST /quote</td><td>200</td><td>Validates full pipeline</td></tr>
</table>

<h2>🔍 Validation Summary</h2>
<p>All inputs are validated using Pydantic and all arithmetic uses Decimal to prevent rounding errors.</p>

<h2>🧰 Verification Testing Tools & Command Examples</h2>
<ul>
<li>pytest</li>
<li>curl</li>
<li>FastAPI Swagger UI</li>
</ul>

<h2>🧯 Troubleshooting & Debugging</h2>
<ul>
<li><b>422 Unprocessable Entity</b> – Input JSON does not match Pydantic schema (email format, missing fields, wrong types).</li>
<li><b>500 Internal Server Error</b> – Logic or AI layer failure; check Uvicorn logs.</li>
<li><b>Incorrect totals</b> – Indicates Decimal conversion issue or invalid numeric input.</li>
<li><b>Swagger not loading</b> – Ensure FastAPI is running on port 8000 and no firewall is blocking it.</li>
</ul>

<h2>🔒 Security & Secrets</h2>
<p>
No API keys are required. The Mock LLM ensures zero data leakage and full offline execution.
</p>

<h2>☁️ Deployment</h2>
<p>
The microservice is containerized using Docker and can be deployed to any cloud or on-premise infrastructure including AWS ECS, Azure Container Apps, GCP Cloud Run, or a private VPS.
</p>
<ul>
<li>Stateless microservice – horizontally scalable</li>
<li>No external API dependencies in Mock LLM mode</li>
<li>Ready for CI/CD pipelines</li>
</ul>

<h2>⚡ Quick-Start Cheat Sheet</h2>
<ul>
<li>Install → Run → Open /docs → Send POST /quote</li>
</ul>

<h2>🧾 Usage Notes</h2>
<p>
Clients must submit valid email addresses and numeric prices. Currency precision is preserved via Decimal.
</p>

<h2>🧠 Performance & Optimization</h2>
<ul>
<li>FastAPI provides asynchronous request handling.</li>
<li>Decimal ensures correctness over raw float performance.</li>
<li>Stateless design allows horizontal scaling.</li>
<li>Docker image is lightweight (Python slim base).</li>
</ul>

<h2>🌟 Enhancements & Features</h2>
<ul>
<li>Replace Mock LLM with OpenAI or Claude</li>
<li>Add PDF quotation generation</li>
<li>CRM integration</li>
</ul>

<h2>🧩 Maintenance & Future Work</h2>
<ul>
<li>Add database persistence</li>
<li>Add authentication</li>
<li>Add async LLM support</li>
</ul>

<h2>🏆 Key Achievements</h2>
<ul>
<li>Built a finance-grade pricing engine using Decimal.</li>
<li>Implemented bilingual AI-driven business communication.</li>
<li>Delivered a fully documented OpenAPI microservice.</li>
<li>Packaged the entire system for cloud deployment.</li>
</ul>

<h2>🧮 High-Level Architecture</h2>

<p>
The Quotation Microservice is designed as a clean, stateless, API-driven financial and AI communication engine.  
It follows a layered microservice architecture that separates input validation, business logic, and AI-based content generation, ensuring scalability, security, and auditability.
</p>

<h3>🔹 Architectural Layers</h3>
<table>
<tr><th>Layer</th><th>Responsibility</th><th>Key Components</th></tr>
<tr><td>Client Layer</td><td>Submits quotation requests</td><td>Postman, CRM, Web App, Swagger UI</td></tr>
<tr><td>API Gateway</td><td>Request routing & validation</td><td>FastAPI</td></tr>
<tr><td>Validation Layer</td><td>Schema & data integrity enforcement</td><td>Pydantic Models</td></tr>
<tr><td>Business Logic Layer</td><td>Financial computation engine</td><td>logic.py (Decimal pricing)</td></tr>
<tr><td>AI Communication Layer</td><td>Bilingual email generation</td><td>mock_llm.py</td></tr>
<tr><td>Response Layer</td><td>Structured JSON output</td><td>FastAPI Serializer</td></tr>
</table>

<h3>🔹 High-Level System Flow</h3>
<pre>
┌──────────────────────┐
│  Client Applications │
│ (CRM, Swagger, API)  │
└───────────┬──────────┘
            │  POST /quote (JSON)
            ▼
┌───────────────────────────┐
│       FastAPI API          │
│   app.main : /quote        │
└───────────┬───────────────┘
            │
            ▼
┌───────────────────────────┐
│     Pydantic Validation   │
│  Email, Items, Price, Tax │
└───────────┬───────────────┘
            │ Validated Data
            ▼
┌───────────────────────────┐
│  Financial Engine         │
│  logic.py (Decimal Math)  │
│  - Line Totals            │
│  - Tax Calculation        │
│  - Grand Total            │
└───────────┬───────────────┘
            │ Calculated Quote
            ▼
┌───────────────────────────┐
│   AI Communication Layer  │
│  mock_llm.py              │
│  - English Email          │
│  - Arabic Email           │
└───────────┬───────────────┘
            │
            ▼
┌───────────────────────────┐
│   Structured API Response │
│  Totals + Email Drafts    │
└───────────┬───────────────┘
            │
            ▼
┌──────────────────────┐
│     Client Receives  │
│   Final Quotation    │
└──────────────────────┘
</pre>

<h3>🔹 Why This Architecture Is Enterprise-Grade</h3>
<ul>
<li>Stateless microservice – horizontally scalable</li>
<li>Strict data validation before any computation</li>
<li>Financial-grade decimal arithmetic</li>
<li>AI layer isolated for safe testing and future LLM integration</li>
<li>API-first design for CRM, ERP, and SaaS integrations</li>
<li>Container-ready for cloud deployment</li>
</ul>

<h2>🗂️ Project Structure</h2>
<pre>
Quotation Microservice/
│
├─ app/
│   ├─ main.py
│   ├─ models.py
│   ├─ logic.py
│   └─ mock_llm.py
│
├─ tests/
│   └─ test_quote.py
│
├─ Dockerfile
├─ requirements.txt
├─ README.md
└─ technical_project_detail.pdf
</pre>

<h2>🧭 How to Demonstrate Live</h2>
<ul>
<li>Run uvicorn</li>
<li>Open /docs</li>
<li>Submit POST /quote</li>
<li>Show totals + bilingual email output</li>
</ul>

<h2>💡 Summary, Closure & Compliance</h2>
<p>
This project demonstrates enterprise-grade API engineering, financial computation accuracy, and AI-assisted business communication in a single microservice. 
It is compliant with modern backend standards including OpenAPI, containerization, test automation, and clean architecture, making it suitable for production, SaaS platforms, and CRM-driven sales automation.
</p>

</body>
</html>
