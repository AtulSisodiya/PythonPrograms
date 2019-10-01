names=[
	{'first':'asta','last':'yuno'},
	{'first':'noelle','last':'mimosa'},
	{'first':'nichronous','last':'zora'}]
lname= list(map(lambda x:x['last'].upper(),filter(lambda last:last['first']=='noelle',names)))
print(lname)
