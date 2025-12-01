# lopptutyo
IC250107-3002 kursin harjoitus

## Tavoite:
Harjoitella Gitin täyttä komentorivikäyttöä sekä hallita versionhallinnan jatkotoiminnot,
kuten stash, revert, rebase ja cherry-pick.
## Työskentely:
Kaikki vaiheet tehdään terminaalissa (Git Bash / PowerShell / macOS Terminal) ja
yhteys GitHubiin muodostetaan SSH:lla.


# työn suunitelma:
- alustavat kommitit
- feature1
-- enemy-score
-- revertoi debug-viestit kommistista
- feature2
-- arrow keys support
- merge conflikti (featuret 1+2 ?)
-- tee myös rebase ennen featureiden mergamista
-- jemmaa stashiin debug-vesit
- feature3, poimi yksittäinen kommitti
-- tägi, versio v1.0
- PR??? mistä?!

# työn etenemineen
- thyhjä projetki luotu
- lisätty koodia
-- git stash/pop käytetty README pivityksen yhteydessä
- feature1 lisätty ja komittoitu
-- git stash, vaihtoo main haaraan.
- feature2 tehty
-- käytin myös git stash ja pop
- yhdistun feature1 ja feature2 haarat main haaran - git merge featureX käyttäen
-- feature2 yhdistäminen aiheutti mergeconflictin main.py tiedostossa.
- feature3 tehty
-- vahingossa tehty main haaran pälle
--- kommiti oli mixed-resetoirtu (eli index oli resetoiru mutta muutokset säilytetty)
-- tehty oeikaan haaran.
-- feature3 oli tethy myös vanhasta main haarasta (enen 1/2 feature), rebaisattu.
-- feature3 ei ollut mergattu suoraan, vaa tehty PR sille haaralle. häksytty siellä.
- tehty tagi v1.0-demo


# peli
saa käyntiin komennolla:
```shell
 py main.py
```
koodi on Python3
