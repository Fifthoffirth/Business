import os

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

sample_content = {
    "Mathematics": {
        "general": """
Algebra Fundamentals
- Quadratic equations are equations of the form ax² + bx + c = 0
- The quadratic formula is x = (-b ± √(b² - 4ac)) / 2a
- Linear equations always form a straight line when graphed
- The slope of a line represents its steepness and direction
""",
        "AS91261": """
Level 2 Mathematics and Statistics: Algebraic Methods (AS91261)

Simplifying Expressions
- Simplify (2x³y²)/(4xy⁴) using the laws of indices
- Simplify (3a²b⁴)/(6ab²) × (2ab³) using index laws
- Express (x + 2)² - 4 in expanded form
- Simplify (x² + 3x)/(x + 3) by factoring where possible
- Write 8^(1/3) × 27^(1/3) in simplified form

Finding Unknown Values
- Solve for x in the equation log₂(x + 3) = 4
- Find the value of m where log₃(m + 1) = 2
- Determine x when 2ˣ = 16
- Solve the equation 3x² + 5x - 2 = 0
- Find p when 2p² - 7p + 3 = 0

Variable Relationships
- Express h in terms of r and V in the formula V = πr²h
- Make y the subject in the equation x = 2y² + 5y
- Express x in terms of a and b in the equation ax + b = x² + 1
- Rearrange the formula A = P(1 + r)ⁿ to make r the subject
- Express the radius r in terms of h if the surface area of a cylinder equals that of a cube with side length h

Real-World Applications
- A rectangle has length (x + 2) and width (x - 1). Express its area in simplified form
- The height of a ball after t seconds is given by h = -4.9t² + vt + 1.5. Find v if the ball reaches 2m at t = 0.5
- A box with square base has surface area 600cm². If the height is h cm, express the side length of the base in terms of h
- The cost C dollars of producing x items is C = 2x² + 50x + 1000. Find the cost of producing 10 items
- The profit P dollars from selling x items is P = 200x - (2x² + 50x + 1000). Find the number of items that gives maximum profit

Advanced Problems
- Find the value of k where y = 2x + k is tangent to y = x² - 4
- Determine the range of values for m where 2x² + mx + 3 ≥ 0 for all x
- Find the values of k where the line y = kx intersects the curve y = x² - 1 at exactly one point
- For what values of p will the equation x² + px + 4 = 0 have real solutions?
- Find the values of k where x² + kx + k = 0 has equal roots

Working Requirements
- All algebraic working must be shown clearly and logically
- Final answers must be given in their simplest form
- Solutions should demonstrate understanding of algebraic methods
- Real-world problems require clear interpretation and modeling
- Graphs should be clearly labeled with all important features shown
""",
        "AS91262": """
Level 2 Mathematics and Statistics: Calculus Methods (AS91262)

Gradient and Derivatives
- Find the gradient of the curve y = ax³ + bx² + cx + d at point (p,q)
- Find another point on the curve y = 2x³ - 9x² + 12x + 3 with the same gradient as at (1,8)
- Find the points where the gradient of f(x) = 3x² - 6x + 2 equals 5
- Show that the line y = mx + c is a tangent to the curve f(x) = ax³ + bx² + cx + d
- Find the gradient function f'(x) for f(x) = x⁴/4 - 2x³/3 - 12x² + 10

Integration and Area
- Find the function whose gradient function is f'(x) = 4x³ - 6x² - 4x passing through (2,-5)
- Find the area between the curve y = x² and the line y = 2x + 1 from x = 0 to x = 3
- Calculate the definite integral of f(x) = 2x³ - 4x² + 5x from x = 1 to x = 4
- Find the area enclosed by two curves f(x) = x² and g(x) = 2x - x²
- Determine the volume of revolution when y = √x is rotated about the x-axis from x = 0 to x = 4

Optimization Problems
- Find the dimensions of a rectangle with perimeter 400m that maximizes its area
- Determine the dimensions of a cylindrical can that minimizes surface area for a volume of 500cm³
- Find the point on the curve y = x² closest to the point (2,0)
- Maximize the profit P = 200x - (2x² + 50x + 1000) where x is the number of items
- Find the dimensions of a box with square base that maximizes volume given surface area 600cm²

Applications and Modeling
- A car decelerates at rate v = -2t m/s. Find the stopping time and distance
- The number of followers N after t days is given by N = 100t/(1+0.1t). Find the maximum followers
- The height of a ball is given by h = -4.9t² + vt + 1.5. Find v if h = 2 when t = 0.5
- The cost of producing x items is C = 2x² + 50x + 1000. Find the minimum cost
- The population growth rate is dP/dt = 0.1P(1-P/1000). Find when growth rate is maximum

Working Requirements
- Show all calculus working clearly and logically
- Include relevant diagrams where helpful
- State any assumptions made in modeling problems
- Verify maxima/minima using derivative tests
- Include units in contextual problems
""",
        "AS91578": """
Level 3 Mathematics and Statistics: Calculus Methods (AS91578)

Differentiation and Applications
1. Basic Differentiation
   - Differentiate f(x) = 4 - 9x⁴
   - Find dy/dx for y = x·sec(6x)
   - Differentiate y = (x² + 3x + 2)sin(x)

2. Parametric Differentiation
   - Given x = 3t² + 1 and y = cos(t), find dy/dx
   - Find velocity when displacement s(t) = ln(3t² + 5t + 2)
   - Solve parametric equations involving trigonometric functions

3. Second Derivatives and Inflection Points
   - Verify solutions to second-order differential equations
   - Find points of inflection for f(x) = ln(x)/x
   - Determine nature of stationary points
   - Analyze curves with multiple derivatives

4. Applications of Derivatives
   - Find ranges where functions are increasing/decreasing
   - Determine stationary points and their nature
   - Find equations of tangent lines
   - Solve optimization problems
   - Analyze rates of change in real-world contexts

5. Complex Functions
   - Functions with natural logarithms and exponentials
   - Combinations of trigonometric functions
   - Rational functions with quadratic terms
   - Implicit differentiation
   - Chain rule applications

6. Limits and Continuity
   - Evaluate limits as x approaches specific values
   - Identify points where functions are continuous but not differentiable
   - Analyze function behavior near critical points
   - Determine existence of limits

7. Real-World Applications
   - Rate problems (e.g., volume changes in geometric shapes)
   - Optimization of areas and volumes
   - Motion problems (velocity and acceleration)
   - Related rates
   - Maximum/minimum problems

Working Requirements:
- Clear and logical presentation of calculus working
- Proper use of differentiation rules
- Verification of solutions where required
- Appropriate use of mathematical notation
- Complete justification of answers
- Clear identification of key steps in solutions

Note: This assessment requires:
- Understanding of differentiation techniques
- Application of chain rule, product rule, and quotient rule
- Analysis of function behavior
- Problem-solving in practical contexts
- Clear mathematical communication
"""
    },
    "Physics": {
        "Level 3 Physics 91523": """
Level 3 Physics: Wave Systems and Applications (91523)

1. Standing Waves and Harmonics
   - Formation of standing waves in pipes
   - Open and closed pipe systems
   - Nodes and antinodes
   - Harmonic frequencies
   - Wave patterns in musical instruments
   - Resonance and natural frequencies
   - Wavelength and frequency relationships

2. Wave Interference and Diffraction
   - Constructive and destructive interference
   - Single and double slit diffraction
   - Diffraction gratings
   - Path difference and phase relationships
   - Intensity patterns
   - Angular separation
   - Spectral analysis

3. Doppler Effect
   - Frequency changes with motion
   - Source and observer motion
   - Applications in sound and light
   - Frequency calculations
   - Beat frequencies
   - Wave compression and expansion
   - Real-world applications

Key Concepts and Applications:

A. Musical Instruments (Pan Flute Example)
   - Standing wave formation in pipes
   - Relationship between pipe length and frequency
   - Harmonic series in open/closed pipes
   - Tuning and frequency adjustment
   - Beat frequency applications
   - Wave speed calculations

B. Light and Diffraction (Laser Example)
   - Diffraction grating calculations
   - Spectral pattern formation
   - Order number significance
   - Wavelength effects
   - Pattern spacing relationships
   - White light dispersion
   - Resolution and intensity

C. Moving Sources (Train Example)
   - Frequency changes with motion
   - Speed calculations using Doppler shift
   - Graphical analysis of frequency changes
   - Observer position effects
   - Sound wave compression/expansion
   - Multiple observer perspectives
   - Real-world applications

Working Requirements:
1. Clear diagrams showing:
   - Wave patterns
   - Node/antinode positions
   - Interference patterns
   - Experimental setups

2. Mathematical working including:
   - Wave equations
   - Frequency calculations
   - Speed determinations
   - Angular relationships
   - Path differences

3. Written explanations of:
   - Physical principles
   - Cause and effect relationships
   - Pattern formations
   - Real-world applications
   - Experimental observations

4. Graph interpretation showing:
   - Frequency changes
   - Position relationships
   - Pattern variations
   - Data analysis
   - Trend explanations

Note: This assessment requires:
- Understanding of wave behavior
- Application of wave principles
- Mathematical problem-solving
- Clear communication of physics concepts
- Practical experimental knowledge
"""
    },
    "Chemistry": """
Atomic Structure
- Atoms are the basic units of matter
- Protons have positive charge and are found in the nucleus
- Electrons orbit the nucleus in energy levels
- The atomic number is the number of protons in an atom

Chemical Bonding
- Ionic bonds form between metals and non-metals
- Covalent bonds involve sharing of electrons
- Hydrogen bonds are relatively weak intermolecular forces
- Van der Waals forces exist between all molecules
""",
    # Add more subjects as needed
}

