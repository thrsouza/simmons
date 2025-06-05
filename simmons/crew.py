from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Define LLM configuration
llm = LLM(model="openai/gpt-4o-mini", temperature=0)

@CrewBase
class SimonsCrew():
    """Simmons crew"""
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def technical_content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_content_writer"],
            verbose=True,
            reasoning=True,
            max_reasoning_attempts=3,
        )

    @agent
    def content_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_reviewer"],
            verbose=True,
        )

    @agent
    def markdown_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["markdown_specialist"],
            verbose=True,
            reasoning=True,
            max_reasoning_attempts=3,
        )

    @task
    def write_technical_content_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_technical_content_task"],
            verbose=True,
        )

    @task
    def review_content_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_content_task"],
            verbose=True,
        )

    @task
    def convert_to_markdown_task(self) -> Task:
        return Task(
            config=self.tasks_config["convert_to_markdown_task"],
            output_file='{output_directory}/{topic}.md',
            verbose=True,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
