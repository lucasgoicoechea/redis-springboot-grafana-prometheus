from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class SkillResult:
    name: str
    output: Dict[str, Any]


class Skill:
    name: str

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        raise NotImplementedError("Skill.execute must be implemented by subclasses")


class DomainAnalysisSkill(Skill):
    name = "domain-analysis"

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        description = inputs.get("domain_description", "")
        output = {
            "problem_statement": (
                "Design a Spring Boot service that combines Redis caching with Prometheus/Grafana observability "
                f"to improve API performance and operational insight for: {description}"
            ),
            "objective": (
                "Create an agentic POC that defines architecture, caching strategy, and monitoring integration "
                "for a Spring Boot microservice."
            ),
            "scope": [
                "Spring Boot service architecture",
                "Redis caching design",
                "Prometheus/Grafana observability",
                "Agentic specification and task planning",
            ],
            "constraints": [
                "Design-focused POC, not a production deployment",
                "Use Redis for caching and Spring Boot Actuator for metrics",
                "Include sample Prometheus scrape config and Grafana dashboard guidance",
            ],
            "stack_references": [
                "Spring Boot",
                "Redis",
                "Prometheus",
                "Grafana",
                "Micrometer",
            ],
        }
        return SkillResult(name=self.name, output=output)


class AgentArchitectureSkill(Skill):
    name = "agent-architecture"

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        output = {
            "architecture_summary": (
                "A Spring Boot API with Redis caching, Actuator metrics, and Prometheus scrape integration, "
                "supported by Grafana visualization and an agentic design workflow."
            ),
            "components": [
                "Spring Boot REST service",
                "Redis cache layer",
                "Actuator / Prometheus metrics export",
                "Grafana dashboard reference",
                "Agentic planning engine",
                "Sample scaffold guidance",
            ],
            "flow": [
                "Receive the Spring Boot monitoring requirement",
                "Analyze data flow and caching needs",
                "Define integration points for Redis and Prometheus",
                "Document architecture and components",
                "Produce the specification and tasks",
                "Generate starter prompts for the agentic workflow",
            ],
            "key_decisions": [
                "Which data should be cached and for how long?",
                "What Prometheus metrics are most valuable?",
                "How should Grafana dashboards visualize system health?",
            ],
        }
        return SkillResult(name=self.name, output=output)


class IntegrationModelingSkill(Skill):
    name = "integration-modeling"

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        output = {
            "cache_policy": [
                "Cache request results with Redis for 10 minutes by default.",
                "Use application-level keys for endpoint caching.",
                "Keep cache invalidation simple for the POC example.",
            ],
            "metrics_plan": [
                "Expose request rate, latency, and cache hit/miss metrics.",
                "Publish metrics through /actuator/prometheus.",
                "Use Micrometer to instrument Redis operations and HTTP requests.",
            ],
            "dashboard_outline": [
                "HTTP request rate and latency panel.",
                "Cache hit/miss ratio panel.",
                "JVM memory and CPU usage panel.",
            ],
        }
        return SkillResult(name=self.name, output=output)


class SkillModelingSkill(Skill):
    name = "skill-modeling"

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        output = {
            "skills": [
                {
                    "id": "domain-analysis",
                    "role": "Capture the Spring Boot monitoring problem and define business value.",
                    "input": ["Domain description"],
                    "output": ["Problem statement", "Objective", "Scope", "Constraints"],
                },
                {
                    "id": "architecture-design",
                    "role": "Recommend service architecture, Redis integration, and observability flow.",
                    "input": ["Problem statement", "Constraints"],
                    "output": ["Architecture summary", "Components", "Flow"],
                },
                {
                    "id": "integration-modeling",
                    "role": "Define Redis caching strategy and Prometheus/Grafana monitoring integration.",
                    "input": ["Architecture design", "Functional requirements"],
                    "output": ["Cache policy", "Metrics plan", "Dashboard outline"],
                },
                {
                    "id": "spec-writing",
                    "role": "Draft the technical specification with acceptance criteria.",
                    "input": ["Domain analysis", "Architecture", "Integration design"],
                    "output": ["Spec document", "Acceptance criteria", "Success metrics"],
                },
                {
                    "id": "task-planning",
                    "role": "Create a prioritized implementation backlog for the POC.",
                    "input": ["Specification", "Dependencies"],
                    "output": ["Ordered tasks", "Delivery phases"],
                },
                {
                    "id": "prompt-design",
                    "role": "Generate starter prompts and example interactions for the agent.",
                    "input": ["Objective", "Target audience"],
                    "output": ["Prompt templates", "Example scenarios"],
                },
            ]
        }
        return SkillResult(name=self.name, output=output)


