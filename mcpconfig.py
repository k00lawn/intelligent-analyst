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
                "/home/abulayth/"
            ]
        }
    }
}