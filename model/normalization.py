class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        #Since we are interating we need a loop
        # While loop ??
        # We can run it while the new value is less than the previous
        
        for i in range(iterations):
            gradient = 2 * init
            x_new = init - learning_rate * gradient
            init = x_new
        return round(init,5)



