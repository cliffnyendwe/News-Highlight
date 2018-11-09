class News:
    '''
    Movie class to define News Objects
    '''


  def __init__(self,id,name,url,category):
      self.id = id
      self.name = name 
      self.url = url 
      self.category = category 


class Review:

    all_reviews = []

      def __init__(self,id,title,description,url,urlToImage,publishedAt):
      self.id = id
      self.title = title
      self.description = description
      self.url = url
      self.urlToImage = urlToImage
      self.publishedAt = publishedAt

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response