# 🧠 MCP Interactive Chatbot with LangChain and Groq

This project is an AI-powered interactive chatbot built using the [MCP (Model Context Protocol)](https://github.com/mcptutorial/mcp-use), LangChain, and Groq's fast LLMs. It enables natural language conversations that can also interact with services like browsers, Airbnb listings, and search engines using MCP.



## 🚀 Features

- ✅ Asynchronous interactive chat interface
- ✅ Memory-enabled conversational agent powered by LangChain
- ✅ Seamless integration with MCP services (Playwright, DuckDuckGo, Airbnb)
- ✅ Super-fast response via [Groq API](https://console.groq.com/)
- ✅ Simple terminal-based experience with memory management (`clear`, `exit`)
- ✅ Scalable setup with modular service integration


## 🧰 Technologies Used

- **Python 3.10+**
- [`mcp_use`](https://github.com/mcptutorial/mcp-use)
- [`LangChain`](https://www.langchain.com/)
- `ChatGroq` from `langchain_groq`
- `asyncio` for non-blocking interactions
- `.env` for managing secrets


## 📁 Project Structure


mcp_demo/
│
├── app.py                 # Main chat interface
├── .env                   # Stores your GROQ API Key
├── browser_mcp.json       # MCP services configuration
├── requirements.txt       # Project dependencies


## 🛠️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/mcp-demo-chatbot
cd mcp_demo
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Add Your GROQ API Key**

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Set Up MCP Services**

Create a file named `browser_mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb"]
    },
    "duckduckgo-search": {
      "command": "npx",
      "args": ["-y", "duckduckgo-mcp-server"]
    }
  }
}
```

Make sure Node.js and `npx` are installed and accessible from your terminal.

## ▶️ Running the App

```bash
python app.py
```

Then start chatting! For example:

- `What is the weather in New York?`
- `Search for the latest AI news`
- `Find me Airbnb rentals in Bangalore`

You can also:
- Type `clear` to reset memory
- Type `exit` to end the session

## ⚠️ Troubleshooting

- **Takes too long to respond?**
  - Ensure MCP services aren't hanging.
  - Try restarting the MCP subprocesses or simplify your prompt.
  - Check internet connection and firewall settings.

- **FileNotFoundError?**
  - Confirm that `browser_mcp.json` is in the same directory as `app.py`.

- **Still not working?**
  - Print debug logs in `app.py` or reinstall dependencies.

## 🧪 Sample Output

```bash
User: What’s the weather in New York?
AI: Based on recent searches via DuckDuckGo, it's currently 15°C and cloudy in New York.
```

## 💻 MCP Services You Can Add

You can extend the chatbot with even more services like:

- **YouTube Search**
- **PDF Readers**
- **Finance APIs**
- **Calendar APIs**
- Or custom tools you write yourself!

Just add them inside `browser_mcp.json` and make sure they're callable via MCP.

## 📦 Example `requirements.txt`

```txt
python-dotenv
mcp_use
langchain
langchain_groq
```

## 📝 License

MIT License. See the [LICENSE](LICENSE) file for details.


## 🙌 Credits

- [MCP Protocol](https://github.com/mcptutorial/mcp-use)
- [LangChain](https://www.langchain.com/)
- [Groq API](https://console.groq.com/)
- [DuckDuckGo Search MCP](https://github.com/mcptutorial/duckduckgo-mcp-server)
- [Playwright MCP](https://github.com/mcptutorial/playwright-mcp-server)


## 🌐 Author

Vishwas R  
Feel free to connect on [LinkedIn](https://www.linkedin.com/vishwas645) or explore other projects on [GitHub](https://github.com/vishwaspw)

```

---

Let me know if you’d like to turn this into a GitHub Pages landing page or want badges and shield links added at the top!
