"""Lesson 4 homework: baseline tasks.

Replace each `raise NotImplementedError` with your implementation.
You may use AI, as long as you can explain every line.
"""
import json

def count_selected(media_ids: list[str]) -> int:
    return len(set(media_ids))


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
   result: dict[str, list[str]] = {}
   for item in media:
        g_id = item.get("gallery_id")
        m_id = item.get("id")
        if g_id and m_id:
            result.setdefault(g_id, []).append(m_id)
   return result


def total_price(prices_minor: list[int | None]) -> int:
   return sum(p for p in prices_minor if p is not None)


def first_missing(required: list[str], present: list[str]) -> str | None:
    present_set = set(present)
    for item in required:
        if item not in present_set:
            return item
    return None


def load_events(path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
