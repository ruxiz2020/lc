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
    def test_hit_counter(self):
        hit_counter = HitCounter()

        # Record some hits
        hit_counter.hit(1)  # 1 hit at timestamp 1
        hit_counter.hit(2)  # 1 hit at timestamp 2
        hit_counter.hit(2)  # Another hit at timestamp 2

        # Check hits within 300 seconds
        self.assertEqual(hit_counter.getHits(2), 3)  # Hits: 1 at t=1, 2 at t=2
        self.assertEqual(hit_counter.getHits(301), 2)  # Hits at t=301: 2 from t=2
        self.assertEqual(hit_counter.getHits(302), 1)  # Hits at t=302: 1 from t=2

        # Add more hits at a later timestamp
        hit_counter.hit(600)  # 1 hit at timestamp 600
        self.assertEqual(hit_counter.getHits(600), 1)  # Only the hit at t=600
        self.assertEqual(hit_counter.getHits(601), 1)  # Only the hit at t=600
        self.assertEqual(hit_counter.getHits(900), 0)  # No hits within the last 300 seconds

if __name__ == "__main__":
    unittest.main()
