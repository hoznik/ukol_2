## Domací úkol 2
Vaším úkolem bude ze zadaného [csv souboru](https://gist.github.com/giorgi-ghviniashvili/6d40c712cfc113d07aa11918faf3a865) zparsovat souřadnice.
Tyto souřadnice dále reverzně geokódujte pomocí [knihovny geocoder](https://github.com/DenisCarriere/geocoder).Pro reverzní geokódování vyzkoušejte různé [providery](https://geocoder.readthedocs.io/#providers). 
Po reverzním geokodóvání byste měli získat informace o poloze bodů (město, oblast, stát). Tyto informace dále zapište do vámi vytvořeného souboru, který bude
obsahovat přehledně zapsané souřadnice bodu a geokódovaný výsledek nejmenší zjistitelné jednotky nebo hierarchii všech zjištěných jednotek.

Následně využijte [souboru](https://github.com/datasets/world-cities/blob/master/data/world-cities.csv), který obsahuje města.
Tento soubor zparsujte, geokódujte (získáte souřadnice) a pak najděte, který bod (nebo body) jsou nejblíže jednotlivým bodům z prvního souboru. Výsledek opět zapíšete do vámi vytvořeného souboru.

Kód odevzdejte na vámi vytvořený GitLab repozitář, kde budu přidaný v roli Developer, abych mohl kód zkontrolovat. Do repozitáře můžete ukládat kód postupně během prací na úkolu.
Pokud vám to bude dávat smysl, můžete použít i větve pro jednotlivé funkcionality vaší aplikace.

## Výjimky
Výjimky (exceptions) umožňují v případě chyby nebo nějaké situace přeskočit část kódu, popřípadě úplně zastavit běh programu.

Situace, ve kterých je použijeme:
* ošetření chyb
* oznámení události
* ošetření situací, které mohou nastat velmi zřídka
* provedení ukončovací akce

S výjimkami jste se už setkali v případě chyb, např. pokud budu dělit 0, tak Python vypíše výjimku ZeroDivisionError.
```python
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Pokud bychom chtěli, aby program nespadl v případě, že budeme dělit 0, ale chceme nějak na dělení 0 zareagovat, tak můžeme použít konstrukci `try`
```python
try:
    var = 1/0
except ZeroDivisionError:
    print('Nemuzes delit 0')
# vypise Nemuzes delit 0
```
V tomhle případě program nespadne na chybě, ale protože jsme se situací počítali, tak na ni zareagujeme varováním o tom, že nemůžeme dělit 0. Program normálně doběhne do konce.
Try můžeme použít všude, kde lze očekávat nějakou chybu. Za klíčovým slovem except následuje název výjimky. Více jich je [zde](https://docs.python.org/3.7/library/exceptions.html).
Můžeme sice použít situaci, kdy ošetříme všechny výjimky, ale tento přístup se moc nedoporučuje, protože se může stát situace, že ošetříme situaci, se kterou jsme nepočítali a nedozvíme se o chybě.
```python
try:
    var = 1/0
except:                     # odchytne vsechny vyjimky
    print('Nemuzes delit 0')

try:
    var = 1/0
except (ZeroDivisionError, ValueError):   # odchytne jen dve zadane vyjimky
    print('Nemuzes delit 0')
```

Pokud bychom chtěli, aby program skončil, ale budeme chtít zobrazit konkrétní chybu, tak můžeme použít klíčové slovo `raise`, které vyhodí konkrétní výjimku.
```python
var1 = 1
var2 = 0

if var2 == 0:
    raise ZeroDivisionError('Nemuzes delit 0')

print(var1/var2)
# vypise
# Traceback (most recent call last):
# File "/home/bulva/PycharmProjects/python-2020/06-vyjimky_a_prace_se_soubory/test.py", line 5, in <module>
#   raise ZeroDivisionError('Nemuzes delit 0')
# ZeroDivisionError: Nemuzes delit 0
```

## Práce se soubory
Práce se soubory v Pythonu je extrémně jednoduchá. Pro práci se soubory (jejich otevření) se používá funkce `open()`.
```python
# otevre soubor
myfile = open('myfile.txt', 'w')

# zapise do souboru
myfile.write('hello text file\n')

# zavre soubor
myfile.close()
```

První argument funkce `open()` je název (nebo cesta) k souboru. Druhý argument je režim:
* r - otevření souboru pro čtení
* w - otevření souboru pro zápis (přepíše obsah)
* a - otevření souboru pro přidání textu na konec souboru

```python
myfile = open('myfile.txt') # defaultni rezim je 'r'
print(myfile.readline()) # prectu radek
```

Soubor můžeme číst i po řádku.
```python
for line in open('myfile.txt'):
    print(line, end='')

# vypise 1. radek
# vypise 2. radek atd.
```

Python3 umožňuje použít funkci `open()` s klíčovým slovem with, které po ukončení bloku zavře soubor.
```python
with open('myfile.txt') as file:
    read_data = file.read()
# zde je soubor uz uzavreny
```

Další funkce pro práci se soubory

![file functions](https://gitlab.com/Bulva/python-2020/raw/master/06-vyjimky_a_prace_se_soubory/images/files.png)