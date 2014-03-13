from haystack import indexes
from food.models import Food

class FoodIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	content_auto = indexes.EdgeNgramField(model_attr='name')

	def get_model(self):
		return Food
