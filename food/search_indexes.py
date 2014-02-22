"""
search_indexes.py - Defines which models to be indexed for use with the 'haystack' app
"""

import datetime
from haystack import indexes
from food.models import Food

class FoodIndex(indexes.SearchIndex, indexes.Indexable):
	"""
	Indexes the Food model, enabling it to be searched.
	"""
	text = indexes.CharField(document=True, use_template=True)

	content_auto = indexes.EdgeNgramField(model_attr='name')

	def get_model(self):
		return Food

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.all()
