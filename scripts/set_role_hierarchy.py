import os
import requests
import json

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = "1501877785197674737"

if not DISCORD_TOKEN:
    print("ERROR: Set DISCORD_TOKEN env var first")
    exit(1)

headers = {"Authorization": f"Bot {DISCORD_TOKEN}", "Content-Type": "application/json"}

response = requests.get(f"https://discord.com/api/v10/guilds/{GUILD_ID}/roles", headers=headers)
if response.status_code != 200:
    print(f"Failed to get roles: {response.status_code} {response.text}")
    exit(1)

roles = response.json()
for role in roles:
    print(f"{role['position']:2} | {role['id']:18} | {role['name']}")

carl_role = next((r for r in roles if r["name"].lower() == "carl-bot"), None)
if not carl_role:
    print("\nERROR: Carl-bot role not found. Make sure Carl-bot is in the server.")
    exit(1)

print(f"\nFound Carl-bot role: {carl_role['name']} (ID: {carl_role['id']})")

custom_roles = [r for r in roles if r["name"].lower() not in ["@everyone", "carl-bot"]]
max_position = max(r["position"] for r in custom_roles) if custom_roles else 0

new_position = max_position + 1

url = f"https://discord.com/api/v10/guilds/{GUILD_ID}/roles/{carl_role['id']}"
data = {"position": new_position}
response = requests.patch(url, headers=headers, json=data)

if response.status_code in [200, 201]:
    print(f"Success! Carl-bot role moved to position {new_position}")
else:
    print(f"Failed: {response.status_code} {response.text}")