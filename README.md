PRE-QUISITE:
1. prepare the .csv files into ./source directory
2. Set up connection to PostgreSQL DB on ./ref/config.py

TO RUN:
TASK 1 - to ingest CRM files:
1. from terminal/command prompt, change directory to the workspace test-dkatalis
2. to run CRM call center logs -> python ingest_crm.py --object crm_call_center_logs
3. to run CRM events -> python ingest_crm.py --object crm_events

TASK 2 - to display visual from LuxuryLoanPortfolio.csv:
1. from terminal/command prompt, change directory to the workspace test-dkatalis
2. to run CRM call center logs -> python luxury_loan.py --object luxury_loan_portfolio
3. using web-browser, go to http://localhost:4050/