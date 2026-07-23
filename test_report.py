
from report import save_report

sample_results = [
    (22, "SSH", "Medium"),
    (80, "HTTP", "Low"),
    (443, "HTTPS", "Low")
]

filename = save_report("127.0.0.1", sample_results)

print("Report created successfully!")
print("Saved as:", filename)