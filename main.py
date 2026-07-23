from banner import show_banner
from utils import validate_ip
from scanner import scan_target
from report import save_report


def main():
    # Display banner
    show_banner()

    # Ask user for target IP
    target = input("\nEnter Target IP Address: ").strip()

    # Validate IP
    if not validate_ip(target):
        print("\n❌ Invalid IP Address!")
        return

    # Scan ports
    results = scan_target(target, 1, 100)

    # Display summary
    print("\n" + "=" * 60)
    print("SCAN SUMMARY")
    print("=" * 60)

    if not results:
        print("No open ports found.")
    else:
        for port, service, risk in results:
            print(f"Port {port:<5} {service:<15} Risk: {risk}")

    # Save report
    filename = save_report(target, results)

    print("\n✅ Report saved successfully!")
    print("Location:", filename)


if __name__ == "__main__":
    main()