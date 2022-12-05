# TrialProject01

-----------------------------------------------------------------------------------------------------------------
Python 3.9.13 | Selenium 4.7.2

W zadanie1.py nalezy uzupełnić username i password. W zadanie2.py nalezy uzupełnić apiKey, username, password.

Zeby nie robić screnshotów przy błedach, nalezy wykomentować je w bloku except kazdego z testów.
Wrzuciłem je sobie dla sprawnego sprawdzania co poszło nie tak przy dodawaniu, usuwaniu projektów.

test_projects() na końcu sprawdza, czy jest obecny Android Demo Project, takze przy testowaniu na 
koncie które ma juz testy/przy remote testingu z tego samego konta nalezy wykomentować tę asercję.

Properties w page'ach pisane z duzymi literami z _ITEM w nazwie - są to tuple (lokator, selektor) do wykorzystania
w metodach danego page'a dla większej przejrzystości. 
Przy pisaniu starałem się uwzględnić mozliwość "rozbudowy" projektu o kolejne testy, page (mam nadzieję ze wyszło).
Starałem się jak najwięcej logiki wrzucić do base_page, zeby reszta page'y była w miarę przejrzysta.

Jako ze tworzymy nowe projekty nie uwzględniam tego, ze mogą zawierać jakieś test-runy przy selektorach 
w delete_project(), takze to byłoby do poprawy, ale _close_project() i tak wyłapie te z test runami  i zamknie 
zanim usunie się w delete_function() takze powinno działać.

Dwie metody mogą być nie do końca jasne,"dokomentowałem" je, ale dla szybkiego podsumowania:

BasePage.safe_wait_for() - mój customowy wait, który przez 3 sekundy szuka metodą find_elements(), jeśli nie znajdzie to zwraca pustą listę. Taka funkcja pomocnicza dla _close_projects() z projects_page. Być moze jeszcze gdzieś się przyda w przyszłości.

BasePeage.click_stale_element() - mój handler dla StaleElementReferenceException, jeśli przy kliknięciu wywali ten exception to czeka sekundę i próbuje ponownie.

