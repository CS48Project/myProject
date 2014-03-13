from haystack import indexes
from food.models import Food

class FoodIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	content_auto = indexes.EdgeNgramField(model_attr='name')

	def get_model(self):
		return Food

	def index_queryset(self, using=None):
		"""Used when the entire index for the model is updated."""
		return self.get_model().objects.all()
