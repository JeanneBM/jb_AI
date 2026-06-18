# Top-p (Nucleus Sampling)

**Top-p** to jedna z najpopularniejszych metod **samplingu** (losowania tokenów) używanych w modelach językowych (LLM) takich jak GPT, Llama, Mistral, Grok itp.

## Co to jest Top-p?

**Top-p** (nazywane też **Nucleus Sampling**) to technika, która zamiast brać pod uwagę stałą liczbę tokenów (jak Top-k), wybiera **dynamiczny zbiór tokenów**, którego suma prawdopodobieństw wynosi co najmniej `p`.

- `p` = wartość z zakresu 0.0 – 1.0 (najczęściej 0.7–0.95)
- Model sortuje tokeny malejąco według prawdopodobieństwa.
- Bierze najmniejszy możliwy zbiór tokenów, którego skumulowane prawdopodobieństwo ≥ `p`.
- Następnie losuje z tego zbioru proporcjonalnie do prawdopodobieństwa.

### Porównanie z innymi metodami

| Metoda          | Jak działa?                              | Zalety                              | Wady                              | Typowe wartości     |
|-----------------|------------------------------------------|-------------------------------------|-----------------------------------|---------------------|
| **Greedy**      | Zawsze najprawdopodobniejszy token      | Deterministyczne, szybkie           | Bardzo powtarzalne, nudne         | —                   |
| **Top-k**       | Bierze k najbardziej prawdopodobnych    | Proste, ogranicza głupoty           | Stała liczba – nieelastyczna      | k = 40–100          |
| **Top-p**       | Bierze najmniejszy zbiór o sumie ≥ p    | **Najlepsza elastyczność**          | Trochę droższy obliczeniowo       | p = 0.8–0.95        |
| **Temperature** | Skaluje rozkład prawdopodobieństw       | Kontrola kreatywności               | Samo w sobie nie obcina tokenów   | temp = 0.7–1.0      |

---

## Jak działa Top-p – przykład

Załóżmy, że model przewiduje następny token z prawdopodobieństwami:

- "kot" → 0.45
- "pies" → 0.25
- "ptak" → 0.12
- "ryba" → 0.08
- "koń" → 0.05
- ... (reszta 0.05)

Przy **Top-p = 0.9**:

1. Sortujemy: kot (0.45) → pies (0.25) → ptak (0.12) → ryba (0.08) → koń (0.05)
2. Sumujemy aż osiągniemy ≥ 0.9:
   - kot + pies + ptak + ryba = **0.90** ← dokładnie 0.9
3. Bierzemy tylko te 4 tokeny i losujemy z nich.

Przy **Top-p = 0.6** model weźmie tylko "kot" + "pies" (0.70).

---

## Zalety Top-p

- **Lepiej dostosowuje się** do kontekstu – w pewnych momentach rozkład jest bardzo skoncentrowany, w innych rozproszony.
- Mniejsza szansa na generowanie nonsensów niż przy wysokiej temperaturze.
- Bardziej naturalny i różnorodny tekst niż Top-k.
- Najczęściej używana metoda w praktyce (razem z temperaturą).

## Typowe kombinacje

```text
Najlepsze ustawienia (2025/2026):
- Creative writing / storytelling     → temperature=0.85–1.0 + top-p=0.92–0.95
- Kod / zadania techniczne            → temperature=0.2–0.5  + top-p=0.8–0.9
- Chat / normalna rozmowa             → temperature=0.7     + top-p=0.9
- Maksymalna determinacja             → temperature=0.0     + top-p=0.7 (lub greedy)
