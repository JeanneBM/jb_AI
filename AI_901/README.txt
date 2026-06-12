1. AI Workloads
Machine Learning

Predict from data.

Regression
→ Predict number

Examples:

House price
Temperature

Classification
→ Predict category

Examples:

Spam / Not Spam
Fraud / Not Fraud

Clustering
→ Group similar items

Examples:

Customer segments
2. Generative AI
Generative AI

Creates:

Text
Images
Code
Audio
Video

Examples:

ChatGPT
Copilot
Image generators
LLM (Large Language Model)

Examples:

GPT models
Phi models

Can:

Summarize
Translate
Generate code
Answer questions
3. Prompt Engineering
Good Prompt Formula

Role + Task + Context + Format

Example:

❌ Bad:

Explain Kubernetes

✅ Good:

Explain Kubernetes to a junior DevOps engineer.
Use simple language and examples.
Prompt Techniques
Zero-shot

Just ask.

Translate to Polish.
Few-shot

Provide examples.

English: Hello
Polish: Cześć

English: Good morning
Polish:
Chain of Thought

Break problem into steps.

Solve step by step.
4. AI Agents
Agent

AI system that:

Receives goals
Makes decisions
Uses tools
Performs actions

Example:

User:

Find flights and create itinerary.

Agent:

Searches flights
Compares prices
Creates plan
Agent Components
Model
Instructions
Memory
Tools
Knowledge

AI-901 introduces this concept heavily.

5. Azure AI Foundry

Azure AI Foundry

Know that it is Microsoft's platform for:

Building AI apps
Testing models
Evaluating prompts
Managing deployments
Creating AI agents

Think:

"GitHub + Azure ML + OpenAI tools for AI projects"

6. Model Evaluation

Questions:

Is the answer accurate?

Correctness

Is the answer relevant?

Groundedness

Is it safe?

Safety

Is it biased?

Fairness

Does it follow instructions?

Compliance

7. RAG (Retrieval-Augmented Generation)

Very important new topic.

Problem:

LLMs hallucinate.

Solution:

RAG = Search + LLM

Process:

User Question
↓
Search Knowledge Base
↓
Retrieve Documents
↓
Send to LLM
↓
Generate Answer

Benefits:

More accurate
Uses company data
Less hallucination
8. Embeddings

Embedding =
text converted into numbers.

Used for:

Semantic search
Vector databases
RAG

Similar meaning → similar vectors

Example:

Dog
Puppy

Vectors close together.

9. Azure AI Services
Vision

Azure AI Vision

Used for:

OCR
Image analysis
Object detection
Captions
Language

Azure AI Language

Used for:

Sentiment analysis
Entity recognition
Summarization
Translation
Speech

Azure AI Speech

Used for:

Speech to Text
Text to Speech
Translation
OpenAI

Azure OpenAI Service

Provides:

GPT models
Embeddings
Image generation
Search

Azure AI Search

Provides:

Full text search
Semantic search
Vector search
RAG integration
10. Responsible AI

Microsoft loves exam questions on this.

Fairness

No discrimination.

Reliability

Works correctly.

Privacy

Protect data.

Inclusiveness

Accessible.

Transparency

Explain behavior.

Accountability

Humans responsible.

Mnemonic:

FRPITA

Fairness
Reliability
Privacy
Inclusiveness
Transparency
Accountability

11. Hallucinations

Hallucination =
model invents information.

Reduce by:

Better prompts
RAG
Grounding
Human review
12. Fine-Tuning vs Prompt Engineering
Method	When
Prompt Engineering	Most cases
RAG	Need company data
Fine-tuning	Specialized behavior

Exam favorite:

Try prompting and RAG before fine-tuning.

13. AI-901 Service Mapping
Scenario	Service
Train ML model	Azure Machine Learning
Analyze image	Azure AI Vision
OCR	Azure AI Vision
Sentiment	Azure AI Language
Translation	Azure AI Language
Speech-to-text	Azure AI Speech
Chatbot with GPT	Azure OpenAI
Enterprise search	Azure AI Search
Build AI agent	Azure AI Foundry
Ground LLM with documents	AI Search + RAG
Semantic search	Embeddings + AI Search
