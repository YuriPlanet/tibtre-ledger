<p align="center" dir="ltr">
  <a href="README.sv.md" lang="sv">Svenska</a> · <a href="README.zh-CN.md" lang="zh-CN">简体中文</a> · <a href="README.de.md" lang="de">Deutsch</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.ru.md" lang="ru">Русский</a> · <a href="README.th.md" lang="th">ไทย</a> · <strong>Türkçe</strong> · <a href="README.md" lang="en">English</a>
</p>

# TIBTRE — VERA20k katkı sistemi

**TIBTRE**, [VERA20k](https://github.com/YuriPlanet/vera20k) projesinde kullanılan katkı sistemidir. Kabul edilen katkıların nasıl değerlendirileceğini, puanlandırılacağını ve proje kararlarına nasıl yansıyacağını belirler.

Bu depo; [kuralları](RULES.md), yalnızca yeni kayıt eklenebilen [katkı defterini](LEDGER.csv), otomatik oluşturulan [bakiyeleri](BALANCES.md) ve kayıtları bağımsız olarak doğrulamaya yarayan araçları içerir.

VERA20k ve bu depo, GitHub kuruluşumuz olan [YuriPlanet](https://github.com/YuriPlanet) altında barındırılır.

## TIBTRE neden var

VERA20k projesini ona katkıda bulunanlar inşa ediyor ve kuruluş fikri, projenin onlara *ait* olmasıdır. TIBTRE, bu fikri daha önem kazanmadan somut hâle getirmenin yoludur:

- **Önceden güvence altına alınan adalet.** VERA20k bir gün tüzel kişilik kurarsa ya da dağıtılacak bir geliri olursa, o zor sorunun — *bunu kim yaptı ve ne kadarını?* — yanıtı zaten hazırdır: ilk günden itibaren herkese açık ve doğrulanabilir biçimde. Bu defter, böyle bir dağıtımın açıkça belirtilmiş dayanağıdır.
- **Bugünden gerçek bir söz hakkı.** VERA20k projesinin yönüyle ilgili kararlar tibtre ile ağırlıklandırılır — tek bir sahibin asla baskın çıkamaması için bir üst sınırla ([`voteweight.py`](voteweight.py)).
- **Kalıcı bir kayıt.** Katkılar herkese açık kurallarla değerlendirilir ([puanlama ölçütleri](docs/grading-rubric.md)), sonsuza dek kaydedilir ve herkes tarafından doğrulanabilir — kimseye güvenmek zorunda kalmadan, katkıda bulunan kişinin kendisi tarafından da ([`identity.py`](identity.py)).

Bir tibtre ≈ VERA20k projesinin gerçekten ihtiyaç duyduğu bir iş üzerinde bir saatlik yüksek kaliteli çalışma — hem kalite hem değer hesaba katılır ve ikisi de herkese açık kurallarla fiyatlandırılır. Başvurmanız gereken bir şey yok: katkıda bulunun, değerlendirilin, kayda geçin.

## Harita

| Dosya / klasör | Nedir |
|---|---|
| `RULES.md` | Politika: tibtre nedir, nasıl kazanılır, değeri nedir |
| `LEDGER.csv` | Yalnızca ekleme yapılabilen, katkıda bulunan ID'sine göre tutulan tahsis defteri — tek doğruluk kaynağı |
| `CONTRIBUTORS.csv` | ID → herkese açık görünen ad (isteğe bağlı, değiştirilebilir; boş = takma adlı, yalnızca ID) |
| `BALANCES.md` | Otomatik oluşturulan bakiye tablosu — defteri düzenledikten sonra `python tally.py` komutunu çalıştırın |
| `tally.py` | `BALANCES.md` dosyasını `LEDGER.csv` dosyasından yeniden oluşturur |
| `voteweight.py` | Oylamalarda sayılan ağırlıkları kişi başına %25 üst sınırla hesaplar (örnekler için `--demo`) |
| `identity.py` | Herkese açık kimlik taahhütlerini (commitment) oluşturur ve doğrular — bir ID'nin size ait olduğunu kimseye güvenmeden kanıtlayın |
| `docs/granting-guide.md` | Tahsis kaydeden onaylayıcılar için adım adım kılavuz |
| `assets/` | Kabul edilen topluluk sanat eserlerinin ve kod olmayan diğer çalışmaların arşivi |

## Teamüller

- Defter **yalnızca eklemeye açıktır**: geçmiş satırlar asla düzenlenmez veya silinmez. Düzeltmeler yeni bir satırla yapılır (negatif tutarlara, nedenini açıklayan bir notla izin verilir).
- Defter **yalnızca katkıda bulunan ID'lerini** (rastgele, örneğin `T-83DE`) içerir, asla isim içermez. Görünen adlar `CONTRIBUTORS.csv` dosyasında tutulur ve geçmişe dokunmadan her an değiştirilebilir ya da boşaltılabilir.
- ID → gerçek kişi eşlemesi, asla yayımlanmaması gereken **ayrı özel klasörde** (`../vera20k-tibtre-private/`) tutulur.
- Her değişiklik git'e işlenir (commit) — commit geçmişi denetim izinin *ta kendisidir*.
- tibtre ile ilgili gelecekteki tüm belgeler `docs/` klasörüne konur.
- Kabul edilen sanat eserleri `assets/` klasörüne `YYYY-MM-DD_T-XXXX_short-title.ext` adıyla konur (ID kullanılır, asla isim değil — dosya adları herkese açık ve kalıcıdır).

[README.md](README.md) dosyasının çevirisidir; farklılık olması durumunda İngilizce sürüm geçerlidir.
