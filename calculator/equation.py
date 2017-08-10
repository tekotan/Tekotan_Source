def solve_1(eq,var='x'):
    eq1 = eq.replace("=","-(")+")"
    c = eval(eq1,{var:1j})
    return "x= " + str(-c.real/c.imag)
import re

def solve_2(eq, var=('x', 'y')):
    var_re = re.compile(r'(\+|\-)\s*(\d*)\s*\*?\s*(x|y)')
    const_re = re.compile(r'(\+|\-)\s*(\-?\d+)$')

    constants, eqns, coeffs, default  = [],[], {'x': [], 'y': []}, {'': '1'}

    for e in eq.split(';'):
        eq1 = e.replace("="," - ").strip()
        if not eq1.startswith('-'):
            eq1 = '+' + eq1
        eqns.append(eq1)

    var_eq1, var_eq2 = map(var_re.findall, eqns)

    constants = [-1*int(x[0][1]) for x in map(const_re.findall, eqns)]
    [coeffs[x[2]].append(int((x[0]+ default.get(x[1], x[1])).strip())) for x in (var_eq1 + var_eq2)]
    
    ycoefficient = coeffs['y']
    xcoefficient = coeffs['x']

    # Adjust equations to take out y and solve for x
    if ycoefficient[0]*ycoefficient[1] > 0:
        ycoefficient[1] *= -1
        xcoefficient[0] *= ycoefficient[1]
        constants[0] *= -1*ycoefficient[1]        
    else:
        xcoefficient[0] *= -1*ycoefficient[1]
        constants[0] *= ycoefficient[1]
        
    xcoefficient[1] *= ycoefficient[0]
    constants[1] *= -1*ycoefficient[0]

    # Obtain x
    xval = sum(constants)*1.0/sum(xcoefficient)

    # Now solve for y using value of x
    z = eval(eqns[0],{'x': xval, 'y': 1j})
    yval = -z.real*1.0/z.imag

    return "x = " + str(xval) + " " + "y = " + str(yval)
