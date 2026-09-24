import json
import sys

def solution():
    data = json.load(sys.stdin)
    events = data["events"]

    dispute = {}
    valid = True

    for event in events:
        dispute_id = event["dispute_id"]
        event_type = event["type"]

        if event_type == "CREATE":
            if dispute_id in dispute:
                valid = False
                break

            dispute[dispute_id] = "OPEN"

        else:
            if dispute_id not in dispute:
                valid = False
                break

            status = dispute[dispute_id]

            if event_type == "SUBMIT_EVIDENCE":
                if status in ("OPEN","UNDER_REVIEW"):
                    dispute[dispute_id] = "UNDER_REVIEW"
                else:
                    valid = False
                    break

            elif event_type == "RESOLVE_WON":
                if status in ("UNDER_REVIEW", "OPEN"):
                    dispute[dispute_id] = "WON"
                else:
                    valid = False
                    break

            elif event_type == "RESOLVE_LOST":
                if status in ("UNDER_REVIEW", "OPEN"):
                    dispute[dispute_id] = "LOST"
                else:
                    valid = False
                    break

            else:
                valid = False
                break

    if not valid:
        print("ERROR")
        return

    dispute = dict(sorted(dispute.items()))
    print(json.dumps(dispute))



