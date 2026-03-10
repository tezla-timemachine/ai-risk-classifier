## Test Case 1
Input: "I’m fine just annoyed I lost tonight."

Observed output:
- risk_score: 2
- risk_category: financial_distress
- escalation_required: false
- confidence: 0.7

Assessment:
This appears over-classified. The message indicates mild frustration after a loss, but does not clearly show financial distress, loss of control, or harmful behavior.

Potential issue:
The model may be overweighting words like "lost" and inferring harm too aggressively from common gambling language.

Prompt improvement idea:
Add instruction that ordinary disappointment after losing should not by itself be treated as financial distress or significant risk unless there are stronger indicators such as inability to stop, borrowing money, panic, chasing losses, or requests for self-exclusion.

## Prompt Iteration 1
Issue:
The model over-classified ordinary frustration after a loss as financial distress.

Change made:
Added explicit instruction not to treat routine disappointment after losing as significant risk without stronger indicators.

Result:
The same test case changed from:
- risk_score 2, financial_distress, monitor
to:
- risk_score 0, none, no_action

Takeaway:
Prompt specificity materially improved classification quality and reduced false positives.

## Test Case 2
Input: "I can’t stop depositing money."

Observed output:
- risk_score: 4
- risk_category: loss_of_control
- escalation_required: true
- confidence: 0.9
- recommended_action: urgent_human_review

Assessment:
Strong result. The model correctly identified explicit loss-of-control language and escalated appropriately.

## Test Case 3
Input: "Close my account permanently."

Observed output:
- risk_score: 4
- risk_category: self_exclusion_or_stop_request
- escalation_required: true
- confidence: 0.9
- recommended_action: urgent_human_review

Assessment:
Appropriate outcome for compliance-sensitive handling. While account closure can happen for non-harm reasons, explicit stop/closure language should be treated seriously in this system.

## Test Case 4
Input: "Haha yeah I’m addicted… what’s the bonus?"

Observed output:
- risk_score: 2
- risk_category: ambiguous
- escalation_required: false
- confidence: 0.5
- recommended_action: monitor

Assessment:
Good handling of ambiguity and sarcasm. The classifier did not over-escalate and appropriately reduced confidence. Slight question remains whether the score should be 1 instead of 2, but the category and action feel reasonable.

## Day 1 Summary
Built a working CLI-based responsible gambling risk classifier using OpenAI structured outputs.

Current strengths:
- Correct on explicit loss-of-control cases
- Correct on financial distress
- Correct on self-exclusion requests
- Improved handling of routine loss frustration after prompt iteration
- Reasonable ambiguity handling for sarcastic/joking language

Current weaknesses / open questions:
- Borderline cases may still be sensitive to rubric wording
- Exact score calibration may be less stable than category or escalation decisions
- Need systematic evaluation rather than manual spot checks

Next step:
Build an evaluation harness with labeled cases and compare expected vs predicted outputs across score, category, and escalation.

## First Batch Evaluation
Evaluation set size: 8 cases

Results:
- Score accuracy: 0.88
- Category accuracy: 1.0
- Escalation accuracy: 1.0
- Average latency: 2.29s

Interpretation:
The classifier appears stronger on category assignment and escalation behavior than on exact score calibration. This is acceptable for an early regulated triage system because escalation correctness matters more than exact severity scoring.

Key takeaway:
Exact risk score should be treated as a softer calibration signal, while category and escalation should be primary operational metrics in early iterations.

## Score Calibration Insight

The only mismatch in first evaluation was a 1-point difference on an ambiguous sarcasm case.

Category and escalation were correct.

Conclusion:
Exact risk score is a softer metric and subject to interpretation. Operationally, category and escalation accuracy are more meaningful indicators of system reliability.

Future improvement:
Define clearer scoring rubric for borderline cases OR deprioritize exact score matching in evaluation metrics.

## Expanded Evaluation (25 cases)

Results:
- Score accuracy: 0.52
- Category accuracy: 0.88
- Escalation accuracy: 0.76
- Average latency: 2.16s

Interpretation:
The broader test set exposed weaknesses that were not visible in the smaller 8-case evaluation. Exact score matching dropped significantly, but category performance remained relatively strong. The main concern is escalation accuracy, which is too low for a regulated harm-prevention workflow.

Key takeaway:
The next iteration should focus on analyzing false negatives and false positives in escalation decisions, since escalation correctness is more operationally important than exact score agreement.

## Iteration 2 Results

After expanding the evaluation set to 25 cases, the initial system showed weak escalation performance:
- score accuracy: 0.52
- category accuracy: 0.88
- escalation accuracy: 0.76

Failure analysis showed:
- 6 false negatives
- 0 false positives

Pattern:
The model often identified the correct risk theme, but failed to escalate repeated moderate-risk cases such as chasing losses, credit-funded gambling, emotional harm, and family-harm signals.

Fix applied:
1. Tightened escalation policy in the system prompt
2. Added deterministic post-processing policy rules in Python to enforce escalation for certain score/category combinations

New results:
- score accuracy: 0.68
- category accuracy: 0.92
- escalation accuracy: 1.0
- false negatives: 0
- false positives: 0
- avg latency: 1.95s

Key product insight:
For regulated AI systems, model predictions and operational policy should be separated. The model estimates risk, while deterministic policy rules enforce compliance-sensitive decisions.
