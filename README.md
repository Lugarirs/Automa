# Automa
# 📰 Daily News Headline Scraper

Automatically fetches top BBC News headlines every day and saves them to `headlines.json` — powered by GitHub Actions.

## 📁 Project Structure

```
├── scraper.py                          # Python scraper script
├── headlines.json                      # Auto-updated daily (generated)
├── requirements.txt                    # Python dependencies
└── .github/
    └── workflows/
        └── scraper.yml                 # GitHub Actions workflow
```

## ⚙️ How It Works

1. GitHub Actions triggers every day at **8:00 AM UTC**
2. It sets up Python and installs `requests`
3. `scraper.py` fetches the BBC News RSS feed
4. Headlines are saved to `headlines.json`
5. The file is auto-committed back to the repo

## 🚀 Setup (3 steps)

1. **Fork or clone** this repo to your GitHub account
2. Go to **Settings → Actions → General** → set Workflow permissions to **Read and write**
3. That's it! The workflow runs automatically every day ✅

## ▶️ Manual Trigger

Go to **Actions tab → Daily News Scraper → Run workflow** to trigger it manually anytime.

## 📄 Output Format (`headlines.json`)

```json
{
  "scraped_at": "2026-03-11 08:00:00 UTC",
  "source": "BBC News RSS",
  "total": 30,
  "headlines": [
    {
      "title": "Headline title here",
      "link": "https://bbc.co.uk/...",
      "published": "Wed, 11 Mar 2026 07:45:00 GMT",
      "description": "Short summary..."
    }
  ]
}
```

## 🆓 Cost

Completely free! GitHub gives 2,000 free Actions minutes/month on free accounts.  
This workflow uses ~30 seconds per run = ~15 minutes/month total.
