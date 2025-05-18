# Nova Act MCP Tool

A Model Control Protocol (MCP) server that provides a `buy_me_pistachios` tool for buying Wonderful Pistachios Salt and Vinegar (22 oz) from Amazon.

## Overview

This project implements a FastMCP server with NovaAct integration that allows Claude or other AI assistants to automate purchasing pistachios from Amazon. It demonstrates how to create custom MCP tools that can perform web automation tasks.

## Prerequisites

- Python 3.7+
- An OpenAI API key (for Claude integration)
- Nova Act API key
- Amazon account credentials

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mcp_agi_house.git
   cd mcp_agi_house
   ```

2. Install the required dependencies:
   ```bash
   pip install fastmcp nova-act python-dotenv
   ```

3. Create a `.env` file in the project root with your credentials:
   ```
   AMAZON_USERNAME=your_amazon_email
   AMAZON_PASSWORD=your_amazon_password
   NOVA_ACT_API_KEY=your_nova_act_api_key
   ```

## Usage

Run the MCP server:

```bash
python agi.py
```

This will start the server on the default port (typically 8000), making the `buy_me_pistachios` tool available to connected AI assistants.

## Adding to Claude or Cursor MCP Configs

### For Claude in the Web UI

1. Claude currently doesn't directly support custom MCP tools in the web interface. However, you can use projects like [Claude-to-MCP](https://github.com/anthropics/claude-to-mcp) to bridge the gap.

### For Cursor

1. Open Cursor settings
2. Navigate to the AI settings section
3. Find the MCP configuration area
4. Add a new MCP tool configuration with:
   ```json
   {
     "tools": [
       {
         "name": "NovaAct_buy_me_pistachios",
         "description": "Buys a bag of wonderful pistachios salt and vinegar 22 oz using credentials from environment variables.",
         "endpoint": "http://localhost:8000/tools/buy_me_pistachios",
         "schema": {
           "type": "function",
           "function": {
             "name": "buy_me_pistachios",
             "description": "Buys a bag of wonderful pistachios salt and vinegar 22 oz using credentials from environment variables. This tool will automate the process of logging in and buying a bag of wonderful pistachios salt and vinegar 22 oz. Returns information about the bought product including name, price, and expected delivery date.",
             "parameters": {
               "type": "object",
               "properties": {},
               "required": []
             }
           }
         }
       }
     ]
   }
   ```

### For Claude API Integration

To use this MCP tool with Claude via the API:

1. Start your MCP server by running `python agi.py`

2. In your API request to Claude, include the MCP tool in the `tools` parameter:

```python
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    system="You are an assistant that helps users shop on Amazon.",
    messages=[
        {"role": "user", "content": "Can you buy me some pistachios?"}
    ],
    tools=[
        {
            "name": "buy_me_pistachios",
            "description": "Buys a bag of wonderful pistachios salt and vinegar 22 oz using credentials from environment variables.",
            "input_schema": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    ],
    tool_choice="auto"
)
```

3. Configure your tool calling handler to connect to your local MCP server:

```python
# Example tool calling handler
def handle_tool_call(tool_call):
    if tool_call.name == "buy_me_pistachios":
        # Make a request to your MCP server
        response = requests.post(
            "http://localhost:8000/tools/buy_me_pistachios",
            json=tool_call.input
        )
        return response.json()
    return {"error": "Unknown tool"}
```

## Troubleshooting

- If you encounter connection issues, make sure your MCP server is running
- For authentication failures, check that your `.env` file contains the correct credentials
- If the browser automation fails, try running with `headless=False` to see what's happening

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license here] 