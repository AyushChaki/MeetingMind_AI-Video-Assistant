<div align="center">

<br/>

```
███╗   ███╗███████╗███████╗████████╗██╗███╗   ██╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗
████╗ ████║██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ ████╗ ████║██║████╗  ██║██╔══██╗
██╔████╔██║█████╗  █████╗     ██║   ██║██╔██╗ ██║██║  ███╗██╔████╔██║██║██╔██╗ ██║██║  ██║
██║╚██╔╝██║██╔══╝  ██╔══╝     ██║   ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║  ██║
██║ ╚═╝ ██║███████╗███████╗   ██║   ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██████╔╝
╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝
```

**AI-powered meeting intelligence — transcribe, summarise, extract, and chat with any video.**

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-f5e642?style=flat-square&logo=python&logoColor=black)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2%2B-1c3c3c?style=flat-square&logo=chainlink&logoColor=white)](https://langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-3ef5a0?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff7b54?style=flat-square)](CONTRIBUTING.md)

<br/>

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-meetingmindai-ff7b54?style=for-the-badge)](https://meetingmindai-video-assistant-u3hambgnruuknqvhsybo79.streamlit.app/)

<br/>

[**Quick Start**](#-quick-start) · [**Features**](#-features) · [**Architecture**](#-architecture) · [**Configuration**](#-configuration) · [**Contributing**](#-contributing)

</div>

---

## 🧠 What is MeetingMind?

MeetingMind is an open-source AI pipeline that turns any **YouTube video or local media file** into structured, actionable intelligence. Feed it a meeting recording, lecture, podcast, or interview — and get back a full transcript, an executive summary, a list of action items, key decisions, open questions, and a persistent RAG-powered chat interface to query the content conversationally.

It ships as both a **CLI tool** and a **Streamlit web app** with a dark, minimal UI.

```
Input (URL / file)
       │
       ▼
 Audio Extraction  ──►  Chunked Transcription  ──►  Title + Summary
                                                          │
                                         Action Items ◄───┤
                                         Key Decisions ◄──┤
                                         Open Questions ◄─┤
                                                          │
                                                    RAG Index
                                                          │
                                                   Chat Interface
```

---
## 📸 Application Preview

### Home Screen

![Home Screen](home.png)<img width="1889" height="881" alt="home png" src="https://github.com/user-attachments/assets/7aa6223c-49de-48d9-939e-c088f322c835" />

### Output Preview

![Chat Interface](output.png)<img width="1801" height="871" alt="output png" src="https://github.com/user-attachments/assets/7ded8641-c109-4662-adcd-c24247960922" />

### Chat Interface

![Chat Interface](chatbot.png)<img width="1828" height="824" alt="chatbot png" src="https://github.com/user-attachments/assets/f2026273-9b16-41d6-ad92-aa3ca6ab74be" />


## ✨ Features

| Capability | Details |
|---|---|
| 🎙️ **Multi-source input** | YouTube URLs, MP4, MKV, MP3, WAV, and more |
| 📝 **Chunked transcription** | Handles long-form content by splitting audio into manageable segments |
| 🌐 **Multilingual** | English and Hinglish supported out of the box; extendable |
| 🏷️ **Auto title generation** | LLM-generated meeting/video title from transcript content |
| 📋 **Executive summary** | Concise paragraph-level summary of the full content |
| ✅ **Action item extraction** | Pulls concrete next steps and ownership signals |
| 🔑 **Key decisions** | Identifies decisions made during the meeting/talk |
| ❓ **Open questions** | Surfaces unresolved questions and outstanding items |
| 💬 **RAG chat** | Ask anything about the content via a retrieval-augmented chat interface |
| 🖥️ **Streamlit UI** | Full-featured dark-mode web app with live progress tracking |
| ⌨️ **CLI mode** | Scriptable pipeline for automation and batch processing |

---

## 🚀 Quick Start

### Prerequisites

- Python **3.10+**
- `ffmpeg` installed and on your `PATH`
- A **Mistral API key** — get one free at [console.mistral.ai](https://console.mistral.ai/)

### 1 — Clone the repo

```bash
git clone https://github.com/your-username/meetingmind.git
cd meetingmind
```

### 2 — Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Set up environment variables

```bash
cp .env.example .env
# Edit .env and add your API keys
```

### 5 — Launch the web app

```bash
streamlit run app.py
```

Or run the CLI directly:

```bash
python main.py
# Enter YouTube URL or local file path: https://youtube.com/watch?v=...
# Language (english/hinglish): english
```

---

## 📁 Project Structure

```
meetingmind/
│
├── app.py                  # Streamlit UI entry point
├── main.py                 # CLI entry point & pipeline orchestrator
├── requirements.txt
├── .env.example
│
├── core/
│   ├── transcriber.py      # Chunked Whisper transcription
│   ├── summarize.py        # LLM summary + title generation
│   ├── extractor.py        # Action items, decisions, questions
│   └── rag_engine.py       # LangChain RAG chain builder & query handler
│
└── utils/
    └── audio_processor.py  # Source detection, download, chunking
```

---

## 🏗️ Architecture

### Pipeline overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         run_pipeline()                          │
│                                                                 │
│  ┌──────────────┐    ┌───────────────┐    ┌──────────────────┐  │
│  │ AudioProcessor│───►│  Transcriber  │───►│   Summarizer     │  │
│  │  (YouTube /  │    │  (Whisper /   │    │  generate_title  │  │
│  │  local file) │    │   chunked)    │    │  summarize()     │  │
│  └──────────────┘    └───────────────┘    └──────────────────┘  │
│                                                    │            │
│                       ┌────────────────────────────┘            │
│                       ▼                                         │
│          ┌────────────────────────┐                             │
│          │       Extractor        │                             │
│          │  · action_items        │                             │
│          │  · key_decisions       │                             │
│          │  · open_questions      │                             │
│          └────────────────────────┘                             │
│                       │                                         │
│                       ▼                                         │
│          ┌────────────────────────┐                             │
│          │      RAG Engine        │                             │
│          │  · build_rag_chain()   │                             │
│          │  · ask_question()      │                             │
│          └────────────────────────┘                             │
└─────────────────────────────────────────────────────────────────┘
```

### Core modules

**`utils/audio_processor.py`**  
Detects whether the source is a YouTube URL or a local path. Downloads YouTube audio via `yt-dlp`, then splits audio into fixed-size chunks using `pydub` to stay within transcription API limits.

**`core/transcriber.py`**  
Iterates over audio chunks and transcribes each using **Whisper `small`** (local model via `openai-whisper`). Concatenates chunk transcripts into a single string.

**`core/summarize.py`**  
Uses an LLM prompt chain to generate a short meeting title (`generate_title`) and a structured executive summary (`summarize`) from the full transcript.

**`core/extractor.py`**  
Three focused extraction prompts — one each for action items, key decisions, and open questions — run against the full transcript and return structured plain-text output.

**`core/rag_engine.py`**  
Embeds the transcript into a FAISS (or Chroma) vector store via LangChain, constructs a `RetrievalQA` chain, and exposes `ask_question(chain, query)` for interactive Q&A.

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and fill in the values:

```env
# ── LLM Provider (Mistral) ────────────────────────────────────
MISTRAL_API_KEY=your-mistral-api-key-here

# ── Whisper ───────────────────────────────────────────────────
# Local Whisper model — no API key required
WHISPER_BACKEND=local
WHISPER_MODEL=small

# ── RAG / Vector store ────────────────────────────────────────
# "faiss" (default, no server needed) or "chroma"
VECTOR_STORE=faiss

# ── Audio chunking ────────────────────────────────────────────
CHUNK_DURATION_MS=60000   # 60 s chunks
```

### LLM backend — Mistral AI

MeetingMind uses the **[Mistral API](https://console.mistral.ai/)** for all summarisation, extraction, and RAG chat. Get your free API key at `console.mistral.ai` and paste it into `.env`.

| Model used | Task |
|---|---|
| `mistral-small-latest` | Title generation, summarisation, extraction prompts |
| `mistral-small-latest` | RAG chain Q&A |

Want to swap providers? MeetingMind's LangChain layer is backend-agnostic — replace the Mistral client in `core/` with any OpenAI-compatible provider (OpenAI, Groq, Together AI, Ollama, etc.).

### Transcription — Whisper `small` (local)

Transcription runs **fully offline** using OpenAI's `whisper` library with the `small` model. No API key or internet connection is needed for this step — audio never leaves your machine.

| Model | VRAM | Speed | Accuracy |
|---|---|---|---|
| `tiny` | ~1 GB | fastest | lower |
| **`small` ✓ used here** | **~2 GB** | **fast** | **good** |
| `medium` | ~5 GB | moderate | better |
| `large` | ~10 GB | slowest | best |

To switch models, update `WHISPER_MODEL` in `.env`.

---

## 🖥️ Streamlit UI walkthrough

| Section | Description |
|---|---|
| **Source input** | Paste a YouTube URL or absolute/relative file path |
| **Language selector** | Choose `english` or `hinglish` before running |
| **Live progress** | Step-by-step animated tracker shows pipeline status in real time |
| **Title card** | Auto-generated meeting title displayed prominently |
| **Results grid** | Summary · Action Items · Key Decisions · Open Questions in a 2-column layout |
| **Full transcript** | Collapsible expander with the complete raw transcript |
| **RAG Chat** | Persistent chat window; ask anything about the meeting content |

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

Tests cover the individual core modules with short fixture transcripts. Audio download and LLM calls are mocked by default to keep the suite fast and offline-friendly.

---

## 📦 requirements.txt

```
streamlit>=1.35
mistralai>=0.4
langchain>=0.2
langchain-mistralai>=0.1
langchain-community>=0.2
faiss-cpu>=1.8
openai-whisper>=20231117
yt-dlp>=2024.5
pydub>=0.25
python-dotenv>=1.0
```

> **Note:** `openai-whisper` downloads the `small` model weights (~460 MB) on first run. Ensure `ffmpeg` is installed and on your `PATH` for audio processing.

---

## 🤝 Contributing

Contributions are welcome and appreciated!

1. Fork the repository
2. Create a feature branch — `git checkout -b feat/your-feature`
3. Commit your changes — `git commit -m "feat: add your feature"`
4. Push to the branch — `git push origin feat/your-feature`
5. Open a Pull Request

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages and ensure `pytest` passes before opening a PR.

---

## 🗺️ Roadmap

- [ ] Speaker diarisation (who said what)
- [ ] Multi-file / batch processing
- [ ] Export to PDF / Notion / Confluence
- [ ] Webhook support for async processing
- [ ] Support for Deepgram and AssemblyAI as transcription backends
- [ ] Docker + `docker-compose` setup

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

Built with ♥ using Python, LangChain, Whisper, and Streamlit.

</div>
