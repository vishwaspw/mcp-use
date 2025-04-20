import asyncio
from dotenv import load_dotenv
import os
from mcp_use import MCPClient, MCPAgent
from langchain_groq import ChatGroq

async def run_memory_chat():
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Update this if your file is renamed or moved
    config_file = "browser_mcp.json"
    print("Initializing chat....")

    # Load multiple services via config file
    client = MCPClient.from_config_file(config_file)

    # Use your preferred LLM - you can swap models here
    llm = ChatGroq(model="gemma-7b-it")

    # Initialize MCP agent with memory and expanded tools/services
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=20,
        memory_enabled=True
    )

    print("\n===== Interactive MCP Chat with Enhanced Services =====")
    print("Type 'exit' to end the conversation.")
    print("Type 'clear' to clear the memory.")
    print("=======================================================\n")

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat....")
                break
            elif user_input.lower() == "clear":
                agent.clear_memory()
                print("Memory cleared.")
                continue

            print("\nAssistant: ", end="", flush=True)
            try:
                print("Sending to agent...")
                response = await agent.run(user_input)
                print("Got response.")
                print(response)
            except Exception as e:
                print(f"An error occurred: {e}")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
