# Microsoft Azure + Foundry – Notatki

## 1. Wprowadzenie do aplikacji AI

- **Aplikacja AI** = oprogramowanie wykorzystujące modele ML do rozumowania, uczenia się i adaptacji.
- Modele ML wykonują **wnioskowanie** (inference) na nowych danych.
- Kluczowe cechy: oparte na modelu, dynamiczne, skalowalne.

**Przykłady branżowe**:
- Opieka zdrowotna: analiza obrazów medycznych
- Finanse: wykrywanie oszustw
- Retail: rekomendacje
- Produkcja: konserwacja predykcyjna
- Edukacja: spersonalizowane tutoringi

## 2. Platforma Microsoft Azure

**4 główne kategorie usług**:
- **Compute** – maszyny wirtualne, kontenery, App Service, AKS
- **Storage** – pliki, bazy danych, blob
- **Networking** – połączenie, bezpieczeństwo, prywatność
- **App Services** – gotowe platformy do hostingu

**Struktura organizacyjna**:
- **Tenant (Dzierżawa)** – tożsamość organizacji
- **Subscription** – kontener rozliczeniowy i limitów
- **Resource Group** – folder na powiązane zasoby
- **Resource** – pojedyncza usługa (model, baza, VM itp.)

**Azure Portal** – centralne miejsce do zarządzania wszystkim.

## 3. Microsoft Foundry – platforma do AI

**Foundry** = korporacyjna PaaS do budowania, wdrażania i zarządzania aplikacjami oraz **agentami AI** na Azure.

### Kluczowe elementy
- **Models** – tysiące modeli (OpenAI GPT-4o/5, Anthropic, Mistral, Llama, Grok, Flux, Sora itp.)
- **Agents** – inteligentni agenci z orkiestracją, tool calling, multi-agent
- **Tools** – Azure AI services (Language, Vision, Speech, Content Understanding)
- **Knowledge (Foundry IQ)** – RAG na danych firmowych (SharePoint, Blob, OneLake, Purview)

**Struktura**:
- **Foundry Resource** → hosting modeli i usług
- **Project** → obszar roboczy (agenci, oceny, indeksy wektorowe, connections)

**Portal Foundry** – nowy interfejs do pracy z modelami, agentami, playground.

## 4. Tworzenie aplikacji AI na Foundry

**Klient-Serwer**:
- **Klient** – UI/CLI, zbieranie inputu, wysyłanie promptu
- **Serwer** – punkt końcowy modelu (REST + SDK)

**Punkty końcowe**:
- OpenAI Responses API (najnowszy)
- Autoryzacja: API Key lub Entra ID + Key Vault

**SDK Python** – najwygodniejszy sposób (`openai`, `azure-ai-*`).

## 5. Analiza Tekstu w Foundry

### Dwa podejścia
1. **Modele ogólnego przeznaczenia** (GPT) – prompt-driven (wyodrębnianie fraz, NER, sentyment, podsumowanie)
2. **Azure Language** – specjalistyczne, deterministyczne usługi

**Azure Language**:
- Wykrywanie języka
- Wykrywanie PII (dane osobowe) + redakcja
- Analiza sentymentu, kluczowych fraz, jednostek

## 6. Technologie Mowy (Azure Speech)

- **Speech-to-Text** – rozpoznawanie mowy
- **Text-to-Speech** – synteza mowy (neuronowe głosy)
- **Voice Live** – pełna zamiana mowy-na-mowę w czasie rzeczywistym (asystent głosowy)

**Voice Live** – jedna usługa łącząca STT + AI + TTS dla konwersacji na żywo.

## 7. Wizja Komputerowa i Modele Wielomodalne

**Modele GPT z wizją** (GPT-4.1, GPT-5 series):
- Opis obrazu
- Visual Question Answering
- Analiza zrzutów, diagramów, dokumentów

**Generowanie obrazów**:
- GPT-Image-1 / 1.5 (najlepsza jakość)
- GPT-Image-1-Mini (szybsza/tańsza)

**Generowanie wideo**:
- **Sora 1 & Sora 2** – tekst→wideo, obraz→wideo, remix

Wszystko dostępne w Playground + Responses API.

## 8. Wyodrębnianie Informacji – Azure Content Understanding

**Najpotężniejsza usługa** do przetwarzania dokumentów, audio i wideo.

**Działanie**:
1. Przesyłasz zawartość (URL lub plik)
2. Wybierasz **analizator** + **schemat**
3. Otrzymujesz ustrukturyzowany JSON

**Typy analizatorów**:
- `prebuilt-invoice`, `prebuilt-receipt` itp.
- Niestandardowe schematy (zagnieżdżone pola, kolekcje)

**Obsługiwane formaty**:
- Dokumenty/PDF/obrazy (OCR + semantyka)
- Audio (transkrypcja + wyodrębnianie pól)
- Wideo (analiza klatek + audio)

**SDK Python** – asynchroniczne `begin_analyze()` + polling.

## Kluczowe takeaways

- **Azure** = infrastruktura i bezpieczeństwo
- **Foundry** = ujednolicona platforma do agentów i modeli AI
- Najlepsze wyniki: modele ogólne (GPT) + specjalistyczne usługi Azure + RAG (Foundry IQ)
- Wszystko dostępne przez **Playground** (testy) i **SDK** (produkcja)
- Content Understanding + Voice Live + Vision = pełny stack multimodalny
