PRD Title: AI-Assisted Responsible Gambling Risk Detection
Author: Terence Field
Team: [TBC]



PM Epic: [Insert link to Project Management tool epic (on JIRA or similar tool)]
Status of PRD: Backlog































Overview
Online gambling operators process a significant volume of customer support interactions each day. Within these conversations, players may express frustration, financial stress, or other signals that could indicate harmful gambling behaviour. Identifying these signals early is important for protecting players, meeting regulatory obligations, and enabling timely intervention by responsible gambling teams.
This proposal outlines the development of an AI-assisted risk detection system that analyses customer chat messages in real time and highlights conversations that may indicate potential gambling harm. The system is intended to support responsible gambling specialists by triaging large volumes of messages and prioritising those that may require human review.
The objective is not to automate decisions or replace human judgement. Instead, the system acts as an early warning mechanism, helping teams identify potential issues more quickly and consistently. By improving the speed and reliability of risk detection, the platform can better support player wellbeing while maintaining compliance with regulatory standards.

































Problem
Customer support teams handle a high volume of conversations with players each day. Within these interactions, players may express concerns, frustration, or behaviours that could indicate the early stages of harmful gambling. These signals are often subtle and expressed in natural language, making them difficult to detect consistently through manual review alone.
Currently, the identification of responsible gambling risks within chat conversations relies largely on individual agents recognising potential warning signs and escalating them appropriately. This process can be inconsistent and depends heavily on the experience and judgement of the agent handling the conversation. As a result, early indicators of harmful behaviour may be missed or identified too late for timely intervention.
This creates both operational and regulatory challenges. From a player protection perspective, delayed detection reduces the ability to intervene early and support vulnerable players. From a compliance standpoint, operators are expected to actively monitor and respond to indicators of gambling harm. Failing to identify and escalate these signals in a timely manner can expose the business to regulatory scrutiny and reputational risk.
A scalable and consistent method of identifying potential risk signals within customer conversations is therefore required to support responsible gambling teams and improve early detection of harmful behaviour.












Objectives
Objective 1 — Improve early detection of gambling risk signals Develop a system capable of identifying potential indicators of harmful gambling behaviour within customer chat messages in a consistent and scalable manner. Success would mean that responsible gambling teams are able to detect risk signals earlier and with greater reliability than through manual review alone.
Objective 2 — Support responsible gambling teams through intelligent triage Provide responsible gambling specialists with a tool that prioritises conversations which may require attention, allowing them to focus their efforts on the highest-risk cases. Success would be measured by improved efficiency in reviewing conversations and a reduction in the likelihood that genuine risk cases are missed.
Objective 3 — Strengthen regulatory compliance and player protection Enhance the operator’s ability to demonstrate proactive monitoring of potential gambling harm indicators within customer interactions. Success would mean improved oversight of player communications, stronger evidence of responsible gambling practices, and better protection for vulnerable players.












Constraints
Constraint 1 — Accuracy and risk of misclassification Natural language within customer conversations can be ambiguous, sarcastic, or emotionally charged, making it difficult to interpret intent with complete certainty. The system must balance identifying genuine risk signals with avoiding excessive false positives that could create unnecessary interventions. As a result, the solution must operate as a triage tool rather than a fully autonomous decision-maker, with all escalations reviewed by a human specialist.
Constraint 2 — Operational capacity of responsible gambling teams Any increase in escalated cases must remain manageable for the responsible gambling operations team. If the system flags too many conversations unnecessarily, it could overwhelm teams and reduce their ability to focus on genuinely high-risk situations. The design must therefore prioritise accuracy and appropriate thresholds to ensure escalations remain operationally sustainable.
Constraint 3 — Data privacy, regulatory, and technical limitations Customer communications are sensitive and subject to strict data protection and regulatory requirements. The system must comply with applicable data privacy standards and internal governance policies. Additionally, integration with existing customer support platforms and internal systems may introduce technical constraints that influence how quickly the system can be deployed and scaled.

















Persona
Who are the target personas for this product, and which is the key persona?





Use Cases
Scenario 1 — Responsible Gambling Specialist reviews escalated conversation
A player contacts customer support and mentions that they have been trying to win back money they lost earlier in the day. The AI system analyses the message in real time and flags the conversation as a potential “chasing losses” signal. The case is escalated to the Responsible Gambling Specialist queue, where a specialist reviews the conversation and determines whether intervention or safer gambling tools should be offered.

