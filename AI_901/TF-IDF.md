# TF-IDF (Term Frequency – Inverse Document Frequency)

**TF-IDF** to jedna z najważniejszych i najpopularniejszych miar ważności słów w przetwarzaniu języka naturalnego (NLP) oraz wyszukiwaniu informacji.

## Co to jest TF-IDF?

TF-IDF ocenia, **jak ważne jest dane słowo dla konkretnego dokumentu** w porównaniu do całego zbioru dokumentów (korpusu).

### Dlaczego działa tak dobrze?

- Bardzo częste słowa („i”, „w”, „na”, „jest”, „to”) pojawiają się prawie wszędzie → mają niską wartość informacyjną.
- Słowa rzadkie, ale charakterystyczne dla tematu (np. „kryptowaluty”, „neurony”, „rakieta”) są bardzo ważne.
- TF-IDF **zwiększa wagę** słów częstych w jednym dokumencie, ale rzadkich w całym korpusie.

## Składowe wzoru

### 1. Term Frequency (TF) – Częstotliwość terminu

Ile razy słowo występuje w dokumencie.

$$
\text{TF}(t, d) = \frac{\text{liczba wystąpień słowa } t \text{ w dokumencie } d}{\text{całkowita liczba słów w dokumencie } d}
$$

### 2. Inverse Document Frequency (IDF) – Odwrotna częstotliwość dokumentowa

Jak rzadkie jest słowo w całym zbiorze.

$$
\text{IDF}(t) = \log\left(\frac{N}{1 + \text{df}(t)}\right)
$$

gdzie:
- \( N \) = liczba wszystkich dokumentów w korpusie
- \( \text{df}(t) \) = liczba dokumentów zawierających słowo \( t \)

### 3. TF-IDF

$$
\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)
$$

## Prosty przykład

**Dokumenty:**

1. Kot siedzi na macie.
2. Pies siedzi na kłodzie.
3. Koty i psy są popularnymi pupilami.

**Wyniki (przybliżone):**

- Słowa „na”, „siedzi” → bardzo niski TF-IDF (prawie 0)
- Słowa „kot”, „mata”, „pies”, „kłoda” → wysoki TF-IDF

W dokumencie nr 1 najwyższe wyniki dostaną słowa: **kot** i **mata**.

## Zastosowania

- Wyszukiwarki (Google, Elasticsearch)
- Klasyfikacja tekstu (spam, sentiment, kategorie)
- Ekstrakcja słów kluczowych / tagowanie
- Klasteryzacja i grupowanie dokumentów
- Systemy rekomendacyjne
- Podsumowywanie tekstów
- Detekcja plagiatu

## Implementacja w Pythonie (scikit-learn)

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Przykładowe dokumenty
documents = [
    "Kot siedzi na macie",
    "Pies siedzi na kłodzie",
    "Koty i psy są pupilami",
    "Mój kot lubi drapak"
]

# Tworzenie wektorów TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Wyświetlenie wyników
feature_names = vectorizer.get_feature_names_out()

# Przykład: TF-IDF dla pierwszego dokumentu
print(tfidf_matrix[0].toarray())
