import random
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class ExamGenerator:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
            nltk.download('stopwords')
            nltk.download('wordnet')

        self.stop_words = set(stopwords.words('english'))

    def read_content(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    def generate_questions_from_text(self, text, subject=None, topic=None):
        # Get questions based on subject/topic
        questions = {
            "Multiple Choice Questions": [],
            "Short Answer Questions": [],
            "Essay Questions": []
        }
        
        # Generate questions based on subject/topic
        if subject and topic:
            if subject == "Mathematics":
                if "91261" in topic:
                    questions = self.generate_math_questions(text, "algebra")
                elif "91262" in topic:
                    questions = self.generate_math_questions(text, "calculus")
                elif "91578" in topic:
                    questions = self.generate_math_questions(text, "calculus_l3")
                else:
                    questions = self.generate_math_questions(text, "general")
            elif subject == "Physics":
                if "91523" in topic:
                    questions = self.generate_physics_questions(text, topic)
                else:
                    questions = self.generate_physics_questions(text)
            elif subject == "Chemistry":
                questions = self.generate_chemistry_questions(text)
            elif subject == "Biology":
                questions = self.generate_biology_questions(text)
        
        # Scramble questions in each category
        for category in questions:
            if questions[category]:
                random.shuffle(questions[category])
        
        # Optionally scramble across categories while maintaining some structure
        all_questions = []
        max_per_round = max(len(questions[cat]) for cat in questions)
        
        for i in range(max_per_round):
            # Add one from each category in random order
            categories = list(questions.keys())
            random.shuffle(categories)
            for category in categories:
                if i < len(questions[category]):
                    all_questions.append((category, questions[category][i]))
        
        # Reconstruct the questions dictionary
        scrambled_questions = {
            "Multiple Choice Questions": [],
            "Short Answer Questions": [],
            "Essay Questions": []
        }
        
        for category, question in all_questions:
            scrambled_questions[category].append(question)
        
        return scrambled_questions

    def determine_subject(self, text):
        # Simple subject determination based on keywords
        physics_keywords = ['force', 'motion', 'energy', 'velocity', 'acceleration']
        chemistry_keywords = ['reaction', 'molecule', 'acid', 'base', 'compound']
        biology_keywords = ['cell', 'organism', 'gene', 'species', 'ecosystem']
        
        text_lower = text.lower()
        
        if any(keyword in text_lower for keyword in physics_keywords):
            return "Physics"
        elif any(keyword in text_lower for keyword in chemistry_keywords):
            return "Chemistry"
        elif any(keyword in text_lower for keyword in biology_keywords):
            return "Biology"
        else:
            return "Mathematics"

    def generate_simplify_questions(self, templates):
        questions = []
        variables = ['x', 'y']  # Limit to common variables
        
        # Fraction with indices
        for _ in range(2):
            var1, var2 = random.sample(variables, 2)
            power1 = random.randint(2, 3)  # More common powers like x² and x³
            power2 = random.randint(1, 2)
            coef1 = random.randint(2, 6)
            coef2 = random.randint(2, 4)
            expression = f"Simplify ({coef1}{var1}^{power1}{var2}^{power2})/({coef2}{var1}{var2})"
            questions.append(expression)
        
        # Expanding brackets
        for _ in range(2):
            var = random.choice(variables)
            a = random.randint(1, 3)
            b = random.randint(1, 5)
            expression = f"Expand ({a}{var} + {b})²"  # Use ² symbol
            questions.append(expression)
        
        # Complex fractions
        for _ in range(2):
            var = random.choice(variables)
            expression = f"Simplify ({var}² + {random.randint(2,4)}{var})/({var} + {random.randint(1,3)})"
            questions.append(expression)

        return questions

    def generate_solve_questions(self, templates):
        questions = []
        
        # Quadratic equations
        for _ in range(2):
            a = random.randint(1, 3)
            b = random.randint(-6, 6)
            c = random.randint(-8, 8)
            equation = f"Solve: {a}x² + {b}x + {c} = 0"  # Use ² symbol
            questions.append(equation)

        # Exponential equations
        for _ in range(2):
            base = random.choice([2, 3, 10])  # Common bases
            result = random.choice([4, 8, 16, 32])  # Common results
            questions.append(f"Solve for x: {base}ˣ = {result}")
        
        # Logarithmic equations
        for _ in range(2):
            base = random.choice([2, 10, 'e'])  # Include natural log
            a = random.randint(1, 3)
            b = random.randint(1, 4)
            if base == 'e':
                questions.append(f"Solve for x: ln(x + {a}) = {b}")
            else:
                questions.append(f"Solve for x: log_{base}(x + {a}) = {b}")

        return questions

    def generate_find_questions(self, templates):
        questions = []
        
        # Finding values
        for _ in range(2):
            a = random.randint(1, 3)
            b = random.randint(-6, 6)
            questions.append(f"Find the value of x where {a}x² + {b}x + {random.randint(-5, 5)} = 0")
        
        # Minimum/Maximum value questions
        for _ in range(2):
            a = random.choice([1, 2])
            h = random.randint(-3, 3)
            k = random.randint(-3, 3)
            questions.append(f"Find the minimum value of y = {a}(x - {h})² + {k}")
        
        # Intersection points
        for _ in range(2):
            m = random.randint(1, 3)
            c = random.randint(-3, 3)
            questions.append(f"Find the points where y = {m}x + {c} intersects with y = x²")

        return questions

    def generate_expression_questions(self, templates):
        questions = []
        
        # Basic formulas
        formulas = [
            ('V', 'πr²h', ['h', 'r', 'V']),
            ('A', 'P(1 + r)ⁿ', ['r', 'P', 'n']),
            ('S', '2πrh + 2πr²', ['r', 'h']),
            ('d', '√((x₂-x₁)² + (y₂-y₁)²)', ['x₁', 'y₁', 'x₂', 'y₂']),
            ('K.E.', '½mv²', ['m', 'v']),
            ('F', 'G(m₁m₂)/r²', ['G', 'm₁', 'm₂', 'r'])
        ]
        
        for formula, expression, variables in formulas:
            subject = random.choice(variables)
            questions.append(f"Express {subject} in terms of the other variables in the formula {formula} = {expression}")

        return questions

    def generate_real_world_questions(self, templates):
        questions = []
        
        # Geometric problems
        shapes = [
            ('rectangle', 'length', 'width'),
            ('cylinder', 'radius', 'height'),
            ('box', 'length', 'width', 'height'),
            ('cone', 'radius', 'height'),
            ('sphere', 'radius', None)
        ]
        
        for shape in shapes:
            if shape[0] == 'rectangle':
                x = random.randint(1, 5)
                questions.append(f"A {shape[0]} has {shape[1]} ({x}x + {random.randint(1, 3)}) and {shape[2]} ({x}x - {random.randint(1, 2)}). Express its area in simplified form")
            elif shape[0] == 'cylinder':
                h = random.randint(5, 20)
                questions.append(f"A {shape[0]} has {shape[2]} {h}cm. If its surface area is {random.randint(100, 500)}cm², express its {shape[1]} in terms of π")
        
        # Rate problems
        rates = [
            ('car', 'speed', 'time', 'distance'),
            ('worker', 'rate', 'time', 'work'),
            ('tank', 'flow rate', 'time', 'volume')
        ]
        
        for rate in rates:
            time = random.randint(2, 8)
            amount = random.randint(20, 100)
            questions.append(f"A {rate[0]} travels at a constant {rate[1]}. If it takes {time} hours to cover {amount}km, express the {rate[1]} in km/h")
        
        # Financial problems
        financial = [
            ('cost', 'revenue', 'profit'),
            ('principal', 'interest', 'time'),
            ('investment', 'return', 'rate')
        ]
        
        for fin in financial:
            initial = random.randint(1000, 5000)
            rate = random.randint(5, 15)
            questions.append(f"An initial {fin[0]} of ${initial} grows at {rate}% per year. Express the {fin[1]} after n years")

        return questions

    def generate_physics_questions(self, text, topic=None):
        questions = {
            "Multiple Choice Questions": [],
            "Short Answer Questions": [],
            "Essay Questions": []
        }
        
        if topic and "91523" in topic:  # Wave Systems questions
            # Standing Waves and Harmonics
            questions["Multiple Choice Questions"].extend([
                "Label the nodes (N) and antinodes (A) in the diagram of a third harmonic in a pan flute.",
                f"Calculate the frequency of the third harmonic in a pipe of length {random.randint(8,12)} cm, given the speed of sound is 343 m/s.",
                f"A pipe of length {random.randint(15,20)} cm is open at one end and closed at the other. Which harmonics can be formed in this pipe?"
            ])
            
            # Wave Interference and Diffraction
            questions["Short Answer Questions"].extend([
                f"A diffraction grating has {random.randint(100,300)} lines per mm. Calculate the angular separation for the first order maximum using light of wavelength {random.randint(400,700)} nm.",
                "Explain the differences between the patterns formed by a diffraction grating versus two slits.",
                "Describe why white light forms a spectrum when passed through a diffraction grating, with violet on the inside and red on the outside."
            ])
            
            # Doppler Effect
            questions["Essay Questions"].extend([
                f"A train approaching at {random.randint(10,30)} m/s sounds its horn. Explain what observers at a station would hear as the train approaches and passes.",
                f"Given that an approaching train's horn has a frequency of {random.randint(1200,1300)} Hz and a receding frequency of {random.randint(1100,1200)} Hz, calculate the train's speed. The speed of sound is 343 m/s.",
                "Analyze the frequency vs. position graph for a moving sound source as it approaches, passes, and moves away from a stationary observer. Explain the changes in frequency at each stage."
            ])
        
        else:  # Original physics questions
            # Mechanics problems
            mechanics = [
                {
                    'type': 'motion',
                    'variables': ['velocity', 'acceleration', 'time', 'distance'],
                    'units': ['m/s', 'm/s²', 's', 'm']
                },
                {
                    'type': 'force',
                    'variables': ['mass', 'acceleration', 'force'],
                    'units': ['kg', 'm/s²', 'N']
                },
                {
                    'type': 'energy',
                    'variables': ['mass', 'height', 'velocity'],
                    'units': ['kg', 'm', 'm/s']
                }
            ]
            
            for mech in mechanics:
                if mech['type'] == 'motion':
                    v = random.randint(5, 30)
                    a = random.randint(1, 10)
                    t = random.randint(2, 8)
                    questions["Short Answer Questions"].append(
                        f"A car accelerates from {v}m/s with acceleration {a}m/s². Calculate its velocity after {t} seconds."
                    )
                elif mech['type'] == 'force':
                    m = random.randint(2, 20)
                    a = random.randint(2, 10)
                    questions["Short Answer Questions"].append(
                        f"Calculate the force needed to give a {m}kg mass an acceleration of {a}m/s²."
                    )
            
            # Electricity problems
            electricity = [
                ('voltage', 'current', 'resistance'),
                ('power', 'current', 'voltage'),
                ('energy', 'power', 'time')
            ]
            
            for elec in electricity:
                if elec[0] == 'voltage':
                    i = random.randint(1, 10)
                    r = random.randint(5, 50)
                    questions["Multiple Choice Questions"].append(
                        f"Calculate the voltage across a {r}Ω resistor when a current of {i}A flows through it."
                    )
            
            # Waves and light
            waves = [
                ('frequency', 'wavelength', 'speed'),
                ('amplitude', 'energy', 'frequency'),
                ('reflection', 'angle', 'surface')
            ]
            
            for wave in waves:
                if wave[0] == 'frequency':
                    v = random.randint(200, 400)
                    λ = random.randint(2, 10)/10
                    questions["Short Answer Questions"].append(
                        f"Calculate the frequency of a wave with speed {v}m/s and wavelength {λ}m."
                    )

            # Essay/explanation questions
            concepts = [
                "Newton's laws of motion",
                "Conservation of energy",
                "Electromagnetic induction",
                "Wave-particle duality",
                "Thermal equilibrium"
            ]
            
            for concept in concepts:
                questions["Essay Questions"].append(
                    f"Explain the concept of {concept} and provide two real-world applications."
                )

        return questions

    def generate_chemistry_questions(self, templates):
        questions = {
            "Multiple Choice Questions": [],
            "Short Answer Questions": [],
            "Essay Questions": []
        }
        
        # Stoichiometry problems
        elements = ['H', 'O', 'N', 'C', 'Na', 'Cl', 'Ca']
        compounds = ['H2O', 'CO2', 'NaCl', 'CaCO3', 'H2SO4']
        
        for _ in range(3):
            compound = random.choice(compounds)
            mass = random.randint(10, 100)
            questions["Short Answer Questions"].append(
                f"Calculate the number of moles in {mass}g of {compound}."
            )
        
        # Acid-base problems
        acids = ['HCl', 'H2SO4', 'HNO3']
        bases = ['NaOH', 'KOH', 'Ca(OH)2']
        
        for _ in range(2):
            acid = random.choice(acids)
            base = random.choice(bases)
            conc = random.randint(1, 5)/10
            questions["Multiple Choice Questions"].append(
                f"Calculate the pH of a {conc}M solution of {acid}."
            )
        
        # Gas law problems
        gas_laws = [
            ('pressure', 'volume', 'temperature'),
            ('moles', 'pressure', 'volume'),
            ('volume', 'temperature', 'pressure')
        ]
        
        for law in gas_laws:
            if law[0] == 'pressure':
                v1 = random.randint(1, 10)
                v2 = random.randint(1, 10)
                p1 = random.randint(1, 5)
                questions["Short Answer Questions"].append(
                    f"A gas has pressure {p1}atm at volume {v1}L. Calculate its pressure when volume changes to {v2}L at constant temperature."
                )
        
        # Electron configuration
        elements_config = [
            ('Na', 11),
            ('Ca', 20),
            ('Fe', 26),
            ('Cu', 29),
            ('Zn', 30)
        ]
        
        for element, number in elements_config:
            questions["Multiple Choice Questions"].append(
                f"Write the electron configuration for {element} (atomic number {number})."
            )
        
        # Reaction mechanisms
        reactions = [
            "SN2 nucleophilic substitution",
            "Acid-base neutralization",
            "Redox reactions",
            "Addition polymerization",
            "Esterification"
        ]
        
        for reaction in reactions:
            questions["Essay Questions"].append(
                f"Explain the mechanism of {reaction}. Include all steps and draw relevant diagrams."
            )

        return questions

    def generate_biology_questions(self, templates):
        questions = {
            "Multiple Choice Questions": [],
            "Short Answer Questions": [],
            "Essay Questions": []
        }
        
        # Cell biology
        cell_organelles = [
            ('mitochondria', 'energy production'),
            ('nucleus', 'genetic material'),
            ('ribosomes', 'protein synthesis'),
            ('chloroplasts', 'photosynthesis'),
            ('Golgi apparatus', 'protein packaging')
        ]
        
        for organelle, function in cell_organelles:
            questions["Multiple Choice Questions"].append(
                f"Explain the role of the {organelle} in {function}."
            )
        
        # Genetics problems
        genetics = [
            ('dominant', 'recessive'),
            ('homozygous', 'heterozygous'),
            ('genotype', 'phenotype')
        ]
        
        for gen in genetics:
            questions["Short Answer Questions"].append(
                f"In a cross between {gen[0]} and {gen[1]} alleles, determine the possible offspring genotypes and phenotypes."
            )
        
        # Ecology relationships
        ecological_concepts = [
            "food web dynamics",
            "nutrient cycling",
            "population growth",
            "species interactions",
            "ecosystem stability"
        ]
        
        for concept in ecological_concepts:
            questions["Essay Questions"].append(
                f"Discuss the importance of {concept} in maintaining ecosystem balance."
            )

        return questions

    def generate_math_questions(self, text, math_type="general"):
        questions = {
            "Multiple Choice Questions": [],
            "Short Answer Questions": [],
            "Essay Questions": []
        }
        
        if math_type == "algebra":
            # Generate algebra questions (AS91261)
            questions["Multiple Choice Questions"].extend(self.generate_simplify_questions(text))
            questions["Short Answer Questions"].extend(self.generate_solve_questions(text))
            questions["Short Answer Questions"].extend(self.generate_find_questions(text))
            questions["Essay Questions"].extend(self.generate_expression_questions(text))
        
        elif math_type == "calculus":
            # Generate calculus questions (AS91262)
            questions["Multiple Choice Questions"].extend(self.generate_derivative_questions(text))
            questions["Short Answer Questions"].extend(self.generate_integration_questions(text))
            questions["Essay Questions"].extend(self.generate_optimization_questions(text))
        
        else:
            # Generate general math questions
            questions["Multiple Choice Questions"].extend(self.generate_simplify_questions(text))
            questions["Short Answer Questions"].extend(self.generate_solve_questions(text))
            questions["Essay Questions"].extend(self.generate_real_world_questions(text))
        
        return questions

    def generate_derivative_questions(self, text):
        questions = []
        
        # Basic derivatives
        functions = [
            f"{random.randint(2,4)}x²",
            f"x³ - {random.randint(2,5)}x",
            f"x² + {random.randint(2,4)}x + {random.randint(1,5)}",
            f"{random.randint(2,3)}x³ - {random.randint(2,4)}x²"
        ]
        
        for func in functions:
            questions.append(f"Find the derivative of f(x) = {func}")
        
        return questions

    def generate_integration_questions(self, text):
        questions = []
        
        # Basic integrals
        functions = [
            f"{random.randint(2,4)}x",
            f"x² - {random.randint(2,5)}x",
            f"{random.randint(2,3)}x² + {random.randint(1,3)}"
        ]
        
        for func in functions:
            questions.append(f"Find ∫({func})dx")  # Use proper integral symbol
        
        return questions

    def generate_optimization_questions(self, text):
        questions = []
        
        # Real-world optimization
        questions.extend([
            "Find the dimensions of a rectangle with perimeter 20 units that has the maximum possible area",
            f"A box with square base has volume {random.randint(100,500)}cm³. Find the dimensions that minimize the surface area",
            f"Find the point on the curve y = x² that is closest to the point (0, {random.randint(2,5)})",
            "Maximize the area of a rectangle inscribed in a circle of radius 5 units"
        ])
        
        return questions

    def save_exam(self, questions, output_filename):
        with open(output_filename, 'w', encoding='utf-8') as file:
            question_number = 1
            for section, section_questions in questions.items():
                if section_questions:  # Only write sections that have questions
                    file.write(f"\n{section}\n")
                    for question in section_questions:
                        file.write(f"{question_number}. {question}\n")
                        question_number += 1

def main():
    generator = ExamGenerator()
    
    # Get all .txt files in the current directory
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt') and f != 'generated_exam.txt']
    
    if not txt_files:
        print("No text files found in the current directory!")
        return

    print("Available exam paper files:")
    for i, file in enumerate(txt_files, 1):
        print(f"{i}. {file}")

    try:
        choice = int(input("\nSelect a file number to generate questions from: ")) - 1
        if 0 <= choice < len(txt_files):
            input_file = txt_files[choice]
            content = generator.read_content(input_file)
            questions = generator.generate_questions_from_text(content)
            
            output_filename = f"generated_exam_from_{input_file}"
            generator.save_exam(questions, output_filename)
            
            print(f"\nExam generated successfully! Saved as '{output_filename}'")
            
            # Print the generated exam
            with open(output_filename, 'r', encoding='utf-8') as file:
                print("\nGenerated Exam:")
                print(file.read())
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main() 