class SpecWritingSkill(Skill):
    name = "spec-writing"

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        objective = inputs.get("objective", "")
        architecture = inputs.get("architecture_summary", "")
        skills = inputs.get("skills", [])

        output = {
            "overview": "Agentic POC specification for a Spring Boot monitoring and caching stack.",
            "objective": objective,
            "architecture": architecture,
            "stack": [
                "Spring Boot",
                "Redis",
                "Spring Boot Actuator",
                "Micrometer Prometheus",
                "Grafana",
            ],
            "functional_requirements": [
                "Define the Spring Boot API and Redis caching behavior.",
                "Expose Prometheus metrics through Actuator.",
                "Document a Grafana dashboard for service health and cache performance.",
                "Provide a sample Spring Boot project skeleton.",
                "Generate a clear task backlog for implementation.",
            ],
            "nonfunctional_requirements": [
                "Cache lookups must be fast and deterministic.",
                "Metrics export must be accessible on /actuator/prometheus.",
                "The design should support operations and observability.",
            ],
            "acceptance_criteria": [
                "The specification highlights Redis caching and observability.",
                "It describes at least 5 modular skills.",
                "It includes a sample implementation guidance section.",
                "It has a measurable task backlog.",
            ],
            "skills_overview": skills,
        }
        return SkillResult(name=self.name, output=output)


class TaskPlanningSkill(Skill):
    name = "task-planning"

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        output = {
            "tasks": [
                {
                    "id": "task-1",
                    "title": "Analyze Spring Boot monitoring and caching goals",
                    "priority": "high",
                },
                {
                    "id": "task-2",
                    "title": "Model the architecture for Redis cache and metrics export",
                    "priority": "high",
                },
                {
                    "id": "task-3",
                    "title": "Create the Spring Boot sample skeleton",
                    "priority": "medium",
                },
                {
                    "id": "task-4",
                    "title": "Write Prometheus scrape and Grafana dashboard guidance",
                    "priority": "medium",
                },
                {
                    "id": "task-5",
                    "title": "Document the POC and verify with tests",
                    "priority": "low",
                },
            ],
            "notes": "Begin with architecture and then move into sample implementation and monitoring guidance.",
        }
        return SkillResult(name=self.name, output=output)


class PromptDesignSkill(Skill):
    name = "prompt-design"

    def execute(self, inputs: Dict[str, Any]) -> SkillResult:
        domain = inputs.get("domain_description", "Spring Boot observability agent")
        output = {
            "prompt_template": (
                "You are an expert system designer. Given the domain description, generate: "
                "1) the problem statement, 2) objective, 3) architecture, 4) integration model, "
                "5) technical specification, 6) task backlog, 7) example prompts."
            ),
            "example_usage": [
                {
                    "label": "Spring Boot Monitoring POC",
                    "input": (
                        "Design an agentic programming POC for a Spring Boot microservice that uses "
                        "Redis caching and Prometheus/Grafana monitoring for API performance and "
                        "operational insight."
                    ),
                    "output": (
                        "A design document with architecture, skill model, tasks, and starter prompts "
                        "for Spring Boot observability and caching."
                    ),
                }
            ],
            "domain": domain,
        }
        return SkillResult(name=self.name, output=output)
