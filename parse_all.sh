#!/bin/bash

grep -F "mimikatz(powershell) # sekurlsa::logonpasswords" *.txt -A 20 | grep Password -B2
