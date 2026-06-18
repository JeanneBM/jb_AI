# CNN – Convolutional Neural Networks

**CNN (Sieci Konwolucyjne)** to rodzaj sztucznej sieci neuronowej zaprojektowany głównie do przetwarzania **danych siatkowych** (obrazy, wideo, dźwięk, dane medyczne itp.).

# CNN (Convolutional Neural Networks) – filtry splotowe i mapy cech

**Convolutional Neural Networks (sieci konwolucyjne)** to najpopularniejsza architektura do przetwarzania obrazów, wideo, dźwięku i tekstu (1D). Kluczowymi elementami są **filtry splotowe** oraz **mapy cech**.

**W trakcie treningu sieć sama uczy się setek/tysięcy takich filtrów na różnych poziomach abstrakcji.**

---

## 1. Filtr splotowy (Kernel / Filter)

Filtr to mała macierz (najczęściej 3×3, 5×5, 7×7), której wartości są parametrami uczenia.

**Przykład filtra 3×3 wykrywającego krawędzie pionowe:**

```
\begin{bmatrix}
-1 & 0 & 1 \\
-1 & 0 & 1 \\
-1 & 0 & 1
\end{bmatrix}
```
---

## Kluczowe elementy CNN

### 1. Filtry splotowe (Kernels / Filtry)
- Małe macierze (najczęściej 3×3, 5×5, 7×7)
- Przesuwają się po obrazie
- Każdy filtr szuka konkretnej cechy (krawędzi, tekstury, kształtu itp.)
- Wagi filtrów są **uczone** podczas treningu

### 2. Operacja splotu (Convolution)
- Filtr nakłada się na obraz, mnoży wartości i sumuje
- Dzięki temu powstaje nowa reprezentacja obrazu

### 3. Mapa cech (Feature Map)
- Wynik działania **jednego filtra** na całym obrazie
- Jeśli warstwa ma 64 filtry → otrzymujemy **64 mapy cech**
- Każda mapa podkreśla inne informacje z obrazu

---

## Hierarchia cech w CNN

| Poziom warstwy     | Co sieć wykrywa                          |
|--------------------|------------------------------------------|
| **Pierwsze warstwy**   | Proste krawędzie, linie, gradienty, kolory |
| **Środkowe warstwy**   | Tekstury, wzory, części obiektów         |
| **Głębokie warstwy**   | Całe obiekty, twarze, sceny, semantyka   |

---

## Dlaczego CNN jest taki skuteczny?

- **Współdzielenie wag** → dramatycznie mniej parametrów
- **Lokalne połączenia** → każdy neuron widzi tylko mały fragment
- **Hierarchiczna budowa cech** → od prostych do bardzo abstrakcyjnych
- **Translacyjna niezmienność** (dzięki poolingowi)

---

## Jednozdaniowe podsumowanie

**CNN to sieć neuronowa, która automatycznie uczy się wykrywać coraz bardziej złożone cechy obrazu za pomocą małych filtrów splotowych, tworząc na każdym poziomie mapy cech.**

Dzięki temu rewolucjonizowała przetwarzanie obrazów od 2012 roku (AlexNet) i pozostaje podstawą większości nowoczesnych modeli wizyjnych.
