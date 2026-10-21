# DEPRECATED !!! Superseeded by https://github.com/dealroom/python-urlextract

# urlextract

Wrapper for extracting only wanted parts from urls.

## Install

**pip:**
`pip install git+https://github.com/dealroom/data-urlextract@main`

**Poetry:**
`poetry add "git+https://github.com/dealroom/data-urlextract#main"`

## Usage

```python
>>> from dealroom_urlextract import extract

>>> extract('http://www.something.com/home.html?abc')
something.com
```

## Notes

Based on [tldextract](https://github.com/john-kurkowski/tldextract).
