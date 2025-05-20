# 🎬 Telegram Remote Bot

Turn your **smartphone into a remote control** for your laptop — perfect for watching movies on your TV via HDMI.

This bot gives you a universal "sofa controller" using Telegram. Control playback, volume, and navigation from anywhere in the room, without touching your keyboard.

---

## ✅ Features

- ⏸ Pause and resume playback
- ⏪ Rewind back
- ⏩ Fast-forward
- 🔉 Decrease volume
- 🔊 Increase volume

All through simple Telegram commands — just type them, and your laptop responds instantly.

---

## 📱 Usage

1. Launch the bot in Telegram (on your phone).
2. Send any of the supported commands (see below).
3. Enjoy full control of your laptop while relaxing on the couch.

---

## 🛋️ Why Use It?

Watching movies with your laptop connected to your TV via HDMI?  
This bot lets you:

- Pause/play without reaching for the keyboard
- Adjust volume easily
- Skip scenes with a tap on your phone
- Stay comfortable — no need to get up

---

## 💬 Supported Commands

| Command         | Action                         |
|-----------------|--------------------------------|
| `/pause` or `pause` | ⏸ Pause or resume playback   |
| `<-`            | ⏪ Rewind 5–10 seconds backward |
| `->`            | ⏩ Skip 5–10 seconds forward    |
| `quiet`         | 🔉 Lower the system volume      |
| `loud`          | 🔊 Raise the system volume      |

---

## ⚙️ Requirements

- Python 3.10+
- Telegram Bot API token
- Required libraries:
  - `pyTelegramBotAPI` (aka `telebot`)
  - `keyboard`
  - `pyautogui`
- Windows system with permissions to emulate keypresses

---

## 🚀 Getting Started

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
