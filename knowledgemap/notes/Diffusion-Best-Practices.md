# Diffusion Best Practices


- Training loss is a hard metric
- Normalize data to [-1, 1]
- small UNet = 10s of millions, large = 100s of millions
- use spatial attention
- Monitor:
    - Training loss
    - Valid loss
    - sample quality
    - gradient norm
- Maintain an EMA of weights
- Use warmup