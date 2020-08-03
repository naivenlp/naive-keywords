import abc


class AbstractPreprocessor(abc.ABC):

    def preprocess(self, text: str, **kwargs) -> str:
        raise NotImplementedError()


if __name__ == '__main__':
    print('hello')
