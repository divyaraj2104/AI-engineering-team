#!/usr/bin/env python
import json
import warnings

from gradio import context
from my_website_builder.crew import MyWebsiteBuilder, myDeveloperAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    inputs = {"requirements": """Build a landing page for an AI startup called "NeuroStack".
                                 Description:
                                    We provide AI-powered document intelligence for law firms.
                                    Features:
                                    - Automatic contract summarization
                                    - Clause extraction
                                    - Risk scoring
                                    - Secure cloud deployment

                                    Tone: Professional, trustworthy, enterprise-grade
                                    """}

    try:
        crew_out = MyWebsiteBuilder().crew().kickoff(inputs=inputs)

        # CrewAI returns CrewOutput. The JSON is usually in crew_out.raw
        data = json.loads(crew_out.raw)

        module_names = data["module_names"]
        components_list = data["components"]
        instructions_list = data["instructions"]

        dev_crew = myDeveloperAgents().crew()

        for i in range(len(module_names)):
            web_page_input = {
                "module_name": module_names[i],
                "components": components_list[i],
                "instruction": instructions_list[i] if i < len(instructions_list) else "",
            }

            web_page_result = dev_crew.kickoff(inputs=web_page_input)
            print(web_page_result.raw)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
