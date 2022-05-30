<p align="center">
    <img src="image.png">
</p>

# ops

<p align="center">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/subatiq/ops?color=black&style=for-the-badge">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/opservatory-cli?color=black&style=for-the-badge">
  <img alt="GitHub" src="https://img.shields.io/github/license/subatiq/ops?color=black&style=for-the-badge">
  <img alt="Gitlab code coverage" src="https://img.shields.io/gitlab/coverage/subatiq/ops/master?color=black&style=for-the-badge">
  <img alt="Code style" src="https://img.shields.io/badge/code%20style-black-black?style=for-the-badge">
</p>


[Opservatory](https://github.com/subatiq/opservatory) CLI

To use, deploy or use a deployed instance of Opservatory.

For more docs on Opservatory, go [here](https://subatiq.github.io/opservatory/)

---

## Install

```
pip install opservatory-cli
```


## Configure opservatory server

```
ops setup
```

In following prompts enter Opservatory server IP or hostname and port (80 by default). Configuration will be saved at `~/.ops/config.json`

## Check config 

```
ops config
```

The output will show the contents of the `config.json`.

## Finding free machines

```
ops free
```

Output will show the list of all free machines with specs. To show only IP addresses and basic info as hostname and CPU, execute:

```
ops free --compact
```

## Finding busy machines

Works the same as `ops free`:

```
ops busy
```



