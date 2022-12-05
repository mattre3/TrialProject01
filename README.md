# TrialProject01

Testy napisz proszę do [https://cloud.bitbar.com/](https://cloud.bitbar.com/) zakadając Trialowe konto.

**Zadanie 1** Napisz 2 testy selenium (najlepiej w jednym pliku *.py) z walidacjami jakie uznasz za wystarczające aby upewnić się, że wszystko poszło zgodnie z planem:

1. Login:
    1. zaloguj na istniejącego użytkownika
    2. wyloguj
2. Projects:
    1. zaloguj na istniejącego użytkownika (może być ten sam)
    2. przejdź do podstrony "Projects"
    3. utwórz trzy nowe projekty o losowo generowanych nazwach (każda po 10 liter)
    4. usuń utworzone projekty w odwrotnej kolejności alfabetycznej (czyli zakładając, że masz projekty "ktnhjfngbd", "zdsgfdgdak" i "bvbcxgrwge" to powinny być usunięte w kolejności: "zdsgfdgdak", "ktnhjfngbd", "bvbcxgrwge")

Uwagi: Testy napisz bez wykorzystywania API BitBaru. Nowy użytkownik ma dwa projekty "demo", które znikają po utworzeniu pierwszego własnego projektu, i pojawiają się ponownie po usunięciu wszystkich własnych projektów.

**Zadane 2 (opcjonalne)**

Dostosuj powyższe testy tak, aby można je było wykonać w BitBarze na jednej z przeglądarek desktopowych (zamiast na przeglądarce lokalnej).

Dostępne w BitBarze konfiguracje przeglądarek znajdziesz tu: [https://cloud.bitbar.com/#public/capabilities-creator](https://cloud.bitbar.com/#public/capabilities-creator)

Z testów możesz usunąć dane logowania, nie będą nam potrzebne do sprawdzenia zadań.

Korzystaj z Pythona 3 i Selenium 4.

-----------------------------------------------------------------------------------------------------------------

Kazdy page ma properties z item na koncu - sa to tuple z lokatorem i selektorem do wykorzystania w metodach.

Skupiłem się na tym, zeby testy były łatwe do "rozbudowy" w przyszłości o kolejne scenariusze, funkcjonalności.
Dlatego np. metoda delete_project() nie skupia się na szczegółach zadania (są one w samym teście), tylko bierze
nazwę projektu, który ma usunąć, sprawdza czy taki istnieje i go usuwa.

Projects page zbudowałem z załozeniem, ze user moze stworzyc równiez wiele projektow o tej samej nazwie.

W przypadku tworzenia, usuwania projektów uzyłem time.sleep(1) zeby dać chwilę na dołączenie/odłączenie elementu w DOMie. Nie mogłem znaleźć 

