#!/usr/bin/env python3
"""
Jasper AI + External Design vs AdCreative.ai All-in-One Benchmark 2026.
Compares split copywriting/design tools against unified AI ad layout software.
"""
import argparse

def calculate_comparison(jasper_sub, graphic_sub, adcreative_sub):
    split_monthly = jasper_sub + graphic_sub
    monthly_diff = split_monthly - adcreative_sub
    annual_diff = monthly_diff * 12.0
    return {
        "split_monthly": split_monthly,
        "adcreative_sub": adcreative_sub,
        "monthly_diff": monthly_diff,
        "annual_diff": annual_diff
    }

def main():
    parser = argparse.ArgumentParser(description="Jasper vs AdCreative.ai Cost Comparison")
    parser.add_argument("--jasper-sub", type=float, default=49.0, help="Jasper Creator monthly in USD (default: $49.00)")
    parser.add_argument("--graphic-sub", type=float, default=400.0, help="External graphics labor/subscription in USD (default: $400.00)")
    parser.add_argument("--adcreative-sub", type=float, default=149.0, help="AdCreative.ai all-in-one in USD (default: $149.00)")
    args = parser.parse_args()

    res = calculate_comparison(args.jasper_sub, args.graphic_sub, args.adcreative_sub)
    print(f"Split Copy & Graphic Stack: ${res['split_monthly']:.2f}/mo")
    print(f"AdCreative.ai Unified Rate: ${res['adcreative_sub']:.2f}/mo")
    print(f"Monthly Net Difference:     ${res['monthly_diff']:.2f}/mo")
    print(f"Annual Total Advantage:     ${res['annual_diff']:.2f}/year")

if __name__ == "__main__":
    main()
