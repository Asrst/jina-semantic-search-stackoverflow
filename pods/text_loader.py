__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Dict

from jina.executors.crafters import BaseCrafter


class TextExtractor(BaseCrafter):
    def craft(self, text: str, *args, **kwargs) -> Dict:
        qid,text,tag = text.split(',')
        return dict(weight=1., text=text, meta_info=qid.encode('utf8'))
