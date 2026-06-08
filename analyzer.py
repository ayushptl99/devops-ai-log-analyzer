def analyze_log(log_content):

    log_content = log_content.lower()

    if "database" in log_content:
        return """
Root Cause:
Database connectivity issue

Severity:
High

Suggested Fix:
Check database status and connection details.
"""

    elif "memory" in log_content:
        return """
Root Cause:
Memory utilization issue

Severity:
Critical

Suggested Fix:
Increase memory or investigate memory leaks.
"""

    elif "timeout" in log_content:
        return """
Root Cause:
Request timeout

Severity:
Medium

Suggested Fix:
Check network latency and application response time.
"""

    else:
        return """
Root Cause:
Unknown

Severity:
Low

Suggested Fix:
Review application logs manually.
"""
