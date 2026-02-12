from crewai import Agent, Task, Crew, LLM

# 🔑 Add your Gemini API key here
GEMINI_API_KEY = "AIzaSyD5JiSmnLbDvQb5f0UOlUKTjJeqHC_W2P4"

# -------------------------
# LLM Setup
# -------------------------
llm = LLM(
    model="gemini-3-flash-preview",
    api_key=GEMINI_API_KEY,
    provider="google"
)

# -------------------------
# Agent 1: Game Narrator
# -------------------------
narrator = Agent(
    role="Game Narrator",
    goal="Create a short treasure hunt story introduction.",
    backstory="You are a creative storyteller who writes short adventure games.",
    llm=llm,
    memory=False
)

# -------------------------
# Agent 2: Puzzle Master
# -------------------------
puzzle_master = Agent(
    role="Puzzle Master",
    goal="Create one simple riddle for the player to solve.",
    backstory="You design fun and simple riddles for adventure games.",
    llm=llm,
    memory=False
)

# -------------------------
# Tasks
# -------------------------
task1 = Task(
    description="Write a short treasure hunt game introduction in 5-6 lines.",
    expected_output="A short adventure story intro.",
    agent=narrator
)

task2 = Task(
    description="Create one simple riddle with the answer included at the end.",
    expected_output="A short riddle and its correct answer.",
    agent=puzzle_master
)

# -------------------------
# Crew Setup
# -------------------------
crew = Crew(
    agents=[narrator, puzzle_master],
    tasks=[task1, task2],
    memory=False
)

# -------------------------
# Run Game
# -------------------------
if __name__ == "__main__":
    print("🏴‍☠️ Welcome to Treasure Hunt Game!\n")
    result = crew.kickoff()
    print("\n🎮 GAME OUTPUT:\n")
    print(result)