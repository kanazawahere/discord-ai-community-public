import os
import requests
import json

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = "1501877785197674737"

if not DISCORD_TOKEN:
    print("ERROR: Set DISCORD_TOKEN env var first")
    exit(1)

headers = {"Authorization": f"Bot {DISCORD_TOKEN}", "Content-Type": "application/json"}

response = requests.get(f"https://discord.com/api/v10/guilds/{GUILD_ID}/channels", headers=headers)
if response.status_code != 200:
    print(f"Failed to get channels: {response.status_code} {response.text}")
    exit(1)

channels = response.json()

categories = {c["id"]: c for c in channels if c["type"] == 4}
forum_channels = [c for c in channels if c["type"] == 15]

print(f"Found {len(categories)} categories, {len(forum_channels)} forum channels")

role_map = {}
for cat_id, cat in categories.items():
    role_map[cat["name"]] = cat_id
    
print("\nCategories:")
for name, cat_id in role_map.items():
    print(f"  {name}: {cat_id}")

response = requests.get(f"https://discord.com/api/v10/guilds/{GUILD_ID}/roles", headers=headers)
roles = response.json()
role_by_name = {r["name"]: r["id"] for r in roles}
print("\nRoles:")
for r in roles:
    if r["name"] not in ["@everyone"]:
        print(f"  {r['name']}: {r['id']}")

PERMISSION_OVERWRITES = {
    "@everyone": {"view_channel": False, "send_messages": False, "create_public_threads": False},
    "🌱 Khai Linh": {"view_channel": True, "send_messages": True, "create_public_threads": True},
    "⚔️ Luyện Khí": {"view_channel": True, "send_messages": True, "create_public_threads": True},
    "🌀 Kết Giới": {"view_channel": True, "send_messages": True, "create_public_threads": True},
    "☁️ Thiên Cơ": {"view_channel": True, "send_messages": True, "create_public_threads": True},
    "👁️ Nội Điện": {"view_channel": True, "send_messages": True, "create_public_threads": True},
}

category_roles = {
    "🌱 Nhập Môn Tu Hành": ["🌱 Khai Linh", "⚔️ Luyện Khí", "🌀 Kết Giới", "☁️ Thiên Cơ", "👁️ Nội Điện"],
    "⚔️ Claude Code Pháp Môn": ["⚔️ Luyện Khí", "🌀 Kết Giới", "☁️ Thiên Cơ", "👁️ Nội Điện"],
    "🔮 Đồng Tu & API": ["🌀 Kết Giới", "☁️ Thiên Cơ", "👁️ Nội Điện"],
    "🌀 MCP Kết Giới": ["🌀 Kết Giới", "☁️ Thiên Cơ", "👁️ Nội Điện"],
    "☁️ Vân Hải Tiên Cung": ["☁️ Thiên Cơ", "👁️ Nội Điện"],
    "📖 Linh Trí Học Cung": ["👁️ Nội Điện"],
}

def build_permissions(allowed_roles, category_name):
    overwrites = []
    
    overwrites.append({
        "id": GUILD_ID,
        "type": "role",
        "deny": str(1024 | 2048 | 32768)
    })
    
    for role_name, role_id in role_by_name.items():
        if role_name in ["@everyone"]:
            continue
        if role_name in ["Hệ Thống Nghịch Thiên Cải Mệnh", "carl-bot"]:
            continue
        
        if role_name in allowed_roles:
            allow = 0
            allow |= 1024
            allow |= 2048
            allow |= 32768
            overwrites.append({"id": role_id, "type": "role", "allow": str(allow)})
        else:
            deny = 0
            deny |= 2048
            deny |= 32768
            overwrites.append({"id": role_id, "type": "role", "deny": str(deny)})
    
    return overwrites

print("\n=== Setting permissions ===")

for cat_name, allowed_roles in category_roles.items():
    cat_id = role_map.get(cat_name)
    if not cat_id:
        print(f"Category not found: {cat_name}")
        continue
    
    overwrites = build_permissions(allowed_roles, cat_name)
    
    url = f"https://discord.com/api/v10/channels/{cat_id}"
    data = {"permission_overwrites": overwrites}
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        print(f"✓ {cat_name}")
    else:
        print(f"✗ {cat_name}: {response.status_code} {response.text}")

print("\n=== Setting @everyone DENY on forum channels ===")

everyone_id = GUILD_ID
for channel in forum_channels:
    cat_id = channel.get("parent_id")
    cat_name = next((k for k, v in role_map.items() if v == cat_id), None)
    
    if not cat_name:
        continue
    
    allowed_roles = category_roles.get(cat_name, [])
    overwrites = []
    
    overwrites.append({"id": everyone_id, "type": "role", "deny": str(1024 | 2048 | 32768)})
    
    for role_name, role_id in role_by_name.items():
        if role_name in ["@everyone", "Hệ Thống Nghịch Thiên Cải Mệnh", "carl-bot"]:
            continue
        if role_name in allowed_roles:
            allow = 1024 | 2048 | 32768
            overwrites.append({"id": role_id, "type": "role", "allow": str(allow)})
    
    url = f"https://discord.com/api/v10/channels/{channel['id']}"
    data = {"permission_overwrites": overwrites}
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        print(f"✓ {channel['name']}")
    else:
        print(f"✗ {channel['name']}: {response.status_code} {response.text}")

print("\nDone!")