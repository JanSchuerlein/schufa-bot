# Schufa Bot 

Der Schufa Bot nutzt das Selenium Framework in Python um mit einem simulierten Chrome-Browser den aktuellen Schufa-Score automatisch aus dem meineschufa.de Portal abzufragen. 

Aufgrund von Cookie-Tracking und der L7 DDos-Protection von Link11 sind reine HTTPS-Requests nicht mehr ohne Weiteres möglich, daher der Weg über Selenium.

Da das Schufa-Portal für die Datenabfrage zusätzlich eine 2FA-Authentifizierung über SMS erfordert, muss die Weiterleitung der SMS-Nachrichten auch automatisch über eine Middleware API an den Bot erfolgen.

Das ist hier beispielhaft über eine simple GET API und eine iOS Automation bei eingehender SMS gelöst, selbstverständlich können auch virtuelle VOIP-Provider/Simkarten dafür genutzt werden, der beschriebene Weg ist der einfachste, ohne seine hinterlegte Rufnummer bei der Schufa ändern zu müssen.

Das Repo ist auf eine Installation und Verwendung unter Linux, vorrangig auf Debian 12 ausgerichtet. 

Der Schufa-Score kann anschließend für beliebige Zwecke verwendet werden, beispielsweise für: 

Tracking, Darstellung auf einer LaMetric, Scriptable Widget auf dem iPhone oder sogar für SmartHome Automationen. 😎

Der im Schufa Portal angezeigte Basis-Score wird mittlerweile im Gegensatz zu früher, live berechnet und kann sich daher immer wieder ändern, eine manuelle Abfrage mitsamt Login ist allerdings auf Dauer mühsam und zeitintensiv.

Aktueller Stand des Bots: *04/2024*

## Voraussetzungen

- meineschufa.de Konto mit aktivem Jahresabonnement
- Python3
- Selenium
- Google Chrome & ChromeDriver

## Bot Installation

Das Repository herunterladen und clonen, anschließend das **install.sh** Script ausführen. 

```bash
git clone git@github.com:JanSchuerlein/schufa-bot.git
./install.sh
```

Das **install.sh** Script installiert automatisch eine virtuelle Python Umgebung im aktuellen Verzeichnis und alle notwendigen Pakete. 

## Einrichtung Selenium & Google Chrome

Wenn du auf deinem System bereits Google Chrome und den aktuellsten Chrome-Driver installiert hast solltest du diesen Schritt überspringen, andernfalls hast du die Möglichkeit über nachfolgende Scripts jeweils beides automatisch zu installieren. 

**Hinweis**: Die Scripts sind darauf ausgelegt, auf einem Server Linux Betriebssystem (amd64), vorrangig Debian 12 ausgeführt zu werden. 

```bash
./install_chrome.sh
./install_chromedriver.sh
```

Alternativ kannst du manuell eine passende Version von Google-Chrome für Selenium mit dem ChromeDriver installieren.

[Google Chrome Download](https://www.google.com/chrome/?platform=linux)

[Chrome-Driver Download](https://chromedriver.chromium.org/downloads)

## Verwendung

Mit nachfolgendem Befehl lässt sich der Bot starten.

**Hinweis**: Beim Ersten Start wird automatisch eine neue **config.json** anhand der **config_template.json** Vorlage erstellt.

```bash
./start.sh
```

## Config

Im automatisch generierten Config File müssen die Schufa-Zugangsdaten sowie die API-URL für die Abfrage des letzten SMS 2FA Tokens hinterlegt werden. Die Optionen für den Chrome-Driver und die Score-API URL sind optional. 

Weitere Infos zum Thema SMS 2FA findest du im nächsten Abschnitt


## Automatische Weiterleitung des 2FA SMS-PIN (Sicherheitscode) an den Bot

Um die 2FA SMS Sicherheitscodes die von der Schufa gesendet werden, automatisch an den Bot weiterleiten zu können, ist der Austausch über eine beliebige Key-Value API (HTTPS/GET) notwendig. In den kommenden Tagen wird an dieser Stelle ein Beispiel-Repo mit einer simplen PHP-API verlinkt. 

Im nachfolgenden Beispiel werden wir durch eine iOS Automation in der App Kurzbefehle, das iPhone anweisen, bei einer eingehenden Schufa SMS, die API-URL mit dem 2FA SMS Token aufzurufen, darüber wird dann automatisch der Sicherheitscode übermittelt. Der Bot ruft nach einer Kurzen Verzögerung die gleiche API URL auf, um den Code abzurufen. Das gleiche lässt sich natürlich auch unter Android einrichten.


![IMG_2412](https://github.com/JanSchuerlein/schufa-bot/assets/2477821/59144f36-2f27-48dd-8f0e-23552dd985ee)![IMG_2411](https://github.com/JanSchuerlein/schufa-bot/assets/2477821/ffd31056-3376-4c3f-88f3-9740c17b2e4d)![IMG_2410](https://github.com/JanSchuerlein/schufa-bot/assets/2477821/63fa4272-50b4-416d-a126-73434d3731be)

