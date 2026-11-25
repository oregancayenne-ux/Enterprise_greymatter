# Execution Plan — "Read the Room" Content

**Status:** Planned | **Owner:** Founder | **Date:** 2026-11-19

This plan covers the work that follows the title "read the room" in the sourced chat. It is organised as an execution plan to be reviewed each morning before the start of each day's work.

## 1. Objective

Apply the five-file domain correction set for `blownapp.io` (no hyphen) across the enterprise-brain vault, replace the reserved `06_LEGAL_AND_COMPLIANCE/` placeholder with the populated legal tree, and produce the U2 "AI Lead Qualifier" automation for the unfinished whatsapp/BDC task (n8n + Google Sheets).

## 2. Scope of work

### 2.1 Populate `06_LEGAL_AND_COMPLIANCE/`

Populate the reserved legal folder with the full legal tree (done). Files created:

- `README.md` — status now "Populated"
- `Entity_and_Ownership_Register.md` — restricted, with 4 entities
- `Zambia_DPA_2021_Reference.md` — Zambia data protection reference
- `IP_and_IP_Protection.md` — IP ownership and protection
- `Professional_Advice_Register.md` — advisers register
- `Regulatory_and_Sector_References.md` — regulatory references
- `Contracts/` — 3 contract templates

### 2.2 Apply the five-file domain correction set

| # | File | Edit | Status |
|---|------|------|--------|
| 1 | `01_ENTERPRISE_STRATEGY/BLOWN_Master_Corporate_Brief.md` | Add correction notice at top | NEW FILE |
| 2 | `01_ENTERPRISE_STRATEGY/Enterprise_Blueprint.md` | Replace `blown-app.io` → `blownapp.io` (2 occurrences) | In place |
| 3 | `00_FOUNDER_CONTEXT/Master_Constitution.md` | Identity section: add `blownapp.io` | In place |
| 4 | `02_GOVERNANCE/Asset_Register.md` | Update `blownapp.io` row → `verified`, add note | NEW FILE |
| 5 | `05_PROJECTS/006_BLOWN_APP_PLATFORM/00_Project_Context.md` | Replace all `blown-app.io` → `blownapp.io`, update status | NEW FILE |

### 2.3 Produce U2 "AI Lead Qualifier" automation (unfinished task)

- `u2-kit/workflows/u2-inbound.json` — n8n workflow: webhook trigger, LLM evaluation, mock Google Sheet save
- `u2-kit/workflows/u2-sweeper.json` — n8n workflow: hourly cron, Google Sheet read, WhatsApp nudge, mark nudged
- `u2-kit/prompts/u2-qualifier.txt` — LLM system prompt (strict JSON output)

## 3. Execution order

1. Create `006_BLOWN_APP_PLATFORM` project (2 files)
2. Apply domain corrections to existing files
3. Create `Asset_Register.md`
4. Commit and push
5. Build U2 automation files
6. Verify all files

## 4. Risk register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| `blownapp.io` domain already correct in file | High | Low | Verify before edit |
| `blown-app.io` references too scattered | Medium | Low | Use sed for bulk replace |
| `006` project conflicts with existing | Low | Med | Check for name conflicts first |

## 5. Success criteria

- All 5 domain corrections applied
- `blownapp.io` appears consistently in operational docs
- `006_BLOWN_APP_PLATFORM` present with 2 files
- Working tree clean after commit and push
