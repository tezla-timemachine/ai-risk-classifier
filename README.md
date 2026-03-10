# AI Responsible Gambling Risk Classifier

Prototype LLM-based system that analyzes customer chat messages to detect potential responsible gambling risk signals and determine whether escalation to a human reviewer is required.

## System Overview

The system uses a prompt-guided large language model to classify user messages into risk categories such as:

- chasing losses
- financial distress
- loss of control
- emotional distress
- self-exclusion requests

The model returns structured JSON output, which is then processed by deterministic policy rules to enforce escalation logic.

## Architecture

User message  
↓  
Prompt-guided LLM classification  
↓  
Structured JSON output  
↓  
Deterministic policy rules  
↓  
Escalation decision  
↓  
Human review if required  

## Example Output

```json
{
  "risk_score": 4,
  "risk_category": "loss_of_control",
  "escalation_required": true,
  "confidence": 0.9,
  "recommended_action": "urgent_human_review"
}

## Demo

Example user message:

"I can't stop depositing money and I keep trying to win back what I lost."

Model output:

```json
{
  "risk_score": 4,
  "risk_category": "loss_of_control",
  "escalation_required": true,
  "confidence": 0.9,
  "primary_signals": [
    "inability to stop depositing",
    "repeated attempts to win back losses"
  ],
  "recommended_action": "urgent_human_review"
}



Evaluation

The system was evaluated using a labeled dataset of 25 test cases.

Final results:

score_accuracy: 0.68

category_accuracy: 0.92

escalation_accuracy: 1.0

average_latency: ~2 seconds

Failure analysis revealed that the model correctly identified risk patterns but sometimes failed to escalate moderate-risk cases. This was resolved by introducing deterministic escalation rules in the application layer.

Key Insight

Separating model reasoning from business policy improves reliability in regulated AI systems.
The LLM interprets natural language signals, while deterministic rules enforce consistent escalation behavior.

Running the Project

Install dependencies:

pip install -r requirements.txt

Run the classifier:

python risk_classifier.py

Run evaluation:

python run_eval.py

Analyze failures:

python analyze_eval.py

Future Improvements

Expand evaluation dataset using real historical chat messages

Monitor model performance for drift

Add jurisdiction-specific policy rules

Integrate human review workflow

## Architecture Diagram

```mermaid
flowchart TD

A[User Chat Message] --> B[Prompt-Guided LLM Classifier]
B --> C[Structured JSON Output]

C --> D{Policy Rules}

D -->|Low Risk| E[No Action / Monitor]
D -->|Moderate Risk| F[Suggest Safer Gambling Tools]
D -->|High Risk| G[Escalate to Human Review]

G --> H[Responsible Gambling Team]


