# Nova Act MCP Server

A Model Context Protocol (MCP) server that provides browser automation capabilities via Nova Act.

## Features

- Browser automation through natural language prompts
- Demonstrates buying products on Amazon (for example purposes)
- Fully compatible with Claude and Cursor MCP configurations

## Setup

### Prerequisites

- Python 3.8+
- Node.js 14+ (for running with npx)
- Nova Act API key (get one from [Nova Act](https://nova-act.com))
- Amazon credentials (if using the example tool)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mcp_agi_house.git
cd mcp_agi_house
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials:
```
NOVA_ACT_API_KEY=your_nova_act_api_key
AMAZON_USERNAME=your_amazon_email
AMAZON_PASSWORD=your_amazon_password
```

## Adding to Claude or Cursor MCP Configuration

### Claude Configuration

Add the following to your Claude MCP configuration:

```json
{
  "mcpServers": {
    "NovaAct": {
      "command": "python",
      "args": [
        "path/to/mcp_agi_house/agi.py"
      ]
    }
  }
}
```

### Cursor Configuration

Add the following to your Cursor MCP configuration file:

```json
{
  "mcpServers": {
    "NovaAct": {
      "command": "python",
      "args": [
        "path/to/mcp_agi_house/agi.py"
      ]
    }
  }
}
```

For a more complete configuration integrating with other MCP servers:

```json
{
  "mcpServers": {
    "SequentialThinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    },
    "BrowserTools": {
      "command": "npx",
      "args": [
        "@agentdeskai/browser-tools-mcp@1.1.0"
      ]
    },
    "NovaAct": {
      "command": "python",
      "args": [
        "path/to/mcp_agi_house/agi.py"
      ]
    }
  }
}
```

Make sure to replace `"path/to/mcp_agi_house/agi.py"` with the actual path to your agi.py file on your system.

## Available Tools

Currently, this MCP server provides the following tools:

- `buy_me_pistachios`: Demonstrates browser automation by purchasing pistachios from Amazon (for example purposes only)

## Customizing

You can modify the `agi.py` file to add your own browser automation tools using the Nova Act library. Follow the example provided in the file.

## License

MIT 