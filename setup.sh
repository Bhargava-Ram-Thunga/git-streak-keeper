#!/bin/bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "=============================================="
echo "   🌿 Git Streak Keeper - Quick Setup"
echo "=============================================="
echo ""

# 1. Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "[1/4] Initializing Git repository..."
    git init -b main
else
    echo "[1/4] Git repository already initialized."
fi

# 2. Run initial update
echo "[2/4] Testing activity update script..."
python3 scripts/update_log.py

# 3. Stage and initial commit
echo "[3/4] Staging files and creating commit..."
git add .
if ! git diff --cached --quiet; then
    git commit -m "feat: setup git streak keeper with daily automated workflow"
    echo "Initial commit created."
else
    echo "Working tree clean, nothing new to commit."
fi

echo ""
echo "[4/4] Remote Repository Setup"
echo "----------------------------------------------"

if command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) detected!"
    echo "Would you like to automatically create and push to a new GitHub repository now? (y/n)"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        echo "Creating repository on GitHub..."
        gh repo create git-streak-keeper --public --source=. --push || {
            echo "Failed to create via gh. You can create it manually on GitHub and run:"
            echo "  git remote add origin <YOUR_REPO_URL>"
            echo "  git push -u origin main"
        }
        echo "Repository created and pushed!"
    else
        echo "Skipping automatic push. You can push manually whenever you are ready."
    fi
else
    echo "GitHub CLI (gh) not found. To push manually:"
    echo "  1. Create a repository on https://github.com/new"
    echo "  2. Run:"
    echo "     git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git"
    echo "     git push -u origin main"
fi

echo ""
echo "=============================================="
echo "🎉 Setup Complete!"
echo "Remember to enable 'Read and write permissions' in your GitHub repo settings:"
echo "Settings -> Actions -> General -> Workflow permissions"
echo "=============================================="
