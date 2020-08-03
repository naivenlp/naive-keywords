from typing import List


class AbstractCallback:

    def on_begin(self, **kwargs):
        raise NotImplementedError()

    def on_preprocess_begin(self, text, **kwargs):
        raise NotImplementedError()

    def on_preprocess_end(self, text, **kwargs):
        raise NotImplementedError()

    def on_extract_begin(self, text, **kwargs):
        raise NotImplementedError()

    def on_extract_end(self, keywords, **kwargs):
        raise NotImplementedError()

    def on_postprocess_begin(self, keywords, **kwargs):
        raise NotImplementedError()

    def on_postprocess_end(self, keywords, **kwargs):
        raise NotImplementedError()

    def on_end(self, keywords, **kwargs):
        raise NotImplementedError()


class CallbackWrapper(AbstractCallback):

    def __init__(self, callbacks: List[AbstractCallback] = None):
        self.callbacks = callbacks

    def on_begin(self, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_begin(**kwargs)

    def on_preprocess_begin(self, text, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_preprocess_begin(text, **kwargs)

    def on_preprocess_end(self, text, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_preprocess_end(text, **kwargs)

    def on_extract_begin(self, text, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_extract_begin(text, **kwargs)

    def on_extract_end(self, keywords, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_extract_end(keywords, **kwargs)

    def on_postprocess_begin(self, keywords, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_postprocess_begin(keywords, **kwargs)

    def on_postprocess_end(self, keywords, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_postprocess_end(keywords, **kwargs)

    def on_end(self, keywords, **kwargs):
        if not self.callbacks:
            return
        for callback in self.callbacks:
            if not callback:
                continue
            callback.on_end(keywords, **kwargs)
