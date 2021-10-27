# Design dokument for eksamensopgave 2

## Elementer:
1. En menu der lader dig vælge mellem de forskellige muligheder
2. En oversigt over kampe i hver runde
3. En side der viser et scoreboard over hvilke hold der fører
4. En side hvor man kan se detaljer for hvert holds kampe
5. En måde at ændre point tildelt pr. vundet kamp eller uafgjorte resultater.

## UI - struktur

Hovedmenu:
* Kampe
1. oversigt over kampe og resultater der kan sorteres pr. runde
* Hold
1. Liste over alle hold der kan lede videre til de enkelte hold
* * Individuelle holdsider:
1. Holdnavn
2. Point
3. Kampe
* Rangliste
1. En simpel rangliste der printer den nuværende rangliste
2. Ranglisten indeholder holdnavn, antal "mål", point, kampe vundet, o




## Filstruktur:

### Opbevaring af data:

Nationer / hold:
{
    "hold_id": integer,
    "nation": string,
    "point": integer,
    "mål": integer,
    "vundet": integer,
    "uafgjort": integer,
    "tabt": integer,
    "kampe": {
        alle de kampe der involverer et matchende hold_id
    }
}

Kampe:
{
    "kamp_id": integer,
    "hold_1_id": integer,
    "hold_2_id": integer,
    "point_hold_1": integer,
    "point_hold_2": integer,
    "vinder": "hold_id"
}

Rangliste:
{
    Kan laves ud fra de andre.
    Opstillingen sorteres efter holdenes points, subsidiært målforskel ellers alfabetisk
}