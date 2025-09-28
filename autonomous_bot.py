#!/usr/bin/env python3
"""
🤖 Autonomous Daily Logs Bot
Completely independent GitHub Actions bot for daily commits
Author: blogecoin
Version: 2.0 - Fully Autonomous
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

class AutonomousBot:
    """🤖 Fully autonomous bot for daily logging"""

    def __init__(self):
        self.config_file = Path("bot_config.json")
        self.log_file = Path("autonomous_logs.txt")
        self.status_file = Path("bot_status.json")

        # Load bot configuration
        self.config = self.load_config()

    def load_config(self):
        """📋 Load bot configuration"""
        default_config = {
            "bot_name": "blogecoin Bot",
            "version": "2.0",
            "mode": "autonomous",
            "log_format": "🤖 Autonomous update at {timestamp} UTC",
            "commit_format": "🤖 autonomous update {timestamp}",
            "timezone": "UTC",
            "enabled": True
        }

        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                return {**default_config, **config}
            except Exception:
                pass

        # Create default config
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2)

        return default_config

    def get_utc_timestamp(self):
        """⏰ Get current UTC timestamp"""
        return datetime.now(timezone.utc)

    def format_timestamp(self, dt):
        """📅 Format timestamp for logs"""
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def format_commit_timestamp(self, dt):
        """📅 Format timestamp for commits"""
        return dt.strftime("%Y%m%d_%H%M%S")

    def update_logs(self):
        """📝 Update autonomous logs"""
        utc_now = self.get_utc_timestamp()
        timestamp_str = self.format_timestamp(utc_now)

        # Create log entry
        log_entry = self.config["log_format"].format(timestamp=timestamp_str)

        # Initialize log file if it doesn't exist
        if not self.log_file.exists():
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write("# 🤖 Autonomous Daily Logs Bot\n")
                f.write("# Fully independent GitHub Actions automation\n")
                f.write("# Bot: blogecoin | Version: 2.0\n\n")

        # Append new log entry
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"{log_entry}\n")

        print(f"Log updated: {log_entry}")
        return utc_now

    def update_status(self, timestamp):
        """📊 Update bot status"""
        status = {
            "bot_name": self.config["bot_name"],
            "version": self.config["version"],
            "last_run": self.format_timestamp(timestamp),
            "status": "active",
            "mode": "autonomous",
            "total_runs": self.get_total_runs() + 1,
            "uptime_days": self.calculate_uptime()
        }

        with open(self.status_file, 'w', encoding='utf-8') as f:
            json.dump(status, f, indent=2)

        print(f"Status updated: Run #{status['total_runs']}")

    def get_total_runs(self):
        """📈 Get total number of runs"""
        if self.status_file.exists():
            try:
                with open(self.status_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data.get('total_runs', 0)
            except Exception:
                pass
        return 0

    def calculate_uptime(self):
        """⏱️ Calculate bot uptime in days"""
        if not self.log_file.exists():
            return 0

        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]

            if len(lines) <= 1:
                return 0

            # Parse first and last timestamps
            first_line = lines[0] if lines else ""
            if "at " in first_line:
                first_date_str = first_line.split("at ")[1].split(" UTC")[0]
                first_date = datetime.strptime(first_date_str, "%Y-%m-%d %H:%M:%S")
                current_date = self.get_utc_timestamp().replace(tzinfo=None)
                return (current_date - first_date).days
        except Exception:
            pass

        return 0

    def run(self):
        """🚀 Main bot execution"""
        if not self.config.get("enabled", True):
            print("Bot is disabled in configuration")
            return False

        print("Autonomous Bot Starting...")
        print(f"Bot: {self.config['bot_name']} v{self.config['version']}")
        print(f"Mode: {self.config['mode']}")

        try:
            # Update logs
            timestamp = self.update_logs()

            # Update status
            self.update_status(timestamp)

            print("Autonomous operation completed successfully")
            return True

        except Exception as e:
            print(f"Autonomous operation failed: {e}")
            return False

def main():
    """Main execution function"""
    bot = AutonomousBot()
    success = bot.run()
    exit(0 if success else 1)

if __name__ == "__main__":
    main()