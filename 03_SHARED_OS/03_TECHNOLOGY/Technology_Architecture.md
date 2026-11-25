# Technology Architecture

**Status:** v1.1 | **Date:** 2026-11-18 | **Owner:** Founder | **Review:** Annual

## Model providers

Model providers are interchangeable. When platform A is unavailable, platform B is the fallback; the enterprise does not tie itself to a single model vendor.

## Candidate platforms

| Platform | Role | Status |
|----------|------|--------|
| **Hermes** | Execution/agent engine | Under assessment; see `05_PROJECTS/001_HERMES_ENGINE/` |
| **OC8** | Governance/control plane | Under evaluation; see `05_PROJECTS/002_OC8_GOVERNANCE_ASSESSMENT/` |

## Integration requirements

- Agents communicate via a documented protocol (see `Agent_Constitution.md`).
- Model providers are wrapped in a provider abstraction layer.
- Security controls (access, data segregation, audit) apply at every layer.

## Proof of concept

Before production adoption, establish proof of concept for OC8/Hermes compatibility. Governance capability is not equivalent to a security boundary on its own.

## Assessment deliverables

- Hermes Engine: `05_PROJECTS/001_HERMES_ENGINE/01_Architecture/README.md`
- OC8 Assessment: `05_PROJECTS/002_OC8_GOVERNANCE_ASSESSMENT/00_Project_Context.md`
