# Local Research MCP Server

A free, private research assistant for Claude Desktop that searches the web and scrapes content using DuckDuckGo and Python. This MCP server gives Claude the ability to access real-time information while keeping all processing local for complete privacy.

## Features

- 🔍 **Free Web Search**: Uses DuckDuckGo's search API without requiring API keys
- 📄 **Content Extraction**: Intelligently extracts clean text from web pages
- 🔒 **Privacy-First**: All processing happens locally on your machine
- ⚡ **Fast Integration**: Works seamlessly with Claude Desktop via MCP
- 🛠️ **Zero Dependencies**: No external services or subscriptions required

## Quick Start

### Prerequisites

- Python 3.10 or higher
- Claude Desktop installed
- Basic command line knowledge

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Unlock-MCP/local-research-server.git
   cd local-research-server
   ```

2. **Set up the environment:**
   ```bash
   uv init
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   uv add "mcp[cli]" duckduckgo-search trafilatura
   ```

4. **Test the server:**
   ```bash
   python research_server.py
   ```

### Claude Desktop Configuration

Add this configuration to your Claude Desktop config file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "local-researcher": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/local-research-server",
        "run",
        "python",
        "research_server.py"
      ]
    }
  }
}
```

Replace `/path/to/your/local-research-server` with the full path to this directory.

## Usage

After configuration, restart Claude Desktop completely. You'll see a plug icon (🔌) indicating the server is connected.

Ask Claude research questions like:
- "What are the latest developments in AI research this week?"
- "Research current renewable energy trends in Europe"
- "Find recent cybersecurity threat reports"

Claude will automatically use your local server to fetch real-time information.

## How It Works

The server implements a single MCP tool that:

1. **Searches** the web using DuckDuckGo's free API
2. **Scrapes** content from the top search results
3. **Extracts** clean, readable text using Trafilatura
4. **Returns** formatted content to Claude for analysis

All processing happens locally with no data sent to external services except for the public web searches.

## Architecture

```
Claude Desktop
    ↓ (MCP Protocol)
Local Research Server
    ↓ (Search API)
DuckDuckGo Search
    ↓ (HTTP Requests)
Target Websites
    ↓ (Content Extraction)
Clean Text → Claude
```

## Configuration Options

The server accepts these parameters for the research tool:

- `query` (string): The search query or research topic
- `num_results` (int): Number of search results to process (default: 3)

## Security Features

- **Input Validation**: Sanitizes search queries
- **Rate Limiting**: Polite delays between web requests
- **Error Handling**: Graceful failure handling
- **Local Processing**: No external data dependencies

## Business Applications

This research server is ideal for:

- **Content Creation**: Research-backed article writing
- **Market Analysis**: Real-time competitor and industry research
- **Due Diligence**: Company and investment research
- **Regulatory Monitoring**: Tracking compliance requirements

## Extending the Server

Consider these enhancements:

- Add RSS feed integration
- Implement search result caching
- Add domain filtering capabilities
- Include publication date extraction
- Add multiple search engine support

## Troubleshooting

### Common Issues

**Server not connecting:**
- Verify the absolute path in Claude config
- Restart Claude Desktop completely
- Check that Python dependencies are installed

**No search results:**
- Verify internet connection
- Check DuckDuckGo service status
- Try different search queries

**Content extraction failing:**
- Some websites block scraping
- Try different search terms for varied sources
- Check the console output for specific errors

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Related Projects

- [MCP Docs Server](https://github.com/Unlock-MCP/mcp-docs-server) - Local documentation access
- [Remote MCP Server](https://github.com/Unlock-MCP/remote-mcp-server) - Enterprise database access
- [UnlockMCP Website](https://unlockmcp.com) - MCP tutorials and resources

## Support

- [Tutorial Guide](https://unlockmcp.com/guides/build-local-research-mcp-server)
- [MCP Documentation](https://unlockmcp.com/guides/getting-started-mcp)
- [Issue Tracker](https://github.com/Unlock-MCP/local-research-server/issues)