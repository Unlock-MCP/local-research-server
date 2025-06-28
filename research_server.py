# research_server.py
import asyncio
from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS
import trafilatura

# Initialize the MCP server with a descriptive name
mcp = FastMCP("LocalResearcher")

@mcp.tool(
    title="Web Research and Content Scraper",
    description="Performs a web search for a query, scrapes the clean text from the top results, and returns it as a single block of text."
)
async def research_and_scrape(query: str, num_results: int = 3) -> str:
    """
    Searches the web and scrapes content from top results.

    Args:
        query: The topic or question to research.
        num_results: The number of top search results to read (default is 3).
    """
    print(f"INFO: Starting research for: '{query}'")
    scraped_texts = []

    try:
        # Use DuckDuckGo to get search results
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=num_results)]

        if not results:
            return "Apologies, I couldn't find any web search results for that query."

        # Loop through each result and scrape its content
        for i, result in enumerate(results):
            url = result['href']
            print(f"INFO: Scraping ({i+1}/{num_results}): {url}")
            try:
                # Trafilatura downloads the page and extracts the main article text
                downloaded_page = trafilatura.fetch_url(url)
                if downloaded_page:
                    main_text = trafilatura.extract(downloaded_page, favor_precision=True)
                    if main_text:
                        # Format the output for Claude
                        scraped_texts.append(f"--- Source {i+1}: {url} ---\n\n{main_text}\n\n")

                # Polite delay between requests
                await asyncio.sleep(0.5)
            except Exception as e:
                # Log errors but continue processing other URLs
                print(f"WARN: Failed to scrape {url}. Reason: {e}")
                continue

    except Exception as e:
        return f"An unexpected error occurred during the research process: {e}"

    if not scraped_texts:
        return "I found search results, but was unable to extract content from any of them."

    # Combine all scraped content and return to Claude
    print("INFO: Research complete. Returning content to Claude.")
    return "".join(scraped_texts)

# Allow the server to be run directly from the command line
if __name__ == "__main__":
    mcp.run()