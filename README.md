# 🤖 Autonomous Daily Logs Bot

**100% Tự động - Không cần can thiệp người dùng**

[![🤖 Autonomous Daily Logs Bot](https://github.com/Gynzrt/daily-logs/actions/workflows/daily-commit.yml/badge.svg)](https://github.com/Gynzrt/daily-logs/actions/workflows/daily-commit.yml)

## 🎯 Tính năng chính

### ✅ **Hoàn toàn tự động**
- 🤖 Chạy độc lập 100% qua GitHub Actions
- ⏰ Tự động kích hoạt mỗi ngày lúc 00:00 UTC
- 🔄 Không cần máy tính bật hay can thiệp người dùng
- 🛡️ Error handling và monitoring tự động

### ✅ **Bot thông minh**
- 📝 Tự động ghi logs với timestamp UTC
- 💾 Tự động commit với message "🤖 autonomous update..."
- 🚀 Tự động push lên GitHub
- 📊 Tracking số lần chạy và uptime

### ✅ **Cấu hình linh hoạt**
- ⚙️ File config JSON cho bot settings
- 📋 Status monitoring qua bot_status.json
- 🔧 Có thể tùy chỉnh format logs và commits
- 🎛️ Bật/tắt bot qua configuration

## 📁 Cấu trúc dự án

```
auto-daily-logs/
├── .github/
│   └── workflows/
│       └── daily-commit.yml      # GitHub Actions workflow
├── autonomous_bot.py             # Script bot chính
├── bot_config.json              # Cấu hình bot
├── autonomous_logs.txt          # File logs (tự động tạo)
├── bot_status.json              # Trạng thái bot (tự động tạo)
└── README.md                    # Documentation này
```

## 🚀 Cách thiết lập

### 1. Tạo repository trên GitHub
```bash
# Tạo repo mới tên: auto-daily-logs
# Có thể public hoặc private
```

### 2. Push code lên GitHub
```bash
git remote add origin git@github.com:Gynzrt/auto-daily-logs.git
git add .
git commit -m "🤖 Initial autonomous bot setup"
git push -u origin main
```

### 3. Kích hoạt GitHub Actions
- Actions sẽ tự động được kích hoạt
- Workflow chạy mỗi ngày lúc 00:00 UTC
- Có thể trigger thủ công trong tab Actions

## 🤖 Hoạt động của bot

### **Mỗi ngày lúc 00:00 UTC:**

1. 🤖 **Bot khởi động tự động**
   - GitHub Actions trigger workflow
   - Setup Python environment
   - Configure Git với user "blogecoin"

2. 📝 **Cập nhật logs**
   ```
   🤖 Autonomous update at 2025-09-28 00:00:00 UTC
   ```

3. 💾 **Commit tự động**
   ```
   🤖 autonomous update 20250928_000000
   ```

4. 🚀 **Push lên GitHub**
   - Tự động push changes
   - Cập nhật status monitoring

## 📊 Monitoring

### **File logs được tạo:**

- `autonomous_logs.txt` - Logs hàng ngày với timestamps
- `bot_status.json` - Trạng thái bot, số lần chạy, uptime

### **GitHub Actions:**
- Xem lịch sử chạy trong tab Actions
- Logs chi tiết cho mỗi lần chạy
- Status badges cho monitoring

## ⚙️ Cấu hình

### **bot_config.json:**
```json
{
  "bot_name": "blogecoin Bot",
  "enabled": true,
  "log_format": "🤖 Autonomous update at {timestamp} UTC",
  "commit_format": "🤖 autonomous update {timestamp}"
}
```

### **Tùy chỉnh:**
- Đổi `enabled: false` để tạm dừng bot
- Sửa `log_format` để thay đổi format logs
- Sửa `commit_format` để thay đổi commit messages

## 🔧 Troubleshooting

### **Nếu bot không chạy:**
1. Kiểm tra tab Actions có enabled không
2. Xem logs trong workflow runs
3. Kiểm tra `bot_config.json` có `enabled: true`

### **Test thủ công:**
```bash
# Trong tab Actions > Run workflow
# Hoặc push commit để trigger
```

## 🎯 Kết quả mong đợi

- ✅ Repository có commit mới mỗi ngày
- ✅ Contribution graph xanh liên tục 🟢
- ✅ Hoàn toàn độc lập, không cần bảo trì
- ✅ Logs chi tiết về hoạt động bot

## 📈 Features nâng cao

- 🤖 **Bot branding** với user "blogecoin"
- 📊 **Uptime tracking** tự động
- 🔄 **Error recovery** tự động
- 📋 **Status monitoring** real-time
- 🛡️ **Fail-safe mechanisms**

---

**🤖 Bot này chạy hoàn toàn tự động - upgrade từ phiên bản cũ!**
