<h1 align="center">🚀 MyWebsiteBuilder</h1>

<p align="center">
  Dynamic Multi-Agent Website Generator built with CrewAI
</p>

<p align="center">
  <b>Orchestrator → Worker Architecture</b> • Shared Memory • Structured Outputs • Sequential Page Generation
</p>

<hr>

<h2>🧠 Overview</h2>

<p>
MyWebsiteBuilder is an AI-powered multi-agent system that autonomously designs and generates 
multi-page websites from a single high-level requirement.
</p>

<p>
It dynamically creates agents and tasks, leverages structured outputs (Pydantic), 
and maintains shared crew memory to ensure cross-page consistency.
</p>

<hr>

<h2>⚙️ Architecture</h2>

<ul>
  <li><b>Engineering Manager Agent</b>
    <ul>
      <li>Breaks requirements into structured modules</li>
      <li>Defines page components and instructions</li>
      <li>Returns structured Pydantic outputs</li>
    </ul>
  </li>
  <li><b>Web Developer Agent</b>
    <ul>
      <li>Generates HTML for each module</li>
      <li>Maintains shared memory across pages</li>
      <li>Ensures theme and navigation consistency</li>
    </ul>
  </li>
</ul>

<hr>

<h2>✨ Key Features</h2>

<ul>
  <li>Dynamic Agent & Task Creation</li>
  <li>Shared Crew Memory (<code>memory=True</code>)</li>
  <li>Sequential Execution Flow</li>
  <li>Pydantic Structured Outputs</li>
  <li>Config-Driven YAML Architecture</li>
</ul>

<hr>

<h2>🛠 Tech Stack</h2>

<ul>
  <li>Python 3.10+</li>
  <li>CrewAI</li>
  <li>Pydantic</li>
  <li>YAML Configurations</li>
  <li>UV Dependency Management</li>
</ul>

<hr>

<h2>▶️ Running the Project</h2>

<pre>
pip install uv
crewai install
crewai run
</pre>

<p>
Make sure to add your <code>OPENAI_API_KEY</code> inside a <code>.env</code> file.
</p>

<hr>

<h2>📌 What This Project Demonstrates</h2>

<ul>
  <li>Multi-Agent Orchestration</li>
  <li>Stateful AI Systems</li>
  <li>Orchestrator-Worker Pattern</li>
  <li>AI Memory Management</li>
  <li>Production-Style Agent Architecture</li>
</ul>

<hr>
