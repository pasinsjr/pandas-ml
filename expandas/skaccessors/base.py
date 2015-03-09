#!/usr/bin/env python

import pandas as pd


def _maybe_sklearn_data(data, target):
    try:
        from sklearn.datasets.base import Bunch
        if isinstance(data, Bunch):
            if target is not None:
                raise ValueError("'target' can't be specified for sklearn.datasets")
            # this should be first
            target = data.target
            # instanciate here to add column name
            columns = getattr(data, 'feature_names', None)
            data = pd.DataFrame(data.data, columns=columns)
            return data, target
    except ImportError:
        pass

    return data, target
