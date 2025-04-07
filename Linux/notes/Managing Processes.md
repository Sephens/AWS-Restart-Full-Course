# Managing Processes in Linux - Comprehensive Guide

## Table of Contents
- [Managing Processes in Linux - Comprehensive Guide](#managing-processes-in-linux---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Processes](#introduction-to-processes)
  - [Programs vs Processes](#programs-vs-processes)
  - [Process States](#process-states)
  - [Process Management Commands](#process-management-commands)
    - [ps command](#ps-command)
    - [pidof command](#pidof-command)
    - [pstree command](#pstree-command)
    - [top command](#top-command)
    - [kill command](#kill-command)
    - [nice and renice commands](#nice-and-renice-commands)
    - [jobs command](#jobs-command)
  - [Job Scheduling](#job-scheduling)
    - [at command](#at-command)
    - [cron command](#cron-command)
    - [crontab command](#crontab-command)
  - [Checkpoint Questions and Answers](#checkpoint-questions-and-answers)
  - [Key Takeaways](#key-takeaways)

## Introduction to Processes

A **process** in Linux is an instance of a running program. Each process has:
- A unique Process ID (PID)
- Its own memory space
- System resources allocated to it

**Key characteristics:**
- Processes can spawn child processes
- The first process (init or systemd) has PID 1
- Processes can be viewed with commands like `ps`, `pstree`, and `top`

**Example:** When you run `ls -l`, the shell creates a new process to execute this command.

## Programs vs Processes

| Concept       | Description | Examples |
|--------------|------------|----------|
| **Program** | A set of instructions stored on disk | `/bin/ls`, `/usr/bin/vim` |
| **Process** | A program that has been loaded into memory and is executing | `ls -l` running in your terminal |

**How a program becomes a process:**
1. System searches for executable in `$PATH`
2. Loads executable into memory
3. Assigns a PID
4. Schedules CPU time

**View your PATH:**
```bash
echo $PATH
# Typical output:
# /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/home/user/bin
```

## Process States

Processes cycle through these states:

1. **Start**: Process is created (via `fork()` and `exec()`)
2. **Ready**: Waiting for CPU time
3. **Running**: Executing on CPU
4. **Waiting**: Blocked (waiting for I/O, signal, etc.)
5. **Stopped**: Process suspended (via SIGSTOP)
6. **Zombie**: Process terminated but parent hasn't collected exit status

**Visualization:**
```
Start → Ready ↔ Running → Stopped
            ↖ Waiting ↙
```

## Process Management Commands

### ps command

Displays information about active processes.

**Common options:**
```bash
ps               # Shows processes for current shell
ps -e            # Shows all processes
ps -ef           # Full-format listing
ps -u username   # Processes for specific user
ps --forest      # Shows process hierarchy
```

**Example finding SSH processes:**
```bash
ps -ef | grep sshd
# Output shows PID, TTY, TIME, and CMD for sshd processes
```

**Advanced usage:**
```bash
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head
# Shows top CPU-consuming processes
```

### pidof command

Finds the PID of a running program.

**Examples:**
```bash
pidof sshd
# Output: 1234 5678 (PIDs of all sshd instances)

pidof -s nginx
# Shows only one PID if multiple exist
```

### pstree command

Displays processes in tree format showing parent-child relationships.

**Options:**
```bash
pstree -p       # Shows PIDs
pstree -a       # Shows command arguments
pstree user     # Shows processes for specific user
```

**Example output:**
```
systemd(1)─┬─sshd(1234)───sshd(5678)───bash(6789)
           ├─nginx(2345)─┬─nginx(2346)
           │             └─nginx(2347)
           └─crond(3456)
```

### top command

Real-time system monitoring tool showing process and resource usage.

**Key sections:**
1. System summary (uptime, load average)
2. Task counts (running, sleeping, stopped, zombie)
3. CPU usage breakdown (us, sy, id, etc.)
4. Memory usage
5. Process list (sorted by CPU by default)

**Interactive commands while running:**
- `M`: Sort by memory usage
- `P`: Sort by CPU usage
- `k`: Kill a process (prompts for PID)
- `q`: Quit

**Example launching top sorted by CPU:**
```bash
top -o %CPU
```

### kill command

Terminates processes by PID.

**Common signals:**
```bash
kill -15 PID   # SIGTERM (graceful termination, default)
kill -9 PID    # SIGKILL (forceful, immediate)
kill -19 PID   # SIGSTOP (pause process)
kill -18 PID   # SIGCONT (continue paused process)
```

**Example terminating unresponsive process:**
```bash
# First try graceful termination
kill 1234

# If still running, force kill
kill -9 1234
```

### nice and renice commands

Adjust process priority (niceness ranges from -20 to 19).

**Examples:**
```bash
nice -n 10 ./long_script.sh  # Start with low priority
renice -n 5 -p 1234         # Change priority of running process
```

**Best practices:**
- Regular users can only increase niceness (lower priority)
- Root can set any priority
- Critical system processes typically have negative niceness

### jobs command

Manages background and foreground jobs in current shell.

**Key commands:**
```bash
command &       # Run command in background
jobs            # List background jobs
fg %1           # Bring job 1 to foreground
bg %2           # Continue job 2 in background
CTRL+Z          # Suspend foreground job
```

**Example workflow:**
```bash
sleep 100 &     # Start in background
jobs            # Shows [1]  Running sleep 100 &
fg %1           # Bring to foreground
CTRL+Z          # Suspend it
bg %1           # Continue in background
```

## Job Scheduling

### at command

Schedules one-time tasks.

**Examples:**
```bash
at 4pm tomorrow
at> ./backup.sh
at> CTRL+D
# Job will run once at specified time

at -l          # List pending jobs
atrm 2         # Delete job number 2
```

### cron command

Schedules recurring tasks using crontab files.

**Crontab format:**
```
* * * * * command_to_run
│ │ │ │ │
│ │ │ │ └─ Day of week (0-6, 0=Sunday)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

**Special syntax:**
```bash
@reboot     Run at startup
@daily      Run once per day
@hourly     Run once per hour
```

### crontab command

Manages cron jobs.

**Key operations:**
```bash
crontab -e      # Edit user's crontab
crontab -l      # List cron jobs
crontab -r      # Remove all cron jobs
```

**Example crontab entry:**
```bash
0 3 * * * /path/to/backup.sh  # Run daily at 3 AM
*/5 * * * * /path/to/check.sh # Run every 5 minutes
```

**System cron directories:**
```bash
/etc/cron.hourly/
/etc/cron.daily/
/etc/cron.weekly/
/etc/cron.monthly/
```

## Checkpoint Questions and Answers

1. **Why might you need to stop a process?**
   - The process is unresponsive or frozen
   - The process is consuming excessive resources
   - The process is behaving maliciously
   - You need to free up system resources
   - Example: A web server using 100% CPU but not serving requests

2. **Why is `ps -ef | grep [process name]` useful?**
   - Quickly finds if a specific process is running
   - Identifies the PID of a process for management
   - Verifies that a service started successfully
   - Example: `ps -ef | grep nginx` shows all nginx processes

3. **What is the difference between the at and cron commands?**
   - `at`: Runs a task **once** at a specified time
     - Example: Run backup at 2am tonight
   - `cron`: Runs tasks **repeatedly** on a schedule
     - Example: Run backup every day at 2am

## Key Takeaways

1. **Process Fundamentals**
   - Every running program is a process with a unique PID
   - Processes have states: running, sleeping, stopped, zombie
   - Parent processes can spawn child processes

2. **Process Inspection**
   - `ps`: List processes
   - `pstree`: Show process hierarchy
   - `top`: Real-time system monitoring

3. **Process Control**
   - `kill`: Terminate processes
   - `nice/renice`: Adjust priority
   - `jobs`: Manage background/foreground processes

4. **Scheduling**
   - `at`: One-time tasks
   - `cron`: Recurring tasks
   - `crontab`: Manage scheduled jobs

5. **Best Practices**
   - Always try SIGTERM (15) before SIGKILL (9)
   - Use `ps -ef | grep` to find specific processes
   - Document cron jobs for maintenance
   - Test commands with `at` before setting up `cron` jobs

**Example Workflow for Troubleshooting:**
1. Identify problematic process with `top` or `ps`
2. Check process hierarchy with `pstree -p`
3. Try graceful termination with `kill -15 PID`
4. If unresponsive, force kill with `kill -9 PID`
5. Verify process ended with `ps -p PID`