def create_sample_files():
    # Create subjects directory in the same folder as the script
    subjects_dir = os.path.join(SCRIPT_DIR, "subjects")
    if not os.path.exists(subjects_dir):
        os.makedirs(subjects_dir)
    
    for subject, content in sample_content.items():
        if isinstance(content, dict):
            # Handle nested content (like Mathematics)
            subject_path = os.path.join(subjects_dir, subject)
            if not os.path.exists(subject_path):
                os.makedirs(subject_path)
            
            # Create general content file
            with open(os.path.join(subject_path, "sample_content.txt"), "w", encoding='utf-8') as f:
                f.write(content["general"])
        else:
            # Handle regular content
            subject_path = os.path.join(subjects_dir, subject)
            if not os.path.exists(subject_path):
                os.makedirs(subject_path)
            
            # Create sample file
            with open(os.path.join(subject_path, "sample_content.txt"), "w", encoding='utf-8') as f:
                f.write(content)

def create_as91261_file():
    math_dir = os.path.join(SCRIPT_DIR, "subjects", "Mathematics")
    if not os.path.exists(math_dir):
        os.makedirs(math_dir)
    
    # Create AS91261 specific file
    with open(os.path.join(math_dir, "AS91261.txt"), "w", encoding='utf-8') as f:
        f.write(sample_content["Mathematics"]["AS91261"])

