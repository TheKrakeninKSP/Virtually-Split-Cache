# Virtually Split Cache (VSC)

The **Virtually Split Cache (VSC)** architecture is designed to dynamically allocate cache space for **data** and **instructions**, improving performance for **data-heavy applications**. Unlike traditional **split L1 caches**, which allocate fixed partitions for data and instructions, VSC adjusts cache allocation **dynamically** based on CPU demand.

While the conventional split L1 cache design is efficient for most computing tasks, it underutilizes cache space in programs where the balance between **data** and **instructions** is highly skewed. For example:
- **Tightly looped programs** reuse a small set of instructions, leaving most of the instruction cache idle.
- **Data-intensive programs** could benefit from **more L1 data cache space**, reducing cache misses.

## Allocation Algorithm

1. **Initial State**: Both cache partitions start with equal sizes.
2. **Monitoring**: CPU requests to each partition are counted.
3. **Reallocation**: If the difference exceeds **20%**, the larger partition gains **8 KB**, and the smaller loses **8 KB**.
4. **Reset Counters**: After reallocation, counters reset for the next cycle.
5. **Limitations**:
   - Minimum partition size: **8 KB**
   - Maximum partition size: **56 KB**
   - Prevents system integrity issues.

## Simulation Setup

### Assumptions:
- Baseline CPU clock speed: **4 GHz** (1 request per cycle).
- Initial cache hit rate: **95%** (Traditional Split Cache).
- Expected VSC hit rate: **99%** in skewed programs.
- Various cache miss penalties tested (e.g., **500, 200, 1000, 75 cycles**).

### Key Results:
- **Higher Miss Penalties (500+ cycles)**: VSC **outperforms** traditional split caches.
- **Lower Miss Penalties (≤ 75 cycles)**: Overhead of VSC **reduces its benefits**.
- **Balanced Workloads**: VSC **dynamically adapts**, improving overall efficiency.

## Inferences

- **VSC is beneficial** for workloads with **high data usage** and **skewed instruction access**.
- **Traditional Split Cache is better** when **instruction caching speed** is crucial.
- **VSC is ideal for specific architectures**, such as **bespoke processors** for **data-heavy applications**.

## Caveats & Conclusion

- **General-purpose CPUs may not benefit** from VSC due to **added overhead**.
- **Optimized for specialized workloads**, not consumer-grade hardware.
- VSC can be **an alternative architecture** in **low-latency, data-dominant environments**.

## References

This work is based on:  
Rolan, D., Fraguela, B. B., & Doallo, R. (2013). [Virtually Split Cache: An Efficient Mechanism to Distribute Instructions and Data](https://dl.acm.org/doi/abs/10.1145/2541228.2541234).
