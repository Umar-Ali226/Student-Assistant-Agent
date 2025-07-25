📘 Smart Student Agent Assistant
This is a simple AI-based assistant built using Python and OpenAI's Agent SDK. It is designed to help students by performing the following tasks:

Answering academic questions 🤓

Providing study tips 📚

Summarizing small text passages 📝

🚀 Features
Easy-to-use OpenAI Agent SDK integration

Uses Gemini 2.5 Flash model for fast, smart responses

Reads API key securely from environment file

Beginner-friendly structure and flow

🧱 Requirements
Python 3.9 or later

Gemini API Key (set in .env file)

Installed libraries: openai, openai-agents, python-dotenv

🔐 Setup Instructions
Clone the repository to your local machine.

Create a .env file in the project directory and add your Gemini API key using the key GEMINI_API_KEY.

Make sure all dependencies are installed using pip.

Run the Python script to test the assistant.

⚙️ How It Works
The assistant loads your Gemini API key securely using environment variables.

It creates an OpenAI-compatible client that points to the Gemini API base URL.

It defines an agent with a simple instruction: help students with academics.

The agent is run using the Runner class, where it takes an input and generates a response based on the given model and configuration.

Finally, the assistant prints out the answer — which could be a summary, a study tip, or an answer to a question.

💡 Use Cases
Quickly get summaries of complex academic topics

Get customized study tips for different subjects

Ask general knowledge or academic questions

📄 Example Input
Can I get information about HSC? Make me a summary of it.

✨ Output (Example)
HSC stands for Higher Secondary Certificate. It is an important educational milestone in many countries...

📩 Credits
This project was created as Assignment 1: Smart Student Agent Assistant for learning purposes using OpenAI’s Agent SDK.
