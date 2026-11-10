# Security Policy

## Supported Versions

Multi-Agent Financial AI is currently under active development.

As the project evolves, security fixes will generally be applied to the latest maintained version.

There are currently no formal release-based support guarantees.

## Reporting a Vulnerability

If you discover a potential security vulnerability, please report it responsibly.

**Please do not disclose security vulnerabilities through public GitHub issues or pull requests.**

Instead, use GitHub's private vulnerability reporting feature if it is enabled for this repository.

If private vulnerability reporting is unavailable, contact the maintainer privately through their GitHub profile:

https://github.com/Mousum-stack

## What to Include

When reporting a vulnerability, please provide:

- A clear description of the vulnerability.
- Steps to reproduce the issue.
- Potential security impact.
- Relevant logs, screenshots, or proof-of-concept examples, if safe to share.
- Any suggested mitigation, if available.

## Security Best Practices

Contributors and users should:

- Never commit API keys, access tokens, passwords, or credentials.
- Store sensitive configuration in environment variables.
- Use `.env` files for local configuration and ensure they are excluded from Git.
- Validate and sanitize external inputs.
- Handle financial data and third-party API responses carefully.
- Avoid exposing sensitive information in logs.
- Keep project dependencies updated.

## Scope

This policy applies to security issues affecting the Multi-Agent Financial AI repository and its associated components.

Thank you for helping keep this project secure.
