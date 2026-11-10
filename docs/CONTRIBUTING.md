# Contributing Guidelines

Thank you for your interest in contributing to Multi-Agent Financial AI!

This project explores multi-agent financial research and risk intelligence using Python and LangGraph. Contributions that improve code quality, documentation, testing, architecture, and reliability are welcome.

## Getting Started

### 1. Fork the repository

Fork the repository to your GitHub account.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-financial-ai.git

cd multi-agent-financial-ai
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Making Changes

1. Create a separate branch for your contribution.
2. Keep changes focused and easy to review.
3. Follow existing project conventions.
4. Add or update documentation when necessary.
5. Include tests for new functionality where appropriate.
6. Avoid committing API keys, credentials, personal data, or other sensitive information.

Example:

```bash
git checkout -b feature/your-feature-name
```

## Code Quality

- Write readable, maintainable Python code.
- Use meaningful variable and function names.
- Keep components modular and focused.
- Handle errors appropriately.
- Document important design decisions.
- Avoid introducing unnecessary dependencies.

## Testing

Before submitting a contribution, run the relevant tests.

If pytest is configured:

```bash
pytest
```

Also verify that your changes do not break existing functionality.

## Submitting a Pull Request

1. Commit your changes with a clear commit message.
2. Push your branch to your fork.
3. Open a pull request against the `main` branch of this repository.
4. Explain the purpose of your changes.
5. Include relevant implementation details and testing information.

## Contribution Scope

Potential contribution areas include:

- LangGraph workflow development.
- Multi-agent architecture and orchestration.
- Financial data collection and validation.
- Financial analysis and risk assessment.
- MCP tool integration.
- Quantitative analysis and machine learning.
- Testing, documentation, and code quality.

Please discuss significant architectural changes through a GitHub issue before starting implementation.

## Questions and Suggestions

For questions, bug reports, or feature suggestions, please open a GitHub issue.

Thank you for helping improve Multi-Agent Financial AI!
