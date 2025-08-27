from fastmcp import Client
from google import genai
import asyncio

config = {
    "mcpServers": {
        "time": {
            "command": "uvx",
            "args": ["mcp-server-time"]
        },
        "filesystem": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                # "/home/abulayth/Desktop",
                "/home/abulayth/Work/aistuff/intelligent-analyst"
            ]
        }
    }
}

mcp_client = Client(config)
gemini_client = genai.Client()

async def main():    
    async with mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents="create a file named 'createdbymcp.txt' with 'hello world'",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[mcp_client.session],  # Pass the FastMCP client session
            ),
        )
        print(response.text)

if __name__ == "__main__":
    asyncio.run(main())