# Italy-Covid-19-Cases

Visualization of Covid-19 Cases in Italy with the data coming from [Civil Defense](http://www.salute.gov.it/nuovocoronavirus). Civil defense provides pdfs. Convertion to xlsx is done [here](https://document.online-convert.com/convert/pdf-to-xlsx).

required packages: [pandas](https://pypi.org/project/pandas/), [numpy](https://pypi.org/project/numpy/),
[matplotlib](https://pypi.org/project/matplotlib/),[glob](https://pypi.org/project/glob3/),os,re,pylab,sys,[datetime](https://pypi.org/project/datetime3/)


## Usage

general.py
-----------------------------------------------------

#### Inputs: 
general - Plot given variables in national level
state - Plot given variables for given state(s)

'Hospitalized with symptoms','Intensive care','Home isolation','Total positive','Recovered','Death toll','Total cases','Tested' are the input
variables for both general and state. 'all' can be used as a wild card.

'Lombardia','Emilia Romagna','Veneto','Piemonte','Marche','Toscana','Lazio','Campania','Liguria','Friuli V.G.','Sicilia','Puglia''Umbria',
'Molise',
'Trento',
'Abruzzo',
'Bolzano',
'Valle d'Aosta',
'Sardegna',
'Calabria',
'Basilicata' are the states in Italy. 'all' can be used as a wild card.


##### General Example: 

<pre>python general.py general 'Intensive care','Home isolation' </pre>

<pre>python general.py general 'Intensive care',Tested </pre>

(one word inputs can be written without quotes)

<pre>python general.py general all</pre>

#### State Example:

<pre>python general.py state 'Intensive care','Home isolation' 'Lombardia'</pre>

<pre>python general.py state 'Intensive care',Tested 'Lombardia','Veneto'</pre>

Multiple states can be given with comma (,) in between

<pre>python general.py state 'Intensive care' all</pre>

activecases.py
-----------------------------------------------------

#### Inputs: 
city - Plot given variables for given city(ies)
state - Plot given variables for given state(s)

'all' can be used as a wild card in state level plot. It creates a mess in city level plots so it is disabled for cities.

'LOMBARDIA', 'EMILIA-ROMAGNA', 'VENETO', 'MARCHE', 'PIEMONTE', 'TOSCANA',
 'CAMPANIA', 'LAZIO', 'LIGURIA', 'FRIULI VENEZIA GIULIA', 'SICILIA',
 'PUGLIA', 'UMBRIA', 'ABRUZZO', 'MOLISE', 'TRENTINO ALTO ADIGE',
 'SARDEGNA', 'BASILICATA', "VALLE D'AOSTA", 'CALABRIA'
are the states in Italy.

'BERGAMO', 'LODI', 'CREMONA', 'PAVIA', 'BRESCIA', 'MILANO'
 'MONZA BRIANZA', 'MANTOVA', 'VARESE', 'SONDRIO', 'COMO', 'LECCO'
 'TOTALE', 'PIACENZA', 'PARMA', 'MODENA', 'RIMINI', 'REGGIO EMILIA'
 'BOLOGNA', 'RAVENNA', 'FORLÌ CESENA', 'FERRARA', 'PADOVA', 'TREVISO'
 'VENEZIA', 'VERONA', 'VICENZA', 'BELLUNO', 'ROVIGO', 'PESARO', 'ANCONA'
 'MACERATA', 'FERMO', 'TORINO', 'NOVARA', 'ASTI', 'VERCELLI'
 'ALESSANDRIA', 'VERBANO-CUSIO-OSSOLA', 'BIELLA', 'CUNEO', 'FIRENZE'
 'SIENA', 'MASSA CARRARA', 'PISTOIA', 'LUCCA', 'AREZZO', 'PISA'
 'LIVORNO', 'PRATO', 'GROSSETO', 'NAPOLI', 'SALERNO', 'CASERTA'
 'AVELLINO', 'BENEVENTO', 'ROMA', 'FROSINONE', 'VITERBO', 'RIETI'
 'LATINA', 'LAZIO FUORI REGIONE', 'SAVONA', 'IMPERIA', 'GENOVA'
 'LA SPEZIA', 'TRIESTE', 'GORIZIA', 'UDINE', 'PORDENONE', 'PALERMO'
 'ENNA', 'CATANIA', 'RAGUSA', 'AGRIGENTO', 'MESSINA', 'SIRACUSA'
 'TARANTO', 'BARI', 'BRINDISI', 'BAT', 'LECCE', 'FOGGIA', 'PERUGIA'
 'TERNI', 'TERAMO', 'PESCARA', "L'AQUILA" 'CHIETI', 'CAMPOBASSO'
 'BOLZANO', 'TRENTO', 'CAGLIARI', 'NUORO', 'ORISTANO', 'SASSARI'
 'POTENZA', 'MATERA', 'AOSTA', 'COSENZA', 'REGGIO CALABRIA', 'CATANZARO'
 'VIBO VALENTIA', 'TOTALE GENERALE', 'ASCOLI PICENO', 'CALTANISSETTA'
 'TRAPANI', 'ISERNIA', 'CITTÀ METROPOLITANA DI CAGLIARI'
 'SUD SARDEGNA', 'CROTONE', 'CALTANISETTA'
 'CITTÀ METROPOLITANA DI CAGIARI'
 are the cities in Italy.

##### City Example: 

<pre>python activecases.py city 'Trieste','Udine' </pre>

<pre>python activecases.py city Milano </pre>

(one word inputs can be written without quotes)


#### State Example:

<pre>python activecases.py state 'Lombardia'</pre>

<pre>python activecases.py state 'Lombardia','Veneto'</pre>

Multiple states can be given with comma (,) in between

<pre>python activecases.py state all</pre>

regionplot.py
-----------------------------------------------------

#### Inputs: 
Input date format: YYYY/MM/DD
'Hospitalized with symptoms','Intensive care','Home isolation','Total positive','Recovered','Death toll','Total cases','Tested' are the input variables. 
Example:
<pre>python regionplot.py 2020/03/21 'Recovered'</pre>