Scenario 2 — Customer Support Agent receives a risk alert during a live conversation
During a live chat session, a player tells a support agent that they have deposited several times and are struggling to stop playing. The system analyses the message and alerts the agent that the conversation contains potential indicators of loss of control. The agent is prompted to escalate the case for responsible gambling review and follow internal guidance on handling vulnerable players.

Scenario 3 — Responsible Gambling Specialist prioritises cases in a queue
The Responsible Gambling team logs into their review dashboard and sees a list of conversations flagged by the system. Each case includes a risk category and severity score. The specialist uses this information to prioritise reviewing higher-risk cases first, ensuring that the most concerning situations are handled promptly.

Scenario 4 — Customer Support Agent unknowingly receives a high-risk message
A player sends a message expressing frustration after losing money but does not explicitly ask for help. The agent initially interprets it as a general complaint. The AI system detects financial distress signals in the language and flags the conversation for review, helping ensure potential harm signals are not missed.

Scenario 5 — Responsible Gambling Specialist investigates repeated risk signals
The system detects multiple conversations from the same player over a short period that contain potential harm indicators. These conversations are grouped together and surfaced to the Responsible Gambling Specialist, enabling them to identify a pattern of behaviour that may require intervention.

Scenario 6 — Compliance team reviews system performance
Compliance staff review reports generated by the system to understand how many conversations have been analysed, how many have been escalated, and what categories of risk have been detected. These insights help demonstrate that the operator is proactively monitoring player communications for responsible gambling signals.

Scenario 7 — Responsible Gambling Specialist reviews self-exclusion request
A player contacts support asking to close their account permanently because they feel their gambling is becoming a problem. The system immediately categorises the message as a self-exclusion request and flags it as a high-priority case. The specialist reviews the request and initiates the appropriate self-exclusion process.

Scenario 8 — Customer Support Agent receives assistance identifying subtle risk language
A player casually mentions they have “spent more than they should have this month.” The agent may not immediately recognise this as a potential financial distress signal. The system highlights the message as a moderate risk indicator, prompting the agent to escalate the conversation for further review.

Scenario 9 — Responsible Gambling team identifies emerging behaviour trends
Over time, aggregated system insights reveal that a growing number of players are expressing frustration related to repeated losses in chat conversations. Responsible Gambling teams can use these insights to monitor behavioural trends and review whether additional player protection measures are required.

Scenario 10 — Operations team monitors escalation volume
Operations managers monitor the number of conversations flagged by the system to ensure escalation levels remain manageable for the Responsible Gambling team. If escalation rates increase unexpectedly, thresholds or prompts can be adjusted to maintain operational balance.

Scenario 11 — Compliance audit scenario
During a regulatory audit, the operator is asked to demonstrate how it proactively identifies potential gambling harm signals within customer communications. The system provides a clear audit trail showing how conversations are analysed, categorised, and escalated for human review.

Scenario 12 — Responsible Gambling Specialist reviews ambiguous cases
Some conversations contain language that may indicate mild frustration but not clear harm. These cases are flagged as moderate risk and surfaced to specialists for review, allowing them to apply professional judgement before determining whether further action is necessary.

Scenario 13 — Customer Support Agent receives guidance during sensitive conversations
When a conversation is flagged as a potential responsible gambling case, the system can prompt the agent to follow internal guidance on handling vulnerable players. This helps ensure that agents respond appropriately and consistently when dealing with sensitive situations.

Scenario 14 — Platform monitors conversations at scale
Thousands of customer chat messages are processed daily. The system automatically analyses each message for risk signals, enabling the operator to monitor player communications at a scale that would not be feasible through manual review alone.

Scenario 15 — Responsible Gambling team improves intervention timing
By identifying potential harm signals earlier in conversations, the system enables the Responsible Gambling team to intervene sooner. Earlier intervention can help provide support to players before harmful behaviour escalates further.












User Stories / Features / Requirements
The following user stories describe how different personas will interact with the system and what functionality is required to support their workflows.

