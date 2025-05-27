from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
import os

text_knowledge_source = TextFileKnowledgeSource(
    file_paths=os.listdir(f"{os.getcwd()}/knowledge/")
)

@CrewBase
class RichardsCrew():
    """
    A crew of agents that can work together to complete tasks.
    """

    @agent
    def technical_content_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_content_analyst"],
            verbose=True,
        )

    @agent
    def senior_software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_software_architect"],
            verbose=True,
        )

    @agent
    def technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_writer"],
            verbose=True,
        )

    @agent
    def peer_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["peer_reviewer"],
            verbose=True,
        )

    @agent
    def documentation_publisher(self) -> Agent:
        return Agent(
            config=self.agents_config["documentation_publisher"],
            verbose=True,
        )

    @task
    def extract_outline_from_transcription(self) -> Task:
        return Task(
            config=self.tasks_config["extract_outline_from_transcription"],
            verbose=True,
        )

    @task
    def expand_and_validate_technical_details(self) -> Task:
        return Task(
            config=self.tasks_config["expand_and_validate_technical_details"],
            verbose=True,
        )

    @task
    def refine_for_clarity_and_structure(self) -> Task:
        return Task(
            config=self.tasks_config["refine_for_clarity_and_structure"],
            verbose=True,
        )

    @task
    def perform_peer_review_and_feedback(self) -> Task:
        return Task(
            config=self.tasks_config["perform_peer_review_and_feedback"],
            verbose=True,
        )

    @task
    def publish_and_distribute_documentation(self) -> Task:
        return Task(
            config=self.tasks_config["publish_and_distribute_documentation"],
            verbose=True,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            knowledge_sources=[text_knowledge_source],
            verbose=True,
        )
