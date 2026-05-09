# Cấu Trúc Kho Dữ Liệu

## 📦 Kho Mẹ (Private)
**Repo:** `kanazawahere/discord-ai-community`

```
├── .env                 ← Private (token)
├── discord-mcp/        ← Private (MCP config)
├── .claude/             ← Private (settings)
├── scripts/             ← Private (Python scripts)
├── docs/
│   ├── ARCHITECTURE.md  ← Public
│   ├── PRIVATE_GUIDE.md ← Private
│   └── ...
├── README.md            ← Public
├── PROJECT_STATE.md     ← Public
└── ANNOUNCEMENTS.md     ← Public
```

## 📦 Kho Con (Public)
**Repo:** `kanazawahere/discord-ai-community-public`

```
├── .github/workflows/  ← Sync from Mẹ
├── docs/               ← Sync from Mẹ
├── README.md           ← Sync from Mẹ
├── PROJECT_STATE.md    ← Sync from Mẹ
└── ANNOUNCEMENTS.md    ← Sync from Mẹ
```

## 🔄 Luồng Sync

```
Kho Mẹ (Private)
    ├── Public files ──────────→ GitHub Action ──→ Kho Con (Public)
    │                              (auto-sync)
    │
    └── Private files
        (không sync)
```

## ✅ Quy Tắc

| Loại | Mẹ (Private) | Con (Public) |
|------|---------------|---------------|
| Scripts | ✅ | ❌ |
| Docs (hướng dẫn sử dụng) | ✅ | ❌ |
| Docs (kiến trúc) | ✅ | ✅ |
| README | ✅ | ✅ |
| PROJECT_STATE | ✅ | ✅ |
| ANNOUNCEMENTS | ✅ | ✅ |
| .env, discord-mcp, .claude | ✅ | ❌ |