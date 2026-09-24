# Custom Tools MCP Server

A small MCP server with two tools:

- `calculate_age(date_of_birth)`: returns age in completed years for a `YYYY-MM-DD` date.
- `random_number(min_value, max_value)`: returns an inclusive random integer. Bounds may be supplied in either order.

## Run locally

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
```

The server uses MCP's standard input/output transport when run locally.

## Deploy with Prefect Horizon

1. Push this repository to GitHub.
2. Sign in at [Prefect Horizon](https://horizon.prefect.io/) with the GitHub account that can access the repository.
3. Create a deployment from `Rafi3215987/custom-tools-repository` (or select the repository in Horizon).
4. Set the server entry point to `server.py:mcp`. Horizon should detect `requirements.txt` automatically.
5. Deploy and copy the resulting MCP endpoint URL, which ends in `/mcp`.

## Connect Claude Desktop

In Claude Desktop, open **Settings → Connectors → Add custom connector**, enter the deployed Horizon MCP URL, and complete the OAuth sign-in flow. The endpoint is the URL shown by Horizon with `/mcp` appended if Horizon does not include it already.
