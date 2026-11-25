#!/usr/bin/env python3
"""Generate compounding enterprise-brain reports.

Reads:
  - 10_DAILY_MEMORIES/day_YYYY-MM-DD.md   (per-day records)
  - git state (log / status / show) in enterprise-brain
  - 05_PROJECTS/*/00_Project_Context.md   (per-project status)
  - 02_GOVERNANCE/Decision_Register.md    (decisions / owners)

Emits (in reports/, regenerated each run):
  - reports/daily/status_YYYY-MM-DD.md     Daily status report
  - reports/weekly/weekly_YYYY-Www.md      Weekly status report (Mon-Fri)
  - reports/forecast.md                    Forward-looking forecast
  - reports/projects/status.md             Per-project report

Ground rules baked in: nothing is asserted complete unless it appears in git;
the day memos are the compounding record; reports are regenerated, not appended.
"""

import os
import re
import subprocess
from datetime import date

VAULT = "/opt/data/enterprise-brain"
MEMORIES = os.path.join(VAULT, "10_DAILY_MEMORIES")
DAILY_DIR = os.path.join(VAULT, "reports", "daily")
WEEKLY_DIR = os.path.join(VAULT, "reports", "weekly")
PROJECTS_DIR = os.path.join(VAULT, "reports", "projects")
FORECAST = os.path.join(VAULT, "reports", "forecast.md")
PROJECTS_OUT = os.path.join(VAULT, "reports", "projects", "status.md")
GIT = ["git", "-C", VAULT]

HEAD = [
    ("overview", r"^## 1\. Day overview"),
    ("completed", r"^## 2\. Completed work"),
    ("planned", r"^## 3\. Planned work for next day"),
    ("decisions", r"^## 4\. Key decisions"),
    ("open", r"^## 5\. Open items / decisions needed"),
    ("notes", r"^## 6\. Notes for later reviews"),
]


def sh(args):
    return subprocess.run(args, capture_output=True, text=True).stdout.strip()


def day_files():
    if not os.path.isdir(MEMORIES):
        return []
    out = []
    for fn in sorted(os.listdir(MEMORIES)):
        if fn.startswith("day_") and fn.endswith(".md"):
            out.append(parse_day(os.path.join(MEMORIES, fn)))
    return out


def parse_day(path):
    text = open(path).read()
    blocks = {}
    current = None
    for line in text.splitlines():
        key = None
        for k, pat in HEAD:
            if re.match(pat, line):
                key = k
                break
        if key:
            current = blocks.setdefault(key, [])
        elif current is not None:
            current.append(line)
    return {
        "file": os.path.basename(path),
        "date": path.split("_")[-1].replace(".md", ""),
        "overview": "\n".join(blocks.get("overview", [])).strip(),
        "completed": "\n".join(blocks.get("completed", [])).strip(),
        "planned": "\n".join(blocks.get("planned", [])).strip(),
        "decisions": "\n".join(blocks.get("decisions", [])).strip(),
        "open": "\n".join(blocks.get("open", [])).strip(),
        "notes": "\n".join(blocks.get("notes", [])).strip(),
    }


def git_last_commit():
    subj = sh(GIT + ["log", "-1", "--format=%h %s"])
    files = sh(GIT + ["show", "--name-status", "-1", "--format="]).splitlines()
    return subj, [f for f in files if f]


def git_status():
    return sh(GIT + ["status", "--short"])


def day_memo_field(memo_text):
    """Clean a day-memo block (open / planned) to single-dash list items."""
    out = []
    for line in memo_text.splitlines():
        line = line.strip()
        if not line:
            continue
        # strip common leading bullets/numbers
        line = re.sub(r"^[-*]\s*", "", line)
        line = re.sub(r"^\d+\.\s*", "", line)
        if line:
            out.append("- " + line)
    return "\n".join(out)


def project_header_field(text, label):
    """Inline header field: '**Label:** Value | ...'"""
    m = re.search(r"\*\*" + re.escape(label) + r":\*\*\s*([^|\n]+)", text)
    return m.group(1).strip() if m else ""


def project_heading_field(text, label):
    """Heading style: '## Label' followed by a value line."""
    m = re.search(r"^##\s*" + re.escape(label) + r"\s*$", text, re.M)
    if not m:
        return ""
    lines = text.splitlines()
    line_idx = None
    for idx, ln in enumerate(lines):
        if re.match(r"^##\s*" + re.escape(label) + r"\s*$", ln):
            line_idx = idx
            break
    if line_idx is None:
        return ""
    for idx in range(line_idx + 1, len(lines)):
        if lines[idx].strip() and not lines[idx].startswith("#"):
            return lines[idx].strip()
    return ""


