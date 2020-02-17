def is_version_greater(version_1, version_2):
    from pkg_resources import parse_version
    return parse_version(version_1) > parse_version(version_2)
