import os
import requests

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = "1501877785197674737"

if not DISCORD_TOKEN:
    print("ERROR: Set DISCORD_TOKEN env var first")
    exit(1)

headers = {"Authorization": f"Bot {DISCORD_TOKEN}", "Content-Type": "application/json"}

response = requests.get(f"https://discord.com/api/v10/guilds/{GUILD_ID}/roles", headers=headers)
roles = response.json()

role_configs = {
    "🌱 Khai Linh": {"color": 0x7CFC00, "hoist": True},
    "⚔️ Luyện Khí": {"color": 0x00BFFF, "hoist": True},
    "🌀 Kết Giới": {"color": 0x9370DB, "hoist": True},
    "☁️ Thiên Cơ": {"color": 0xFFD700, "hoist": True},
    "👁️ Nội Điện": {"color": 0xFF4500, "hoist": True},
    "🩶 Phàm Nhân": {"color": 0x808080, "hoist": False},
}

print("=== Setting role colors & hoist ===\n")

for role in roles:
    role_name = role["name"]
    if role_name not in role_configs:
        print(f"  Skip: {role_name}")
        continue
    
    config = role_configs[role_name]
    url = f"https://discord.com/api/v10/guilds/{GUILD_ID}/roles/{role['id']}"
    data = {
        "color": config["color"],
        "hoist": config["hoist"]
    }
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        print(f"✓ {role_name}: color=#{config['color']:06x}, hoist={config['hoist']}")
    else:
        print(f"✗ {role_name}: {response.status_code} {response.text}")

print("\nDone!")