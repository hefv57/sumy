# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from itertools import chain
from ..utils import cached_property
from ._sentence import Sentence


class Paragraph(object):
    def __init__(self, sentences):
        for sentence in sentences:
            if not isinstance(sentence, Sentence):
                raise TypeError("Only instances of class 'Sentence' are allowed.")

        self._sentences = tuple(sentences)

    @cached_property
    def sentences(self):
        return tuple(s for s in self._sentences if not s.is_heading)

    @cached_property
    def headings(self):
        return tuple(s for s in self._sentences if s.is_heading)

    @cached_property
    def words(self):
        return tuple(chain(*(s.words for s in self._sentences)))
