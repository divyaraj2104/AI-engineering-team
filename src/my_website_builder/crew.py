from dis import Instruction
from tabnanny import verbose
from gradio.mcp import tool
from pydantic import BaseModel
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List



@CrewBase
class myDeveloperAgents():
    """Full stack developer agents"""
    agents_config = "config/web_developer_agents.yaml"
    tasks_config = "config/web_developer_tasks.yaml"
    

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def webpage_creator(self) -> Agent:
        return Agent(config=self.agents_config['webpage_creator'], 
        verbose=True,
        allow_code_execution=True)

    @task
    def create_webpage(self) -> Task:
        return Task(config=self.tasks_config['create_webpage'],verbose=True)

    @crew
    def crew(self) -> Crew:
        """Creates the website component"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True
        )



class engineering_manager_output_format(BaseModel):
    module_names: List[str]
    components: List[List[str]]
    instructions: List[str]

@CrewBase
class MyWebsiteBuilder():
    """MyWebsiteBuilder crew"""
    agents_config = "config/engineering_manager_agent.yaml"
    tasks_config = "config/engineering_manager_task.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]
    @agent
    def engineering_manager(self) -> Agent:
        return Agent(config=self.agents_config['engineering_manager'],verbose=True)

    @task
    def design_app(self) -> Task:
        return Task(
            config=self.tasks_config['design_app'],
            verbose=True,
            output_pydantic=engineering_manager_output_format,
        )


    @crew
    def crew(self) -> Crew:
        """Creates the MyWebsiteBuilder crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
