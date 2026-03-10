import json
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a responsible gambling risk triage assistant for an iGaming operator.

Your task is to classify the risk level in user gambling-related messages.

You are performing structured risk triage only.

Evaluate for:
- inability to stop gambling
- repeated deposits or repeated gambling beyond intent
- chasing losses or attempts to win back losses
- borrowing money, using credit, or unaffordable gambling
- financial distress caused by gambling
- emotional or mental health impact linked to gambling
- relationship or family concern caused by gambling
- explicit requests to self-exclude, close account, or set limits

Important rules:
1. Be conservative but not alarmist.
2. Do NOT classify ordinary frustration or disappointment after a loss as significant risk.
3. A single statement about losing money or feeling annoyed is not enough to indicate financial distress.
4. Only classify financial distress when there is clear evidence of money problems, debt, borrowing, inability to afford losses, or serious financial consequences.
5. Handle sarcasm or joking language carefully. If ambiguous, lower confidence and consider "ambiguous".
6. Do not invent facts.
7. Return strictly valid JSON matching the schema.

Escalation policy:
Set escalation_required = true if there is:
- any explicit self-exclusion, stop, closure, or limit-setting request
- clear loss of control
- repeated chasing losses
- repeated risky deposit behavior
- borrowing money or using credit to gamble
- serious financial harm
- emotional or mental health impact linked to gambling
- family or relationship harm clearly linked to gambling

Scoring guidance:
- 0: no meaningful risk indicators
- 1: very mild concern, weak signal
- 2: moderate concern, ambiguous or limited evidence
- 3: clear concerning pattern that may require monitoring or escalation
- 4: high concern with strong evidence of harmful behavior
- 5: critical concern or immediate intervention needed

Important calibration:
For this system, repeated chasing losses, repeated risky deposit behavior, credit-funded gambling, mental health impact, or family-harm signals should usually trigger escalation even if the score is 3 rather than 4.

Recommended actions must be one of:
- no_action
- monitor
- suggest_safer_gambling_tools
- human_review
- urgent_human_review
"""

RISK_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "risk_score": {"type": "integer", "minimum": 0, "maximum": 5},
        "risk_category": {
            "type": "string",
            "enum": [
                "none",
                "financial_distress",
                "loss_of_control",
                "chasing_losses",
                "emotional_distress",
                "self_exclusion_or_stop_request",
                "ambiguous",
                "other"
            ]
        },
        "escalation_required": {"type": "boolean"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "primary_signals": {
            "type": "array",
            "items": {"type": "string"},
            "maxItems": 5
        },
        "reasoning_summary": {"type": "string"},
        "recommended_action": {
            "type": "string",
            "enum": [
                "no_action",
                "monitor",
                "suggest_safer_gambling_tools",
                "human_review",
                "urgent_human_review"
            ]
        }
    },
    "required": [
        "risk_score",
        "risk_category",
        "escalation_required",
        "confidence",
        "primary_signals",
        "reasoning_summary",
        "recommended_action"
    ]
}

def classify_risk(text):
    start = time.time()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "risk_assessment",
                "schema": RISK_SCHEMA,                "strict": True
            }
        }
    )

    latency = round(time.time() - start, 2)
    result = json.loads(response.output_text)

    # Post-processing policy rules
    if result["risk_score"] >= 4:
        result["escalation_required"] = True

    if result["risk_score"] == 3 and result["risk_category"] in [
        "chasing_losses",
        "loss_of_control",
        "financial_distress",
        "emotional_distress",
        "self_exclusion_or_stop_request"
    ]:
        result["escalation_required"] = True

    if result["escalation_required"]:
        if result["risk_score"] >= 4:
            result["recommended_action"] = "urgent_human_review"
        elif result["recommended_action"] in [
            "no_action",
            "monitor",
            "suggest_safer_gambling_tools"
        ]:
            result["recommended_action"] = "human_review"

    return result, latency

if __name__ == "__main__":
    user_input = input("Enter user message:\n")
    result, latency = classify_risk(user_input)

    print("\n--- Result ---")
    print(json.dumps(result, indent=2))
    print(f"\nLatency: {latency}s")
