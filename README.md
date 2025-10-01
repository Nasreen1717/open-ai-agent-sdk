
# Open AI Agent SDK – Demo Project

This repository demonstrates how to build AI-powered agents using the **OpenAI SDK**, custom tools, and contextual data.
The project is structured with examples for single-agent interaction, context-aware agents, and tool-augmented agents.

---

## 📂 Project Structure

```
.
├── context.py        # Contextual agent with UserInfo and purchase history tool
├── single_agent.py   # Simple agent example
├── tool2.py          # Weather tool integration example
├── .gitignore        # Ignored files for uv project
├── requirements.txt  # Project dependencies
```

---

## 🚀 Features

* **Single Agent**: Generate responses directly with minimal setup.
* **Context-Aware Agent**: Pass structured user context (e.g., user profile, purchase history).
* **Tool-Augmented Agent**: Extend agent capabilities with custom tools like weather lookup.
* **Async + Sync Support**: Run agents synchronously or asynchronously.

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/open-ai-agent-sdk.git
cd open-ai-agent-sdk

# Create & activate environment (uv)
uv venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Install dependencies
uv pip install -r requirements.txt
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root folder with your OpenAI API key:

```ini
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Usage

### Run Single Agent

```bash
python single_agent.py
```

➡ Example output: *A short poem on programming.*

### Run Contextual Agent

```bash
python context.py
```

➡ Example output: *The user Ali recently purchased a laptop.*

### Run Weather Tool Agent

```bash
python tool2.py
```

➡ Example output: *The weather in Karachi is hot 🔥*

---

## 📌 Notes

* The examples simulate logic; replace placeholder functions with real APIs for production use.
* All scripts are modular; you can add new tools by using the `@function_tool` decorator.

---

## 📄 License

This project is licensed under the MIT License.

---


