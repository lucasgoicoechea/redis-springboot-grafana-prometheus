import unittest

from agentic_poc.agent import AgenticPOC


class TestAgenticPOC(unittest.TestCase):
    def test_agentic_poc_run_returns_expected_structure(self):
        agent = AgenticPOC()
        result = agent.run("Spring Boot Redis monitoring POC")

        self.assertEqual(result["domain_description"], "Spring Boot Redis monitoring POC")
        self.assertIn("results", result)
        self.assertIn("domain-analysis", result["results"])
        self.assertIn("prompt-design", result["results"])

    def test_prompt_design_includes_prompt_template(self):
        agent = AgenticPOC()
        result = agent.run("Spring Boot Redis monitoring POC")
        prompt_design = result["results"]["prompt-design"]

        self.assertIn("prompt_template", prompt_design)
        self.assertIn("example_usage", prompt_design)
        self.assertIn("domain", prompt_design)

    def test_spec_writes_observability_requirements(self):
        agent = AgenticPOC()
        result = agent.run("Spring Boot Redis monitoring POC")
        spec = result["results"]["spec-writing"]

        self.assertIn("Prometheus", " ".join(spec.get("stack", [])))
        self.assertIn("Grafana", " ".join(spec.get("stack", [])))
        self.assertGreaterEqual(len(spec.get("functional_requirements", [])), 5)

    def test_task_planning_contains_priority_tasks(self):
        agent = AgenticPOC()
        result = agent.run("Spring Boot Redis monitoring POC")
        task_planning = result["results"]["task-planning"]

        self.assertIn("tasks", task_planning)
        self.assertGreaterEqual(len(task_planning["tasks"]), 5)
        self.assertIn("priority", task_planning["tasks"][0])


if __name__ == "__main__":
    unittest.main()
