import sys, os; sys.path.insert(0, "src/backend")
from agent_core import agent_turn
print(agent_turn("coordinator", "discover niche + score 5 candidates"))
