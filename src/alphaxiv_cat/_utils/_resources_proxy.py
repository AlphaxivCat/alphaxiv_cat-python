from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `alphaxiv_cat.resources` module.

    This is used so that we can lazily import `alphaxiv_cat.resources` only when
    needed *and* so that users can just import `alphaxiv_cat` and reference `alphaxiv_cat.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("alphaxiv_cat.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
