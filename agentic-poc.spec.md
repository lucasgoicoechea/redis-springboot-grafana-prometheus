# Agentic POC Specification

## Objective

Design an agentic proof-of-concept for a Spring Boot service with Redis caching and Prometheus/Grafana observability.

The agent should produce:

- a clear problem statement,
- a reusable architecture,
- modular skills,
- a technical specification,
- a prioritized task plan,
- sample implementation guidance.

## Problem

Modern Spring Boot applications need fast caching and reliable observability.
Teams often struggle to combine Redis performance improvements with Prometheus/Grafana monitoring in a coherent design.

This POC addresses that gap by demonstrating an agentic planning workflow for the full stack.

## Scope

Includes:

- problem analysis for Spring Boot + Redis + monitoring,
- agent architecture proposal,
- functional requirements for caching and metrics,
- sample Spring Boot skeleton guidance,
- backlog and delivery plan.

Excludes:

- production deployments,
- infrastructure provisioning,
- full application testing against real Redis/Grafana instances.

## Agent roles and responsibilities

1. Domain analyst
   - defines the Spring Boot monitoring and caching challenge.
2. Architecture designer
   - proposes the service and observability architecture.
3. Integration modeler
   - maps Redis caching and Prometheus metrics into the design.
4. Specification author
   - writes the technical spec and acceptance criteria.
5. Work planner
   - breaks requirements into executable tasks.
6. Prompt designer
   - generates high-quality agent launch prompts.

## Proposed skills

- `domain-analysis` — understand the Spring Boot/Redis/monitoring context.
- `architecture-design` — define service components and data flow.
- `integration-modeling` — map Redis cache policy and observability design.
- `spec-writing` — produce a detailed technical specification.
- `task-planning` — create the implementation backlog.
- `prompt-design` — craft starter prompts and usage examples.

## Expected flow

1. Receive the target scenario: Spring Boot plus Redis caching and observability.
2. Analyze the requirements and business value.
3. Model the architecture and integration points.
4. Write the POC spec and acceptance criteria.
5. Generate the task backlog.
6. Provide example prompts for the agentic workflow.

## Acceptance criteria

- The POC clearly describes the Spring Boot monitoring problem.
- It specifies Redis caching and Prometheus/Grafana observability.
- It defines at least 5 skills with inputs and outputs.
- It includes a prioritized task list.
- It provides examples of how to launch the agent.
- It references the sample `spring-boot-sample/` scaffold.
