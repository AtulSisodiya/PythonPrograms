playlist={
'title': "College bus",
'created by': "atul sisodiya",
'songs':[
	{'title':'Kohinoor','artist':['Divine'],'duration':2.5},
	{'title':'pachtaoge','artist':['Arijit Singh'],'duration':3.1},
	{'title':'here i am','artist':['marshmello'],'duration':3.2},
	{'title':'friends','artist':['Mark luichi'],'duration':2.5}
]
}
totallength=0
for song in playlist['songs']:
	totallength+=song['duration']
print(totallength)