def project_summaries():
    folders = sorted(d.name for d in os.scandir(os.path.join(VAULT, "05_PROJECTS")) if d.is_dir())
    out = []
    for folder in folders:
        pdir = os.path.join(VAULT, "05_PROJECTS", folder)
        ctx = os.path.join(pdir, "00_Project_Context.md")
        if os.path.isfile(ctx):
            text = open(ctx).read()
            out.append({"path": "05_PROJECTS/" + folder, "text": text, "header": text.splitlines()[0]})
    return out


def render_day_report(day):
    lines = []
    lines.append("# Daily Status Report — {}".format(day["date"]))
    lines.append("")
    lines.append("**Status:** Draft | **Date:** {} | **Owner:** Founder | **Review:** Daily".format(day["date"]))
    lines.append("")
    lines.append("## 1. Yesterday in review")
    lines.append("")
    subj, files = git_last_commit()
    lines.append("- Last commit: `{}`".format(subj))
    lines.append("- Files changed (git show -1 --name-status):")
    lines.append("")
    if files:
        for f in files[:14]:
            lines.append("  - `{}`".format(f))
        if len(files) > 14:
            lines.append("  - ... and {} more.".format(len(files) - 14))
    else:
        lines.append("  - (no file changes)")
    lines.append("")
    lines.append("Day memo captured the same work:")
    lines.append("")
    lines.append("```")
    lines.append(day["completed"])
    lines.append("```")
    lines.append("")
    lines.append("## 2. Working tree")
    lines.append("")
    if git_status():
        lines.append("Modified / untracked:")
        for f in git_status().splitlines():
            if f:
                lines.append("- `{}`".format(f))
    else:
        lines.append("Clean — nothing modified, no untracked files.")
    lines.append("")
    lines.append("## 3. Open items / decisions needed")
    lines.append("")
    if day["open"]:
        for blk in day_memo_field(day["open"]).splitlines():
            lines.append(blk)
    lines.append("")
    lines.append("## 4. Tomorrow's focus (from plan)")
    lines.append("")
    if day["planned"]:
        for blk in day_memo_field(day["planned"]).splitlines():
            lines.append(blk)
    else:
        lines.append("- No next-day plan captured today — next brief should carry one.")
    lines.append("")
    lines.append("## 5. Health")
    lines.append("")
    lines.append("- Day memos on file: {}.  Working-tree clean: {}.\n".format(len(day_files()), "yes" if not git_status() else "no"))
    lines.append("")
    return "\n".join(lines)


def render_weekly(days):
    today = date.today()

    def is_workday(d):
        try:
            y, m, dd = d["date"].split("-")
            return date(int(y), int(m), int(dd)).weekday() < 5
        except (ValueError, TypeError):
            return False

    work_days = sorted([d for d in days if is_workday(d)], key=lambda d: d["date"], reverse=True)[:5]
    lines = []
    lines.append("# Weekly Status Report — {}".format(today.strftime("%Y-W%W")))
    lines.append("")
    lines.append("**Status:** Draft | **Date:** {} | **Owner:** Founder | **Review:** Weekly".format(today.strftime("%Y-%m-%d")))
    lines.append("")
    lines.append("## 1. Coverage")
    lines.append("")
    if work_days:
        lines.append("Working days included: {}.".format(", ".join(d["date"] for d in work_days)))
        if len(work_days) < 5:
            lines.append("> Partial week: only {} day memo(s) on file for Mon-Fri. Treat as a draft until the week closes.".format(len(work_days)))
    else:
        lines.append("No working-day memos on file this week. Vault is in flux; re-generate on Monday.")
    lines.append("")
    lines.append("## 2. Themes this week")
    lines.append("")
    for i, d in enumerate(work_days, 1):
        lines.append("### {} — {}".format(i, d["date"]))
        lines.append("")
        lines.append("Opened with: {}".format(d["overview"][:320]))
        lines.append("")
        lines.append("Completed (from memo):")
        lines.append("")
        lines.append("```")
        lines.append(d["completed"][:500])
        lines.append("```")
        lines.append("")
        if d["planned"]:
            lines.append("Next-day plan:")
            for blk in day_memo_field(d["planned"]).splitlines():
                lines.append(blk)
        lines.append("")
    lines.append("## 3. Cross-week open items")
    lines.append("")
    all_open = []
    for d in work_days:
        for blk in day_memo_field(d["open"]).splitlines():
            if blk not in all_open:
                all_open.append(blk)
    for blk in all_open:
        lines.append(blk)
    lines.append("")
    lines.append("## 4. Next week's focus")
    lines.append("")
    if work_days:
        for blk in day_memo_field(work_days[0]["planned"]).splitlines():
            lines.append(blk)
    lines.append("")
    return "\n".join(lines)


