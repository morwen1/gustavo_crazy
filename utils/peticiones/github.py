import requests



def obtain_repos():

	client_id = "c1ede9d9a43ce65cb242"
	client_secret="a41a0513048990f870c76fa6e2cf88656771c467"
	get = requests.get('https://api.github.com/users/whatever?client_id={}&client_secret={}'.format(client_id,client_secret))
	repos = "https://api.github.com/users/morwen1/repos"

	data = requests.get(repos)
	data=data.json()
	mined_data = []
	for i in data:
		if i['fork'] ==False:
			mined_data.append(i)
		return mined_data


