# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V4SubscribeParams", "Subscription", "SubscriptionKeys"]


class V4SubscribeParams(TypedDict, total=False):
    subscription: Required[Subscription]


class SubscriptionKeys(TypedDict, total=False):
    auth: Required[str]

    p256dh: Required[str]


class Subscription(TypedDict, total=False):
    endpoint: Required[str]

    keys: Required[SubscriptionKeys]
