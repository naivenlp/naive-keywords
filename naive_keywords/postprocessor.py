import abc
from typing import List

from .keyword import Keyword


class AbstractPostprocessor(abc.ABC):

    def postprocess(self, keywords: List[Keyword], **kwargs):
        raise NotImplementedError()


if __name__ == '__main__':
    print('hello')
