# tests/test_takeover.py

from __future__ import annotations

from unittest.mock import MagicMock

import dns.resolver

from hunterx.modules.takeover.fingerprints import match
from hunterx.modules.takeover.resolver import CNAMEResolver


def test_match_finds_known_service():

    fp = match("myapp.herokuapp.com")

    assert fp is not None
    assert fp.service == "Heroku"


def test_match_returns_none_for_unknown_cname():

    fp = match("random.example.com")

    assert fp is None


def test_resolve_chain_detects_dangling():

    context = MagicMock()

    #
    # First call: CNAME lookup returns a Heroku target.
    # Second call: A lookup on that target raises NXDOMAIN,
    # confirming it's dangling.
    #

    cname_answer = MagicMock()

    cname_answer.target = "myapp.herokuapp.com."

    def resolve_side_effect(name, record_type):

        if record_type == "CNAME" and name == "sub.example.com":

            return [cname_answer]

        if record_type == "A":

            raise dns.resolver.NXDOMAIN

        raise dns.resolver.NXDOMAIN

    context.dns.resolver.resolve.side_effect = resolve_side_effect

    resolver = CNAMEResolver()

    chain, dangling = resolver.resolve_chain(
        context,
        "sub.example.com",
    )

    assert chain == ["myapp.herokuapp.com"]
    assert dangling is True




    # uv run pytest tests/test_takeover.py -v