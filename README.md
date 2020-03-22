# Italy-Covid-19-Cases

Visualization of Covid-19 Cases in Italy with the data coming from [Civil Defense](http://www.salute.gov.it/nuovocoronavirus). 

required packages: [pandas](https://pypi.org/project/pandas/), [numpy](https://pypi.org/project/numpy/),
[matplotlib](https://pypi.org/project/matplotlib/),[glob](https://pypi.org/project/glob3/),os,re,pylab,sys,[datetime](https://pypi.org/project/datetime3/)


## Usage

general.py

#### Inputs: 
general - Plot given variables in national level
state - plot given variables for given state(s)

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

<pre>python general.py state a'Intensive care' all</pre>

