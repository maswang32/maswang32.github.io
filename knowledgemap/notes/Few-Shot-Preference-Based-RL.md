# Few-Shot Preference-Based RL
- Start with an existing reward function, every k-steps, they ask for 10 new responses from their expert, who specifies new preferences based on their observation.

- Update the reward model:
    - at each fine-tuning step, start from reward model, and fine-tune based on ALL human annotations collected during the course of policy training


- reduces amount of data by 20x.
- Meta-World - what are the human preference? If the task is backflip, the human is asked if the robot has a good backflip or not.
- what about training the policy using expert-annotated rewards? Much more data inefficient, need more than 10 annotations.