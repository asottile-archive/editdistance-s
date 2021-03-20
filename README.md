[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.editdistance-s?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=70&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/70/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=70&branchName=master)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/editdistance-s/master.svg)](https://results.pre-commit.ci/latest/github/asottile/editdistance-s/master)

editdistance-s
==============

Fast implementation of the edit distance (Levenshtein distance).

### fork

this is a fork of [editdistance] with the following changes:

- `__hash__` based support is removed as it makes incorrect assumptions
- only strings (type `str`) are supported
- cffi replaces cython (so `abi3` wheels can be produced)
- the module is renamed to `editdistance_s`
- the public api does not contain `eval` (only `distance`)

[editdistance]: https://github.com/roy-ht/editdistance

### installation

```bash
pip install editdistance-s
```

- wheels should be available on pypi in most cases

### api

#### `distance(s1: str, s2: str) -> int`

compute the edit distance

```pycon
>>> import editdistance_s
>>> editdistance_s.distance('hello', 'hell☃')
1
```
