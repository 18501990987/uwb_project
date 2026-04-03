import csv
import time

output_file = "uwb_log.csv"

headers = ["ts_ms", "anchor_id", "range_m", "valid", "quality"]

def fake_data():
    samples = [
        [1000, "A", 1.23, 1, 80],
        [1100, "B", 2.05, 1, 78],
        [1200, "C", 1.88, 1, 82],
    ]
    return samples

if __name__ == "__main__":
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for row in fake_data():
            writer.writerow(row)
            print("saved:", row)
            time.sleep(0.5)

    print("log saved to", output_file)