"""
Tests for the research server functionality.
"""

import pytest
import asyncio
from unittest.mock import Mock, patch
from research_server import research_and_scrape


@pytest.mark.asyncio
async def test_research_and_scrape_success():
    """Test successful research and scraping."""
    
    # Mock DuckDuckGo search results
    mock_results = [
        {'href': 'https://example.com/article1', 'title': 'Test Article 1'},
        {'href': 'https://example.com/article2', 'title': 'Test Article 2'}
    ]
    
    # Mock trafilatura content extraction
    mock_content = "This is test content from the webpage."
    
    with patch('research_server.DDGS') as mock_ddgs, \
         patch('trafilatura.fetch_url') as mock_fetch, \
         patch('trafilatura.extract') as mock_extract:
        
        # Setup mocks
        mock_ddgs.return_value.__enter__.return_value.text.return_value = mock_results
        mock_fetch.return_value = "mock_html_content"
        mock_extract.return_value = mock_content
        
        # Execute the function
        result = await research_and_scrape("test query", 2)
        
        # Verify results
        assert "Source 1: https://example.com/article1" in result
        assert "Source 2: https://example.com/article2" in result
        assert mock_content in result


@pytest.mark.asyncio
async def test_research_and_scrape_no_results():
    """Test behavior when no search results are found."""
    
    with patch('research_server.DDGS') as mock_ddgs:
        mock_ddgs.return_value.__enter__.return_value.text.return_value = []
        
        result = await research_and_scrape("test query")
        
        assert "couldn't find any web search results" in result


@pytest.mark.asyncio
async def test_research_and_scrape_extraction_failure():
    """Test behavior when content extraction fails."""
    
    mock_results = [
        {'href': 'https://example.com/article1', 'title': 'Test Article 1'}
    ]
    
    with patch('research_server.DDGS') as mock_ddgs, \
         patch('trafilatura.fetch_url') as mock_fetch, \
         patch('trafilatura.extract') as mock_extract:
        
        mock_ddgs.return_value.__enter__.return_value.text.return_value = mock_results
        mock_fetch.return_value = "mock_html_content"
        mock_extract.return_value = None  # Extraction fails
        
        result = await research_and_scrape("test query")
        
        assert "unable to extract content" in result


@pytest.mark.asyncio
async def test_research_and_scrape_network_error():
    """Test behavior when network errors occur."""
    
    with patch('research_server.DDGS') as mock_ddgs:
        mock_ddgs.side_effect = Exception("Network error")
        
        result = await research_and_scrape("test query")
        
        assert "unexpected error occurred" in result


@pytest.mark.asyncio 
async def test_research_and_scrape_partial_failure():
    """Test behavior when some URLs fail to scrape."""
    
    mock_results = [
        {'href': 'https://example.com/article1', 'title': 'Test Article 1'},
        {'href': 'https://example.com/article2', 'title': 'Test Article 2'}
    ]
    
    with patch('research_server.DDGS') as mock_ddgs, \
         patch('trafilatura.fetch_url') as mock_fetch, \
         patch('trafilatura.extract') as mock_extract:
        
        mock_ddgs.return_value.__enter__.return_value.text.return_value = mock_results
        
        # First URL succeeds, second fails
        mock_fetch.side_effect = ["mock_html_content", Exception("Failed to fetch")]
        mock_extract.return_value = "This is test content"
        
        result = await research_and_scrape("test query", 2)
        
        # Should contain content from successful scrape
        assert "Source 1: https://example.com/article1" in result
        assert "This is test content" in result
        # Should not contain failed URL content
        assert "Source 2: https://example.com/article2" not in result


def test_default_parameters():
    """Test that default parameters work correctly."""
    
    # This test would require mocking asyncio.run or similar
    # for a full integration test
    pass