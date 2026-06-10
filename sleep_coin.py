import tkinter as tk
import random
from datetime import datetime

# ---------- Theme ----------
BG = "#1a1a2e"
CARD = "#16213e"
GOLD = "#ffd166"
TEXT = "#e8e8e8"
MUTED = "#8a8aa3"
SLEEP_COLOR = "#7f9cf5"
GAME_COLOR = "#5eead4"

window = tk.Tk()
window.title("Sleep Coin 3000")
window.geometry("420x460")
window.configure(bg=BG)
window.resizable(False, False)

sleep_count = 0
game_count = 0
energy_count = 0

title = tk.Label(
    window,
    text="Sleep Coin 3000",
    font=("Segoe UI", 20, "bold"),
    bg=BG,
    fg=GOLD
)
title.pack(pady=(25, 0))

subtitle = tk.Label(
    window,
    text="The only honest coin on the market",
    font=("Segoe UI", 10, "italic"),
    bg=BG,
    fg=MUTED
)
subtitle.pack(pady=(0, 15))

coin_label = tk.Label(
    window,
    text="⚪",
    font=("Segoe UI Emoji", 60),
    bg=BG,
    fg=GOLD
)
coin_label.pack()

result_label = tk.Label(
    window,
    text="Result: ???",
    font=("Segoe UI", 13, "bold"),
    bg=BG,
    fg=TEXT
)
result_label.pack(pady=(10, 5))

stats_label = tk.Label(
    window,
    text=f"😴 {sleep_count}   🎮 {game_count}   ☕ {energy_count}",
    font=("Segoe UI", 11),
    bg=CARD,
    fg=TEXT,
    padx=15,
    pady=8
)
stats_label.pack(pady=5)

achievement_label = tk.Label(
    window,
    text="",
    font=("Segoe UI", 12, "bold"),
    bg=BG,
    fg=GOLD
)
achievement_label.pack(pady=10)


def flip_coin():
    button.config(state="disabled")
    coin_label.config(fg=GOLD)
    result_label.config(text="Flipping...", fg=MUTED)
    achievement_label.config(text="")

    # Spin animation
    frames = ["⚪", "🟡", "⚫", "🟡", "⚪", "🟡", "⚫", "🟡"]
    for i, frame in enumerate(frames):
        window.after(80 * (i + 1), lambda f=frame: coin_label.config(text=f))

    window.after(80 * (len(frames) + 2), show_result)


def show_result():
    global sleep_count
    global game_count
    global energy_count

    hour = datetime.now().hour

    if 0 <= hour < 2:
        choices = ["sleep"] * 90 + ["game"] * 10
        achievement_label.config(text="😴 The council is becoming concerned.")

    elif 2 <= hour < 8:
        choices = ["sleep"] * 99 + ["game"]

        if 3 <= hour < 6:
            achievement_label.config(text="🏆 What Are You Even Doing?")
        elif 6 <= hour < 8:
            achievement_label.config(text="🏆 Congratulations, You Reached Morning")
        else:
            achievement_label.config(text="😴 Sleep is strongly recommended.")

    else:
        choices = ["game", "energy"]
        achievement_label.config(text="🌞 Daytime mode: choose your destiny.")

    result = random.choice(choices)

    if result == "sleep":
        coin_label.config(text="😴", fg=SLEEP_COLOR)
        result_label.config(text="😴 Go To Sleep", fg=SLEEP_COLOR)
        sleep_count += 1

    elif result == "game":
        coin_label.config(text="🎮", fg=GAME_COLOR)
        result_label.config(text="🎮 One More Game", fg=GAME_COLOR)
        game_count += 1

    elif result == "energy":
        coin_label.config(text="☕", fg=GOLD)
        result_label.config(text="☕ You Need Energy", fg=GOLD)
        achievement_label.config(text="E = coffee * milk²")
        energy_count += 1

    stats_label.config(
        text=f"😴 {sleep_count}   🎮 {game_count}   ☕ {energy_count}"
    )

    button.config(state="normal")


button = tk.Button(
    window,
    text="FLIP THE COIN",
    command=flip_coin,
    font=("Segoe UI", 12, "bold"),
    bg=GOLD,
    fg=BG,
    activebackground="#ffc233",
    activeforeground=BG,
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2"
)
button.pack(pady=20)

footer = tk.Label(
    window,
    text="Results are 100% scientific. Probably.",
    font=("Segoe UI", 9),
    bg=BG,
    fg=MUTED
)
footer.pack(side="bottom", pady=10)

window.mainloop()