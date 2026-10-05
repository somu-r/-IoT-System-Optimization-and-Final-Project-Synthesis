# Week 6 IoT System Optimization – Smart Environmental Monitoring

## Project overview
This project is a simulated IoT smart environmental monitoring system designed to demonstrate the Week 6 objective:
optimizing an existing IoT system to reduce latency, network traffic, energy consumption, and packet-retry overhead while improving reliability.

The simulated deployment contains **20 sensor nodes** sending temperature and humidity data to an MQTT gateway/broker and monitoring application.

## Optimization implemented
1. **Event-driven transmission:** nodes transmit when readings change beyond configurable thresholds instead of sending every sample.
2. **Periodic heartbeat:** a compact update is forced every 10 samples so the gateway can still verify node availability.
3. **Smaller application payload:** optimized messages use a smaller simulated payload.
4. **Retry-aware reliability:** the model includes packet-loss probability and limited retransmission.
5. **Gateway-oriented architecture:** aggregation is performed before data reaches the monitoring layer.

## Results
| Metric | Baseline | Optimized |
|---|---:|---:|
| Transmissions | 2000 | 701 |
| Average latency | 161.00 ms | 98.74 ms |
| P95 latency | 203.24 ms | 119.50 ms |
| Success rate | 98.95% | 99.71% |
| Total bytes | 108000 | 26638 |
| Total energy | 8701.56 mJ | 2036.30 mJ |

## Repository structure
```text
iot-week6-optimization/
├── README.md
├── docs/
│   └── Week6_IoT_Optimization_Report.docx
├── simulation/
│   └── iot_optimization_simulation.py
├── logs/
│   ├── baseline_log.csv
│   └── optimized_log.csv
└── results/
    └── comparison.csv
```

## How to run
Requires Python 3.9+.

```bash
python simulation/iot_optimization_simulation.py
```

The simulation uses a fixed random seed so the benchmark can be reproduced.

## Notes
This is a simulation-based academic project. The latency, loss, payload and energy models are intentionally simplified to demonstrate optimization methodology; they are not measurements from physical hardware.

## Suggested GitHub repository name
`iot-week6-system-optimization`

## Author
Student IoT Internship – Week 6 Final Project
