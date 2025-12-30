#!/bin/bash
# Setup script for Gemini CLI Demo

set -e

echo "Setting up Gemini CLI Demo environment..."

# Check Python version
python3 --version || { echo "Python 3 is required"; exit 1; }

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -e ".[dev]"

echo ""
echo "Setup complete! To activate the environment:"
echo "  source .venv/bin/activate"
echo ""
echo "To run tests:"
echo "  pytest tests/ -v"
echo ""
echo "To start Gemini CLI:"
echo "  gemini"
echo ""
echo "See README.md for demo scenarios."
