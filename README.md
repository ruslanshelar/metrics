# Metrics script
   This python script allows you to print basic server metrics about your CPU and memory.

   Allowed commands:
   ```$xslt
   cpu
   mem
```

## Script usage examples

#### print CPU metrics

Execute script with **cpu** argument: `python metrics.py cpu`

#### print memory metrics

Execute script with **mem** argument:  `python metrics.py mem`

## Docker usage

Run docker container with command specified in allowed commands list
##### Example

```
docker run -t --rm shredderr/metrics:latest cpu

system.cpu.idel 36157203.91
system.cpu.user 1090674.92
system.cpu.guest 0.0
system.cpu.iowait 37102.74
system.cpu.stolen 11416.82
system.cpu.system 186124.65


```
