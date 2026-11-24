import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ENTRY = "Once a year they set a cake on fire, sing at it, then eat the evidence. I joined in. 5/5, would sing again."

def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be blank"
    assert text.encode("utf-8").decode("utf-8") == text, "entry must round-trip as UTF-8"
    from pathlib import Path

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))

if __name__ == "__main__":
    main()
