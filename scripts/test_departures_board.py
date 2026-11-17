"""Offline tests for departures_board.py: no network, no GitHub, nothing posted."""
import os, sys
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import departures_board as B

SHA_A, SHA_B = "a" * 40, "b" * 40


def run(monkeypatch, departed=(), returned=(), posts=None, argv=()):
    calls = []
    monkeypatch.setattr(B, "changes", lambda b, a: (list(departed), list(returned)))
    monkeypatch.setattr(B, "git", lambda *a: "2026-11-18")
    monkeypatch.setattr(B, "board", lambda repo: ("R", "C", dict(posts or {})))
    monkeypatch.setattr(B, "look", lambda url: "the URL answered 404 to GET and POST")
    monkeypatch.setattr(B, "submitter", lambda repo, n, u: (66, "someone", "2026-09-01"))
    monkeypatch.setattr(B, "gql", lambda q, **v: calls.append(("create" if "createDiscussion" in q else "reply", v)))
    monkeypatch.setattr(sys, "argv", ["x", "--before", SHA_A, "--after", SHA_B, *argv])
    B.main()
    return calls


def test_new_departure_posts_once_with_the_at(monkeypatch):
    calls = run(monkeypatch, departed=[("Zugabot Image Generation", "https://z.example/img")])
    assert [c[0] for c in calls] == ["create"]
    body = calls[0][1]["b"]
    assert body.splitlines() == ["**Zugabot Image Generation**", "`https://z.example/img`",
                                 "Listed 2026-09-01 (#66, @someone). Departed 2026-11-18: the URL answered 404 to GET and POST.",
                                 "It comes back the night it answers a 402 again."]


def test_rerun_posts_nothing(monkeypatch):
    posts = {("Zugabot Image Generation", "https://z.example/img"): ("D1", "")}
    assert run(monkeypatch, departed=[("Zugabot Image Generation", "https://z.example/img")], posts=posts) == []


def test_return_gets_one_reply_and_rerun_none(monkeypatch):
    key = ("Z", "https://z.example/img")
    calls = run(monkeypatch, returned=[key], posts={key: ("D1", "")})
    assert calls == [("reply", {"d": "D1", "b": "Back on the shelf 2026-11-18."})]
    assert run(monkeypatch, returned=[key], posts={key: ("D1", "Back on the shelf 2026-11-18.")}) == []


def test_departing_again_replies_not_reposts(monkeypatch):
    key = ("Z", "https://z.example/img")
    calls = run(monkeypatch, departed=[key], posts={key: ("D1", "Back on the shelf 2026-11-20.")})
    assert [c[0] for c in calls] == ["reply"] and calls[0][1]["b"].startswith("Departed again 2026-11-18")


def test_more_than_ten_refuses_and_posts_nothing(monkeypatch):
    many = [(f"L{i}", f"https://l{i}.example") for i in range(11)]
    with pytest.raises(SystemExit) as e:
        run(monkeypatch, departed=many)
    assert "REFUSED" in str(e.value)
    assert len(run(monkeypatch, departed=many, argv=["--allow-many"])) == 11


def test_no_before_commit_refuses(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["x", "--before", "0" * 40, "--after", SHA_B])
    with pytest.raises(SystemExit) as e:
        B.main()
    assert "REFUSED" in str(e.value)


def test_listings_parser_reads_shelf_lines():
    text = "## apis\n- [A](https://a.example/x) — desc\nnot a line\n- [B C](https://b.example) — d\n"
    assert B.listings(text) == {"https://a.example/x": "A", "https://b.example": "B C"}

def test_rerun_of_a_big_night_posts_nothing_and_stays_green(monkeypatch):
    many = [(f"L{i}", f"https://l{i}.example") for i in range(11)]
    assert run(monkeypatch, departed=many, posts={k: ("D", "") for k in many}) == []


def test_name_fallback_is_scoped_to_the_same_host(monkeypatch):
    asked = []
    def fake_first_pr(repo, needle):
        asked.append(needle)
        return (None, None) if len(asked) == 1 else ({"number": 9, "user": {"login": "x"}, "merged_at": "2026-08-01T00:00:00Z"}, "2026-08-01")
    monkeypatch.setattr(B, "first_pr", fake_first_pr)
    assert B.submitter("o/r", "Coinbase Developer Platform", "https://coinbase.com/cloud") == (9, "x", "2026-08-01")
    assert asked[1] == "[Coinbase Developer Platform](https://coinbase.com"


def test_a_failed_git_read_refuses_instead_of_reading_empty():
    with pytest.raises(SystemExit) as e:
        B.git("show", "0123456789abcdef0123456789abcdef01234567:DEPARTURES.md")
    assert "REFUSED" in str(e.value)
