#Imports
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_headlines,search_news
from ..models import News,Headlines
from ..models import Review
from .forms import ReviewForm


#views

@main.route('/')
def index():
    """ 
    View root page function that returns the index page and its data 
    """
    #   getting news
    business_news=get_news('business')
    entertainment_news=get_news('entertainement')
    general_news=get_news('general')
    health_news=get_news('health')
    science_news=get_news('science')
    sports_news=get_news('sports')
    technology_news=get_news('technology')

    title = 'Home - News Center'


    search_search = request.args.get('search_query')

    if search_movie:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, general = general_news, entertainment = entertainment_news,health = health_news,sports = sports_news,science = science_news,technology = technology_news )

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = movie_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_movie(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)


@main.route('/headlines/<id>')
def headlines(id):
    """  
    View headlinse from a specific source
    """
    headlines = get_headlines(id)
    title = f'{id}'

    return render_template('news.html',title = title,headlines = headlines)
                          
                          
                          