def render_forecast():
    lines = []
    lines.append("# Forecast — next 30 days (rolling)")
    lines.append("")
    lines.append("**Anchors:** `01_ENTERPRISE_STRATEGY/Enterprise_Blueprint.md`, `01_ENTERPRISE_STRATEGY/Financial_Doctrine.md`, `02_GOVERNANCE/Decision_Register.md`, and day-memo open items.")
    lines.append("")
    lines.append("## 1. Targets (anchors)")
    lines.append("")
    for t in [
        "006 `blownapp.io` SaaS platform: production platform, at least one paying client within 12–24 months.",
        "003 Pilot Client Automotive: live demo, documented value, path to a paid contract (WhatsApp API channel).",
        "Recurring technology budget USD 50–100/month; one-off capex ≤ USD 500 at founder discretion; >USD 500 needs a Decision Register entry.",
        "First asset `verified`: `blownapp.io` (2026-11-19); others `pending-verification` until documentation lands.",
    ]:
        lines.append("- {}".format(t))
    lines.append("")
    lines.append("## 2. Next-30-day trajectory")
    lines.append("")
    all_open = []
    for d in day_files():
        for blk in day_memo_field(d["open"]).splitlines():
            if blk not in all_open:
                all_open.append(blk)
    if all_open:
        for blk in all_open:
            lines.append(blk)
    lines.append("")
    lines.append("The next 30 days rest on three decisions: (1) fund the 006 stack/billing shortlist; (2) engage the professional advisers; (3) collect verification documentation for `810wn.com`, Unigad, and Intellurgy.")
    lines.append("")
    lines.append("## 3. Milestones (12–24 months, per blueprint)")
    lines.append("")
    for m in ["Three to five paying managed-AI clients.", "One profitable digital asset.", "Regional recognition in 2–3 years."]:
        lines.append("- {}".format(m))
    lines.append("")
    lines.append("Aspirational targets from the blueprint, not forecasts of certainty.")
    lines.append("")
    return "\n".join(lines)


def render_projects(projects):
    lines = []
    lines.append("# Project Report — 05_PROJECTS")
    lines.append("")
    lines.append("**Status:** Draft | **Date:** {} | **Owner:** Founder | **Review:** Per project / 40-day review".format(date.today().strftime("%Y-%m-%d")))
    lines.append("")
    lines.append("## 1. Project status")
    lines.append("")
    lines.append("| Project | Status | Owner | Overview | Measurable outcome |")
    lines.append("|---------|--------|-------|----------|--------------------|")
    for p in projects:
        text = p["text"]
        status = project_header_field(text, "Status") or "Defined"
        owner = project_header_field(text, "Owner") or "Founder"
        overview = project_heading_field(text, "Overview")
        outcome = project_header_field(text, "Measurable outcome")
        if not outcome:
            outcome = project_heading_field(text, "Measurable outcome")
        lines.append("| `{}` | {} | {} | {} | {} |".format(
            p["path"], status, owner, overview[:120], outcome[:140]))
    lines.append("")
    return "\n".join(lines)


def main():
    days = day_files()
    today = date.today()

    os.makedirs(DAILY_DIR, exist_ok=True)
    os.makedirs(WEEKLY_DIR, exist_ok=True)
    os.makedirs(PROJECTS_DIR, exist_ok=True)

    if days:
        day = days[0]
        dpath = os.path.join(DAILY_DIR, "status_{}.md".format(day["date"]))
        open(dpath, "w").write(render_day_report(day))
    else:
        dpath = os.path.join(DAILY_DIR, "status_{}.md".format(today.strftime("%Y-%m-%d")))
        open(dpath, "w").write("""# Daily Status Report — {}
**Status:** Draft | **Date:** {} | **Owner:** Founder | **Review:** Daily

## 1. Yesterday in review
No day memo on file and no git commit detected. Re-establish context from the vault before drafting.

## 2. Working tree
See `git status` directly — no day memo available to summarise.

## 3. Focus
Add the day's plan to a `day_YYYY-MM-DD.md` memo so tomorrow's brief has something to carry forward.
""".format(today.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")))

    wpath = os.path.join(WEEKLY_DIR, "weekly_{}.md".format(today.strftime("%G-W%V")))
    open(wpath, "w").write(render_weekly(days))

    fpath = FORECAST
    open(fpath, "w").write(render_forecast())

    ppath = PROJECTS_OUT
    open(ppath, "w").write(render_projects(project_summaries()))

    print("reported {:d} day memo(s)".format(len(days)))
    print("daily  -> {}".format(dpath))
    print("weekly -> {}".format(wpath))
    print("forecast -> {}".format(fpath))
    print("projects -> {}".format(ppath))


if __name__ == "__main__":
    main()
