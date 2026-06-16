#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Active-Modules.py (Core Async Orchestrator)"""

import asyncio
import sys
import argparse

async def run_module(script_name, target_url):
    print(f"[ACTIVE] Đang kích hoạt: {script_name}")
    proc = await asyncio.create_subprocess_exec(
        sys.executable, script_name, "--url", target_url,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    
    if proc.returncode == 0:
        print(f"[RESULT] {script_name} → SUCCESS")
        if stdout:
            print(stdout.decode('utf-8', errors='ignore').strip())
    else:
        print(f"[RESULT] {script_name} → FAILED")
        if stderr:
            print(stderr.decode('utf-8', errors='ignore').strip())

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True)
    args = parser.parse_args()

    # Kích hoạt đồng thời cả 4 Siphons phi chặn luồng
    await asyncio.gather(
        run_module("AI-Cache-Siphon.py", args.url),
        run_module("Bing-Siphon.py", args.url),
        run_module("Google-Siphon.py", args.url),
        run_module("Traffic-Siphon.py", args.url)
    )

if __name__ == "__main__":
    asyncio.run(main())
