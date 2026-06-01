from __future__ import annotations

import json
from pathlib import Path

from agentic_poc.agent import AgenticPOC


def format_section(data: dict) -> str:
    lines: list[str] = []
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                if isinstance(item, dict):
                    lines.append("  -")
                    for inner_key, inner_value in item.items():
                        lines.append(f"      {inner_key}: {inner_value}")
                else:
                    lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)


def main() -> int:
    output_dir = Path("demo-output")
    output_dir.mkdir(exist_ok=True)

    domain_description = (
        "Design a Spring Boot microservice with Redis caching and Prometheus/Grafana monitoring "
        "that improves API response times and operational insight."
    )

    agent = AgenticPOC()
    result = agent.run(domain_description)

    json_path = output_dir / "agentic_poc_result.json"
    text_path = output_dir / "agentic_poc_result.txt"
    spec_md_path = output_dir / "agentic_poc_generated_spec.md"
    tasks_md_path = output_dir / "agentic_poc_generated_tasks.md"

    with json_path.open("w", encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=2, ensure_ascii=False)

    with text_path.open("w", encoding="utf-8") as text_file:
        text_file.write("Agentic POC Demo Result\n")
        text_file.write("========================\n\n")
        text_file.write(f"Domain: {result['domain_description']}\n\n")
        for skill_name, payload in result["results"].items():
            text_file.write(f"=== {skill_name} ===\n")
            text_file.write(format_section(payload))
            text_file.write("\n\n")

    spec = result["results"].get("spec-writing", {})
    with spec_md_path.open("w", encoding="utf-8") as spec_file:
        spec_file.write("# Generated POC Specification\n\n")
        spec_file.write(f"## Overview\n{spec.get('overview', '')}\n\n")
        spec_file.write(f"## Objective\n{spec.get('objective', '')}\n\n")
        spec_file.write("## Architecture\n")
        spec_file.write(f"{spec.get('architecture', '')}\n\n")
        spec_file.write("## Stack\n")
        for item in spec.get("stack", []):
            spec_file.write(f"- {item}\n")
        spec_file.write("\n## Functional Requirements\n")
        for requirement in spec.get("functional_requirements", []):
            spec_file.write(f"- {requirement}\n")
        spec_file.write("\n## Acceptance Criteria\n")
        for criteria in spec.get("acceptance_criteria", []):
            spec_file.write(f"- {criteria}\n")

    tasks = result["results"].get("task-planning", {}).get("tasks", [])
    with tasks_md_path.open("w", encoding="utf-8") as tasks_file:
        tasks_file.write("# Generated Task Backlog\n\n")
        for task in tasks:
            tasks_file.write(f"- [{task.get('priority', 'medium')}] {task.get('title', '')}\n")

    print(f"Demo output written to: {json_path.resolve()}")
    print(f"Demo summary written to: {text_path.resolve()}")
    print(f"Generated spec written to: {spec_md_path.resolve()}")
    print(f"Generated tasks written to: {tasks_md_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