User Story 1 — Responsible Gambling Specialist Reviews Escalated Case
As a Responsible Gambling Specialist I want to see a queue of conversations that have been flagged as potential risk cases So that I can prioritise and review the most concerning player interactions quickly.
Requirements
The system must generate a prioritised queue of flagged conversations.
Each case must display the detected risk category and risk score.
Specialists must be able to open a case and review the full conversation context.
The system must record when a case has been reviewed and by whom.
Acceptance Criteria
Flagged conversations appear in a review queue within the Responsible Gambling dashboard.
Each case clearly displays the associated risk score and risk category.
Selecting a case opens the full chat conversation and message history.
The system records the reviewer and timestamp when a case is marked as reviewed.

User Story 2 — Customer Support Agent Receives Risk Signal During Chat
As a Customer Support Agent I want to be alerted when a conversation may contain responsible gambling risk signals So that I can escalate the case appropriately and follow internal guidance.
Requirements
The system must analyse chat messages in near real time.
If risk signals are detected, the system must notify the agent or automatically flag the conversation for specialist review.
The system must provide guidance on escalation procedures where appropriate.
Acceptance Criteria
Chat messages are analysed automatically as they are received.
When risk signals are detected, the conversation is flagged within the support system.
The system indicates that escalation to the Responsible Gambling team is required.
The flagged conversation becomes visible within the Responsible Gambling review queue.

User Story 3 — Responsible Gambling Specialist Understands Why a Case Was Flagged
As a Responsible Gambling Specialist I want to understand the reason a conversation was flagged So that I can make informed decisions when reviewing cases.
Requirements
The system must display the detected risk signals for each flagged case.
Risk categories must be clearly labelled (e.g., financial distress, chasing losses, loss of control).
The system must provide a short explanation or summary of the detected signals.
Acceptance Criteria
Each flagged conversation includes a visible risk category label.
Detected signals are listed within the case details view.
The system provides a short reasoning summary explaining why the case was flagged.

User Story 4 — Compliance Team Reviews Monitoring Activity
As a Compliance or Risk Manager I want to view reports on how many conversations were analysed and escalated So that I can demonstrate that responsible gambling monitoring processes are in place.
Requirements
The system must record the total number of messages analysed.
The system must track escalation rates and risk category distributions.
Reports must be exportable for audit or regulatory review.
Acceptance Criteria
Analytics dashboards display the number of conversations analysed over a defined period.
Escalation rates and risk categories are summarised in reporting dashboards.
Reports can be exported for compliance review or audit purposes.

User Story 5 — Responsible Gambling Specialist Reviews Self-Exclusion Requests
As a Responsible Gambling Specialist I want to quickly identify conversations that include self-exclusion requests So that I can prioritise urgent cases and apply the correct procedures.
Requirements
The system must detect self-exclusion language within chat messages.
Self-exclusion cases must be prioritised within the escalation queue.
The system must clearly label these cases as high priority.
Acceptance Criteria
Messages containing self-exclusion requests are classified as high-risk cases.
Self-exclusion conversations appear at the top of the escalation queue.
The case is clearly labelled as a self-exclusion request.

User Story 6 — Operations Team Monitors System Performance
As an Operations Manager I want to monitor how many cases the system escalates So that I can ensure the Responsible Gambling team is not overwhelmed by unnecessary cases.
Requirements
The system must track escalation volumes over time.
Escalation rates must be visible through reporting dashboards.
Alerts should be generated if escalation rates increase unexpectedly.
Acceptance Criteria
Escalation metrics are visible within an operational dashboard.
Historical escalation trends can be viewed across defined time periods.
Alerts are triggered if escalation rates exceed predefined thresholds.

User Story 7 — Engineering Team Maintains System Reliability
As an Engineering Team Member I want to monitor system performance and latency So that the system can process chat messages reliably without impacting customer support systems.
Requirements
The system must log processing latency for chat analysis.
System errors must be recorded and monitored.
The system must operate reliably at expected message volumes.
Acceptance Criteria
Processing latency is recorded for each analysed message.
System error logs are generated and accessible to engineering teams.
The system maintains stable performance under expected message load.

These user stories define the core behaviours required for the system to support Responsible Gambling teams, Customer Support Agents, Compliance teams, and Engineering stakeholders.








