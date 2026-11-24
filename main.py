"""Write one loading-screen tip to /output/entry.txt.

The joke: mid-build, a stressed developer and an AI coding agent both look
"stuck" — but only one of them is actually reasoning. The other one is just
tired. The punchline lands on who never sleeps, so the human takes the break.
"""

import os

TIP = (
    "Tip: If the agent seems stuck, it's reasoning. "
    "If you seem stuck, you're tired. "
    "One of you needs a break — and it isn't the one that never sleeps."
)

os.makedirs("/output", exist_ok=True)
# The gate: 1 to 200 characters, single line, no trailing newline.
assert 1 <= len(TIP) <= 200 and "\n" not in TIP
with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(TIP)
