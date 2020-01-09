from collections.abc import MutableMapping
from datetime import timedelta, datetime

class ExpirableMapping(MutableMapping):

	def __init__(self, mapping, ttl):
		self.mapping = mapping
		self.ttl = ttl
		self.expires = {}

	def _expired(self, key):
		return self.expires[key] <= datetime.now()

	def _expire_time(self):
		return datetime.now() + self.ttl

	def expire(self):
		for key in list(self.mapping):
			if self._expired(key):
				del self[key]

	def __getitem__(self, key):
		if self._expired(key):
			del self[key]
			raise KeyError(key)
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

	def __len__(self):
		self.expire()
		return len(self.mapping)

	def __repr__(self):
		self.expire()
		return repr(self.mapping)

	def __str__(self):
		self.expire()
		return str(self.mapping)
