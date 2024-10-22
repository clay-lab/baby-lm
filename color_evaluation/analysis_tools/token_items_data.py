from collections import namedtuple
import numpy as np
from .pos_tags import pos_categorical_dtypes, pos_mappings
from .sumdata import *
from .word_ratings import *


token_field = 'token'


class Key(namedtuple('Key', ['token_id', 'pos'])):
    """
    token_id: token index
    pos: pos tag
    """

# string representations of row information


def row_prefix_str(row, tag_field='pos', tag_width=4, token_width=10, sep=' ', with_cnt=False, reverse_token_tag=True, align=True):
    if tag_field and not pd.isna(row[tag_field]):
        token_str = f"{row[token_field]:<{token_width}}"
        tag_str = f"{row[tag_field]:<{tag_width}}"
        prefix = (
            tag_str + sep + token_str
            if reverse_token_tag else
            token_str + sep + tag_str
        )
    else:
        prefix = (
            f"{row[token_field]:<{token_width + len(sep) + tag_width}}"
            if align else
            row[token_field]
        )
    if with_cnt:
        prefix += sep + f"{row['cnt']:>6}"
    return prefix


def row_str(row, names, **kwargs):
    return (row_prefix_str(row, with_cnt=True, **kwargs)
        + ': ' + ' '.join(f"{row[name].ppl:9.3f}" for name in names))


# extending items with various information


def extend_point_items(items, name, attr, n=None):
    if n is None:
        n = {'tsne': 2, 'eigen': 5, 'pca': 5}[attr]
    for idx in range(n):
        items[f'{name} {attr} {idx}'] = items[name].map(lambda value: getattr(value, attr + '_point')[idx])


def diff_field_suffix(baseline_name, value_attr):
    return f' {value_attr} - {baseline_name} {value_attr}'


def diff_field_name(name, baseline_name, value_attr):
    return name + diff_field_suffix(baseline_name, value_attr)


def extend_items_value_diff(items, name, baseline_name, value_attr):
    items[diff_field_name(name, baseline_name, value_attr)] = items[f'{name} {value_attr}'] - items[f'{baseline_name} {value_attr}']


def extend_items_for_name(items, name, baseline_name=None):
    # add f'{name} loss'
    items[f'{name} loss'] = items[name].map(lambda value: value.mean_loss)
    # add f'{name} prob'
    items[f'{name} prob'] = np.exp(-items[f'{name} loss'])

    if baseline_name is not None:
        # add f'{name} loss diff'
        extend_items_value_diff(items, name, baseline_name, 'loss')
        # add f'{name} prob diff'
        extend_items_value_diff(items, name, baseline_name, 'prob')

    try:
        # add tsne
        extend_point_items(items, name, 'tsne')
    except AttributeError:
        pass
    try:
        # add eigen
        extend_point_items(items, name, 'eigen')
    except AttributeError:
        pass
    try:
        # add pca
        extend_point_items(items, name, 'pca')
    except AttributeError:
        pass


def extend_pos(items):
    for pos_field, pos_mapping in pos_mappings.items():
        items[pos_field] = items['pos'].map(pos_mapping).astype(pos_categorical_dtypes.get(pos_field, 'category'))


def extend_items(items, names, idx2word, baseline_name=None):
    """Extend the fields of items
    """
    # extend various pos fields
    extend_pos(items)
    # add 'logcnt'
    items['logcnt'] = np.log(items['cnt'])

    # use the first name as the baseline by default
    if baseline_name is None:
        baseline_name = names[0]

    extend_items_for_name(items, baseline_name)  # get results from the baseline_name first
    for name in names:
        if name != baseline_name:
            extend_items_for_name(items, name, baseline_name)

    # add all fields from imported data
    try:
        concreteness_data.extend_items(items, 'conc Word', idx2word)
    except Exception as err:
        print('failed to extend items by concreteness data:')
        print(err)
    try:
        norm_data.extend_items(items, 'norm Word', idx2word)
    except Exception as err:
        print('failed to extend items by norm data:')
        print(err)
