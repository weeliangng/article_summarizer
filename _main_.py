from newspaper import Article

from summarizer import summarize



url = "https://www.channelnewsasia.com/sport/algerians-cheer-moroccos-world-cup-exploits-despite-tough-ties-3137471"

article = Article(url)
article.download()
article.parse()
#article.nlp()



print(summarize(article.text, 0.05))