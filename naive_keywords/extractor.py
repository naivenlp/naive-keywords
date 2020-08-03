import abc
from typing import List

from .callback import AbstractCallback, CallbackWrapper
from .keyword import Keyword
from .postprocessor import AbstractPostprocessor
from .preprocessor import AbstractPreprocessor
from .strategy import AbstractStrategy


class AbstractExtractor(abc.ABC):

    def extract(self, inputs, **kwargs):
        raise NotImplementedError()


class KeywordsExtractor(AbstractExtractor):

    def __init__(self,
                 preprocessor: AbstractPreprocessor,
                 strategy: AbstractStrategy,
                 postprocessor: AbstractPostprocessor,
                 **kwargs):
        self.preprocessor = preprocessor
        self.strategy = strategy
        self.postprocessor = postprocessor

    def extract(self, inputs, callbacks: List[AbstractCallback] = None, **kwargs) -> List[Keyword]:
        text = inputs
        callback_wrapper = CallbackWrapper(callbacks=callbacks)
        callback_wrapper.on_begin(**kwargs)

        callback_wrapper.on_preprocess_begin(text, **kwargs)
        text = self.preprocessor.preprocess(text, **kwargs)
        callback_wrapper.on_preprocess_end(text, **kwargs)

        callback_wrapper.on_extract_begin(text, **kwargs)
        keywords = self.strategy.run(text, **kwargs)
        callback_wrapper.on_extract_end(keywords, **kwargs)

        callback_wrapper.on_postprocess_begin(keywords, **kwargs)
        keywords = self.postprocessor.postprocess(keywords, **kwargs)
        callback_wrapper.on_postprocess_end(keywords)

        callback_wrapper.on_end(keywords, **kwargs)
        return keywords
