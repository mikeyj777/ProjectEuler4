import numpy as np
from scipy.optimize import root
from scipy.optimize import newton
from datetime import datetime

# the Solver class has a main method "solve".  This works thru successive solver
# methods to attempt to provide a solution.
# the answer will be stored in Solver.answer.
# a direct solving method can be called.  For example, 
# "Solver.bisect()" can be called and will run the bisection method.
# all methods return a boolean based on their solved status.


class Solver:

    def __init__(self, args, arg_to_vary, fxn_to_solve, ytol, x_pct_diff_tol = 0.0001, max_iterations = 60, target = 0, bisect_params = {}, use_scipy = False, other_params = {}):

            self.args = args
            self.arg_to_vary = arg_to_vary
            self.fxn_to_solve = fxn_to_solve
            self.ytol = ytol
            self.x_pct_diff_tol = x_pct_diff_tol
            self.max_iterations = int(max_iterations)
            self.target = target
            self.bisect_params = bisect_params
            self.use_scipy = use_scipy
            self.other_params = other_params
            self.answer = -np.inf
            self.t_start = -1
            self.run_time = -1

    def set_bisect_parameters(self, lower_limit = 0, upper_limit = 1, output_increases_as_input_increases = True):
        # if secant fails, class will attempt bisection method.  
        # following parameters are needed for bisect meth:
        #
        # bisect_params['upper_limit']: float
        # bisect_params['lower_limit']: float

        # if decrease in x is expected to give an increase in y, this is
        # termed here an "inverse association". 
        # 'inverse_assoc' would be set to True.
        # bisect_params['inverse_assoc']: bool


        self.bisect_params = {
            'lower_limit': lower_limit,
            'upper_limit': upper_limit,
            'inverse_assoc': not output_increases_as_input_increases
        }



    def solve(self):
        self.t_start = datetime.now()
        if self.use_scipy:
            # print('attempting scipy newton method')
            if self.scipy_newton():
                return self.successful_return()

            # print('attempting scipy hybrid root method')
            if self.scipy_root():
                return self.successful_return()
                    
        # print('attempting secant method.')
        if self.solver_secant():
            return self.successful_return()

        # print('attempting bisection method.')
        if self.solver_bisect():
            return self.successful_return()

        return False

        
    def successful_return(self):
        
        self.run_time = datetime.now() - self.t_start
        # print(f'successfully completed in {self.run_time.seconds} sec.')
        return True

    def scipy_newton(self):
        res = newton(self.fxn_to_solve, self.arg_to_vary, args=(self.args,), maxiter=self.max_iterations, full_output=True, disp=False, tol=0.001)
        root_results = res[1]

        if root_results.converged:
            self.answer = res[0]
            return True


    def scipy_root(self):
        
        sol = root(self.fxn_to_solve, self.arg_to_vary, args=(self.args,))
        ans = -1
        if sol.success:
            self.answer = sol.x[0]
            return True
        print('scipy root hybrid method failed.')
        return False
    

    def solver_secant(self):
        # positive_only = False

        # if len(self.other_params) > 0:
        #     positive_only = self.other_params['positive answers only']
        x0 = self.arg_to_vary
        dt = x0 / 100
        if dt == 0:
            dt = 0.001
        y0 = self.fxn_to_solve(x0, self.args) - self.target
        x1 = x0 + dt
        y1 = self.fxn_to_solve(x1, self.args) - self.target
        if y1 - y0 == 0:
            return False
        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
        y2 = self.fxn_to_solve(x2, self.args) - self.target
        curr_x_pct_diff = (x2 - x1) / x1
        x0, x1 = x1, x2
        y0, y1 = y1, y2
        curr_iter = 0
        # check_for_pos = True
        t0 = datetime.now()
        while abs(curr_x_pct_diff) > self.x_pct_diff_tol and curr_iter < self.max_iterations:
            curr_iter += 1
            x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
            y2 = self.fxn_to_solve(x2, self.args) - self.target
            if y2 == y1:
                return False
            curr_x_pct_diff = (x2 - x1) / x1
            # print(f'secant method.  iter:{curr_iter}.  curr x:{self.sci_not(x2)}.  curr y:{self.sci_not(y2)}. x_diff: {self.sci_not(curr_x_pct_diff)}. ')
            x0, x1 = x1, x2
            y0, y1 = y1, y2
            

            #if there is a requirement that the calculated y value be greater than zero
            # check_for_pos = (not positive_only) or (positive_only and y2 > 0)

        if abs(curr_x_pct_diff) < self.x_pct_diff_tol:
            # print(f'x_tol:{self.x_pct_diff_tol} x2:{x2} curr_iter:{curr_iter}. time: {datetime.now() - t0}')
            self.answer = x1
            return True

        return False

    def sci_not(self,x, num_dps = 2):
        return ('{:.' + str(num_dps) + 'e}').format(x)

    def solver_bisect(self):
        
        if len(self.bisect_params) > 0:
                ulim = self.bisect_params['upper_limit']
                llim = self.bisect_params['lower_limit']
                # if decrease in x is expected to give an increase in y, this is
                # termed here an "inverse association". 
                # 'inverse_assoc' would be set to True.
                inverse_assoc = self.bisect_params['inverse_assoc']
        else:
            print('bisection parameters not provided')
            return False

        x0 = (ulim + llim) / 2
        ans = self.fxn_to_solve(x0, self.args)
        curr_iter = 0
        while abs(ans - self.target) > self.ytol and curr_iter < self.max_iterations:
            curr_iter += 1
            if ans > self.target:
                if inverse_assoc:
                    llim = x0
                else:
                    ulim = x0
            else:
                if inverse_assoc:
                    ulim = x0
                else:
                    llim = x0
            x0 = (llim + ulim) / 2
            ans = self.fxn_to_solve(x0, self.args)
            # print(f'iter:{curr_iter} ulim:{ulim} llim:{llim} x0:{x0} ans:{ans}')

        if abs(ans - self.target) <= self.ytol:
            self.answer = x0
            return True

        return False