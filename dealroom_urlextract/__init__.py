import tldextract


class InvalidURLFormat(Exception):
    pass


INVALID_CHARACTERS = [" ", "\\", "<", ">", "{", "}", ";"]


def extract(url: str, keep_subdomain: bool = True) -> str:
    """Extract the correct formatting for a given url.

    >>> extract('http://www.something.com/home.html?abc')
    'something.com'
    >>> extract('https://app.example.co.uk/something.html')
    'app.example.co.uk'

    Args:
        url: Any url-like string.

    Raises:
        InvalidURLFormat: if suffix is not valid (i.e. .com, .co, etc.) or the domain starts or ends with a hyphen "-".

    Returns:
        str: cleaned url with only wanted parts.
    """

    if not isinstance(url, str):
        raise InvalidURLFormat("URL must be string.")

    url = url.lower().strip()

    contains_invalid_char = any(
        invalid_char in url for invalid_char in INVALID_CHARACTERS
    )
    if contains_invalid_char:
        chars = "', '".join(INVALID_CHARACTERS)
        raise InvalidURLFormat(
            f"{url} Website urls can't contain these characters: '{chars}'"
        )

    # Domain and suffix are required
    subdomain, domain, suffix = tldextract.extract(url)
    if not domain or not suffix:
        raise InvalidURLFormat(
            f"{url} Domain or suffix are missing or could not be extracted."
        )

    # Check if format is valid
    if domain.startswith("-") or domain.endswith("-"):
        raise InvalidURLFormat(
            f"{url} Domain names can't have a hyphen as the first or last character"
        )

    # Exclude www subdomain, keep the rest
    if subdomain:
        if subdomain == "www":
            subdomain = ""
        if "www." in subdomain:
            subdomain = subdomain.replace("www.", "")

    website = domain + "." + suffix
    if keep_subdomain and subdomain:
        website = subdomain + "." + website

    return website.lower().strip()


def extract_with_path(url: str) -> str:
    """Extract the correct formatting for a passed url including the full path.

    >>> extract_with_path('http://www.something.com/home/asd.html?abc')
    'something.com/home/asd.html'
    >>> extract_with_path('https://app.example.co.uk/en/about/something.html')
    'app.example.co.uk/en/about/something.html'

    Args:
        url: Any url-like string.

    Raises:
        InvalidURLFormat: if suffix is not valid (i.e. .com, .co, etc.) or the domain starts or ends with a hyphen "-".

    Returns:
        str: cleaned url with only wanted parts.
    """
    url = url.lower().strip()
    base = extract(url)
    path = url.split(base, 1)[-1]
    if len(path) > 0:
        path = path.split("?")[0]
        if path[-1] == "/":
            path = path[:-1]
    return base + path
