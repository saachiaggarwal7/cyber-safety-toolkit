# Password Strength Checker

## Description

A Python script that evaluates password strength using multiple security criteria and provides feedback on missing requirements.

## Security Policy

This tool enforces the following checks:

- Minimum length of 12 characters (mandatory)
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

### Note

Passwords shorter than 12 characters are automatically classified as Weak regardless of any other criteria.

## Features

- Weak / Medium / Strong classification
- Reports missing password requirements
- Uses regular expressions (Regex) for validation

## Example

Input:

Abc123

Output:

Weak Password
- length cannot be less than 12
- Missing special characters