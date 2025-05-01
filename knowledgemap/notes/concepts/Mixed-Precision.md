# Mixed Precision
- Weights are float32, but during forward pass, we use fp16 for everything.
- bf16 is like fp16, but has better dynamic range
- 1.5x - 3x speedup (for both, in my observation)
- You can increase batch size as well.

Last Reviewed: 4/30/25