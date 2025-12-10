from mcp.server.fastmcp import FastMCP
import requests

server = FastMCP("weather-tools-server")

# ------- TOOL 1 ------
@server.tool()
def get_weather(city: str):
    """Get weather of a city"""
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    return {
        "city": city,
        "temp": data["current_condition"][0]["temp_C"],
        "desc": data["current_condition"][0]["weatherDesc"][0]["value"],
    }

# ------- TOOL 2 ------
@server.tool()
def save_to_file(filename: str, text: str):
    """Save given text into a file"""
    with open(f"../output/{filename}", "w", encoding="utf-8") as f:
        f.write(text)
    return {"status": "saved", "file": filename}


if __name__ == "__main__":
    server.run()
