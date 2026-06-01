from __future__ import annotations

import argparse
import json

from .agent import AgenticPOC


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Spring Boot monitoring and Redis caching POC agent."
    )
    parser.add_argument(
        "domain",
        nargs="+",
        help="Domain description or problem the agent should solve.",
    )
    parser.add_argument(
        "--output",
        choices=["json", "text"],
        default="text",
        help="Output format.",
    )
    return parser.parse_args()


def format_text(result: dict) -> str:
    output_lines = ["Agentic POC result:", ""]
    output_lines.append(f"Domain: {result['domain_description']}")
    output_lines.append("")

    for skill_name, data in result["results"].items():
        output_lines.append(f"=== {skill_name} ===")
        for key, value in data.items():
            if isinstance(value, list):
                output_lines.append(f"{key}:")
                for item in value:
                    if isinstance(item, dict):
                        output_lines.append("  -")
                        for inner_key, inner_value in item.items():
                            output_lines.append(f"      {inner_key}: {inner_value}")
                    else:
                        output_lines.append(f"  - {item}")
            else:
                output_lines.append(f"{key}: {value}")
        output_lines.append("")

    return "\n".join(output_lines)


def main() -> int:
    args = parse_args()
    domain_description = " ".join(args.domain)
    agent = AgenticPOC()
    result = agent.run(domain_description)

    if args.output == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_text(result))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
