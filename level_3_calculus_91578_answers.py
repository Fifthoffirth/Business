class Level3Calculus91578Answers:
    def __init__(self):
        # Marking criteria for different question types
        self.marking_criteria = {
            "differentiation": {
                "achievement": [
                    "Basic derivative rules applied correctly",
                    "Some steps of working shown",
                    "Correct use of basic differentiation rules"
                ],
                "merit": [
                    "Chain rule applied correctly",
                    "Product/quotient rule used appropriately",
                    "Clear and logical working",
                    "Correct handling of composite functions"
                ],
                "excellence": [
                    "Complex derivatives found correctly",
                    "Full justification provided",
                    "Clear and elegant solution path",
                    "Verification of solutions where appropriate"
                ]
            },
            "implicit": {
                "achievement": [
                    "Basic implicit differentiation",
                    "Correct use of chain rule",
                    "Some working shown"
                ],
                "merit": [
                    "Correct handling of products",
                    "Clear organization of terms",
                    "Accurate simplification"
                ],
                "excellence": [
                    "Complex implicit differentiation",
                    "Full justification of steps",
                    "Clear and concise solution"
                ]
            },
            "rates_of_change": {
                "achievement": [
                    "Basic rate of change calculation",
                    "Correct use of chain rule",
                    "Understanding of related rates"
                ],
                "merit": [
                    "Clear connection between rates",
                    "Accurate calculations",
                    "Proper units included"
                ],
                "excellence": [
                    "Complex rate problems solved",
                    "Clear justification of approach",
                    "Thorough verification of answer"
                ]
            },
            "inflection_points": {
                "achievement": [
                    "First derivative found",
                    "Attempt at second derivative",
                    "Basic working shown"
                ],
                "merit": [
                    "Both derivatives correct",
                    "Critical points identified",
                    "Clear solution process"
                ],
                "excellence": [
                    "Full coordinates found",
                    "Nature of point verified",
                    "Complete justification provided"
                ]
            }
        }

        # Sample solutions for common question types
        self.sample_solutions = {
            "product_rule": {
                "example": "y = (x² + 3x + 2)sin(x)",
                "solution": "(2x + 3)sin(x) + (x² + 3x + 2)cos(x)",
                "key_points": [
                    "Identify parts for product rule",
                    "Find individual derivatives",
                    "Apply product rule formula",
                    "Combine terms correctly"
                ]
            },
            "chain_rule": {
                "example": "y = ln(3x² + 5x + 2)",
                "solution": "(6x + 5)/(3x² + 5x + 2)",
                "key_points": [
                    "Identify outer and inner functions",
                    "Apply chain rule correctly",
                    "Simplify result if possible"
                ]
            },
            "implicit": {
                "example": "x² + y² = 25",
                "solution": "dy/dx = -x/y",
                "key_points": [
                    "Differentiate both sides",
                    "Group terms with dy/dx",
                    "Solve for dy/dx"
                ]
            }
        }

    def check_answer(self, question_type, student_answer, question_text):
        """
        Check student's answer against marking criteria
        Returns: (grade, feedback)
        """
        if question_type not in self.marking_criteria:
            return "not_assessed", "Question type not recognized"

        # Normalize answer for comparison
        student_answer = self._normalize_answer(student_answer)
        
        # Check for excellence criteria
        if self._meets_excellence_criteria(question_type, student_answer):
            return "excellence", self._generate_feedback(question_type, "excellence")
        
        # Check for merit criteria
        if self._meets_merit_criteria(question_type, student_answer):
            return "merit", self._generate_feedback(question_type, "merit")
        
        # Check for achievement criteria
        if self._meets_achievement_criteria(question_type, student_answer):
            return "achieved", self._generate_feedback(question_type, "achieved")
        
        return "not_achieved", "Review the key concepts and show your working clearly"

    def _normalize_answer(self, answer):
        """Remove spaces and convert to lowercase for comparison"""
        return ''.join(answer.lower().split())

    def _meets_excellence_criteria(self, question_type, answer):
        """Check if answer meets excellence criteria"""
        criteria = self.marking_criteria[question_type]["excellence"]
        # Check for clear working, justification, and verification
        return all(self._check_criterion(answer, criterion) for criterion in criteria)

    def _meets_merit_criteria(self, question_type, answer):
        """Check if answer meets merit criteria"""
        criteria = self.marking_criteria[question_type]["merit"]
        return all(self._check_criterion(answer, criterion) for criterion in criteria)

    def _meets_achievement_criteria(self, question_type, answer):
        """Check if answer meets achievement criteria"""
        criteria = self.marking_criteria[question_type]["achievement"]
        return any(self._check_criterion(answer, criterion) for criterion in criteria)

    def _check_criterion(self, answer, criterion):
        """Check if an answer meets a specific criterion"""
        # Implementation would include specific checks for each criterion
        # This would need to be customized based on the specific requirements
        pass

    def _generate_feedback(self, question_type, grade):
        """Generate specific feedback based on question type and grade"""
        criteria = self.marking_criteria[question_type][grade]
        feedback = f"Your answer demonstrates {grade} level understanding:\n"
        for criterion in criteria:
            feedback += f"- {criterion}\n"
        return feedback

    def get_marking_guide(self, question_type):
        """Return marking guide for a specific question type"""
        if question_type in self.marking_criteria:
            return self.marking_criteria[question_type]
        return None 