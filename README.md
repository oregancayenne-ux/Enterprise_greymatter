# Enterprise Brain — Founder's OS Vault

**Status:** Live | **Owner:** Founder | **Review:** Based on Master Constitution

A structured vault for the founder's AI enterprise: its constitution, strategy, governance, security, projects, and templates, reconciled from the Founder's OS document set (Rev 1.1).

## Structure

```
00_FOUNDER_CONTEXT/          # Constitution, vision/mission, onboarding, founder profile, preferences, values
01_ENTERPRISE_STRATEGY/      # Financial doctrine, enterprise blueprint
02_GOVERNANCE/               # Decision register, human approval policy, model consultation protocol
03_SHARED_OS/                # Shared operating system (agent constitution, security, technology, knowledge)
05_PROJECTS/                 # Enterprise projects (Hermes, OC8, Pilot Automotive, 810WN, Personal AI)
07_AI_MODEL_WORKSPACE/       # Universal onboarding prompt
08_TEMPLATES/                # Project, agent spec, and decision templates
```

## Integration with the vault structure

| New folder | Maps to (existing vault) |
|------------|---------------------------|
| `00_FOUNDER_CONTEXT` | `people/` + `strategy/` |
| `01_ENTERPRISE_STRATEGY` | `strategy/` |
| `02_GOVERNANCE` | `_templates/` (governance templates) |
| `03_SHARED_OS` | `operations/` (shared operating procedures) |
| `05_PROJECTS` | `projects/` |

The legacy `inbox/`, `_templates/`, `companies/` folders remain for operational intake.

## Ownership

- **Founder:** final authority over strategy, constitutional changes, budgets, sensitive data policies, production deployment, and high-impact actions.
- **Delegated execution:** defined in `02_GOVERNANCE/Human_Approval_Policy.md`.

## Guidance

- Follow the compact header convention: `Title | Status | Version | Date | Owner | Review date`.
- Cross-reference using relative paths.
- Record significant decisions in `02_GOVERNANCE/Decision_Register.md`.
- Security acceptance gate required before production deployment (10-point gate in `03_SHARED_OS/02_SECURITY/Security_Constitution.md`).
