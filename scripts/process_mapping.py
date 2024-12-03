import pandas as pd
import re
from pm4py.objects.log.obj import EventLog, Trace, Event
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.alpha import algorithm as alpha_miner

# Paths to the files
case_txt_path = '../data/process/case_1.txt'
domains_csv_path = '../results/datamesh/domains.csv'

# Step 1: Extract process from case_1.txt
print("Step 1: Extracting process from case_1.txt")
with open(case_txt_path, 'r') as file:
    case_process = [line.strip() for line in file if line.strip()]

# Dynamically identify action verbs from the text
def extract_action_verbs(lines):
    verbs = set()
    for line in lines:
        # Use regex to find verbs based on sentence structure
        matches = re.findall(r'\b[A-Z][a-z]+s\b', line)  # Finds words ending with 's' and starting with an uppercase
        verbs.update(matches)
    return verbs

action_verbs = extract_action_verbs(case_process)
print(f"Dynamically identified action verbs: {action_verbs}")

# Function to extract activity dynamically
def extract_activity(line):
    for verb in action_verbs:
        if verb in line:
            return line.split(verb, 1)[-1].strip()
    return line  # Default: return the entire line if no verb is found

# Dynamically extract activities
activities = [extract_activity(line) for line in case_process]
print(f"Extracted activities: {activities}")

# Step 2: Create EventLog object from activities
print("Step 2: Creating event log")
event_log = EventLog()
trace = Trace()
for idx, activity in enumerate(activities):
    event = Event()
    event["concept:name"] = activity
    event["case:concept:name"] = "Case 1"  # Single case for this process
    event["time:timestamp"] = pd.Timestamp.now()  # Placeholder for timestamp
    trace.append(event)
event_log.append(trace)

# Step 3: Apply Alpha Miner to discover the process model (ignored visualization)
print("Step 3: Discovering process model (no visualization)")
net, im, fm = alpha_miner.apply(event_log)

# Step 4: Map domains from domains.csv
print("Step 4: Mapping domains from domains.csv")
domains_df = pd.read_csv(domains_csv_path)
domains_df["Keywords"] = domains_df[["Entity A", "Relationship", "Entity B"]].apply(lambda x: ", ".join(x), axis=1)

# Identify involved domains
involved_domains = []
for activity in activities:
    for _, row in domains_df.iterrows():
        if any(keyword.strip() in activity for keyword in row["Keywords"].split(", ")):
            involved_domains.append(row["Domain"])

# Remove duplicates
involved_domains = list(set(involved_domains))
print(f"Involved domains: {involved_domains}")
