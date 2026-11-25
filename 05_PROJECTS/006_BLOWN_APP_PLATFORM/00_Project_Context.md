# blownapp.io — BLOWN Application & SaaS Platform

**Status:** Defined — project brief | **Version:** 1.2 | **Date:** 2026-11-19 | **Owner:** Founder
**Parent Division:** Software & SaaS (primary); Cloud & Infrastructure (hosting)
**Review:** At 40-day strategic review

**Domain status:** `blownapp.io` — **registered and verified 2026-11-19**. Owner: Blown-Flux Enterprise. Credentials: founder secret manager.

## Overview

BLOWN Application & SaaS Platform is the enterprise's flagship digital product: an AI Business Operating System delivered as a multi-tenant SaaS platform. The platform is built on `blownapp.io` (no hyphen).

## Purpose

Deliver the AI Business Operating System as a repeatable, revenue-generating SaaS platform. First product of the BLOWN portfolio.

## Measurable outcome

A production SaaS platform on `blownapp.io` generating recurring subscription revenue, with at least one paying client within 12–24 months.

## Information architecture

- `app.blownapp.io` — main application portal
- `accounts.blownapp.io` — identity and account management
- `api.blownapp.io` — API gateway
- `docs.blownapp.io` — developer documentation
- `support.blownapp.io` — customer support
- `status.blownapp.io` — platform availability
- `billing.blownapp.io` — subscription and billing interface
- `labs.blownapp.io` — experimental product environments

## Decision Register

- PA-01 | Which BLOWN product launches first? | **RESOLVED: AI Business Operating System** (founder decision 2026-11-19)
- PA-02 | Technology stack | On hold — pending discovery
- PA-03 | Billing provider | On hold — pending discovery
- PA-04 | Domain ownership | **RESOLVED 2026-11-19** — `blownapp.io` registered and verified; owner Blown-Flux Enterprise; credentials in founder secret manager

## Current status / next actions

**Status:** Defined. Blocked on PA-02 (stack) and PA-03 (billing provider) before architecture begins.

## Data classification

- **Public** — marketing pages, docs
- **Internal** — platform configuration, agent policies
- **Project-secret** — platform credentials, subdomain configuration
- **Personal** — (not stored in this project)

## Standards

- Follow the project template: `08_TEMPLATES/Project_Template/`
- Cross-reference relative paths
- Security acceptance gate required before production deployment (`03_SHARED_OS/02_SECURITY/Security_Constitution.md`)
