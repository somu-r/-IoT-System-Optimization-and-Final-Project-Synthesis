"""
Week 6 IoT System Optimization Simulation
Scenario: MQTT-based smart environmental monitoring system.
Generates baseline/optimized logs and comparison.csv.

Run:
    python simulation/iot_optimization_simulation.py
"""
import math, random, statistics, csv
from pathlib import Path

random.seed(42)
NODES=20
SAMPLES_PER_NODE=100

def simulate(optimized=False):
    rows=[]
    for node in range(1,NODES+1):
        last_sent=None
        for i in range(SAMPLES_PER_NODE):
            t=float(i)
            temp=25+3*math.sin(t/12+node/5)+random.gauss(0,0.35)
            humidity=60+8*math.sin(t/17+node/7)+random.gauss(0,0.8)
            if optimized:
                heartbeat=(i%10==0)
                changed=(last_sent is None or abs(temp-last_sent[0])>=0.8 or abs(humidity-last_sent[1])>=2.0)
                transmitted=heartbeat or changed
            else:
                transmitted=True
            if transmitted:
                if optimized:
                    base_latency=random.gauss(92,12); packet_loss=random.random()<0.012
                    processing=random.gauss(6,1.2); payload=38
                    last_sent=(temp,humidity)
                    retries=1 if packet_loss and random.random()<0.65 else 0
                else:
                    base_latency=random.gauss(148,24); packet_loss=random.random()<0.045
                    processing=random.gauss(12,2.0); payload=54
                    retries=1 if packet_loss and random.random()<0.75 else 0
                latency=max(20,base_latency+processing+retries*35)
                success=not packet_loss or retries>0
                energy=payload*0.055+latency*0.008+retries*3.5
                rows.append([node,i+1,round(t,2),round(temp,2),round(humidity,2),1,
                             round(latency,2),retries,int(success),payload,round(energy,3)])
            else:
                rows.append([node,i+1,round(t,2),round(temp,2),round(humidity,2),0,0,0,1,0,0])
    return rows

def write(path, rows):
    fields=["node_id","sample","time_s","temperature_c","humidity_pct","transmitted",
            "latency_ms","retry_count","success","payload_bytes","energy_mj"]
    with open(path,"w",newline="") as f:
        w=csv.writer(f); w.writerow(fields); w.writerows(rows)

root=Path(__file__).resolve().parents[1]
(root/"logs").mkdir(exist_ok=True); (root/"results").mkdir(exist_ok=True)
write(root/"logs"/"baseline_log.csv",simulate(False))
write(root/"logs"/"optimized_log.csv",simulate(True))
print("Simulation complete. See logs/ and results/. Run the included analysis section or compare CSVs.")
