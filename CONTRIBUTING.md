# Contributing to Local Research MCP Server

Thank you for your interest in contributing to the Local Research MCP Server! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync --dev
   ```

## Development Setup

### Prerequisites

- Python 3.10 or higher
- uv package manager
- Claude Desktop for testing

### Running Tests

```bash
pytest
```

### Code Formatting

We use Black and Ruff for code formatting and linting:

```bash
black .
ruff check .
```

## Contributing Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Write descriptive commit messages
- Add docstrings to all functions and classes

### Pull Request Process

1. Create a feature branch from `main`
2. Make your changes with appropriate tests
3. Update documentation if needed
4. Ensure all tests pass and code is formatted
5. Submit a pull request with a clear description

### Issue Reporting

When reporting bugs or requesting features:

- Use the GitHub issue templates
- Provide detailed reproduction steps
- Include system information (OS, Python version, etc.)
- Attach relevant logs or error messages

## Areas for Contribution

### Enhancements

- **Multiple Search Engines**: Add support for additional search providers
- **Content Caching**: Implement intelligent caching of search results
- **Output Formatting**: Better formatting of scraped content
- **Configuration**: User-configurable settings and preferences
- **Error Handling**: More robust error recovery and reporting

### Documentation

- Improve installation instructions
- Add troubleshooting guides
- Create video tutorials
- Expand API documentation

### Testing

- Add unit tests for core functionality
- Integration tests with different search queries
- Performance testing and optimization
- Cross-platform compatibility testing

## Security Considerations

When contributing, please consider:

- Input validation and sanitization
- Rate limiting and respectful web scraping
- Privacy protection and data handling
- Error handling without information disclosure

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Please read and follow it in all interactions.

## Questions?

If you have questions about contributing:

- Check existing issues and discussions
- Create a new issue for questions
- Reach out via the project's communication channels

Thank you for helping make this project better!