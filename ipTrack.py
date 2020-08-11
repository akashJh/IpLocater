#Imports Needed

from urllib.request import urlopen
import json 
import folium

#Tracing Data of the IP Addr
def getIP(ip):
	#ip=input("Enter the IP:")
	res=urlopen("http://ip-api.com/json/"+ip)
	data=res.read()
	values=json.loads(data)
	lat=float(values['lat'])
	lon=float(values['lon'])
	printData(values)
	makeMap(lat,lon)

#Printing IP Data
def printData(val):
	print("IP Data:")
	print(val)

#Making Map from Lat and Lon
def makeMap(lat,lon):
	map=folium.Map(location=[lat,lon],zoom_start=7)
	folium.Marker(location=[lat,lon],popup="Location Found").add_to(map)
	map.save("map.html")
	print("[*]Map Saved")

def main():
	ip=input("Enter the IP:")
	getIP(ip)

main()
