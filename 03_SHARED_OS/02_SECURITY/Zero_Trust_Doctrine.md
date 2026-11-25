# Zero Trust Doctrine

**Status:** v1.1 | **Date:** 2026-11-18 | **Owner:** Founder | **Review:** Annual

## Principle

Never trust, always verify. No implicit trust for entities inside the network boundary or inside the corporate domain.

## Boundaries

- **Founder env:** isolated to the founder's workspace.
- **R&D env:** the research and development network, including the Hermes evaluation environment.
- **Production env:** the live services environment — most restricted.

## Assumptions

- The network is hostile; every request is authenticated and authorised.
- The boundary is the minimum set of service-to-service trust rules.
- Security and governance capability is not equivalent to a security boundary on its own.

## Enforcement

- Network policies restrict east-west traffic.
- Service mesh or equivalent for mTLS between services.
- Audit logging for all privileged actions.
