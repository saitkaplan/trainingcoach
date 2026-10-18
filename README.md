# Training Coach

A Pomodoro timer built with Tkinter: 25 minutes of work, 5-minute short breaks and a 20-minute long break after every fourth round, with a check mark for each finished work session. One of the first programs I wrote while learning Python, between July and November 2023, kept here as it was. Built while following Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp* (Udemy, The App Brewery).

## Run

Requires Python 3 with Tkinter (included in the standard installers). Run it from the project folder, because `tomato.png` is loaded from the current folder.

```bash
cd trainingcoach
python3 main.py
```

## Notes

- The code is kept exactly as written back then; only line endings were normalized.
- Pressing Reset before Start prints an error to the console; the app keeps working. Pressing Start twice runs two timers at once.
- `setup.py` built a Windows `.exe` with `py2exe`. It relies on `distutils`, which was removed in Python 3.12, so it no longer works on current Python versions.
- `tomato.png` comes from the course materials and is not covered by the MIT license.

## License

[MIT](LICENSE) (code only; see the note on `tomato.png` above)

---

## Antrenman Koçu (Türkçe)

Tkinter ile yazılmış bir Pomodoro sayacı: 25 dakika çalışma, 5 dakikalık kısa molalar ve her dördüncü turdan sonra 20 dakikalık uzun mola; biten her çalışma turu bir onay işaretiyle gösterilir. Python öğrenirken, Temmuz ile Kasım 2023 arasında yazdığım ilk programlardan biri; hatıra olarak olduğu gibi saklanıyor. Angela Yu'nun *100 Days of Code: The Complete Python Pro Bootcamp* kursunu (Udemy, The App Brewery) takip ederken yazıldı.

### Çalıştırma

Tkinter içeren Python 3 gerekir (standart kurulumlarda hazır gelir). `tomato.png` bulunulan klasörden yüklendiği için proje klasöründen çalıştır.

```bash
cd trainingcoach
python3 main.py
```

### Notlar

- Kod o zaman yazıldığı gibi duruyor; yalnızca satır sonları düzenlendi.
- Start'tan önce Reset'e basılırsa konsola hata düşer; uygulama çalışmaya devam eder. Start'a iki kez basılırsa iki sayaç aynı anda işler.
- `setup.py`, `py2exe` ile Windows için `.exe` üretiyordu. Python 3.12'de kaldırılan `distutils` modülüne dayandığı için güncel Python sürümlerinde çalışmaz.
- `tomato.png` kurs materyalidir ve MIT lisansına dahil değildir.

### Lisans

[MIT](LICENSE) (yalnızca kod; yukarıdaki `tomato.png` notuna bakın)
