import math 

class Shape:
    """
    A base class for geometric shapes.
    This class provides a blueprint for creating shape objects and includes methods
    to calculate the area, perimeter, and semi-perimeter of a shape. Subclasses
    should override the `_CalcArea` and `_CalcPeri` methods to provide specific
    implementations for different shapes.

    Methods:
    --------
    _CalcArea():
        Abstract method to calculate the area of the shape. Must be implemented
        by subclasses.
    _CalcPeri():
        Abstract method to calculate the perimeter of the shape. Must be
        implemented by subclasses.
    _CalcSemiPeri():
        Calculates the semi-perimeter of the shape as half of the perimeter.
        Returns:
            float: The semi-perimeter of the shape.
    """

    def _CalcArea(self):
        pass
    def _CalcPeri(self):
        pass
    def _CalcSemiPeri(self):
        return self._CalcPeri()/2

class Circle(Shape):
    """
    This class inherits from the `Shape` base class and provides 
    methods to calculate the area, arc length, and perimeter of
    the circle/sector object.

    Attributes
    ----------
    radius : float
        The radius of the circle or sector. Must be a positive value.
    angle : float, optional
        The angle of the sector in radians. (default 2*math.pi)

    Methods
    -------
    __init__(radius, angle=2*math.pi)
        Initializes the Circle object with a given radius and angle.

    Raises
    ------
    TypeError
        If the radius or angle is not a numeric value.
    ValueError
        If the radius is negative or the absolute value of the angle is not in the range (0, 2π].
    """

    def __init__(self, radius, angle=(2*math.pi)):
        """
        Constructs all the necessary attributes for the circle object.

        Parameters
        -----------
        radius : float
            The radius of the circle or sector. Must be positive.
        angle : float , optional
            The angle of the sector in radians. (default 2*math.pi)
        
        Raises
        --------
        TypeError
            If the radius or angle is not a numeric value.
        ValueError
            If the radius is negative or the absolute value of the angle is not in the range (0, 2π].
        """

        if not isinstance(radius, (int, float)) or not isinstance(angle, (int, float)):
            raise TypeError("Radius and angle must be numeric values.")
        
        if (radius <= 0):
            raise ValueError("Radius must be positive.")
        
        if (abs(angle) > 2*math.pi or abs(angle) == 0):
            raise ValueError("The absolute value of the angle must be in the range (0, 2π].")

        self.radius = radius
        self.angle = angle

        self.area = self._CalcArea()
        self.arcLen = self._CalcArcLen()
        self.perimeter = self._CalcPeri()

    def _CalcArea(self):
        """
        Returns the area of the circle/sector.

        Parameters
        -----------
        None

        Returns
        --------
        float
            The area of the circle or sector.
        
        Raises
        ------
        None
        """
        return ((abs(self.angle) / 2) * (self.radius**2))

    def _CalcArcLen(self):
        """
        Calculates the arc length of the circle/sector.

        Parameters
        ----------
        None

        Returns
        -------
        float
            The arc length of the circle or sector.

        Raises
        ------
        None
        """
        return (abs(self.angle) * self.radius)
    
    def _CalcPeri(self):
        """
        Calculates the perimeter of the circle/sector.

        Parameters
        ----------
        None

        Returns
        -------
        float
            The perimeter of the circle or sector.

        Raises
        ------
        None
        """
    
        if (abs(self.angle) == 2*math.pi): # Circle
            return (abs(self.angle) * self.radius)
        
        else: # Sector
            return (abs((self.angle * self.radius)) + (2 * self.radius))

""" Left here for future proofing.
        if self. radius != 0: # To check if it's a point or an object.
            if self.angle >= 2 * math.pi: # Then it's a full circle, the perimeter doesn't change.
                return (2 * math.pi * self.radius)
            
            elif self.angle < (2 * math.pi) and self.angle > 0: # Then it's a sector, perimeter includes (2*radius).
                return (self.angle * self.radius) + (2 * self.radius)

            else: # Edge cases, where the angle is negative or 0.
                if self.angle == 0: # Then, it's a point, returns 0.
                    return 0
                elif self.angle < 0 and self.angle < (-1) * (2 * math.pi): # Then it's a sector, length cannot be negative, multiplies with (-1).
                    return (-1) * (self.angle * self.radius) + (2 * self.radius)
                else:
                    return (-1) * (2 * math.pi * self.radius) # Then it's a full circle, length cannot be negative, multiplies with (-1).
                
        else:
            return 0
"""

