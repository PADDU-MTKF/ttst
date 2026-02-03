# 📡 Telegram Channel Post Triggered Request Bot

A **Python automation script** that monitors a **Telegram channel** for new posts and automatically triggers a **sequence of HTTP POST requests** based on the detected post.

This project is designed for **event-driven automation**, where actions start immediately when a new Telegram channel post is published.

---

## 🚀 What This Script Does

- Continuously monitors a **Telegram channel** using the Bot API
- Detects **new channel posts**
- Builds a Telegram post link dynamically
- Triggers a **predefined sequence of API requests**
- Sends requests in **phases with controlled delays**
- Runs request execution in a **separate thread**
- Supports **test mode** and **production mode**

---

## 🧠 How It Works

1. The script polls Telegram’s `getUpdates` API
2. Tracks the last `update_id` to avoid duplicate processing
3. When a **new channel post** is detected:
   - Extracts the `message_id`
   - Builds the post URL
   - Starts a background thread
4. The background thread:
   - Sends multiple POST requests
   - Uses varying quantities
   - Applies time delays between batches
5. Logs total requests sent, quantity used, and time taken

---

> Raw Early Stage Project But Functional


