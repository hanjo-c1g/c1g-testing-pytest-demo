# Pytest Warenkorb-Demo mit Coverage

Dieses Repository zeigt eine **pytest-Demo**, bei der ein einfacher **Warenkorb** getestet wird.  
Zusätzlich wird ein **Coverage-Report** generiert, um zu sehen, welche Codezeilen nicht getestet wurden.

## 📦 Installation & Vorbereitung

1. Stelle sicher, dass **Python 3.7+** installiert ist.
2. Installiere `pytest` und `pytest-cov` mit:

   ```sh
   pip install pytest pytest-cov
   ```

3. Klone dieses Repository oder lade es als ZIP herunter.
4. Navigiere in das Projektverzeichnis.

## 🚀 Nutzung

Um die Tests auszuführen, gib folgenden Befehl ein:

```sh
pytest --cov=cart --cov-report=term-missing
```

Falls alles erfolgreich ist, solltest du eine Ausgabe wie diese sehen:

```
Name       Stmts   Miss  Cover   Missing
----------------------------------------
cart.py       15      2    85%   18-19
----------------------------------------
TOTAL         15      2    85%
```

➡ Hier sehen wir, dass **Zeile 18-19 nicht getestet** wurde.  

### **📊 HTML Coverage Report generieren**

Für eine visuelle Darstellung kannst du diesen Befehl nutzen:

```sh
pytest --cov=cart --cov-report=html
```


## 🛠 Aufgabe für Teilnehmer

1. **Schau dir den Coverage-Report an**: Welche Methode fehlt im Test?  
2. **Erstelle einen neuen Test für `apply_discount()` in `test_cart.py`**  
3. **Führe den Coverage-Test erneut aus**: Hat sich die Coverage verbessert?  

Viel Spaß mit `pytest` & Code Coverage! 🚀
