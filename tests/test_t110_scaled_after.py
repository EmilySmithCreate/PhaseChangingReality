"""T110's scaled window (scripts/run_t107_boundary_feet.scaled_after, 7 November 2026): the recorded times after the
escape scale with L / after_scale_length and round to the block; without the key the times are as written."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from run_t107_boundary_feet import scaled_after


def test_without_the_key_the_times_are_as_written():
    cfg = dict(after=[0, 50, 200, 500], block=10)
    assert scaled_after(cfg, 128) == [0, 50, 200, 500]


def test_with_the_key_the_times_scale_with_length_and_round_to_the_block():
    cfg = dict(after=[0, 50, 200, 500], block=10, after_scale_length=32)
    assert scaled_after(cfg, 32) == [0, 50, 200, 500]
    assert scaled_after(cfg, 48) == [0, 80, 300, 750]
    assert scaled_after(cfg, 64) == [0, 100, 400, 1000]
    assert scaled_after(cfg, 128) == [0, 200, 800, 2000]
    assert scaled_after(cfg, 256) == [0, 400, 1600, 4000]
    assert all(t % 10 == 0 for t in scaled_after(cfg, 48))
