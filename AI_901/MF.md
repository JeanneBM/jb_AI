# Microsoft Foundry – Notatki (AI-901)

# Czym jest Microsoft Foundry?

**Microsoft Foundry** to platforma do tworzenia, testowania i wdrażania aplikacji wykorzystujących sztuczną inteligencję.

Pozwala programistom oraz specjalistom AI:

- korzystać z gotowych modeli AI,
- tworzyć własne aplikacje AI,
- testować prompty,
- wdrażać modele,
- budować agentów AI,
- monitorować wykorzystanie modeli.

Można powiedzieć, że Foundry jest środowiskiem podobnym do Visual Studio dla aplikacji AI.

---

# Architektura Microsoft Foundry

```text
                    Microsoft Foundry
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   Model Catalog      Playground          Management
        │                   │                   │
        │                   │                   │
        └──────────────┬────┘                   │
                       │                        │
                  Deployment                   │
                       │                        │
                  REST Endpoint                │
                       │                        │
                  Aplikacja                    │
```

---

# Najważniejsze elementy Foundry

## 1. Project

Project grupuje wszystkie zasoby AI.

Przechowuje:

- modele
- deploymenty
- prompty
- połączenia
- agentów
- ustawienia

Można go traktować jako odpowiednik projektu w Visual Studio.

---

## 2. Hub

Hub zarządza wieloma projektami.

Jeden Hub może zawierać wiele projektów.

Przykład:

```text
Hub

├── Chatbot HR
├── Chatbot IT
├── Invoice AI
└── Document Search
```

---

# Model Catalog

Model Catalog zawiera gotowe modele AI.

Przykłady modeli:

- GPT-4.1
- GPT-4o
- GPT-4o Mini
- Phi-3
- Phi-4
- Llama
- Mistral
- DeepSeek
- Cohere
- Stability AI

Nie trzeba samodzielnie trenować modeli.

Wystarczy wybrać model.

---

# Playground

Playground służy do testowania modeli.

Można:

- wpisywać prompty,
- testować odpowiedzi,
- zmieniać parametry modelu,
- eksperymentować bez pisania kodu.

Playground jest najczęściej używany podczas tworzenia aplikacji.

---

# Prompt

Prompt to instrukcja przekazywana modelowi.

Przykład:

```text
Napisz streszczenie tego dokumentu.
```

---

# System Prompt

Instrukcja określająca zachowanie modelu.

Przykład:

```text
Jesteś profesjonalnym doradcą podatkowym.
```

System Prompt wpływa na wszystkie odpowiedzi modelu.

---

# Prompt Flow

Prompt Flow umożliwia tworzenie bardziej złożonych przepływów AI.

Przykład:

```text
Pytanie użytkownika

↓

Azure AI Search

↓

GPT

↓

Walidacja

↓

Odpowiedź
```

Pozwala:

- testować różne prompty,
- porównywać modele,
- debugować aplikacje,
- mierzyć jakość odpowiedzi.

---

# Deployment

Deployment oznacza udostępnienie modelu.

Proces:

```text
Model

↓

Deployment

↓

Endpoint

↓

Aplikacja
```

Po wykonaniu deploymentu aplikacja może korzystać z modelu przez REST API.

---

# Endpoint

Endpoint to adres REST API modelu.

Przykład:

```text
POST /chat/completions
```

Aplikacja komunikuje się właśnie z endpointem.

---

# Model Deployment

Każdy deployment:

- wskazuje model,
- posiada nazwę,
- posiada endpoint,
- może mieć własne limity.

Przykład:

```text
Model

GPT-4o

↓

Deployment

chat-production

↓

Endpoint

https://xxx.openai.azure.com/
```

---

# Temperature

Parametr określający losowość odpowiedzi.

| Temperature | Efekt |
|--------------|--------|
| 0.0 | odpowiedzi bardzo przewidywalne |
| 0.2 | mało kreatywne |
| 0.7 | naturalne |
| 1.0 | bardzo kreatywne |

