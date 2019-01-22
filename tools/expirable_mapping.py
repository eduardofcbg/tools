from collections.abc import MutableMapping
from datetime import datetime, timedelta

from toolz.functoolz import memoize

class ExpirableMapping(MutableMapping):

	def __init__(self, ttl, mapping=None):
		self.ttl = ttl
		self.mapping = mapping or {}
		self.expires = {}

	def _expired(self, key):
		return self.expires[key] <= datetime.now()

	def _expire_time(self):
		return datetime.now() + self.timedelta

	def expire():
		for key in self.mapping:
			if self._expired(key):
				del self[key]

	def __getitem__(self, key):
		if self._expired(key):
			raise KeyError()
		return self.mapping[key]

	def __setitem__(self, key, value):
		self.mapping[key] = value
		self.expires[key] = self._expire_time()

	def __delitem__(self, key):
		del self.mapping[key]
		del self.expires[key]

	def __iter__(self):
		self.expire()
		return iter(self.mapping)

	def __len__():
		self.expire()
		return len(self.mapping)