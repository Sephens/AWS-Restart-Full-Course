# Comprehensive Lab Guide: Internet Protocol Troubleshooting Commands

## Introduction
This lab provides hands-on experience with essential network troubleshooting commands across different OSI model layers. You'll learn to diagnose connectivity issues, analyze network paths, verify service availability, and test application-layer communication.

## Task 2: Practicing Troubleshooting Commands

### Layer 3 (Network) Commands

#### 1. ping Command
**Purpose**: Tests basic IP connectivity between hosts using ICMP packets.

**Command Example**:
```bash
ping 8.8.8.8 -c 5
```

**Options**:
- `-c 5`: Send exactly 5 packets (default continues until stopped)
- `-i 2`: Set interval between packets to 2 seconds
- `-s 100`: Set packet size to 100 bytes

**Expected Output**:
```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=12.3 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=11.8 ms
...
--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
```

**Troubleshooting Scenarios**:
- **No response**: Check security groups, NACLs, firewalls blocking ICMP
- **High latency**: Network congestion or routing issues
- **Packet loss**: Physical connectivity problems or overloaded devices

#### 2. traceroute Command
**Purpose**: Maps the network path and measures transit delays.

**Command Example**:
```bash
traceroute 8.8.8.8
```

**Options**:
- `-n`: Show numerical addresses (no DNS resolution)
- `-m 15`: Set max hops to 15 (default 30)
- `-w 2`: Wait 2 seconds per probe (default 5)

**Expected Output**:
```
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  10.0.0.1 (10.0.0.1)  1.234 ms  1.456 ms  1.678 ms
 2  192.168.1.1 (192.168.1.1)  5.432 ms  5.678 ms  5.901 ms
 ...
 8  8.8.8.8 (8.8.8.8)  12.345 ms  12.567 ms  12.789 ms
```

**Interpreting Results**:
- `***`: No response from that hop
- High latency spikes: Potential network congestion
- Consistent packet loss: Problem at specific network segment

### Layer 4 (Transport) Commands

#### 1. netstat Command
**Purpose**: Displays network connections, routing tables, and interface statistics.

**Command Examples**:
```bash
netstat -tp    # Established connections
netstat -tlp   # Listening services
netstat -ntlp  # Listening services (numeric)
```

**Options**:
- `-t`: TCP connections
- `-u`: UDP connections
- `-l`: Listening ports
- `-p`: Show PID/program name
- `-n`: Numeric output (no DNS resolution)

**Expected Output**:
```
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name
tcp        0      0 0.0.0.0:22    0.0.0.0:*       LISTEN 1234/sshd
tcp        0      0 10.0.1.5:22   192.168.1.10:54321 ESTABLISHED 5678/sshd: ec2-user
```

**Common Uses**:
- Verify service is listening on expected port
- Identify unexpected connections
- Check for port conflicts

#### 2. telnet Command
**Purpose**: Tests TCP connectivity to specific ports.

**Installation**:
```bash
sudo yum install telnet -y
```

**Command Example**:
```bash
telnet www.google.com 80
```

**Expected Successful Output**:
```
Trying 142.250.190.36...
Connected to www.google.com.
Escape character is '^]'.
```

**Common Responses**:
- `Connection refused`: Port closed/no service listening
- `Connection timed out`: Network/firewall blocking
- Successful connection: Port is open and service available

### Layer 7 (Application) Commands

#### curl Command
**Purpose**: Transfers data using various network protocols (HTTP, FTP, etc.)

**Command Example**:
```bash
curl -vLo /dev/null https://aws.com
```

**Options**:
- `-v`: Verbose output
- `-L`: Follow redirects
- `-o /dev/null`: Discard output
- `-I`: Fetch headers only
- `-k`: Ignore SSL errors

**Expected Output**:
```
* About to connect() to aws.com port 443 (#0)
* Connected to aws.com (54.239.28.85) port 443 (#0)
* Initializing NSS with certpath: sql:/etc/pki/nssdb
* SSL connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
> GET / HTTP/1.1
> User-Agent: curl/7.76.1
> Host: aws.com
> Accept: */*
> 
< HTTP/1.1 200 OK
< Content-Type: text/html
< Content-Length: 12345
...
```

**Troubleshooting Uses**:
- Verify web server response codes (200, 404, 500 etc.)
- Check SSL/TLS certificate validity
- Test API endpoints
- Compare response times

## Practical Troubleshooting Flow

1. **Connectivity Check**:
   ```bash
   ping 8.8.8.8
   ```

2. **Path Analysis**:
   ```bash
   traceroute 8.8.8.8
   ```

3. **Port Verification**:
   ```bash
   telnet example.com 443
   ```

4. **Service Validation**:
   ```bash
   curl -Iv https://example.com
   ```

5. **Local Service Check**:
   ```bash
   netstat -ntlp | grep 80
   ```

## Command Comparison Table

| Command | OSI Layer | Purpose | Key Options |
|---------|-----------|---------|-------------|
| ping | Network (3) | Basic connectivity | -c, -i, -s |
| traceroute | Network (3) | Path analysis | -n, -m, -w |
| netstat | Transport (4) | Connection monitoring | -t, -u, -l, -p |
| telnet | Transport (4) | Port testing | [port] |
| curl | Application (7) | HTTP testing | -v, -I, -k |

## Real-World Troubleshooting Scenarios

### Scenario 1: Web Server Unreachable
1. Check basic connectivity:
   ```bash
   ping webserver.example.com
   ```

2. Verify DNS resolution:
   ```bash
   nslookup webserver.example.com
   ```

3. Test HTTP port:
   ```bash
   telnet webserver.example.com 80
   ```

4. Check web service:
   ```bash
   curl -I http://webserver.example.com
   ```

### Scenario 2: High Latency to Database
1. Measure baseline latency:
   ```bash
   ping database.internal
   ```

2. Analyze network path:
   ```bash
   traceroute database.internal
   ```

3. Verify database port:
   ```bash
   telnet database.internal 5432
   ```

4. Check local connections:
   ```bash
   netstat -ntp | grep 5432
   ```

## Best Practices

1. **Start Simple**: Begin with ping before complex tools
2. **Work Up Layers**: Progress from Layer 3 to Layer 7
3. **Document Findings**: Record command outputs for comparison
4. **Use Multiple Tools**: Correlate results from different commands
5. **Understand Limitations**: Some hosts block ICMP or specific ports

This comprehensive guide provides the essential commands and methodologies for effective network troubleshooting across all OSI layers. By mastering these tools, you can systematically diagnose and resolve a wide range of network connectivity issues.