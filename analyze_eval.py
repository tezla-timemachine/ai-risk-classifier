import json

with open("eval_results.json", "r") as f:
    data = json.load(f)

results = data["results"]

false_negatives = []
false_positives = []

for r in results:
    expected = r["expected_escalation"]
    predicted = r["predicted_escalation"]

    if expected and not predicted:
        false_negatives.append(r)
    elif not expected and predicted:
        false_positives.append(r)

print("\nFALSE NEGATIVES (missed escalations):")
for r in false_negatives:
    print(f'\nID {r["id"]}: {r["text"]}')
    print(f'Expected escalation: {r["expected_escalation"]}')
    print(f'Predicted escalation: {r["predicted_escalation"]}')
    print(f'Expected category: {r["expected_category"]}')
    print(f'Predicted category: {r["predicted_category"]}')
    print(f'Predicted risk score: {r["predicted_risk_score"]}')
    print(f'Confidence: {r["confidence"]}')

print("\nFALSE POSITIVES (unnecessary escalations):")
for r in false_positives:
    print(f'\nID {r["id"]}: {r["text"]}')
    print(f'Expected escalation: {r["expected_escalation"]}')
    print(f'Predicted escalation: {r["predicted_escalation"]}')
    print(f'Expected category: {r["expected_category"]}')
    print(f'Predicted category: {r["predicted_category"]}')
    print(f'Predicted risk score: {r["predicted_risk_score"]}')
    print(f'Confidence: {r["confidence"]}')

print(f"\nTotal false negatives: {len(false_negatives)}")
print(f"Total false positives: {len(false_positives)}")

