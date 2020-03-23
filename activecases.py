import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import glob, os, re, sys
from datetime import datetime

if sys.argv[1:][0] not in ['city','state']:
    raise TypeError('First Parameters must be city or state')
if sys.argv[1:][0] == 'city' and sys.argv[1:][1] == 'all':
	raise TypeError('You do not want to see all cities in one graph believe me!')
if sys.argv[1:][0] == 'city':
	city_names = sys.argv[1:][1].split(',')
	city_names = [x.upper() for x in city_names]
elif sys.argv[1:][0] == 'state':
	state_names = sys.argv[1:][1].split(',')
	state_names = [x.upper() for x in state_names]

xlsxs = glob.glob('active_cases/*.xlsx')
# PDF2XLSX
# https://document.online-convert.com/convert/pdf-to-xlsx

# Empty Dataframes
grandtotal = pd.DataFrame(columns = ['Date','Number'])
states = pd.DataFrame(columns = ['Date','State','Number'])
cities = pd.DataFrame(columns = ['Date','City','Number'])
for xlsx in xlsxs:
	data = pd.read_excel(xlsx, encoding='utf-8')
	# Remove empty Rows
	data = data[data.iloc[:, 0].notna()]
	# Remove non-city rows
	noncities = ['in fase di verifica e aggiornamento','In aggiornamento','Friuli in aggiornamento','Altro/In fase di aggiornamento','Da aggiornare','in fase di aggiornamento',
	'altro/in fase di aggiornamento','altro/in fase di verifica','altro in fase di aggiornamento']
	data = data[~data.iloc[:, 0].isin(noncities)]

	# Date info
	match = re.search(r'\d{2}/\d{2}/\d{4}', data.columns[0])
	date = datetime.strptime(match.group(), '%d/%m/%Y').date()

	first_column = data.iloc[:, 0]
	second_column = data.iloc[:, 1]

	# Grand Total
	gt_index = data[first_column == 'Totale Generale'].index[0]
	grandtotal = grandtotal.append({'Date': date,'Number': second_column[gt_index]}, ignore_index=True)

	# Fix Enna
	enna_index = data[first_column == 'Enna'].index
	for enna in enna_index:
		if np.isnan(second_column[enna]):
			second_column[enna] = 0

	# State
	first_column = first_column.replace('TOTALE', 'Totale')
	totale_index = data[first_column == 'Totale'].index
	nan_index = second_column.index[second_column.apply(np.isnan)] #data[second_column == np.nan].index
	# print(totale_index,nan_index)
	for totale,nan in zip(totale_index,nan_index):
		# print(first_column[nan],second_column[totale])
		states = states.append({'Date': date,'State':first_column[nan].upper(), 'Number': int(second_column[totale])}, ignore_index=True)

	for i,(col1,col2) in enumerate(zip(first_column,second_column)):
		# Delete (aggiornamento mancante) from Parma
		if '(aggiornamento mancante)' in col1:
			col1 = col1.replace(' (aggiornamento mancante)', '')
		# City
		cities = cities.append({'Date': date,'City':col1.upper(), 'Number': col2}, ignore_index=True)

if  sys.argv[1:][0] == 'state':
	if state_names == ['ALL']:
		state_names = states.State.unique()
	elif any(elem not in states['State'].str.upper().tolist() for elem in state_names) == True:
		raise TypeError('One or few of the given state(s) are not in Italy')
if  sys.argv[1:][0] == 'city':
	if any(elem not in cities['City'].str.upper().tolist() for elem in city_names) == True:
		raise TypeError('One or few of the given city(ies) are not in Italy')



## Grand total
# # gca stands for 'get current axis'
# ax = plt.gca()
# grandtotal.plot(kind='line',x='Date',y='Number',ax=ax)
# plt.show()

# # State
# state_name = 'FRIULI VENEZIA GIULIA'
# ax = plt.gca()
# # Set title and labels for axes
# ax.set(xlabel='Date',
#        ylabel='',
#        title='Number of Infected People at ' + state_name)
# ax.set_yscale('log')

# states[states['State'].str.match(state_name)].plot(kind='line',x='Date',y='Number',ax=ax)
# print(states[states['State'].str.match(state_name)])
# ax.get_legend().remove()
# plt.grid('on')
# plt.show()


# # City
# city_name = 'Trieste'
# ax = plt.gca()
# # Set title and labels for axes
# ax.set(xlabel='Date',
#        ylabel='',
#        title='Number of Infected People at ' + city_name)
# ax.set_yscale('log')

# cities[cities['City'].str.match(city_name)].plot(kind='line',x='Date',y='Number',ax=ax)
# print(cities[cities['City'].str.match(city_name)])
# ax.get_legend().remove()
# plt.grid('on')
# plt.show()

# Cities
if sys.argv[1:][0] == 'city':
	ax = plt.gca()
	ax.set_yscale('log')

	# Give each state a unique color
	NUM_COLORS = len(city_names)
	cm = plt.get_cmap('gist_rainbow')
	ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
	for name in city_names:
		cities[cities['City'].str.match(name)].plot(kind='line',x='Date',y='Number',ax=ax,label=name)
	# Put a legend below current axis
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
	          fancybox=True, shadow=True, ncol=7)
	# Set title and labels for axes
	ax.set(xlabel='Date',
	       ylabel='',
	       title='Number of Infected People')
	plt.grid('on')
	plt.show()

# States
if sys.argv[1:][0] == 'state':
	ax = plt.gca()
	# Set title and labels for axes
	ax.set(xlabel='Date',
	       ylabel='',
	       title='Number of Infected People' )
	ax.set_yscale('log')
	# state_names = states.State.unique()
	# Give each state a unique color
	NUM_COLORS = len(state_names)
	cm = plt.get_cmap('gist_rainbow')
	ax.set_color_cycle([cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
	for name in state_names:
		states[states['State'].str.match(name)].plot(kind='line',x='Date',y='Number',ax=ax,label=name)
	# Put a legend below current axis
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
	          fancybox=True, shadow=True, ncol=7)
	plt.grid('on')
	plt.show()
