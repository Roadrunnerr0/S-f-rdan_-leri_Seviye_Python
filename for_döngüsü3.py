#FOR döngüsü - Ders 17.1
playlist = {
    "Metallica": "Enter Sandman",
    "Scorpions": "Maybe I Maybe You",
    "Pantera":"Piss",
    "Linkin Park": "Lying inside you"
}

for sanatci in playlist.keys(): #böyle yaparsak anahtarları yazmış oluruz yani müzik gruplarını
    print(sanatci) 

for sanatci in playlist.value(): #böyle yaparsakda şarkıları görmüş oluruz
    print(sanatci)