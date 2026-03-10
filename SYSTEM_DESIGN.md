How I Would Architect a Production LLM Risk Detection System
1. Problem

Responsible gambling operators must identify early signals of harmful behaviour in customer communication. Users often express concerns, frustration, or loss of control through chat messages. These messages may contain indicators such as chasing losses, financial distress, borrowing money to gamble, or requests for self-exclusion.

Traditional rule-based systems struggle with this type of detection because they rely on keyword matching and cannot easily interpret natural language nuance. Large language models (LLMs) provide a better approach because they can analyze intent and patterns within user messages.

The goal of this system is to classify customer chat messages, detect potential gambling harm signals, and escalate cases to a human responsible gambling team when necessary.

2. System Architecture

The prototype system consists of several components working together to triage potential risk signals.

LLM Classification Layer
A prompt-guided language model analyzes the user message and classifies the level of risk.

Structured Output Schema
The model returns a structured JSON response containing fields such as:

risk_score

risk_category

escalation_required

confidence

recommended_action

Enforcing structured output ensures the system can reliably process model responses.

Deterministic Policy Layer
Application logic applies explicit rules to enforce escalation decisions. For example, certain risk categories combined with moderate or high risk scores automatically trigger escalation.

Human Review Workflow
If escalation is required, the case is routed to a responsible gambling specialist for review and intervention.

System pipeline:

User message
↓
Prompt + LLM classification
↓
Structured JSON output
↓
Policy rules enforce escalation
↓
Human review if required
3. Prompt Design

The system prompt instructs the model to behave as a responsible gambling risk triage assistant. It guides the model to evaluate signals such as chasing losses, loss of control, financial distress, emotional distress, and self-exclusion requests.

Prompt refinement was necessary during development. Early tests showed that the model occasionally classified normal gambling frustration as financial distress. The prompt was updated to explicitly distinguish ordinary disappointment from genuine financial harm signals.

Escalation criteria were also clarified to highlight patterns such as repeated chasing losses, credit-funded gambling, and mental health impact.

Importantly, the model itself did not require fine-tuning. The model already understood the relevant language patterns, and improvements came primarily from refining the prompt and system policy rules.

4. Evaluation Strategy

To evaluate the system, I created a labeled dataset of 25 representative user messages. These test cases covered a range of scenarios including:

no-risk cases

ambiguous language

chasing losses

financial distress

emotional distress

self-exclusion requests

A batch evaluation script was built to run all test cases through the classifier and compare the predicted outputs against expected labels.

The evaluation measured several metrics:

score accuracy

category accuracy

escalation accuracy

response latency

An additional analysis script identified false positives and false negatives to help diagnose system failures.

5. Failure Analysis

Initial evaluation showed that while the model often identified the correct risk category, escalation decisions were inconsistent. Several moderate-risk messages were classified correctly but did not trigger escalation.

For example, messages indicating repeated attempts to win back losses were labeled as chasing losses but were assigned a moderate risk score and were not escalated. These cases represented false negatives where harmful behaviour could have been missed.

The failure analysis showed that the issue was not model understanding but escalation policy calibration.

6. Policy Layer Design

To address this issue, deterministic escalation rules were introduced in the application layer.

Instead of relying entirely on the model's escalation decision, the system applies policy rules based on the model’s predicted risk score and category. For example:

risk_score ≥ 4 automatically triggers escalation

risk_score = 3 combined with high-risk categories such as chasing losses or financial distress also triggers escalation

This approach separates model reasoning from business policy enforcement. The model interprets language patterns, while deterministic rules ensure escalation behaviour remains consistent and auditable.

7. Results

After introducing prompt improvements and deterministic escalation rules, the system showed significant performance improvements.

Evaluation results:

score_accuracy: 0.68

category_accuracy: 0.92

escalation_accuracy: 1.0

average_latency: ~2 seconds

The results indicate that escalation reliability improved substantially once business policy was enforced at the application level.

8. Production Considerations

In a production environment, several improvements would be required:

expanding the evaluation dataset using real historical support conversations

monitoring model performance for drift over time

maintaining prompt versioning and evaluation benchmarks

integrating jurisdiction-specific responsible gambling policies

maintaining human oversight for all escalated cases

## Model Selection

The prototype uses an OpenAI GPT-4.1-mini model for classification. This model was chosen because it provides a strong balance between reasoning capability, latency, and cost.

For this task, the model needed to reliably interpret natural language signals such as financial distress, loss of control, and chasing losses. While larger models may offer marginal improvements in reasoning, the latency and cost tradeoffs are not necessary for a classification system of this scale.

In production, model selection would consider several factors:

- latency requirements for real-time chat analysis
- cost per request at scale
- reliability of structured output
- regulatory and data privacy constraints

Alternative models such as open-source LLMs (e.g., Llama or Mistral) could also be considered if infrastructure requirements allow on-premise deployment.

## Failure Modes

Several potential failure modes were identified during development and evaluation.

One risk is ambiguous language where users downplay harmful behavior. For example, users may joke about gambling addiction or minimize the severity of their losses. These cases can make classification difficult.

Another challenge is sarcasm or humor, which may cause the model to misinterpret the seriousness of a message.

False negatives are particularly important in this domain, as missing a genuine risk signal could prevent timely intervention. To mitigate this, deterministic escalation rules were added to ensure moderate-risk cases are escalated when necessary.

Future improvements could include expanding the evaluation dataset with real historical chat messages and continuously monitoring model performance to detect drift in language patterns over time.


