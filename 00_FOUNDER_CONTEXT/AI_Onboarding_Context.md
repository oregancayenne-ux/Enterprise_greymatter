# AI Onboarding Context

**Status:** v1.1 | **Date:** 2026-11-18 | **Owner:** Founder | **Review:** As required

Defines how AI agents and models are onboarded, prompted, and operated within this enterprise.

## Output modes

This document defines two output modes for AI recommendations:

- **Standard mode:** Full 8-step output requirement for every recommendation (heavy, used for major decisions and new agent deployments).
- **Light mode:** Condensed output for small, bounded refinements that do not require full justification.

The mode used is specified per request or inferred from task complexity.

## Human approval policy

All AI-recommended actions that are irreversible, high-cost, or otherwise consequential require founder approval before execution. See `../02_GOVERNANCE/Human_Approval_Policy.md` for the approval framework.

## Model consultation protocol

When multiple AI models are used for independent critique, the following apply:

- Each model produces an independent assessment before any synthesis.
- Disagreements are surfaced; the founder resolves material conflicts.
- The AI must flag when a multi-model cross-check would materially improve a decision.

## Verification

For current technical and product matters, verify authoritative sources whenever feasible. Authoritative sources are defined in `../04_KNOWLEDGE_MANAGEMENT/Source_of_Truth.md`.

## Onboarding checklist

- [ ] Confirm the agent's role and scope.
- [ ] Agree on the model provider(s) and fallback chain.
- [ ] Agree on the output mode (standard/light).
- [ ] Confirm approval boundaries.
- [ ] Record the agent in the project's Decision Register.
