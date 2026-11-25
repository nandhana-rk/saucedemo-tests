"""Turn reports/junit.xml into a Markdown test report (docs/TEST_REPORT.md)."""
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "reports/junit.xml")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "docs/TEST_REPORT.md")

root = ET.parse(src).getroot()
suite = root if root.tag == "testsuite" else root.find("testsuite")

rows, counts = [], {"PASS": 0, "FAIL": 0, "XFAIL": 0, "SKIP": 0}
for tc in suite.iter("testcase"):
    name = tc.get("name")
    t = float(tc.get("time", 0))
    if tc.find("failure") is not None or tc.find("error") is not None:
        status = "FAIL"
    elif tc.find("skipped") is not None:
        kind = tc.find("skipped").get("type", "")
        status = "XFAIL" if "xfail" in kind else "SKIP"
    else:
        status = "PASS"
    counts[status] += 1
    rows.append((tc.get("classname", "").split(".")[-1], name, status, t))

total = len(rows)
lines = [
    "# Test Execution Report",
    "",
    f"- **Application under test:** https://www.saucedemo.com",
    f"- **Tool:** Playwright (Python) + pytest",
    f"- **Generated:** {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}",
    f"- **Total duration:** {float(suite.get('time', 0)):.1f}s",
    "",
    "## Summary",
    "",
    "| Total | Passed | Failed | Known bugs (xfail) | Skipped |",
    "|---|---|---|---|---|",
    f"| {total} | {counts['PASS']} | {counts['FAIL']} | {counts['XFAIL']} | {counts['SKIP']} |",
    "",
    "`xfail` = test encodes the expected behaviour for a defect already listed in "
    "[BUG_LOG.md](BUG_LOG.md); it is expected to fail until the defect is fixed.",
    "",
    "## Results",
    "",
    "| Module | Test | Result | Time (s) |",
    "|---|---|---|---|",
]
for mod, name, status, t in rows:
    lines.append(f"| {mod} | `{name}` | {status} | {t:.2f} |")

out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {out}")
