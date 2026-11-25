# Agent Specification Template

**Status:** v1.1 | **Date:** 2026-11-18 | **Owner:** Founder | **Review:** As needed

## Template structure

```
Agent name: [name]
Scope: [bounded task range]
Model: [provider + version]
Output mode: [standard | light]
Approval boundary: [autonomous | human approval required for X]
Data classification: [public | internal | project-secret | personal]
Decision responsibility: [recursive | bounded | human]
Verification: [sources to check]
```

## Required sections

1. Scope and mandate
2. Authority and boundaries
3. Model and configuration
4. Output mode and format
5. Data classification
6. Decision responsibility and recursion limit
7. Verification requirements
8. Handoff and escalation

## Notes

- Agents never possess secret knowledge; they reason from accessible data.
- Irreversible actions require human approval.
