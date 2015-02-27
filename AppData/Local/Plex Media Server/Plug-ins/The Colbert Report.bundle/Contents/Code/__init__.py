NAME = 'The Colbert Report'
TCR_URL = 'http://thecolbertreport.cc.com'

EPISODES_URL = 'http://thecolbertreport.cc.com/full-episodes'
EPISODES_FEED = '%s/feeds/f1010/1.0/426a554e-f89f-4796-8aa3-60098c5b2645/279eb4d6-ecfd-11e0-aca6-0026b9414f30/%%s' % TCR_URL

TCR_SEARCH = '%s/feeds/f1030/1.0?keywords=&tags=%%s&sortBy=date&startingIndex=%%d' % TCR_URL

####################################################################################################
def Start():

	ObjectContainer.title1 = NAME
	HTTP.CacheTime = CACHE_1HOUR
	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'

####################################################################################################
@handler('/video/thecolbertreport', NAME)
def MainMenu():

	oc = ObjectContainer()

	if Client.Platform and Client.Platform not in ('Android'):
		oc.add(DirectoryObject(key=Callback(FullEpisodes), title=L('fullepisodes')))

	oc.add(DirectoryObject(key=Callback(ParseSearchResults, title2=L('allvideos')), title=L('allvideos')))
	oc.add(SearchDirectoryObject(identifier='com.plexapp.plugins.thecolbertreport', title=L('search'), prompt=L('searchprompt'), term=L('videos')))

	return oc

####################################################################################################
@route('/video/thecolbertreport/fullepisodes', allow_sync=True)
def FullEpisodes():

	oc = ObjectContainer(title2=L('fullepisodes'))

	html = HTML.ElementFromURL(EPISODES_URL)
	episode_id = html.xpath('//div[@id="video_player"]/@data-mgid')[0].split(':')[-1]

	json_obj = JSON.ObjectFromURL(EPISODES_FEED % episode_id)

	for result in json_obj['result']['episodes']:

		if result['type'] != 'episode':
			continue

		oc.add(EpisodeObject(
			url = result['canonicalURL'].replace('/episodes/', '/full-episodes/'),
			title = result['title'],
			summary = result['description'] if result['description'] != '' else result['shortDescription'],
			duration = int(float(result['duration']))*1000,
			thumb = Resource.ContentsOfURLWithFallback(url=result['images'][0]['url'] if len(result['images']) > 0 else ''),
			originally_available_at = Datetime.FromTimestamp(int(result['publishDate']))
		))

	return oc

####################################################################################################
@route('/video/thecolbertreport/search', page=int, allow_sync=True)
def ParseSearchResults(title2, tags='', page=0):

	oc = ObjectContainer(title2=title2)
	url = TCR_SEARCH % (String.Quote(tags), page*25)

	json_obj = JSON.ObjectFromURL(url, cacheTime=CACHE_1HOUR)

	for result in json_obj['result']['results']:

		if result['type'] != 'video':
			continue

		oc.add(VideoClipObject(
			url = result['canonicalURL'],
			title = result['title'],
			summary = result['description'],
			duration = int(float(result['duration']))*1000,
			thumb = Resource.ContentsOfURLWithFallback(url=result['images'][0]['url'] if len(result['images']) > 0 else ''),
			originally_available_at = Datetime.FromTimestamp(int(result['publishDate']))
		))

	if 'nextPageURL' in json_obj['result'] and json_obj['result']['nextPageURL'] != '':
		oc.add(NextPageObject(
			key = Callback(ParseSearchResults, title2=title2, tags=tags, page=page+1),
			title = L('more')
		))

	return oc
