<p align="center" dir="ltr">
  <strong>Svenska</strong> · <a href="README.zh-CN.md" lang="zh-CN">简体中文</a> · <a href="README.de.md" lang="de">Deutsch</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.ru.md" lang="ru">Русский</a> · <a href="README.th.md" lang="th">ไทย</a> · <a href="README.tr.md" lang="tr">Türkçe</a> · <a href="README.md" lang="en">English</a>
</p>

# TIBTRE — bidragssystemet för VERA20k

**TIBTRE** är bidragssystemet som används av [VERA20k](https://github.com/YuriPlanet/vera20k). Det anger hur godkända bidrag värderas, tilldelas poäng och vägs in i projektets beslut.

Det här repot innehåller [reglerna](RULES.md), [huvudboken över bidrag](LEDGER.csv) där rader bara läggs till, automatiskt genererade [saldon](BALANCES.md) och verktyg för att kontrollera uppgifterna oberoende.

VERA20k och det här repot ligger under [YuriPlanet](https://github.com/YuriPlanet), vår GitHub-organisation.

## Varför TIBTRE finns

VERA20k byggs av sina bidragsgivare, och grundtanken är att projektet ska *tillhöra* dem. TIBTRE gör den tanken konkret innan den hinner spela roll:

- **Rättvisa i förväg.** Om VERA20k någon gång bildar en juridisk person eller får intäkter att fördela är den svåra frågan – *vem byggde det här, och hur mycket?* – redan besvarad: öppet och kontrollerbart, från första dagen. Den här huvudboken är den uttalade grunden för en sådan fördelning.
- **Verkligt inflytande, redan nu.** Beslut om projektets inriktning viktas med tibtre – med ett tak, så att ingen enskild innehavare någonsin kan dominera ([`voteweight.py`](voteweight.py)).
- **Ett bestående register.** Bidrag värderas enligt offentliga regler ([bedömningsmallen](docs/grading-rubric.md)), registreras för alltid och kan kontrolleras av vem som helst – även av bidragsgivaren själv, utan att behöva lita på någon ([`identity.py`](identity.py)).

En tibtre ≈ en timmes högkvalitativt arbete med något som VERA20k verkligen behöver – både kvalitet och värde räknas, och båda prissätts enligt de offentliga reglerna. Inget att ansöka om: bidra, bli värderad, bli registrerad.

## Karta

| Fil / mapp | Vad det är |
|---|---|
| `RULES.md` | Policyn: vad tibtre är, hur man tjänar det och vad det är värt |
| `LEDGER.csv` | Huvudboken över tilldelningar, där rader bara läggs till, med bidragsgivar-ID som nyckel – den enda sanningskällan |
| `CONTRIBUTORS.csv` | ID → offentligt visningsnamn (valfritt, kan ändras; tomt = pseudonym) |
| `BALANCES.md` | Genererad saldotabell – kör `python tally.py` efter att du har ändrat huvudboken |
| `tally.py` | Genererar om `BALANCES.md` från `LEDGER.csv` |
| `voteweight.py` | Räknar ut röstvikterna i omröstningar med taket på 25 % per person (`--demo` visar exempel) |
| `identity.py` | Skapar och kontrollerar de offentliga identitetsåtagandena – bevisa att ett ID är ditt utan att lita på någon |
| `docs/granting-guide.md` | Steg-för-steg-guide för godkännare som registrerar en tilldelning |
| `assets/` | Arkiv med godkända konstverk från communityn och annat material som inte är kod |

## Konventioner

- I huvudboken läggs rader **bara till**: tidigare rader ändras eller raderas aldrig. Rättelser blir en ny rad (negativa belopp är tillåtna, med en anteckning som förklarar varför).
- Huvudboken innehåller **bara bidragsgivar-ID:n** (slumpmässiga, som `T-83DE`), aldrig namn. Visningsnamnen finns i `CONTRIBUTORS.csv` och kan när som helst ändras eller tömmas utan att historiken påverkas.
- Kopplingen ID → verklig person finns i den **separata privata mappen** (`../vera20k-tibtre-private/`), som aldrig får publiceras.
- Varje ändring checkas in i git – commit-historiken *är* granskningsspåret.
- All framtida dokumentation om tibtre läggs i `docs/`.
- Godkända konstverk läggs i `assets/` med namnet `YYYY-MM-DD_T-XXXX_short-title.ext` (ID, aldrig namn – filnamn är offentliga och permanenta).

Översättning av [README.md](README.md); vid skillnader gäller den engelska versionen.
