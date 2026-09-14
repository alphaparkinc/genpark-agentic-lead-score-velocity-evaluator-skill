import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgenticLeadScoreVelocityEvaluatorClient

def main():
    client = AgenticLeadScoreVelocityEvaluatorClient()
    res = client.evaluate_lead_score()
    print("=== Agentic Lead Score Velocity Evaluator Output ===")
    print(f"Intent Score: {res['total_intent_score']}/100 | Stage: {res['funnel_stage']}")
    print(f"Conversion Probability: {res['conversion_probability_pct']}%")
    print(f"Next Best Action: {res['next_best_action']}")
    print(f"Urgency: {res['urgency_level']}")

if __name__ == '__main__':
    main()
