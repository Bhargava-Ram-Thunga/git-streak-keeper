#!/usr/bin/env python3
"""
Daily Activity Logger
Updates ACTIVITY.md and activity.json with current UTC date, streak count, and quotes.
"""

import json
import os
import random
from datetime import datetime, timezone

QUOTES = [
    "“The secret of getting ahead is getting started.” – Mark Twain",
    "“Continuous improvement is better than delayed perfection.” – Mark Twain",
    "“Small daily improvements over time lead to stunning results.” – Robin Sharma",
    "“Consistency is what transforms average into excellence.” – Anonymous",
    "“Action is the foundational key to all success.” – Pablo Picasso",
    "“Success doesn't come from what you do occasionally, it comes from what you do consistently.” – Marie Forleo",
    "“Code is like humor. When you have to explain it, it’s bad.” – Cory House",
    "“Simplicity is prerequisite for reliability.” – Edsger W. Dijkstra",
    "“Make it work, make it right, make it fast.” – Kent Beck",
    "“First, solve the problem. Then, write the code.” – John Johnson",
    "“It always seems impossible until it's done.” – Nelson Mandela",
    "“Don’t watch the clock; do what it does. Keep going.” – Sam Levenson",
    "“Focus on being productive instead of busy.” – Tim Ferriss",
    "“Little by little, one travels far.” – J.R.R. Tolkien",
]

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(PROJECT_ROOT, "ACTIVITY.md")
DATA_FILE = os.path.join(PROJECT_ROOT, "activity.json")


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"total_contributions": 0, "last_updated": None, "history": []}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def update_log():
    now_utc = datetime.now(timezone.utc)
    date_str = now_utc.strftime("%Y-%m-%d")
    time_str = now_utc.strftime("%H:%M:%S UTC")
    iso_time = now_utc.isoformat()

    data = load_data()
    data["total_contributions"] += 1
    data["last_updated"] = iso_time

    quote = random.choice(QUOTES)
    data["history"].append({"date": date_str, "time": time_str, "quote": quote})

    # Keep history bounded in JSON (last 100 entries)
    if len(data["history"]) > 100:
        data["history"] = data["history"][-100:]

    save_data(data)

    # Render ACTIVITY.md
    content = f"""# 📈 Activity Tracker & Streak Keeper

> Automated streak tracker log. Keep the momentum going every single day!

### 📊 Summary
- **Total Automated Contributions**: `{data['total_contributions']}`
- **Last Active**: `{date_str} at {time_str}`
- **Current Streak Motivation**:
  > {quote}

---

### 🕒 Recent Activity Log (UTC)

| Date | Time | Message |
| :--- | :--- | :--- |
"""
    # Show last 20 entries in Markdown
    recent_history = list(reversed(data["history"]))[:20]
    for item in recent_history:
        content += f"| `{item['date']}` | `{item['time']}` | {item['quote']} |\n"

    content += "\n---\n*Automated with ❤️ via [GitHub Actions](https://github.com/features/actions).*\n"

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[SUCCESS] Updated activity log for {date_str} {time_str} (Total: {data['total_contributions']})")


if __name__ == "__main__":
    update_log()
