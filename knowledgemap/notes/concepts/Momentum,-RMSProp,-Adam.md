# Momentum, RMSProp, Adam

Notes from "A visual explanation"

Momentum in Physics - F = ma, a force will cause a constant change in velocity.
Same as momentum in ML - momentum = velocity, 
forces = decay (friction), and the additional gradient
derivative = applying a force for one time frame, leading to an acceleration (change in velocity)
momentum helps with plateaus and local minima


AdaGrad - history of squared gradients for a direction accumulate, updates in that direction are divided by this
encourages exploration in directions where not many changes have happened
escapes saddle points better - regular GD optimizes steeper features first
slow b/c squared gradient accumuates


RMSProp - squared gradients decay, squared gradients have momentum

Adam - gradients have momentum, so do squared gradients.
momentum allows for escaping local minima
sum of squares = explore new directions



Notes from Andrew NG:
Momentum cancels oscillations
Corrections are usually applied to Adam so things get rolling earlier
Last Reviewed: 11/9/24