def create_as91262_file():
    math_dir = os.path.join(SCRIPT_DIR, "subjects", "Mathematics")
    if not os.path.exists(math_dir):
        os.makedirs(math_dir)
    
    # Create AS91262 specific file
    with open(os.path.join(math_dir, "AS91262.txt"), "w", encoding='utf-8') as f:
        f.write(sample_content["Mathematics"]["AS91262"])

def create_subject_structure(subject_path, subject_name):
    """Create the folder structure for a subject"""
    # Create main folders
    folders = ['exemplars', 'answers', 'resources']
    for folder in folders:
        folder_path = os.path.join(subject_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Create exemplar and answer pairs for Mathematics AS91261
    if subject_name == "Mathematics":
        exemplar_content = {
            "AS91261_exemplar1": {
                "question": """
Simplify (2x³y²)/(4xy⁴)
Working:
1. Group like terms
2. Apply index laws for division
3. Simplify coefficients
""",
                "answer": """
Solution:
(2x³y²)/(4xy⁴)
= (2/4)(x³/x)(y²/y⁴)
= (1/2)(x²)(y⁻²)
= x²/(2y²)

Key points:
- Coefficient simplification: 2/4 = 1/2
- Index law for division: x³/x = x² (subtract indices)
- Index law for division: y²/y⁴ = y⁻² (subtract indices)
"""
            },
            "AS91261_exemplar2": {
                "question": """
Solve the equation: 2x² - 7x + 3 = 0
Working:
1. Identify as quadratic equation
2. Use quadratic formula or factoring
3. Show all steps
""",
                "answer": """
Solution using factoring:
2x² - 7x + 3 = 0
(2x - 1)(x - 3) = 0
x = 1/2 or x = 3

Verification:
- When x = 1/2: 2(1/2)² - 7(1/2) + 3 = 2(1/4) - 7/2 + 3 = 1/2 - 7/2 + 3 = 0
- When x = 3: 2(3)² - 7(3) + 3 = 18 - 21 + 3 = 0
"""
            }
        }
        
        # Create exemplar files and their corresponding answers
        exemplars_path = os.path.join(subject_path, 'exemplars')
        answers_path = os.path.join(subject_path, 'answers')
        
        for exemplar_name, content in exemplar_content.items():
            # Save exemplar
            with open(os.path.join(exemplars_path, f"{exemplar_name}.txt"), 'w', encoding='utf-8') as f:
                f.write(content["question"])
            
            # Save answer
            with open(os.path.join(answers_path, f"{exemplar_name}_answer.txt"), 'w', encoding='utf-8') as f:
                f.write(content["answer"])

def create_as91578_file():
    math_dir = os.path.join(SCRIPT_DIR, "subjects", "Mathematics")
    if not os.path.exists(math_dir):
        os.makedirs(math_dir)
    
    # Create AS91578 specific file with new name
    with open(os.path.join(math_dir, "Level 3 Calculus 91578.txt"), "w", encoding='utf-8') as f:
        f.write(sample_content["Mathematics"]["AS91578"])

def create_physics_91523_file():
    physics_dir = os.path.join(SCRIPT_DIR, "subjects", "Physics")
    if not os.path.exists(physics_dir):
        os.makedirs(physics_dir)
    
    # Create Physics 91523 file
    with open(os.path.join(physics_dir, "Level 3 Physics 91523.txt"), "w", encoding='utf-8') as f:
        f.write(sample_content["Physics"]["Level 3 Physics 91523"])

def create_physics_91523_source():
    physics_dir = os.path.join(SCRIPT_DIR, "subjects", "Physics")
    if not os.path.exists(physics_dir):
        os.makedirs(physics_dir)
    
    content = """
Level 3 Physics: Wave Systems and Applications (91523)

1. Standing Waves in Musical Instruments
   - Formation of standing waves in pipes
   - Open and closed pipe harmonics
   - Node and antinode positions
   - Frequency calculations
   - Wave speed in air
   - Beat frequency analysis
   - Tuning techniques

   Example Questions:
   a) Draw and label nodes (N) and antinodes (A) for the third harmonic in a pan flute
   b) Calculate the frequency of a harmonic given pipe length and sound speed
   c) Explain standing wave formation in pipes with one closed end
   d) Solve tuning problems using beat frequency

2. Wave Interference and Diffraction
   - Diffraction grating principles
   - Order number and wavelength relationships
   - Pattern formation and analysis
   - Slit separation calculations
   - White light spectra
   - Angular separation
   - Intensity distribution

   Example Questions:
   a) Explain the meaning of nλ in diffraction gratings
   b) Calculate dot patterns from diffraction data
   c) Compare diffraction grating vs double slit patterns
   d) Analyze spectral formation with white light

3. Doppler Effect Applications
   - Frequency changes with motion
   - Source and observer perspectives
   - Speed calculations
   - Graphical analysis
   - Real-world applications
   - Wave compression and rarefaction
   - Frequency shift calculations

   Example Questions:
   a) Describe sound changes for moving sources
   b) Explain frequency changes for approaching objects
   c) Calculate source speed from frequency data
   d) Analyze frequency-position graphs

Working Requirements:
1. Diagrams must show:
   - Clear wave patterns
   - Labeled nodes and antinodes
   - Proper wavelength representation
   - Accurate pattern spacing

2. Calculations require:
   - Proper equation selection
   - Clear working steps
   - Correct units
   - Final answer verification

3. Explanations need:
   - Physical principles
   - Clear reasoning
   - Relevant examples
   - Proper terminology

4. Graph analysis includes:
   - Trend identification
   - Physical interpretation
   - Key point analysis
   - Relationship explanations

Assessment Notes:
- Show all working clearly
- Include relevant diagrams
- Use correct physics terminology
- Explain assumptions made
- Verify calculations where possible
"""
    
    # Create Physics 91523 file
    with open(os.path.join(physics_dir, "Level 3 Physics 91523.txt"), "w", encoding='utf-8') as f:
        f.write(content)

def create_chemistry_91390_source():
    chemistry_dir = os.path.join(SCRIPT_DIR, "subjects", "Chemistry")
    if not os.path.exists(chemistry_dir):
        os.makedirs(chemistry_dir)
    
    content = """
Level 3 Chemistry: Structure, Bonding and Energy (91390)

1. Molecular Structure and Bonding
   A. Lewis Structures and Molecular Shapes
      - Drawing Lewis dot structures
      - VSEPR theory and molecular geometry
      - Bond angles and electron domains
      - Formal charges and resonance
      
   Example Questions:
   1. Draw and analyze structures:
      - Lewis structure for PF₅
      - Shape of SeCl₄²⁻
      - Bond angles in molecules
      - Electron domain geometry
      
   2. Compare molecular properties:
      - T-shaped vs trigonal planar BrCl₃
      - Bond polarity effects
      - Molecular polarity
      - Dipole arrangements

2. Electronic Structure and Periodicity
   A. Electron Configuration and Trends
      - Electron configuration notation
      - Orbital diagrams
      - Periodic trends
      - Ionization energy patterns
      
   Example Questions:
   1. Analyze electron configurations:
      - Meaning of 3p⁶ notation
      - Orbital filling patterns
      - Energy level diagrams
      
   2. Apply periodic trends:
      - Compare ionization energies
      - Arrange elements (Ar, Ne, P)
      - Justify trend patterns
      - Electron shell effects

3. Thermochemistry and Intermolecular Forces
   A. Energy Changes and Molecular Interactions
      - Enthalpy calculations
      - Entropy considerations
      - Intermolecular forces
      - Boiling point relationships
      
   Example Questions:
   1. Analyze molecular interactions:
      - Forces in NH₃, SO₂, C₅H₁₂
      - Boiling point comparisons
      - Hydrogen bonding effects
      
   2. Calculate energy changes:
      - Enthalpy of reactions
      - Calorimetry data
      - Error analysis
      - Spontaneity predictions

Working Requirements:
1. Diagrams must include:
   - Clear Lewis structures
   - Proper electron placement
   - Correct bond angles
   - Formal charge markings

2. Calculations require:
   - Balanced equations
   - Proper units
   - Clear working steps
   - Error consideration

3. Explanations need:
   - Correct terminology
   - Clear reasoning
   - Specific examples
   - Trend justification

Assessment Notes:
- Show all working clearly
- Include relevant structures
- Use correct chemical notation
- Consider all interactions
- Verify calculations
"""
    
    # Create Chemistry file with new name
    with open(os.path.join(chemistry_dir, "Level 3 Chemistry 91390.txt"), "w", encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    create_sample_files()
    create_as91261_file()
    create_as91262_file()
    create_as91578_file()
    create_physics_91523_file()
    create_physics_91523_source()
    create_chemistry_91390_source() 