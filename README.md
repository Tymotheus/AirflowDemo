# Airflow Demo
## KNI Kernel 3.04.2025

This is a repository showcasing some basic airflow functionalities, aimed to be demo-ed during the
lecture _Data Engineering @ ING: Introduction to the world of Big Data_ showcased at the meeting of
students' association **KNI Kernel AGH**.
Presentation is given by Tymoteusz Ciesielski and Jakub Mrówka.

In order to run the repo, requirements need to be installed.
You also need to generate your github PAT and add it for example in the Airflow UI.
Admin ==> Connections ==> Add ==> name: "github_default"

The repo was tested on macbook, there is a known issue for sending http requests on macs through python
and hence the NO_PROXY env var is set. Alternatively, mac_proxy_fix.py example is added.
