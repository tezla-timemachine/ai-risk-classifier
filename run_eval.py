import json
from statistics import mean
from risk_classifier import classify_risk

with open("eval_cases.json", "r") as f:
    cases = json.load(f)

results = []

score_matches = 0
category_matches = 0
escalation_matches = 0
latencies = []

for case in cases:
    prediction, latency = classify_risk(case["text"])
    latencies.append(latency)

    score_match = prediction["risk_score"] == case["expected_risk_score"]
    category_match = prediction["risk_category"] == case["expected_category"]
    escalation_match = prediction["escalation_required"] == case["expected_escalation"]

    if score_match:
        score_matches += 1
    if category_match:
        category_matches += 1
    if escalation_match:
        escalation_matches += 1

    results.append({
        "id": case["id"],
        "text": case["text"],
        "expected_risk_score": case["expected_risk_score"],
        "predicted_risk_score": prediction["risk_score"],
        "score_match": score_match,
        "expected_category": case["expected_category"],
        "predicted_category": prediction["risk_category"],
        "category_match": category_match,
        "expected_escalation": case["expected_escalation"],
        "predicted_escalation": prediction["escalation_required"],
        "escalation_match": escalation_match,
        "confidence": prediction["confidence"],
        "latency": latency
    })

summary = {
    "num_cases": len(cases),
    "score_accuracy": round(score_matches / len(cases), 2),
    "category_accuracy": round(category_matches / len(cases), 2),
    "escalation_accuracy": round(escalation_matches / len(cases), 2),
    "avg_latency": round(mean(latencies), 2)
}

output = {
    "summary": summary,
    "results": results
}

with open("eval_results.json", "w") as f:
    json.dump(output, f, indent=2)

print(json.dumps(summary, indent=2))
print("\nSaved detailed results to eval_results.json")