Features In
Feature 1 — Real-Time Chat Risk Detection
This feature enables the system to analyse customer chat messages in real time and identify language that may indicate harmful gambling behaviour. Messages will be evaluated for signals such as financial distress, chasing losses, loss of control, and self-exclusion requests.
The goal of this feature is to support early identification of potential harm signals within customer conversations. By analysing messages automatically, the platform can monitor large volumes of interactions consistently and surface conversations that may require closer review.
Scope includes analysing incoming messages, assigning a risk score and category, and generating structured outputs that can be used by internal systems.
Primary use case: identifying potential risk signals during live support conversations between players and customer support agents.

Feature 2 — Escalation and Case Prioritisation
This feature enables conversations that contain potential high-risk indicators to be escalated automatically to the Responsible Gambling team for review. Cases will be prioritised according to the severity of the detected signals, ensuring the most concerning conversations are reviewed first.
The goal of this feature is to help Responsible Gambling Specialists focus on the most critical cases rather than manually reviewing large volumes of conversations.
Scope includes escalation thresholds, prioritised case queues, and visibility of the signals detected within each conversation.
Primary use case: helping Responsible Gambling Specialists identify and review the highest-risk cases efficiently.

Feature 3 — Responsible Gambling Review Interface
This feature provides a simple internal interface where Responsible Gambling Specialists can review conversations that have been flagged by the system. The interface will display the relevant chat history, the detected risk signals, and the system’s recommended classification.
The goal of this feature is to provide a clear workflow for human review and ensure that all escalated cases are assessed by specialists before any intervention is made.
Scope includes a review queue of flagged conversations, conversation context, classification details, and an audit trail of escalations.
Primary use case: enabling specialists to review flagged conversations quickly and determine appropriate next steps.

Features Out
Feature 1 — Automated Player Interventions
The system will not automatically apply account restrictions, deposit limits, or self-exclusion actions. All decisions affecting player accounts will remain subject to review by a Responsible Gambling Specialist.
This approach ensures that sensitive decisions impacting player accounts continue to involve human judgement and comply with regulatory expectations.

Feature 2 — Analysis of Non-Chat Player Behaviour
The initial version of the product will focus exclusively on analysing customer chat messages. Behavioural indicators such as deposit patterns, session duration, or gameplay activity will not be included in this phase.
Expanding the system to include behavioural data may be explored in future iterations once the chat-based risk detection system has been validated.

Feature 3 — Player-Facing AI Communication
The system will not generate automated responses or communicate directly with players within customer support conversations. Its role is limited to identifying potential risk signals and supporting internal teams.
Customer interactions will continue to be handled by trained support agents and Responsible Gambling Specialists to ensure appropriate and sensitive communication with players.










Design
Early design work will focus on a simple internal workflow that supports fast and consistent review by Responsible Gambling Specialists. At this stage, the priority is usability and clarity rather than a fully polished interface.
Initial design concepts will cover:
a prioritised queue of flagged conversations
a case detail view showing the full chat context
clear display of risk score, risk category, and detected signals
escalation status and audit history
basic filtering to help specialists review urgent cases first
Designs should support quick decision making and avoid unnecessary complexity. The interface should make it easy for specialists to understand why a conversation has been flagged and what action, if any, is recommended.
Early wireframes and sketches will be created during discovery and linked into this document as they become available. Final UI designs and interaction flows will be added once reviewed and approved by Product, Design, and Operations stakeholders.










Technical Considerations
The proposed solution will rely on a language model to analyse customer chat messages and identify potential responsible gambling risk signals. Messages will be processed in near real time, allowing potential harm indicators to be detected during or shortly after customer conversations take place.
The system will generate structured outputs containing key information such as risk score, risk category, and escalation recommendation. These outputs will then be evaluated against predefined escalation rules to determine whether a conversation should be surfaced for review by the Responsible Gambling team.
Key technical considerations include:
reliable processing of incoming chat messages at scale
structured output formats to ensure consistent system behaviour
deterministic escalation rules to support responsible gambling policy enforcement
integration with existing customer support platforms and internal tools
evaluation and monitoring mechanisms to track system performance and accuracy
A detailed engineering approach, including architecture diagrams and implementation details, will be documented separately in the engineering technical design document. This document will outline the proposed system architecture, model selection, data flow, and integration requirements.












