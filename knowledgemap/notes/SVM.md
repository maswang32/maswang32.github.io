# SVM

uses hinge loss

minimize max(0, 1 - y * f(x))

max(0, 1 - y_i (w * x_i + b))


1 - y_i y_hat_i

if y_i is 1, this is 1 - score

if it is -1, this is 1 + score

"1" is the margin

with no margin, when GT is positive, y_hat_i wants to be POSITIVE (- score will be negative)
with no margin, when GT is negative, y_hat_i wants to be large, negative (+ score will be small)


when we have the margin, 1 - score and y_i positive, then if we are super correct (y_hat_i > 1) there  is NO LOSS
when we have the margin, 1 + score is the loss (y_i negative), then there is NO LOSS  if score  is < -1 (we are super correct above a margin.) If the score  is -0.5, there  is still a loss!

see linear classifier notes



Last Reviewed: 10/28/2025