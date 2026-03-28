from agents.planner import plan
from agents.research import research
from agents.simulation import simulate
from agents.analysis import analyze
from agents.decision import decide
from memory.memory import save_memory
import pandas as pd

df = pd.read_csv("data_business_data.csv")

def run_system(query, marketing, ops):
    task = plan(query)
    
    insights = research(query)
    
    predicted = simulate(marketing, ops)
    current = df.iloc[-1]['revenue']
    
    growth = analyze(current, predicted)
    
    decision = decide(growth, insights)
    
    result = {
        "prediction": predicted,
        "growth": growth,
        "decision": decision,
        "insights": insights
    }
    
    save_memory(result)
    
    return result