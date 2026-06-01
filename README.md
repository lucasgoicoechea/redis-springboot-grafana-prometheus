# Agentic POC for Spring Boot Monitoring and Redis Caching

This repository is a complete proof-of-concept that uses agentic design principles to define a Spring Boot microservice architecture with Redis caching and Prometheus/Grafana observability.

## What is included

- `.agent.md`: custom agent definition for the Spring Boot monitoring POC.
- `agentic-poc.spec.md`: technical specification for the POC.
- `agentic-poc.tasks.md`: task backlog and implementation plan.
- `agentic-poc.prompt.md`: prompt for starting the design agent.
- `agentic-poc.skills.md`: formal skill model for the solution.
- `agentic_poc/`: Python implementation of the POC agent.
- `spring-boot-sample/`: starter Spring Boot skeleton with Redis, Prometheus, and Grafana guidance.

## How to run the POC

1. Install Python 3.10+.
2. From the project folder, run:

```powershell
python -m agentic_poc.main "Design a Spring Boot microservice with Redis caching and Prometheus/Grafana monitoring."
```

3. For JSON output:

```powershell
python -m agentic_poc.main "Design a Spring Boot microservice with Redis caching and Prometheus/Grafana monitoring." --output json
```

4. To run the demo and generate the example artifacts:

```powershell
python demo.py
```

5. To run unit tests:

```powershell
python -m unittest discover -s tests
```

## Spring Boot sample

A starter sample application is available in `spring-boot-sample/`.
It includes:

- `pom.xml` with Spring Boot, Redis, Actuator, and Prometheus dependencies.
- REST endpoints for caching with Redis.
- Actuator and Prometheus configuration.
- Prometheus scrape configuration sample.
- Grafana dashboard starter JSON.

## What the agent does

The Python POC agent simulates a design workflow that:

- analyzes the problem domain,
- proposes an architecture for Spring Boot and Redis,
- models reusable skills,
- generates a technical specification,
- creates a prioritized task backlog,
- designs starter prompts for the solution.

## Extension

You can extend `agentic_poc/skills.py` to connect to an actual LLM or to generate richer Spring Boot scaffolding from the agent design.
