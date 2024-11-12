from pandas.api.types import CategoricalDtype


pos_categorical_dtypes = {
    'syntactic category': CategoricalDtype(['noun', 'verb', 'adjective', 'adverb', 'function word', 'cardinal number', '.'], ordered=True),
}

# read https://spacy.io/models/en for all tags; use spacy.explain(tag) to get explanation of a tag

pos_mappings = {
    'POS tag': {
        "$": ".",
        "''": ".",
        ",": ".",
        "-LRB-": ".",
        "-RRB-": ".",
        ".": ".",
        ":": ".",
        "ADD": "UH",
        "AFX": "UH",
        "CC": "CC",
        "CD": "CD",
        "DT": "DT",
        "EX": "EX",
        "FW": "UH",
        "GW": "UH",
        "HYPH": ".",
        "IN": "IN",
        "JJ": "JJ",
        "JJR": "JJR",
        "JJS": "JJS",
        "LS": ".",
        "MD": "MD",
        "NFP": "UH",
        "NN": "NN",
        "NNP": "NNP",
        "NNPS": "NNS",
        "NNS": "NNS",
        "PDT": "PDT",
        "POS": "POS",
        "PRP": "PRP",
        "PRP$": "PRP$",
        "RB": "RB",
        "RBR": "RBR",
        "RBS": "RBS",
        "RP": "RP",
        "SYM": ".",
        "TO": "TO",
        "UH": "UH",
        "VB": "VB",
        "VBD": "VBD",
        "VBG": "VBG",
        "VBN": "VBN",
        "VBP": "VBP",
        "VBZ": "VBZ",
        "WDT": "WDT",
        "WP": "WP",
        "WP$": "WP$",
        "WRB": "WRB",
        "XX": ".",
        "_SP": ".",
        "``": ".",
    },
    'POS tag (compressed)': {
        "$": ".",
        "''": ".",
        ",": ".",
        "-LRB-": ".",
        "-RRB-": ".",
        ".": ".",
        ":": ".",
        "ADD": "UH",
        "AFX": "UH",
        "CC": "CC",
        "CD": "CD",
        "DT": "DT",
        "EX": "PRP",
        "FW": "UH",
        "GW": "UH",
        "HYPH": ".",
        "IN": "IN",
        "JJ": "adjective",
        "JJR": "adjective",
        "JJS": "adjective",
        "LS": ".",
        "MD": "MD",
        "NFP": "UH",
        "NN": "noun",
        "NNP": "noun",
        "NNPS": "noun",
        "NNS": "noun",
        "PDT": "DT",
        "POS": "POS",
        "PRP": "PRP",
        "PRP$": "PRP",
        "RB": "adverb",
        "RBR": "adverb",
        "RBS": "adverb",
        "RP": "RP",
        "SYM": ".",
        "TO": "TO",
        "UH": "UH",
        "VB": "verb",
        "VBD": "verb",
        "VBG": "verb",
        "VBN": "verb",
        "VBP": "verb",
        "VBZ": "verb",
        "WDT": "wh-word",
        "WP": "wh-word",
        "WP$": "wh-word",
        "WRB": "wh-word",
        "XX": ".",
        "_SP": ".",
        "``": ".",
    },
    'syntactic category': {
        "$": ".",
        "''": ".",
        ",": ".",
        "-LRB-": ".",
        "-RRB-": ".",
        ".": ".",
        ":": ".",
        "ADD": ".",
        "AFX": ".",
        "CC": "function word",
        "CD": "cardinal number",
        "DT": "function word",
        "EX": "function word",
        "FW": ".",
        "GW": ".",
        "HYPH": ".",
        "IN": "function word",
        "JJ": "adjective",
        "JJR": "adjective",
        "JJS": "adjective",
        "LS": ".",
        "MD": "function word",
        "NFP": ".",
        "NN": "noun",
        "NNP": "noun",
        "NNPS": "noun",
        "NNS": "noun",
        "PDT": "function word",
        "POS": "function word",
        "PRP": "function word",
        "PRP$": "function word",
        "RB": "adverb",
        "RBR": "adverb",
        "RBS": "adverb",
        "RP": "function word",
        "SYM": ".",
        "TO": "function word",
        "UH": ".",
        "VB": "verb",
        "VBD": "verb",
        "VBG": "verb",
        "VBN": "verb",
        "VBP": "verb",
        "VBZ": "verb",
        "WDT": "function word",
        "WP": "function word",
        "WP$": "function word",
        "WRB": "function word",
        "XX": ".",
        "_SP": ".",
        "``": ".",
    },
}