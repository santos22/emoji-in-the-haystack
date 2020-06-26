import datetime

from haystack import indexes
from search.models import Emoji


class EmojiIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # code = indexes.CharField(model_attr='code')

    def get_model(self):
        return Emoji