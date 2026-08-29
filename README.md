# 🌿 Git Streak Keeper

An automated, lightweight GitHub repository that keeps your GitHub contribution graph active and green every day using GitHub Actions scheduled workflows.

---

## 🎯 How It Works

1. **Scheduled GitHub Action**: A GitHub Action runs automatically on a configured cron schedule (e.g. daily at 04:30 UTC).
2. **Activity Logger**: A Python script (`scripts/update_log.py`) appends a timestamped motivational quote/entry and updates contribution statistics in `ACTIVITY.md` and `activity.json`.
3. **Commit & Push**: GitHub Actions commits the change with your GitHub author identity and pushes it back to your `main` branch.
4. **Green Contribution**: GitHub registers the commit on your default branch and turns that day's square green on your profile graph!

---

## 🚀 Quickstart Guide

### Step 1: Initialize & Push to Your GitHub

You can publish this repository to your GitHub account using the GitHub CLI (`gh`) or standard git:

#### Option A: Using GitHub CLI (Fastest)
```bash
cd /Users/bhargavaramthunga/.gemini/antigravity/scratch/git-streak-keeper
git init
git add .
git commit -m "feat: initial commit for git streak keeper"
gh repo create git-streak-keeper --public --source=. --push
```
*(Or `--private` if you prefer a private repo — GitHub can show private contributions if you enable "Private contributions" in your profile settings!)*

#### Option B: Manual Git Push
1. Create a new repository on [GitHub](https://github.com/new) (e.g. `git-streak-keeper`).
2. Run in terminal:
```bash
cd /Users/bhargavaramthunga/.gemini/antigravity/scratch/git-streak-keeper
git init
git branch -M main
git add .
git commit -m "feat: initial commit for git streak keeper"
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/git-streak-keeper.git
git push -u origin main
```

---

## ⚙️ Essential GitHub Configuration (Must Check!)

To ensure your automated commits are counted on your contribution graph:

### 1. Enable GitHub Actions Write Permissions
GitHub Actions needs permission to push commits to your repository:
1. Go to your repository on GitHub.
2. Click **Settings** > **Actions** > **General**.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Click **Save**.

### 2. Match Your Commit Email (Important for Graph Credit)
GitHub counts contributions when the commit email matches your GitHub account:
- By default, the workflow uses your GitHub username with `<username>@users.noreply.github.com`, which GitHub automatically recognizes.
- If you use a custom email for GitHub commits, add a Repository Variable:
  - Go to **Settings** > **Secrets and variables** > **Actions** > **Variables** tab.
  - Add `GIT_USER_EMAIL`: your verified GitHub email (e.g. `you@example.com`).
  - Add `GIT_USER_NAME`: your name or GitHub username.

### 3. Display Private Contributions (If repo is Private)
If you made your repository private, enable private contributions on your profile:
1. Go to your GitHub profile.
2. Click **Contribution settings** (dropdown above your contribution graph on the right).
3. Check **Private contributions**.

---

## ⏰ Customizing the Schedule

Edit [.github/workflows/daily-commit.yml](.github/workflows/daily-commit.yml) to change when or how often the workflow runs:

```yaml
on:
  schedule:
    # Run once daily at 04:30 UTC
    - cron: '30 4 * * *'
    
    # Example: Run twice daily (04:30 UTC and 16:30 UTC)
    # - cron: '30 4,16 * * *'
```

> **Note**: GitHub Actions cron schedules have a slight jitter/delay depending on GitHub's server load (usually within a few minutes).

---

## 🧪 Testing Immediately

You don't have to wait for the cron schedule to verify it:
1. Go to the **Actions** tab in your GitHub repository.
2. Click **Daily Contribution Streak Keeper** in the left sidebar.
3. Click the **Run workflow** dropdown button, then click **Run workflow**.
4. Once completed (takes ~15 seconds), refresh your repository and your profile page to see the new commit!

---

## 📂 Project Structure

```
├── .github/
│   └── workflows/
│       └── daily-commit.yml   # Scheduled GitHub Actions workflow
├── scripts/
│   └── update_log.py          # Python activity & streak updater
├── ACTIVITY.md                # Rendered markdown streak table
├── activity.json              # Structured history of updates
├── setup.sh                   # Helper setup script
└── README.md                  # Documentation
```
