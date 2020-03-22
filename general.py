import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import glob, os, re, pylab, sys
from datetime import datetime


if sys.argv[1:][0] not in ['general','state']:
    raise TypeError('First Parameters must be general or state')
if sys.argv[1:][1] == 'all':
	parameters = [x.upper() for x in ['Hospitalized with symptoms','Intensive care','Home isolation','Total positive','Recovered','Death toll','Total cases','Tested']] 
else:
	parameters = sys.argv[1:][1].split(',')
	parameters = [x.upper() for x in parameters]
if sys.argv[1:][0] == 'general':
	if len(sys.argv[1:]) > 2:
		import warnings
		warnings.warn('Extra inputs in the end are ignored!')
if sys.argv[1:][0] == 'state':
	given_states = sys.argv[1:][2].split(',')
	given_states = [x.upper() for x in given_states]

xlsxs = glob.glob('general/*.xlsx')

# Empty Dataframes
grandtotal = pd.DataFrame(columns = ['Date','Hospitalized with symptoms','Intensive care','Home isolation','Total positive','Recovered','Death toll','Total cases','Tested'])
grandtotal.columns = [x.upper() for x in grandtotal.columns]
# Raise an error if input variable is not a variable
if all(elem in grandtotal.columns for elem in parameters) == False and sys.argv[1:][0] == 'general':
    raise TypeError('One or few of the given parameters are not provided by civil defense')
states = pd.DataFrame(columns = ['Date','State','Hospitalized with symptoms','Intensive care','Home isolation','Total positive','Recovered','Death toll','Total cases','Tested'])
states.columns = [x.upper() for x in states.columns]
for xlsx in xlsxs:
	data = pd.read_excel(xlsx, header=None,skiprows=1, encoding='utf-8')
	# Get Date
	match = re.search(r'\d{2}/\d{2}/\d{4}', data[1].iloc[0])
	date = datetime.strptime(match.group(), '%d/%m/%Y').date()
	# Remove Not first rows
	data = data.drop([0,1,2])
	# Give names
	data.columns = ['States','Hospitalized with symptoms','Intensive care','Home isolation','Total positive','Recovered','Death toll','Total cases','Tested','Temp']
	data.columns = [x.upper() for x in data.columns]	
	# Remove empty column
	data = data.drop(columns=['Temp'.upper()])
	# Remove total numbers
	data = data.drop([25, 26, 27, 28, 29])
	# Totale Row
	hospitalized = data['Hospitalized with symptoms'.upper()].iloc[-1]
	intensive = data['Intensive care'.upper()].iloc[-1]
	isolation = data['Home isolation'.upper()].iloc[-1]
	totalpos = data['Total positive'.upper()].iloc[-1]
	recovered = data['Recovered'.upper()].iloc[-1]
	death = data['Death toll'.upper()].iloc[-1]
	totalcase = data['Total cases'.upper()].iloc[-1]
	tested = data['Tested'.upper()].iloc[-1]
	# Remove Totale row
	data = data.drop([24])

	# Raise an error if given state is not in Italy
	if sys.argv[1:][0] == 'state':
		if given_states == ['ALL']:
			given_states = data['States'.upper()].str.upper().tolist()
		elif any(elem not in data['States'.upper()].str.upper().tolist() for elem in given_states) == True:
			raise TypeError('One or few of the given state(s) are not in Italy')
	# Grand Total
	grandtotal = grandtotal.append({'Date'.upper(): date,'Hospitalized with symptoms'.upper():hospitalized,
		'Intensive care'.upper():intensive,'Home isolation'.upper():isolation,'Total positive'.upper():totalpos,
		'Recovered'.upper():recovered,'Death toll'.upper():death,'Total cases'.upper():totalcase,'Tested'.upper():tested}, ignore_index=True)

	# States
	for index, row in data.iterrows():
		states = states.append({'Date'.upper(): date,'State'.upper():row[0].upper(),'Hospitalized with symptoms'.upper():row[1],
		'Intensive care'.upper():row[2],'Home isolation'.upper():row[3],'Total positive'.upper():row[4],
		'Recovered'.upper():row[5],'Death toll'.upper():row[6],'Total cases'.upper():row[7],'Tested'.upper():row[8]}, ignore_index=True)
# Grand total
if sys.argv[1:][0] == 'general':
	
	# gca stands for 'get current axis'
	ax = plt.gca()
	ax.set_yscale('log')
	# Set title and labels for axes
	ax.set(xlabel='Date',
	       ylabel='',
	       title='' )
	grandtotal.plot(kind='line',x='Date'.upper(),y=parameters,ax=ax)
	# Put a legend below current axis
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
	          fancybox=True, shadow=True, ncol=4)
	plt.grid('on')
	plt.show()
# State
if sys.argv[1:][0] == 'state':
	charar = np.chararray((len(given_states), len(parameters)), itemsize=500)
	for i, state in enumerate(given_states):
		for j, parameter in enumerate(parameters):
			charar[i][j] = str(state + ' ' + parameter)
	ax = plt.gca()
	# Set title and labels for axes
	ax.set(xlabel='Date',
	       ylabel='',
	       title='')
	ax.set_yscale('log')
	for i, state in enumerate(given_states):
		for j, parameter in enumerate(parameters):

			states[states['State'.upper()].str.match(state)].plot(kind='line',x='Date'.upper(),y=parameter,ax=ax,label=charar[i,j])
	# Put a legend below current axis
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
	          fancybox=True, shadow=True, ncol=7)
	plt.grid('on')
	plt.show()