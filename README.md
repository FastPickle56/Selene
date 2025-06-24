# Selene Telegram Bot 🌙

A moon-goddess–themed AI bot built with Python, Telegram, and the OpenAI API.

## ✨ Features

- `/start`: Greets the user with poetic charm  
- Intelligent chat with GPT-3.5  
- Generates DALL·E images from natural language prompts (e.g., "create a moonlit forest", "draw Selene in a white dress")

## 🚀 Setup Instructions

### Environment Variables

Add the following variables either locally in a `.env` file or via your hosting service (Railway, Render, etc.):

```
TELEGRAM_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

### Run Locally

```
pip install -r requirements.txt
python main.py
```

### 🛠 Deployment (Recommended: Railway)

1. Go to [https://railway.app](https://railway.app)
2. Click "New Project" > "Deploy from GitHub"
3. Connect your GitHub account and choose this repo
4. Add the `TELEGRAM_TOKEN` and `OPENAI_API_KEY` under "Variables"
5. Deploy and you're live!

---

Made with moonlight and Python 🌕✨
