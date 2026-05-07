# Architecture

Marketing Ops Fusion is organized as an operator-facing intelligence core rather than a single-purpose script.

## Layers

1. `src/core`
   - eventing and state coordination primitives
2. `src/agents`
   - specialist decision modules for marketing domains
3. `src/connectors`
   - external platform adapters and ingestion clients
4. `src/models`
   - shared contracts and data structures
5. `config`
   - strategies, thresholds, and compliance-oriented settings

## Intended Runtime Model

The long-term runtime shape is:

- ingest events from marketing, commerce, and CRM systems
- normalize them into shared models
- enrich them through specialist agents
- emit recommendations, alerts, or execution decisions
- persist the decision trail for operator review
