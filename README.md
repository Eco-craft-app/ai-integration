<p align="center">
  <img src="https://github.com/Eco-craft-app/.github/blob/main/profile/leaves_header.png" alt="Eco-craft header">
</p>

<h1 align="center">🧠 AI Integration — Eco-craft 🧠</h1>

> **Moduł integrujący sztuczną inteligencję w projekcie Eco-craft. Wykorzystujemy Gemini API, rozpoznawać odpady oraz proponować kreatywne pomysły na upcycling.**

## 📝 Wprowadzenie
Moduł AI Integration to system analizy wizualnej dedykowany dla aplikacji Eco-craft, wspierającej inicjatywy związane z upcyclingiem i recyklingiem. Wykorzystując Gemini API, moduł przetwarza zdjęcia odpadów, klasyfikuje je i generuje rekomendacje dotyczące potencjalnych projektów upcyclingowych. Dzięki temu, użytkownicy mogą w kreatywny sposób ponownie wykorzystać odpady, minimalizując negatywny wpływ na środowisko. 

## ⚙️ Wymagania
Aby uruchomić moduł, upewnij się, że spełniasz poniższe wymagania:

- Python 3.10 lub nowszy
- Docker (opcjonalnie, dla konteneryzacji aplikacji)
- Gemini API Key (dostęp do Gemini API)

### 📦 Wymagane pakiety Python:
- httpx
- python-dotenv
- google-generativeai
- fastapi
- pillow
- aiohttp
- asyncio
- uvicorn
  

## 🚀 Endpointy i ich funkcje
### 1. Czat z ekspertem (/expert)
- Umożliwia interakcję z wirtualnym ekspertem ds. zarządzania odpadami i ekologii.  
- *Status*: Nie jest wykorzystywany w aplikacji Eco-craft.

### 2. Wykrywanie odpadów na zdjęciu (/detect)
- Analizuje zdjęcie dostarczone przez URL i identyfikuje rodzaje odpadów.  
- *Status*: Nie używany w aplikacji Eco-craft.

- *Przykład zapytania:*
```json
{
    "Photo_URL": "https://example.com/image.jpg"
}
```
- *Przykład odpowiedzi:*
```json
{
    "response": "plastikowa butelka, puszka aluminiowa"
}
```
### 3. Wskazówki recyklingowe na podstawie zdjęcia (/recycling_photo)  
- Pobiera zdjęcie z podanego URL, analizuje je w celu rozpoznania odpadów, a następnie generuje szczegółowe wskazówki dotyczące recyklingu.  
- *Status*: Wykorzystywane w aplikacji Eco-craft.  
- *Przykład zapytania:*
```json
{
    "Photo_URL": "https://example.com/recycling.jpg"
}
```
- *Przykład odpowiedzi:*
```json
{
    "response": [
        {
            "bin": "Plastik i metal",
            "details": {
                "material": "plastik",
                "size": "średnie",
                "variety": "przezroczyste"
            },
            "explanation": "Wrzuć do pojemnika na plastik i metal.",
            "item": "plastikowa butelka"
        }
    ]
}
```
### 4. Alternatywna analiza zdjęcia (/recycling_photo_2)
- Działa podobnie do /recycling_photo, ale wykorzystuje model z endpointu /detect do wykrywania odpadów, co jest mniej efektywne.
- *Status*: Nie używany w aplikacji Eco-craft.

### 5. Wskazówki recyklingowe na podstawie tekstu (/recycling_text)

- Generuje porady dotyczące recyklingu na podstawie listy przedmiotów przekazanych w formacie tekstowym.
- Status: Nie wykorzystywany w aplikacji Eco-craft.
- *Przykład zapytania:*
```
{
    "items": ["plastikowa butelka", "papierowa torba"]
}
```
- *Przykład odpowiedzi:*
```json
{
    "response": [
        {
            "item": "plastikowa butelka",
            "bin": "Plastik i metal",
            "explanation": "Wrzuć do pojemnika na plastik i metal."
        }
    ]
}
```
### 6. Pomysły na upcycling z tekstu (/upcycling_text)  
- Na podstawie listy odpadów generuje kreatywne pomysły na ich ponowne wykorzystanie (upcycling).
- *Status*: Wykorzystywane w aplikacji Eco-craft.
- *Przykład zapytania:*
```json
{
    "Message": [
        {
            "item": "plastikowa butelka",
            "bin": "Plastik i metal",
            "details": {"material": "plastik", "size": "średnie"}
        }
    ]
}
```
- *Przykład odpowiedzi:*
```json
{
    "response": [
        {
            "project": "Organizer na biurko z butelek",
            "description": "Wykorzystaj pocięte plastikowe butelki jako organizery na długopisy i ołówki."
        }
    ]
}
```
### 7. Generowanie pomysłów na upcycling ze zdjęcia (/upcycling_photo)  
- Pobiera zdjęcie, identyfikuje śmieci za pomocą /recycling_photo, a następnie generuje pomysły na ich ponowne wykorzystanie.  
- *Status*: Wykorzystywane w aplikacji Eco-craft.
- *Przykład zapytania:*
```json
{
    "Photo_URL": "https://example.com/upcycling.jpg"
}
```
- *Przykład odpowiedzi:*
```json
{
    "response": [
        {
            "project": "Doniczka z plastikowych butelek",
            "description": "Przetnij butelki, aby stworzyć ozdobne doniczki na rośliny."
        },
        {
            "project": "Organizer na biurko",
            "description": "Użyj kolorowych butelek jako przegródki do przechowywania akcesoriów biurowych."
        }
    ]
}
```
## 📁 Struktura Projektu
```
ai-integration/
├── app.py                # Główna aplikacja FastAPI
├── docker-compose.yaml   # Plik konfiguracyjny dla Docker Compose.
├── Dockerfile            # Plik konfiguracyjny do budowy obrazu Dockera.
├── utils/                # Katalog zawierający pomocnicze skrypty lub moduły.
├── prompts/              # Katalog zawierający pliki związane z zapytaniami
├── requirements.txt      # Lista zależności Pythona.
├── LICENCE               # Licencja
└── README.md             # Dokumentacja projektu
```

## 🛠️ Wsparcie techniczne
Jeśli napotkasz jakiekolwiek problemy lub masz pytania dotyczące projektu, skontaktuj się z nami:
- Jakub Michalski — Python Developer, Prompt Engineer
✉️ michalski.jakub21@zsz-gostyn.com.pl

## Licencja
Projekt jest dostępny na licencji MIT License. Szczegółowe informacje znajdują się w pliku [LICENSE](LICENCE).

## Dziękujemy za zainteresowanie naszym projektem! Mamy nadzieję, że pomoże on w zrównoważonym zarządzaniu odpadami i rozwoju kreatywnych projektów upcyclingowych.


![Eco-craft Footer](https://github.com/Eco-craft-app/.github/blob/main/profile/leaves_footer.png)
