#!/bin/bash
# Installs Homebrew (if needed) and Python so you can run learnClass.py

set -e

if ! command -v brew &> /dev/null; then
  echo "Installing Homebrew (you may be asked for your Mac password)..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Add Homebrew to PATH for this session (common on Apple Silicon)
  [[ -x /opt/homebrew/bin/brew ]] && eval "$(/opt/homebrew/bin/brew shellenv)"
  [[ -x /usr/local/bin/brew ]] && eval "$(/usr/local/bin/brew shellenv)"
fi

echo "Installing Python..."
brew install python

echo ""
echo "Done. Run your script with:"
echo "  python3 learnClass.py"
echo "or:"
echo "  python learnClass.py"
