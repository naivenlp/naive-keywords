class Keyword(object):

    def __init__(self):
        self.text = ""
        self.weight = 0.0
        self.tags = []

    def add_tag(self, tag):
        if tag in self.tags:
            return
        self.tags.append(tag)

    def __str__(self):
        return 'Keyword(text={}, weight={}, tags={})'.format(self.text or 'null', self.weight, self.tags)

    def __repr__(self):
        return {'text': self.text, 'weight': self.weight, 'tags': self.tags}


if __name__ == '__main__':
    keyword = Keyword()
    print(keyword)
    print(keyword.__str__())
    print(keyword.__repr__())

    keyword.add_tag('n')
    keyword.add_tag('s')
    print(keyword)
    print(keyword.__str__())
    print(keyword.__repr__())
