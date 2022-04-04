# Meraki Organization Port Checker
This script provides an automatic, 0-effort way to proactively check all MS model switch ports in your Meraki organization.

## Contacts
* Iván Ces Gándara 
 - https://www.linkedin.com/in/ivances/
 - Ivancesgandaravdj@gmail.com

## Solution Components
* Python3
* Meraki Dashboard API
* Excel


## Dependencies/Environment
Required Packages
 - Requests (pip install requests)
 - Json (pip install json)
 - Pandas (pip install pandas)
 - OS (pip install os)
 
 Provided under [requirements.txt](requirements.txt)

## Starting the Application
Once Dependencies are installed:

# Modify the following lines on the code:
Line 23 -> Modify it with the base URL of your Meraki Dashboard.

Line 37 -> Modify it with your user's API key.

# Start Application
 - Navigate on the CMD into the folder where the script is located.
 - Execute the script "meraki_org_port_check.py" with Python


# Application Output
 - The application will generate an Excel file with the state of all ports MS switches on the organization and, if some port is on error/failure state, the application will note the error description on the Excel for a quick view of the entire organization failures.

You can see an example of the Excel [here](./OUTPUT_DEMO/Report-2022-03-29_15-44-12.xlsx)


### Developer Resources
- Meraki API Reference - [See Docs](https://developer.cisco.com/meraki/api-v1/)

### LICENSE

Provided under MIT License, for details see [here](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
