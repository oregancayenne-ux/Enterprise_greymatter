# Security Constitution

**Status:** v1.1 | **Date:** 2026-11-18 | **Owner:** Founder | **Review:** Annual

## Purpose

Four security domains with 12 mandatory design principles. Security is a foundational, non-negotiable principle and a commercial capability.

## Domain 1 — Access control

1. Least-privilege access; no standing root/admin on production systems.
2. Multi-factor authentication for all human and service accounts.
3. Rotated credentials; no long-lived secrets.

## Domain 2 — Data protection

4. Data classified and segregated: public, internal, project-secret, personal.
5. Encryption at rest and in transit for all sensitive data.
6. Retention reviewed and purged on schedule.

## Domain 3 — Network & infrastructure

7. Network segmentation; production isolated from experimentation.
8. All external-facing services behind authenticated, monitored gateways.
9. Automated patching SLA for critical vulnerabilities within 24 hours.

## Domain 4 — Operational security

10. No production deployment based solely on an AI recommendation; test and review.
11. Security is a commercial capability — treat it as a differentiator, not a tax.
12. Security acceptance is a business enabler: apply the 10-point gate to enable, not block.

## Security acceptance gate

Every production deployment passes a 10-point gate:
1. Access review
2. Secrets audit
3. Logging enabled
4. Backups verified
5. Vulnerability scan
6. Dependency audit
7. Rollback plan
8. Monitoring alert
9. Documentation
10. Human sign-off

Acceptance gates are enforced in the associated project's Decision Register (see `../02_GOVERNANCE/Decision_Register.md`).
