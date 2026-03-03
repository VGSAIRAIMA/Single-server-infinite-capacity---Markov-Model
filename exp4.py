# M/M/1 Queue Model (∞ capacity, FIFO)

# INPUTS
arr_time = float(input("Enter mean inter-arrival time (seconds): "))
ser_time = float(input("Enter mean service time of Lathe Machine (seconds): "))
robot_time = float(input("Enter additional Robot time (seconds): "))

# Arrival and Service Rates
lam = 1 / arr_time                 # arrival rate λ
mu = 1 / (ser_time + robot_time)  # service rate μ

print("\n--------------------------------------------")
print("Single Server with Infinite Capacity (M/M/1):(∞/FIFO)")
print("--------------------------------------------")

print(f"Mean arrival rate (λ) = {lam:.4f} per second")
print(f"Mean service rate (μ) = {mu:.4f} per second")

# Stability condition
if lam < mu:

    # M/M/1 formulas
    Ls = lam / (mu - lam)          # avg number in system
    Lq = lam**2 / (mu*(mu-lam))    # avg number in queue
    Ws = 1 / (mu - lam)            # avg time in system
    Wq = lam / (mu*(mu-lam))       # avg waiting time in queue

    rho = lam / mu                 # utilization

    print("\n----- Results -----")
    print(f"Average number of materials in system (Ls) = {Ls:.3f}")
    print(f"Average number of materials in conveyor (Lq) = {Lq:.3f}")
    print(f"Average waiting time in system (Ws) = {Ws:.3f} sec")
    print(f"Average waiting time in conveyor (Wq) = {Wq:.3f} sec")
    print(f"Probability system is busy = {rho:.3f}")
    print(f"Probability system is empty = {1-rho:.3f}")

else:
    print("\nWARNING: System is unstable (Arrival rate ≥ Service rate)")
    print("Queue will grow infinitely (Overflow condition)")

print("--------------------------------------------")