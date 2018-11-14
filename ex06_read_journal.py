#!/usr/bin/env python3
"""
- Read the system log and dump all lines.
- Use filter to dump only lines related to systemd
- Use map to extract only date and time
"""

from systemd import journal

def journal_filter(msg, identifier):
    return msg.get("SYSLOG_IDENTIFIER") == identifier 

def journal_map_datetime(logentry):
    return logentry["__REALTIME_TIMESTAMP"].strftime("%Y-%m-%d %H:%M:%S")

def journal_get_entries(jr):
    jr.seek_head()
    systemd_filter = filter(lambda entry: journal_filter(entry, "systemd"), jr)
    return map(journal_map_datetime, systemd_filter)

jreader = journal.Reader()
print(list(journal_get_entries(jreader)))


