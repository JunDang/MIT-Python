import urllib2
text = urllib2.urlopen("http://climate.weather.gc.ca/advanceSearch/searchHistoricDataStations_e.html?searchType=stnProv&timeframe=1&lstProvince=ON&optLimit=yearRange&StartYear=1900&EndYear=2015&Year=2015&Month=1&Day=28&selRowPerPage=1600&cmdProvSubmit=Search").read()
print text