class Triangle(Shape):
    """
    This class inherits from the `Shape` base class and provides methods 
    to calculate the area and the perimeter of the triangle object.

    The triangle can be constructed using one of the following cases:
    1. SSS: All three sides (a, b, c) are provided.
    2. SAS: Two sides (a, b) and the included angle (gamma) are provided.
    3. ASA: One side (a) and two adjacent angles (beta, gamma) are provided.
    4. AAS: One side (a) and two opposite angles (alpha, beta) are provided.

    Attributes
    ----------
    a : float , optional
        A side of the triangle. Defaults to None.
    b : float , optional
        A side of the triangle. Defaults to None.
    c : float , optional
        A side of the triangle. Defaults to None.
    alpha : float , optional
        The angle seeing the side a. Defaults to None.
    beta : float, optional
        The angle seeing the side b. Defaults to None.
    gamma : float , optional
        The angle seeing the side c. Defaults to None.
    isTri : bool
        Indicates whether the triangle is valid.
    area : float
        The area of the triangle.
    peri : float
        The perimeter of the triangle.
    
    Methods
    -------
    __init__(a=None, b=None, c=None, alpha=None, beta=None, gamma=None)
        Initializes the Triangle object with given side lengths and angles.
        Validates the triangle and calculates its properties.
    _CalcPeri()
        Calculates the perimeter of the triangle.
    """

    INVALID_ARGS_MSG = (
    "Invalid arguments: Please provide a valid combination of sides and angles.\n"
    "Valid combinations are:\n"
    "1. SSS: a, b, c (all three sides)\n"
    "2. SAS: a, b, gamma (two sides and the included angle)\n"
    "3. ASA: a, beta, gamma (one side and two adjacent angles)\n"
    "4. AAS: a, alpha, beta (one side and two opposite angles)"
    )

    INVALID_ANG_SUM = (
    "Invalid triangle: The sum of the angles must be equal to π radians."
    )

    def __init__(self, a=None, b=None, c=None, alpha=None, beta=None, gamma=None):
        """
        Initializes the Triangle object with given side lengths and angles.

        Validates the triangle based on the provided attributes and calculates
        its properties (area and perimeter). The triangle can be constructed
        using one of the following cases:
        1. SSS: All three sides (a, b, c) are provided.
        2. SAS: Two sides (a, b) and the included angle (gamma) are provided.
        3. ASA: One side (a) and two adjacent angles (beta, gamma) are provided.
        4. AAS: One side (a) and two opposite angles (alpha, beta) are provided.

        Parameters
        ----------
        a : float, optional
            A side of the triangle. Defaults to None.
        b : float, optional
            A side of the triangle. Defaults to None.
        c : float, optional
            A side of the triangle. Defaults to None.
        alpha : float, optional
            The angle opposite side `a` (in radians). Defaults to None.
        beta : float, optional
            The angle opposite side `b` (in radians). Defaults to None.
        gamma : float, optional
            The angle opposite side `c` (in radians). Defaults to None.

        Raises
        ------
        ValueError
            If the provided attributes do not form a valid triangle.
        """
        isASA, isAAS, isSAS, isHeron, isTri = False, False, False, False, False # Required bools for case checks.

        # Validate the triangle based on the given attributes
        if a is not None and b is not None and c is not None:  # Case SSS
            # Calculating the unknown angles.
            gamma = math.acos((a**2 + b**2 - c**2)/(2*(a*b)))
            beta = math.acos((a**2 + b**2 - c**2)/(2*(a*c)))
            alpha = (math.pi - beta - gamma)

            if not (a + b > c and a + c > b and b + c > a):
                raise ValueError("Invalid triangle: The given side lengths do not satisfy the triangle inequality.")
            
            isHeron = True

        elif a is not None and b is not None and gamma is not None:  # Case SAS
            # Calculating the unknown side.
            c = math.sqrt((a**2) + (b**2) - 2*(a*b)*math.cos(gamma))
            
            if c == 0:
                raise ValueError("Invalid triangle: The given side lengths results in c being 0.")

            # Calculating the unknown angles.
            alpha = (math.sin(gamma)*(a/c))
            beta = (math.pi - alpha - gamma)

            if not (0 < gamma < math.pi):
                raise ValueError(self.INVALID_ANG_SUM)
            
            isSAS = True

        elif a is not None and beta is not None and gamma is not None:  # Case ASA
            # Calculating the unknown angle.
            alpha = (math.pi - beta - gamma)

            # Calculating the unknown sides lengths.
            b = (a * (math.sin(beta)/math.sin(alpha)))
            c = (a * (math.sin(gamma)/math.sin(beta+gamma)))

            if not math.isclose(beta + gamma, math.pi - alpha, rel_tol=1e-9):
                raise ValueError(self.INVALID_ANG_SUM)
            
            isASA = True

        elif a is not None and alpha is not None and beta is not None:  # Case AAS
            # Calculating the unknown angle.
            gamma = (math.pi - alpha - beta)

            if alpha == 0:
                raise ValueError("Invalid triangle: The angle alpha must be greater than zero.")

            # Calculating the unknown side lengths.
            b = (a * (math.sin(beta)/math.sin(alpha)))
            c = (a * (math.sin(gamma)/math.sin(alpha)))

            if not math.isclose(alpha + beta + gamma, math.pi, rel_tol=1e-9):
                raise ValueError("Invalid triangle: The sum of the angles must be equal to π radians.")

            isAAS = True

        else:
            raise ValueError(self.INVALID_ARGS_MSG)

        if any([isASA, isAAS, isSAS, isHeron]):
            isTri = True

        else:
            raise ValueError(self.INVALID_ARGS_MSG)

        if isTri:
            # If validation passes, set the attributes.
            self.a, self.b, self.c = a, b, c # Sides of the triangle.
            self.alpha, self.beta, self.gamma = alpha, beta, gamma # Angles of the triangle.

            # Initialize other attirbutes.
            #peri, semiperi, area = 0.0, 0.0, 0.0 # Perimeter, semiperimeter (used for Heron's Formula), and the area of the triangle.
            #self.peri, self.semiperi, self.area = peri, semiperi, area # Properties of the triangle.

            # Initialize bools of cases.
            self.isASA, self.isAAS, self.isSAS, self.isHeron = isASA, isAAS, isSAS, isHeron # Case of triangle.

            self.isTri = isTri # Validity of the triangle.

            self.peri = self._CalcPeri()
            self.semiperi = self._CalcSemiPeri()

            if (self.isHeron == True): # Case Heron
                self.area = math.sqrt(self.semiperi*(self.semiperi-self.a)*(self.semiperi-self.b)*(self.semiperi-self.c)) # Heron's Formula
            
            elif (self.isSAS == True): # Case SAS
                self.area = ((0.5) * (self.a * self.b) * math.sin(self.gamma))

            elif (self.isASA == True): # Case ASA
                self.area = ((self.a**2)/2)*((math.sin(self.beta)*(math.sin(self.gamma)))/(math.sin(self.alpha)))

            elif (self.isAAS == True): # Case AAS
                self.area = ((self.a**2)/2)*((math.sin(self.beta)*(math.sin(self.alpha+self.beta)))/(math.sin(self.alpha)))

            else:
                raise ValueError(self.INVALID_ARGS_MSG)

        else:
            raise ValueError(self.INVALID_ARGS_MSG)


    def _CalcPeri(self):
        """
        Calculates the perimeter of the triangle.

        Parameters
        ----------
        None

        Returns
        -------
        float
            The perimeter of the triangle if all sides are defined.

        Raises
        ------
        ValueError
            If one or more sides of the triangle are not defined.
        """
        if (self.a is not None and self.b is not None and self.c is not None):
            return self.a + self.b + self.c
        else:
            raise ValueError(self.INVALID_ARGS_MSG)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self._CalcArea()
        self.peri = self._CalcPeri()

    def _CalcArea(self):
        return self.length*self.width

    def _CalcSemiPeri(self):
        return self.length+self.width

    def _CalcPeri(self):
        return 2*self._CalcSemiPeri() # Semiperimeter of the rectangle
    
#tri = Triangle(3, b=None, c=None, alpha=math.pi/2, beta=math.pi/4)
#print(tri.area)
#print(tri.CalcArea())

#tri = Triangle(3,b=None,c=None, alpha=math.pi/2, beta=math.pi/4)
#print("%.4f" % tri.area)