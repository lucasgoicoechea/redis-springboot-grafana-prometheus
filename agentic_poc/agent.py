from __future__ import annotations

from typing import Any, Dict

from .skills import (
    AgentArchitectureSkill,
    DomainAnalysisSkill,
    IntegrationModelingSkill,
    PromptDesignSkill,
    SkillModelingSkill,
    SpecWritingSkill,
    TaskPlanningSkill,
)


class AgenticPOC:
    def __init__(self) -> None:
        self.skills = [
            DomainAnalysisSkill(),
            AgentArchitectureSkill(),
            IntegrationModelingSkill(),
            SkillModelingSkill(),
            SpecWritingSkill(),
            TaskPlanningSkill(),
            PromptDesignSkill(),
        ]

    def run(self, domain_description: str) -> Dict[str, Any]:
        context: Dict[str, Any] = {"domain_description": domain_description}
        results: Dict[str, Any] = {}

        for skill in self.skills:
            skill_input = self._prepare_input(skill, context, results)
            result = skill.execute(skill_input)
            results[skill.name] = result.output
            context.update(result.output)

        return {
            "domain_description": domain_description,
            "results": results,
        }

    def _prepare_input(self, skill: Any, context: Dict[str, Any], results: Dict[str, Any]) -> Dict[str, Any]:
        base_input = context.copy()

        if skill.name == "agent-architecture":
            base_input["problem_statement"] = results.get("domain-analysis", {}).get("problem_statement", "")
        elif skill.name == "integration-modeling":
            base_input["architecture_summary"] = results.get("agent-architecture", {}).get("architecture_summary", "")
        elif skill.name == "skill-modeling":
            base_input["objective"] = results.get("domain-analysis", {}).get("objective", "")
        elif skill.name == "spec-writing":
            base_input["objective"] = results.get("domain-analysis", {}).get("objective", "")
            base_input["architecture_summary"] = results.get("agent-architecture", {}).get("architecture_summary", "")
            base_input["skills"] = results.get("skill-modeling", {}).get("skills", [])
        elif skill.name == "task-planning":
            base_input["spec"] = results.get("spec-writing", {})
        elif skill.name == "prompt-design":
            base_input["objective"] = results.get("domain-analysis", {}).get("objective", "")

        return base_input
