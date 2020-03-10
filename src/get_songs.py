def get_songs(artistid, song_dir = "songs"):
	song_dir = Path(song_dir)
	url = f"https://genius.p.rapidapi.com/artists/{artistid}/songs"

	headers = {
		'x-rapidapi-host': "genius.p.rapidapi.com",
		'x-rapidapi-key': "8c62b01aa3msh79ca17d82d4e5dep1a3ddejsn9346cf9aa3cb"
	}

	stepsize = 50
	page = 1
	
	response = requests.request("GET", url, headers=headers, params={"sort":"title","per_page":str(stepsize),"page":str(page)})
	song_page = response.json()['response']['songs']
	songs = song_page
	while response.json()['response']['next_page']:
		response = requests.request("GET", url, headers=headers, params={"sort":"title","per_page":str(stepsize),"page":str(page)})
		song_page = response.json()['response']['songs']
		songs.extend(song_page)
		page = response.json()['response']['next_page']
		
		for s in songs:
			if s['primary_artist']['id']==artistid and s['lyrics_state']=='complete':
				path = song_dir.joinpath( f"{s['primary_artist']['name']}_{s['title'].replace('/','')}.song")
				if not path.is_file():
					soup = BeautifulSoup(requests.get(s['url']).content, 'html.parser')
					lyrics_tag = soup.find('div', class_='lyrics')
					if lyrics_tag is not None:
						lyrics = lyrics_tag.get_text()
						f = open(path, "w")
						f.write(lyrics)
						f.close()
return songs