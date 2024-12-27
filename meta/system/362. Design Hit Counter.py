import unittest


class HitCounter:
    def __init__(self):
        # Arrays of size 300 (seconds in a 5-minute window).
        # self.timestamps[i] tracks the most recent timestamp
        # at the i-th slot. self.hits[i] tracks how many hits
        # occurred at that timestamp (in that slot).
        self.timestamps = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        # Map the current timestamp to an index in [0..299].
        i = timestamp % 300

        # If the slot's existing timestamp matches the current one,
        # it means we are still in the same second, so just increment.
        if self.timestamps[i] == timestamp:
            self.hits[i] += 1
        else:
            # Otherwise, this slot corresponds to an older time
            # outside the current second, so overwrite it.
            self.timestamps[i] = timestamp
            self.hits[i] = 1  # Reset the hit count for the new timestamp.

    def getHits(self, timestamp: int) -> int:
        # Sum up all hits for which the timestamp is within
        # the last 300 seconds (i.e., timestamp - stored_timestamp < 300).
        # If timestamp - t >= 300, it means the event is older than 5 minutes.
        return sum(
            h
            for t, h in zip(self.timestamps, self.hits)
            if timestamp - t < 300
        )



# --- Test Code -------------------------------------------------------------
class TestHitCounter(unittest.TestCase):
    def test_no_hits_initially(self):
        hc = HitCounter()
        self.assertEqual(hc.getHits(1), 0, "Initially, no hits should be recorded.")

    def test_simple_hits(self):
        hc = HitCounter()
        # Record a couple of hits at second 1
        hc.hit(1)
        hc.hit(1)
        # Record a hit at second 2
        hc.hit(2)

        # At second 2, we should see 3 hits in the last 300 seconds.
        self.assertEqual(hc.getHits(2), 3, "We expect 3 hits by second 2.")

        # At second 3, still 3 hits in the last 300 seconds (timestamps 1 and 2).
        self.assertEqual(hc.getHits(3), 3, "We expect 3 hits by second 3.")

    def test_hits_rolling_window(self):
        hc = HitCounter()
        # Suppose we add 2 hits at second 100, 1 hit at second 200.
        hc.hit(100)
        hc.hit(100)
        hc.hit(200)

        # At second 399, all 3 hits should still be counted (399 - 100 < 300).
        self.assertEqual(hc.getHits(399), 3, "All hits should be counted at second 399.")

        # At second 400, the hits at second 100 are exactly 300 seconds old,
        # meaning 400 - 100 = 300, which is outside the 300-second window.
        # So we should only count the hit at second 200.
        self.assertEqual(hc.getHits(400), 1, "Only the hit at second 200 should remain.")

    def test_edge_case_many_hits(self):
        hc = HitCounter()
        # Let’s add 5 hits at second 1
        for _ in range(5):
            hc.hit(1)
        self.assertEqual(hc.getHits(1), 5, "We expect 5 hits by second 1.")

        # Then add 300 hits at second 301 (which is exactly 300 seconds later).
        for _ in range(300):
            hc.hit(301)

        # Now at second 301, hits at second 1 are just out of range:
        # 301 - 1 = 300, so they're excluded. We should see 300 hits.
        self.assertEqual(hc.getHits(301), 300, "Only the 300 hits at second 301 should be counted.")

    def test_large_gap(self):
        hc = HitCounter()
        hc.hit(10)
        hc.hit(10)
        hc.hit(11)
        # At second 1010, these hits are far outside the 300-second window.
        self.assertEqual(hc.getHits(1010), 0, "Hits at second 10 and 11 should expire by second 1010.")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