Success Metrics
Success for this project will be measured through a combination of system performance metrics and operational outcomes. These metrics will help determine whether the system is effectively identifying potential responsible gambling risks while remaining practical for operational teams to use.
Primary success metrics include:
Escalation Accuracy Measures how reliably the system identifies conversations that genuinely require review by the Responsible Gambling team. High escalation accuracy indicates that the system is successfully prioritising the most relevant cases.
False Negative Rate Measures how often genuine risk cases are missed by the system. Reducing false negatives is critical, as missed risk signals may delay intervention for vulnerable players.
Risk Category Classification Accuracy Measures how accurately the system categorises messages into responsible gambling risk types such as financial distress, chasing losses, or loss of control. Consistent categorisation supports more effective case triage and analysis.
Average Processing Latency Measures the time required for the system to analyse and classify a message. Maintaining low latency ensures the system can operate effectively alongside live customer support interactions.
Operational metrics will also be monitored, including:
escalation volume relative to Responsible Gambling team capacity
time required for specialists to review escalated conversations
proportion of escalated cases confirmed as genuine risk indicators
These metrics will help ensure the system improves detection of harmful behaviour signals without creating unnecessary operational burden.
Detailed reporting requirements, measurement methodology, and dashboards will be documented in the Analytics Requirements and Measurement Approach document.






GTM Approach
The initial launch of this product will be focused on internal adoption rather than external marketing. The system is designed to support Responsible Gambling and Customer Support teams by improving the identification and prioritisation of potential gambling harm signals within customer conversations.
Internal messaging will position the product as a player protection and operational support tool that enhances the organisation’s ability to monitor and respond to potential responsible gambling risks. The emphasis will be on strengthening existing responsible gambling processes, improving early detection of harmful behaviour, and supporting teams with more consistent and scalable monitoring capabilities.
The rollout will take place in stages. The first phase will involve a controlled pilot with the Responsible Gambling team to evaluate system performance, gather operational feedback, and refine escalation thresholds. During this stage, training and documentation will be provided to ensure teams understand how to interpret system outputs and integrate them into existing workflows.
Following a successful pilot, the system will be integrated more broadly into customer support operations. Internal communications will focus on how the system assists agents and specialists in identifying risk signals more reliably, while reinforcing that all decisions affecting players remain subject to human review.
If appropriate in future phases, external messaging may highlight the operator’s commitment to responsible gambling and proactive player protection. Any external communication will be carefully aligned with compliance and regulatory expectations.
A more detailed launch and communication plan will be outlined in a dedicated Go-To-Market Brief once pilot timelines and operational readiness are confirmed.










Open Issues
Several areas require further validation and refinement before full deployment. These issues will be addressed during the pilot and evaluation phases of the project.
Escalation Threshold Calibration The appropriate thresholds for escalating conversations to the Responsible Gambling team must be carefully defined. If thresholds are too sensitive, the system may generate an excessive number of cases for review. If thresholds are too strict, genuine risk signals may be missed. This will be addressed through pilot testing and continuous evaluation using real conversation data.
Model Performance on Real Customer Conversations While early testing can be conducted using curated examples, real customer conversations often contain ambiguous language, humour, or incomplete context. The model’s performance will need to be evaluated against historical chat data to ensure reliability in real-world conditions. Evaluation datasets and failure analysis will be used to identify and correct weaknesses.
Operational Capacity of Responsible Gambling Teams Introducing automated detection may increase the number of cases that require specialist review. It will be important to monitor escalation volumes and ensure they remain manageable for the Responsible Gambling team. Escalation thresholds and prioritisation logic may need adjustment based on operational feedback.
Integration with Existing Customer Support Systems The system will need to integrate with existing customer support tools and workflows. Technical limitations or platform constraints may affect how easily chat messages can be analysed in real time. Collaboration with engineering and platform teams will be required to ensure reliable data flow and system stability.
Governance and Oversight of AI Decisions As the system will assist in identifying potential harm signals, clear governance will be required around how model outputs are used and monitored. Documentation, audit logs, and performance reporting will be necessary to ensure transparency and maintain regulatory confidence in the system.
















Q&A
What are common questions about the product along with the answers you’ve decided? This is a good place to note key decisions.























Feature Timeline and Phasing













PRD Checklist:
Here’s a list of topics you must include in your PRD: 













