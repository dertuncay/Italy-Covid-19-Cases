import json, itertools, re, sys, glob
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib import cm
from descartes import PolygonPatch
from shapely.geometry import Polygon
from datetime import datetime

def isNaN(num):
    return num != num

def reg_fix(name):
	if name == 'Emilia-Romagna':
		return 'EMILIA ROMAGNA'
	elif name == 'Friuli-Venezia Giulia':
		return 'FRIULI V.G.'
	elif name == 'Trentino Alto-Adige':
		return 'TRENTO'
	else:
		return name

pars = ['Hospitalized with symptoms','Intensive care','Home isolation','Total positive','Recovered','Death toll','Total cases','Tested']
pars = [x.upper() for x in pars]
if sys.argv[1:][1].upper() in pars == False:
	raise TypeError('This measure is not provided by Italian Civil Defense')
par = sys.argv[1:][1].upper()

date_info = pd.DataFrame()
xlsxs = glob.glob('general/*.xlsx')
for xlsx in xlsxs:
	data = pd.read_excel(xlsx, header=None,skiprows=1, encoding='utf-8')
	# Get Date
	match = re.search(r'\d{2}/\d{2}/\d{4}', data[1].iloc[0])
	date = datetime.strptime(match.group(), '%d/%m/%Y').date()
	date_info = date_info.append({'Path': xlsx,'Date'.upper():date}, ignore_index=True)

given_date = datetime.strptime(sys.argv[1:][0], '%d/%m/%Y').date()
indx = date_info[date_info['DATE'] == given_date].index
if len(indx) == 0:
	raise TypeError('Check your given date! It must be dd/mm/YYYY format')

# Load json file
with open('italy_map/regioni.json') as json_file:
    json_data = json.load(json_file) # or geojson.load(json_file)
# Load xlsx file
data = pd.read_excel(date_info['Path'][indx[0]], header=None,skiprows=1, encoding='utf-8')
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
data = data.drop([24,25, 26, 27, 28, 29])
# Totale Row
# States
states = pd.DataFrame()
for index, row in data.iterrows():
	states = states.append({'Date'.upper(): date,'State'.upper():row[0].upper(),'Hospitalized with symptoms'.upper():row[1],
	'Intensive care'.upper():row[2],'Home isolation'.upper():row[3],'Total positive'.upper():row[4],
	'Recovered'.upper():row[5],'Death toll'.upper():row[6],'Total cases'.upper():row[7],'Tested'.upper():row[8]}, ignore_index=True)

fig = plt.figure() 
ax = fig.gca() 
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.axis('off')
# NUM_COLORS = len(json_data['features'])
norm = mpl.colors.Normalize(vmin = states[par].min(), vmax = states[par].max())
cmap = cm.autumn
m = cm.ScalarMappable(norm=norm, cmap=cmap)
total = 0
for i, region in enumerate(json_data['features']):
	poly = region['geometry']
	reg_name = region['properties']['regione']
	reg_name = reg_fix(reg_name)
	indx = states[states['STATE'] == reg_name.upper()].index[0]
	# Centroid
	C = Polygon(poly['coordinates'][0])
	if isNaN(states[par][indx]):
		num = 0
	else:
		num = int(states[par][indx])
	total += num 
	ax.annotate(s=reg_name + '\n' + str(num), xy=(C.centroid.x,C.centroid.y), horizontalalignment='center')
	ax.add_patch(PolygonPatch(poly, fc=m.to_rgba(states[par][indx]), ec='white', alpha=0.5, zorder= 2))
	ax.axis('scaled')
plt.xlim([6,19])
plt.ylim([36,48])
bol_indx = states[states['STATE'] == 'Bolzano'.upper()].index[0]
bolzano = int(states[par][bol_indx])
plt.title(par + ' on ' + str(date) + '\n Bolzano: ' + str(bolzano) + '\n Total: ' + str(total))
plt.show()
