#!/usr/bin/env python3

import sys
import subprocess

def exec_raw(command: str):
    print(f'exec_raw: {command}', file=sys.stderr, flush=True)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode != 0:
        raise RuntimeError(f'command failed with code: {process.returncode}')
    output = str(process.stdout.read().decode("utf-8")).strip("\n")
    print(f'exec_raw output: {output}', file=sys.stderr, flush=True)
    return output


if len(sys.argv) < 2:
    print('ERROR: a parameter is required!', file=sys.stderr)
    exit(1)

action = sys.argv[1]
if len(sys.argv) > 2:
    sink_name = sys.argv[2][:-1] # remove linebrak at the end
else:
    sink_name = ''


if action == 'list':
    sinks = exec_raw('pactl list short sinks')
    sinks = sinks.split('\n')
    for sink in sinks:
        sink = sink.split('\t')
        print(sink[1])

if action == 'run':
    exec_raw(f'pacmd set-default-sink "{sink_name}"')

