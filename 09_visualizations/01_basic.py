import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from chart_config import setup
from merged_loader import load_merged

setup()
df = load_merged()

one = df[df["code"] == "G0001"].sort_values("date")

fig, ax = plt.subplot(figsize=(12,4))

ax.plot(one['date'], one['close'])

ax.set_title("가온전자 주가 추이")