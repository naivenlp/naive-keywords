import abc


class AbstractStrategy(abc.ABC):

    def run(self, inputs, **kwargs):
        raise NotImplementedError()


class TFIDFStrategy(AbstractStrategy):

    def run(self, inputs, **kwargs):
        pass


class TextRankStrategy(AbstractStrategy):

    def run(self, inputs, **kwargs):
        pass


class EmbedRankStrategy(AbstractStrategy):

    def run(self, inputs, **kwargs):
        pass
