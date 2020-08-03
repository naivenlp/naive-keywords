import abc
import logging
import os

import jieba


class AbstractSpliter(abc.ABC):

    def split(self, tokens: List[str], **kwargs) -> List[str]:
        raise NotImplementedError()


class TokenSplitter(AbstractSpliter):

    def __init__(self, split_dicts=None, sep='\t'):
        super().__init__()
        self.split_dicts = split_dicts or []
        self.sep = sep
        self.split_map = {}

    def _load_split_dicts(self):
        if not self.split_dicts:
            return
        for f in self.split_dicts:
            if not os.path.exists(f):
                continue
            with open(f, mode='rt', encoding='utf8') as fin:
                for line in fin:
                    line = line.rstrip('\n').strip()
                    if not line:
                        continue
                    tokens = line.split(self.sep)
                    if len(tokens) != 2:
                        continue
                    from_token, to_token = tokens[0].strip(), tokens[1].strip()
                    self.add_split(from_token, to_token)

    def add_split(self, from_token, to_token):
        tokens = ''.join(to_token.split())
        if len(tokens) != len(from_token):
            return
        if not from_token:
            return
        self.split_map[from_token] = to_token

    def split(self, tokens, **kwargs) -> List[str]:
        results = []
        for token in tokens:
            if token in self.split_map:
                values = self.split_map.get(token)
                # split by space
                for v in values.split():
                    results.append(v)
            else:
                results.append(token)
        return results


class AbstractConcatenater(abc.ABC):

    def concat(self, tokens: List[str], **kwargs) -> List[str]:
        raise NotImplementedError()


class TokenConcatenater(AbstractConcatenater):

    def __init__(self, concat_dicts=None):
        super().__init__()
        self.concate_dicts = concat_dicts or []
        self.concate_set = set()

    def _load_concat_dicts(self):
        if not self.concate_dicts:
            return
        for f in self.concate_dicts:
            if not os.path.exists(f):
                continue
            with open(f, mode='rt', encoding='utf8') as fin:
                for line in fin:
                    line = line.rstrip('\n').strip()
                    if not line:
                        continue
                    concated_token = line
                    self.add_concate(concated_token)

    def add_concate(self, token):
        if not token:
            return
        self.concate_set.add(token)

    def concat(self, tokens: List[str], **kwargs) -> List[str]:
        if not tokens:
            return []
        results, stack = [],  []
        while tokens:
            if not stack:
                stack.append(tokens.pop(0))
                continue
            cur = tokens.pop(0)
            prev = stack.pop()
            concated = prev + cur
            if concated in self.concate_set:
                stack.append(concated)
                continue
            while stack:
                results.append(stack.pop(0))
            results.append(prev)
            stack.append(cur)
        return results


class AbstractTokenizer(abc.ABC):

    def tokenize(self, text, **kwargs):
        raise NotImplementedError()


class JiebaTokenizer(AbstractTokenizer):

    def __init__(self,
                 user_dicts: List[str] = None,
                 spliter: AbstractSpliter = None,
                 concater: AbstractConcatenater = None,
                 do_lower_case=True):
        super().__init__()
        self.user_dicts = user_dicts or []
        self.spliter = spliter
        self.concater = concater
        self.do_lower_case

    def _load_user_dict(self):
        if not self.user_dicts:
            return
        for f in self.user_dicts:
            if not os.path.exists(f):
                logging.warning('Load user dict {} failed. File does not exist.', f)
                continue
            with open(f, mode='rt', encoding='utf8') as fin:
                jieba.load_userdict(fin)
            logging.info('Load user dict: {} successfully.', f)

    def tokenize(self, text, **kwargs):
        tokens = []
        cut_all = kwargs.get('cut_all', False)
        hmm = kwargs.get('hmm', True)
        for t in jieba.cut(text, cut_all=cut_all, HMM=hmm):
            t = t.strip()
            if not t:
                continue
            if self.do_lower_case:
                t = t.lower()
            tokens.append(t)
        if self.spliter:
            tokens = self.spliter.split(tokens, **kwargs)
        if self.concater:
            tokens = self.concater.concat(tokens, **kwargs)
        return tokens
