from datetime import datetime
import os

def save_report(target, results):
    # Create reports folder if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/report_{target.replace('.', '_')}.txt"

    with open(filename, "w") as report:
        report.write("=" * 60 + "\n")
        report.write("SecureScan Pro - Scan Report\n")
        report.write("=" * 60 + "\n")
        report.write(f"Target : {target}\n")
        report.write(f"Date   : {datetime.now()}\n\n")

        if not results:
            report.write("No open ports found.\n")
        else:
            report.write(f"{'PORT':<10}{'SERVICE':<20}{'RISK'}\n")
            report.write("-" * 45 + "\n")

            for port, service, risk in results:
                report.write(f"{port:<10}{service:<20}{risk}\n")

    return filename