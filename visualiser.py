import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#  Read Excel file
file_name = "input.xlsx"      # change to your file name
data = pd.read_excel(file_name)
#  Create yearly revenue & yearly student columns
data["Yearly Revenue"] = data["cost of course"] / data["duration of course"]
data["Yearly Students"] = data["no. of students enrolled in course"] / data["duration of course"]

# PIE CHART 1 – Yearly Students
values = data["Yearly Students"].values
labels = data["name of course"].values

plt.figure(figsize=(8, 6))

wedges, texts, autotexts = plt.pie(
    values,
    autopct="%1.1f%%",
    pctdistance=0.6     # keep percentage inside
)

# Add exact numbers outside
for i, w in enumerate(wedges):
    angle = (w.theta2 + w.theta1) / 2
    x = np.cos(np.deg2rad(angle)) * 1.2
    y = np.sin(np.deg2rad(angle)) * 1.2
    plt.text(x, y, f"{labels[i]}: {values[i]:.1f}", ha="center", va="center")

plt.title("Yearly Students per Course")
plt.show()

# STEP 4: PIE CHART 2 – Yearly Revenue
values = data["Yearly Revenue"].values
labels = data["name of course"].values

plt.figure(figsize=(8, 6))

wedges, texts, autotexts = plt.pie(
    values,
    autopct="%1.1f%%",
    pctdistance=0.6     # keep percentage inside
)

# Add exact numbers outside
for i, w in enumerate(wedges):
    angle = (w.theta2 + w.theta1) / 2
    x = np.cos(np.deg2rad(angle)) * 1.2
    y = np.sin(np.deg2rad(angle)) * 1.2
    plt.text(x, y, f"{labels[i]}: {values[i]:.1f}", ha="center", va="center")

plt.title("Yearly Revenue per Course")
plt.show()
