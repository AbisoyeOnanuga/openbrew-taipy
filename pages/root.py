from taipy.gui import Markdown
import numpy as np
from .data.data import fetch_data

data = fetch_data()

selector_location = list(np.sort(data['Name'].astype(str).unique()))
selected_location  = '(405) Brewing Co'

root = Markdown("pages/root.md")
