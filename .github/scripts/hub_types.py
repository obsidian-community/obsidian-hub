from typing import Dict, Union, List, Any, Optional

# Type aliases:

ThemeDownloads = Dict[str, Dict[str, Union[str, int]]]
ThemeSettings = List[Dict[str, str]]
ThemePluginSupport = Union[Dict[str, List[Union[str, Any]]], Dict[str, List[str]]]
ThemeStorage = Dict[str, Union[str, List[str], Optional[ThemeSettings], Optional[ThemePluginSupport], int]]