---

# Max Tokens

Określa maksymalną długość odpowiedzi.

Więcej tokenów:

- dłuższa odpowiedź,
- większy koszt.

---

# Top P

Alternatywa dla Temperature.

Kontroluje losowość poprzez wybór najbardziej prawdopodobnych słów.

Na egzaminie wystarczy wiedzieć:

- Temperature
- Top P

Nie należy zmieniać obu parametrów jednocześnie.

---

# Azure AI Search

Foundry bardzo często współpracuje z Azure AI Search.

Schemat:

```text
Użytkownik

↓

Azure AI Search

↓

Dokumenty

↓

GPT

↓

Odpowiedź
```

To właśnie jest RAG.

---

# RAG

Retrieval-Augmented Generation

Schemat:

```text
Pytanie

↓

Wyszukiwanie

↓

Dokumenty

↓

Model

↓

Odpowiedź
```

Korzyści:

- aktualne informacje,
- mniejsze halucynacje,
- odpowiedzi oparte o dane firmy.

---

# Agents

Foundry umożliwia budowę agentów AI.

Agent potrafi:

- planować,
- podejmować decyzje,
- wykonywać zadania,
- korzystać z narzędzi,
- wywoływać API.

Przykład:

```text
Użytkownik

↓

Agent

↓

Azure Search

↓

SQL

↓

REST API

↓

GPT

↓

Odpowiedź
```

---

# Connections

Project może posiadać połączenia z:

- Azure OpenAI
- Azure AI Search
- Azure Storage
- Azure SQL
- GitHub
- Azure Key Vault

Dzięki temu aplikacja korzysta z wielu usług Azure.

---

# Monitoring

Foundry umożliwia monitorowanie:

- liczby zapytań,
- wykorzystania tokenów,
- kosztów,
- błędów,
- opóźnień.

---

# Bezpieczeństwo

Foundry wspiera:

- Microsoft Entra ID
- RBAC
- Key Vault
- Private Endpoints
- Managed Identity

---

# Typowy proces tworzenia aplikacji AI

```text
1. Tworzenie Project

↓

2. Wybór modelu

↓

3. Test w Playground

↓

4. Dopracowanie promptów

↓

5. Deployment

↓

6. Endpoint REST

↓

7. Aplikacja korzysta z modelu
```

---

# Najczęściej pojawiające się pojęcia na AI-901

| Pojęcie | Znaczenie |
|----------|-----------|
| Project | Zbiór zasobów AI |
| Hub | Zarządza projektami |
| Model Catalog | Lista dostępnych modeli |
| Playground | Testowanie modeli |
| Prompt | Polecenie dla modelu |
| System Prompt | Instrukcja zachowania modelu |
| Prompt Flow | Budowa przepływów AI |
| Deployment | Udostępnienie modelu |
| Endpoint | REST API modelu |
| Agent | Wykonuje zadania |
| Azure AI Search | Wyszukiwanie dokumentów |
| RAG | Search + LLM |
| Temperature | Kreatywność odpowiedzi |
| Max Tokens | Maksymalna długość odpowiedzi |
| Monitoring | Statystyki i koszty |

---

# Ściąga (1 minuta przed egzaminem)

✅ **Project** → miejsce pracy nad aplikacją AI

✅ **Hub** → zarządza wieloma projektami

✅ **Model Catalog** → wybór modelu

✅ **Playground** → testowanie promptów

✅ **Prompt** → polecenie dla modelu

✅ **Deployment** → udostępnienie modelu

✅ **Endpoint** → REST API

✅ **Azure AI Search** → wyszukiwanie danych

✅ **RAG** → Search + GPT

✅ **Agent** → wykonuje zadania z użyciem narzędzi

✅ **Temperature** → kreatywność odpowiedzi

✅ **Monitoring** → tokeny, koszty i wydajność
