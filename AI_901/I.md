# Pojęcia Sztucznej Inteligencji – Notatki

## 1. Generatywna AI (Generative AI)

- **Definicja**: Gałąź AI umożliwiająca generowanie nowej treści (tekst, obrazy, wideo, kod).
- **Działanie**: Oparte na modelach językowych trenowanych na ogromnych zbiorach danych (głównie internet).
- **Prompt**: Instrukcja/pytanie w języku naturalnym → model generuje odpowiedź.
- **LLM** (Large Language Model) vs **SLM** (Small Language Model):
  - LLM: duże, ogólne, drogie.
  - SLM: mniejsze, specjalistyczne, łatwiejsze do wdrożenia lokalnie.

### Agenci AI
- Aplikacje oparte na generatywnej AI, które:
  1. Rozumują i generują język.
  2. Używają **narzędzi** (wiedza + akcje).
  3. Reagują na kontekst.
- **Elementy agenta**:
  - LLM (mózg)
  - Instrukcje (system prompt)
  - Narzędzia (search, email, kalendarz, API itp.)
- Możliwe systemy **multi-agent** (zespoły specjalistów).

**Typowe zastosowania**:
- Chatboty
- Asystenci automatyzujący zadania
- Tworzenie treści
- Tłumaczenie
- Podsumowania

## 2. Przetwarzanie Języka Naturalnego (NLP) i Analiza Tekstu

### Techniki analizy tekstu
- Wykrywanie języka
- Klasyfikacja tekstu (w tym analiza sentymentu)
- Wyodrębnianie kluczowych terminów i jednostek nazwanych (NER)
- Redagowanie danych osobowych (PII)
- Podsumowanie

**Tokenizacja** – dzielenie tekstu na tokeny (słowa, pod-słowa, znaki).

### Metody statystyczne
- **Częstotliwość terminów**
- **TF-IDF** – ważność terminu w dokumencie względem korpusu
- **Bag-of-Words** – reprezentacja wektorowa ignorująca kolejność

**Zaawansowane**: stemming, lematyzacja, POS tagging, N-gramy.

## 3. Technologie Mowy

### Rozpoznawanie mowy (Speech-to-Text)
- Przechwytywanie audio → MFCC → model akustyczny → model językowy → transkrypcja

### Synteza mowy (Text-to-Speech)
- Normalizacja tekstu → analiza lingwistyczna (fonemy) → prosodia → vocoder → audio

**Zastosowania**: asystenci głosowi, transkrypcja, ułatwienia dostępu, tłumaczenie mówione.

## 4. Wizja Komputerowa (Computer Vision)

### Zadania
- **Klasyfikacja obrazów** – przypisanie etykiety
- **Wykrywanie obiektów** – lokalizacja + etykieta (bounding box)
- **Segmentacja semantyczna** – piksel-po-pikselu
- **Modele wielomodalne** – obraz + tekst (opisy, podpisy)

### Architektury
- **CNN** (Convolutional Neural Networks) – filtry splotowe, mapy cech
- **Vision Transformers (ViT)** – traktowanie fragmentów obrazu jako tokenów
- **Modele wielomodalne** – wspólna przestrzeń wektorowa obraz + tekst

**Generowanie obrazu**: modele dyfuzyjne (np. na bazie promptu tekstowego).

## 5. Wyodrębnianie Informacji (Information Extraction)

### OCR (Optical Character Recognition)
**Etapy**:
1. Pozyskanie obrazu
2. Udoskonalenie (redukcja szumu, korekta skosu, kontrast)
3. Wykrywanie regionów tekstu
4. Rozpoznawanie znaków + kontekst
5. Generowanie tekstu + metadane pozycji

### Wyodrębnianie pól
- Szablony / reguły
- Uczenie maszynowe / GNN
- Generatywne AI (LLM + prompt)

**Proces**:
- OCR → wykrywanie pól → mapowanie klucz-wartość → normalizacja → walidacja → integracja

**Typowe dokumenty**: faktury, paragony, kontrakty, formularze medyczne, dokumenty wysyłkowe.

## 6. Odpowiedzialne Używanie AI

**Kluczowe zasady**:
- **Bezstronność** – minimalizacja biasów
- **Niezawodność i bezpieczeństwo**
- **Prywatność i ochrona danych**
- **Inkluzywność**
- **Przezroczystość**
- **Rozliczalność**

**Praktyki**:
- Testowanie na bias
- Filtry treści
- Ujawnianie użycia AI
- Audyty i governance

## 7. Duże Modele Językowe (LLM) – Jak Działają

### Tokenizacja
- Tekst → tokeny (słowa + subwordy + interpunkcja)

### Transformer
- **Encoder** – uwaga (self-attention) → osadzenia (embeddings)
- **Decoder** – generowanie sekwencji (masked attention)
- **Kodowanie pozycyjne** – informacja o kolejności

**Proces**:
1. Tokeny → wektory losowe + pozycyjne
2. Warstwy uwagi → kontekstowe osadzenia
3. Dekoder iteracyjnie przewiduje następny token

**Podobieństwo semantyczne** – mierzone cosinusem wektorów osadzeń.

## 8. Prompt Engineering

**Typy promptów**:
- **System prompt** – rola i ograniczenia
- **User prompt** – konkretne pytanie/zadanie

**Dobre praktyki**:
- Jasne i konkretne
- Podawanie kontekstu
- Przykłady (few-shot)
- Określanie formatu wyjścia
- Używanie RAG (Retrieval-Augmented Generation)

**Historia konwersacji** – utrzymanie kontekstu.

## Kluczowe takeaways

- Generatywna AI + agenci = nowa era automatyzacji.
- Wszystkie obszary (tekst, mowa, obraz) opierają się na **transformacjach** i **uwadze**.
- Najlepsze wyniki daje połączenie wielu technik + odpowiedzialne podejście.
- Prompt + RAG + narzędzia = potężny agent.

---
