from crewai import Agent, Task, Crew


def build_crew(topic: str):

    researcher = Agent(
        role="Senior Researcher",
        goal=f"Find accurate data on {topic}",
        backstory="Expert in market research",
        verbose=True
    )

    analyst = Agent(
        role="Data Analyst",
        goal="Analyze research and extract insights",
        backstory="Expert in analytics",
        verbose=True
    )

    writer = Agent(
        role="Report Writer",
        goal="Write professional report",
        backstory="Expert content writer",
        verbose=True
    )

    research_task = Task(
        description=f"Research detailed information about {topic}",
        expected_output="Detailed research findings with key facts and insights",
        agent=researcher
    )

    analysis_task = Task(
        description="Analyze the research and generate insights",
        expected_output="Clear analysis with insights, trends, and conclusions",
        agent=analyst
    )

    writing_task = Task(
        description="Write final structured business report",
        expected_output="Well-structured professional report with headings",
        agent=writer
    )

    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        verbose=True
    )

    return crew