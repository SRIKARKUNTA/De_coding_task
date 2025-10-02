import json

def write_stats(stats: dict) -> None:
    """
    Write processing stats to JSON file.
    """
    with open('processing_stats.json', 'w') as f:
        json.dump(stats, f, indent=4)