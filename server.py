from datetime import date, datetime
import random

from mcp.server.fastmcp import FastMCP


# Create one MCP server
mcp = FastMCP("Custom Tools Server")


@mcp.tool()
def calculate_age(date_of_birth: str) -> int:
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(
            "Invalid date format. Use YYYY-MM-DD."
        )

    today = date.today()

    if dob > today:
        raise ValueError("Date of birth cannot be in the future.")

    age = today.year - dob.year

    # Birthday has not occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age


@mcp.tool()
def random_number(min_value: int, max_value: int) -> int:

    if min_value > max_value:
        temp = min_value
        min_value = max_value
        max_value = min_value
        
    return random.randint(min_value, max_value)


if __name__ == "__main__":
    mcp.run()