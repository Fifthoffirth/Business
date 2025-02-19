class AS91261Answers:
    def __init__(self):
        # Dictionary of question types and their marking criteria
        self.marking_criteria = {
            "simplify": {
                "achievement": [
                    "Correct use of index laws",
                    "Basic simplification of terms",
                    "Putting fractions over common denominator"
                ],
                "merit": [
                    "Complete simplification",
                    "Correct factorisation",
                    "No algebraic errors"
                ],
                "excellence": [
                    "Elegant solution",
                    "Most efficient method",
                    "Clear logical steps"
                ]
            },
            "solve": {
                "achievement": [
                    "Correct application of basic algebra",
                    "Recognition of equation type",
                    "Some progress towards solution"
                ],
                "merit": [
                    "Correct solution method",
                    "Minor calculation errors only",
                    "Clear working shown"
                ],
                "excellence": [
                    "Complete correct solution",
                    "Verification of answer",
                    "All steps shown clearly"
                ]
            }
        }

        # Sample answers for common question types
        self.sample_answers = {
            "Simplify (2x³y²)/(4xy⁴)": {
                "answer": "x²/(2y²)",
                "steps": [
                    "(2x³y²)/(4xy⁴)",
                    "= (2/4)(x³/x)(y²/y⁴)",
                    "= (1/2)(x²)(y⁻²)",
                    "= x²/(2y²)"
                ],
                "key_points": [
                    "Coefficient simplification: 2/4 = 1/2",
                    "Index law for division: x³/x = x²",
                    "Index law for division: y²/y⁴ = y⁻²",
                    "Final form with positive indices"
                ]
            },
            "Solve 2x² - 7x + 3 = 0": {
                "answer": "x = 1/2 or x = 3",
                "steps": [
                    "2x² - 7x + 3 = 0",
                    "Factoring: (2x - 1)(x - 3) = 0",
                    "Therefore: x = 1/2 or x = 3",
                    "Verification: Substitute back"
                ],
                "key_points": [
                    "Correct factorisation",
                    "Found both solutions",
                    "Verified solutions"
                ]
            }
        }

    def check_answer(self, question, student_answer):
        """
        Check student's answer against sample answers and marking criteria
        Returns: (grade, feedback)
        grade: 'not_achieved', 'achieved', 'merit', 'excellence'
        feedback: Specific feedback on the answer
        """
        if question not in self.sample_answers:
            return "not_assessed", "Question not found in marking schedule"

        correct_answer = self.sample_answers[question]["answer"]
        steps = self.sample_answers[question]["steps"]
        key_points = self.sample_answers[question]["key_points"]

        # Normalize answers for comparison
        student_answer = self._normalize_answer(student_answer)
        correct_answer = self._normalize_answer(correct_answer)

        # Check for exact match
        if student_answer == correct_answer:
            return "excellence", "Perfect answer! All steps correct and well presented."

        # Check for merit-level answer
        if self._check_merit(student_answer, correct_answer, steps):
            return "merit", "Good work! Solution mostly correct with clear working."

        # Check for achievement-level answer
        if self._check_achievement(student_answer, correct_answer, steps):
            return "achieved", "Basic understanding shown. Keep practicing!"

        return "not_achieved", "Review the topic and try again. Show your working clearly."

    def _normalize_answer(self, answer):
        """Normalize answer for comparison (remove spaces, convert to lowercase)"""
        return ''.join(answer.lower().split())

    def _check_merit(self, student_answer, correct_answer, steps):
        """Check if answer meets merit criteria"""
        # Contains most of the correct steps
        # Minor errors only
        return any(self._normalize_answer(step) in student_answer for step in steps[1:])

    def _check_achievement(self, student_answer, correct_answer, steps):
        """Check if answer meets achievement criteria"""
        # Shows basic understanding
        # At least one correct step
        return any(self._normalize_answer(step) in student_answer for step in steps)

    def get_marking_guide(self, question_type):
        """Return marking guide for a question type"""
        if question_type in self.marking_criteria:
            return self.marking_criteria[question_type]
        return None 