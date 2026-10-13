<p align="center" dir="ltr">
  <a href="README.sv.md" lang="sv">Svenska</a> · <a href="README.zh-CN.md" lang="zh-CN">简体中文</a> · <strong>Deutsch</strong> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.ru.md" lang="ru">Русский</a> · <a href="README.th.md" lang="th">ไทย</a> · <a href="README.tr.md" lang="tr">Türkçe</a> · <a href="README.md" lang="en">English</a>
</p>

# TIBTRE — das Beitragssystem für VERA20k

**TIBTRE** ist das Beitragssystem von [VERA20k](https://github.com/YuriPlanet/vera20k). Es legt fest, wie angenommene Beiträge bewertet, gutgeschrieben und bei Projektentscheidungen berücksichtigt werden.

Dieses Repository enthält die [Regeln](RULES.md), das [Hauptbuch der Beiträge](LEDGER.csv), in dem Einträge nur hinzugefügt werden, die automatisch erzeugten [Kontostände](BALANCES.md) und Werkzeuge zur unabhängigen Prüfung der Aufzeichnungen.

VERA20k und dieses Repository werden unter [YuriPlanet](https://github.com/YuriPlanet) gehostet, unserer GitHub-Organisation.

## Warum es TIBTRE gibt

VERA20k wird von seinen Mitwirkenden gebaut, und die Grundidee ist, dass es ihnen auch *gehören* soll. Mit tibtre wird diese Idee greifbar, bevor es darauf ankommt:

- **Fairness im Voraus.** Sollte VERA20k jemals eine juristische Person gründen oder Einnahmen zu verteilen haben, ist die schwierige Frage – *wer hat das gebaut, und wie viel davon?* – bereits beantwortet: öffentlich und überprüfbar, vom ersten Tag an. Dieses Hauptbuch ist die erklärte Grundlage für jede solche Verteilung.
- **Echte Mitsprache, schon heute.** Entscheidungen über die Ausrichtung des Projekts werden nach tibtre gewichtet – mit einer Obergrenze, damit niemand mit großem Bestand jemals allein bestimmen kann ([`voteweight.py`](voteweight.py)).
- **Eine dauerhafte Aufzeichnung.** Beiträge werden nach öffentlichen Regeln bewertet ([das Bewertungsschema](docs/grading-rubric.md)), dauerhaft festgehalten und sind für alle überprüfbar – auch für die Mitwirkenden selbst, ohne jemandem vertrauen zu müssen ([`identity.py`](identity.py)).

Ein tibtre ≈ eine Stunde hochwertiger Arbeit an etwas, das VERA20k wirklich braucht – Qualität und Wert zählen beide, und beide werden nach den öffentlichen Regeln bepreist. Du musst nichts beantragen: beitragen, bewertet werden, eingetragen werden.

## Übersicht

| Datei / Ordner | Was es ist |
|---|---|
| `RULES.md` | Die Regeln: was tibtre ist, wie man es verdient und was es wert ist |
| `LEDGER.csv` | Hauptbuch der Zuteilungen, in dem Einträge nur hinzukommen, geführt nach Mitwirkenden-ID – die einzige maßgebliche Quelle |
| `CONTRIBUTORS.csv` | ID → öffentlicher Anzeigename (optional, änderbar; leer = pseudonym) |
| `BALANCES.md` | Generierte Tabelle der Kontostände – nach Änderungen am Hauptbuch `python tally.py` ausführen |
| `tally.py` | Erzeugt `BALANCES.md` aus `LEDGER.csv` neu |
| `voteweight.py` | Berechnet die gezählten Stimmgewichte bei Abstimmungen mit der Obergrenze von 25 % pro Person (`--demo` zeigt Beispiele) |
| `identity.py` | Erzeugt und prüft die öffentlichen Identitäts-Commitments – beweise, dass eine ID dir gehört, ohne jemandem vertrauen zu müssen |
| `docs/granting-guide.md` | Schritt-für-Schritt-Anleitung für Freigebende, die eine Zuteilung eintragen |
| `assets/` | Archiv angenommener Kunstwerke aus der Community und anderer Beiträge, die kein Code sind |

## Konventionen

- Ins Hauptbuch kommen Einträge **nur hinzu**: Vergangene Zeilen werden nie bearbeitet oder gelöscht. Korrekturen bekommen eine neue Zeile (negative Beträge sind erlaubt, mit einer Notiz zur Begründung).
- Das Hauptbuch enthält **nur Mitwirkenden-IDs** (zufällig, etwa `T-83DE`), niemals Namen. Anzeigenamen stehen in `CONTRIBUTORS.csv` und können jederzeit geändert oder geleert werden, ohne die Historie zu berühren.
- Die Zuordnung ID → reale Person liegt im **separaten privaten Ordner** (`../vera20k-tibtre-private/`), der niemals veröffentlicht werden darf.
- Jede Änderung wird in git committet – die Commit-Historie *ist* der Prüfpfad.
- Alle künftige Dokumentation zu tibtre gehört nach `docs/`.
- Angenommene Kunstwerke kommen nach `assets/`, benannt als `YYYY-MM-DD_T-XXXX_short-title.ext` (ID, niemals Name – Dateinamen sind öffentlich und dauerhaft).

Übersetzung von [README.md](README.md); bei Abweichungen gilt die englische Version.
