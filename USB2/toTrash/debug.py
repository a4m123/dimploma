#!/usr/bin/env python3
import os
import time
from datetime import datetime

def main():
    message = "WATER LEAKEGE! - " + datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print((message))

if __name__ == "__main__":
    main()