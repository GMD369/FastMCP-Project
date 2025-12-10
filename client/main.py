from fastmcp import FastMCPClient, Agent

# 1. Connect to tool server
client = FastMCPClient("http://127.0.0.1:8000/mcp")
agent = Agent(client)

# 2. Define Task
task = """
Get Lahore weather using get_weather tool.
Then save summary inside a file called 'weather.txt'.
"""

# 3. Run Agent
result = agent.run(task)
print(result)
