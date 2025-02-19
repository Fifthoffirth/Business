class Level3Physics91523Answers:
    def __init__(self):
        # Marking criteria for different question types
        self.marking_criteria = {
            "standing_waves": {
                "achievement": [
                    "Correct wave shape drawn",
                    "At least one node/antinode correctly labeled",
                    "Basic understanding of wave formation"
                ],
                "merit": [
                    "Correct wavelength calculation with minor errors",
                    "Most nodes/antinodes correctly labeled",
                    "Clear understanding of wave patterns"
                ],
                "excellence": [
                    "All calculations correct",
                    "Complete and accurate wave diagram",
                    "Full explanation of wave formation"
                ]
            },
            "wave_interference": {
                "achievement": [
                    "Basic understanding of wave reflection/interference",
                    "Recognition of phase relationships",
                    "Understanding of end conditions"
                ],
                "merit": [
                    "Justified end conditions",
                    "Explanation of wavelength relationships",
                    "Clear understanding of node/antinode formation"
                ],
                "excellence": [
                    "Complete justification of end conditions",
                    "Full explanation of wavelength relationships",
                    "Correct pressure model explanation"
                ]
            },
            "doppler_effect": {
                "achievement": [
                    "Recognition of frequency changes",
                    "Basic understanding of motion effects",
                    "Simple graphical interpretation"
                ],
                "merit": [
                    "Correct equations selected",
                    "Clear explanation of frequency changes",
                    "Accurate calculations with minor errors"
                ],
                "excellence": [
                    "Complete calculations",
                    "Full explanation of frequency changes",
                    "Comprehensive graphical analysis"
                ]
            }
        }

        # Sample answers and key points
        self.sample_answers = {
            "standing_waves": {
                "key_points": [
                    "Node at closed end",
                    "Antinode at open end",
                    "Correct wavelength pattern",
                    "Proper labeling"
                ],
                "calculations": {
                    "frequency": "f = v/λ where λ = 4L/n for odd harmonics",
                    "wavelength": "λ = 4L for fundamental frequency",
                    "length_change": "ΔL = v/(4f) for fundamental"
                }
            },
            "wave_interference": {
                "key_points": [
                    "Path difference = nλ",
                    "Maxima spacing relationship",
                    "Intensity pattern explanation",
                    "Spectral dispersion"
                ],
                "calculations": {
                    "grating": "d sin θ = nλ",
                    "angular_separation": "θ = arcsin(nλ/d)",
                    "number_of_maxima": "n_max = d/λ"
                }
            },
            "doppler_effect": {
                "key_points": [
                    "Frequency increase on approach",
                    "Actual frequency at passing",
                    "Frequency decrease on recession"
                ],
                "calculations": {
                    "approaching": "f_obs = f_source(v/(v-v_source))",
                    "receding": "f_obs = f_source(v/(v+v_source))",
                    "source_speed": "v_source = v(Δf/f_avg)"
                }
            }
        }

    def check_answer(self, question_type, student_answer, correct_answer):
        """Check student answer against marking criteria"""
        if self._meets_excellence_criteria(question_type, student_answer):
            return "excellence", self._generate_feedback(question_type, "excellence")
        
        if self._meets_merit_criteria(question_type, student_answer):
            return "merit", self._generate_feedback(question_type, "merit")
        
        if self._meets_achievement_criteria(question_type, student_answer):
            return "achieved", self._generate_feedback(question_type, "achievement")
        
        return "not_achieved", "Review the concepts and show clear working"

    def _meets_excellence_criteria(self, question_type, answer):
        """Check if answer meets excellence criteria"""
        criteria = self.marking_criteria[question_type]["excellence"]
        return all(self._check_criterion(answer, criterion) for criterion in criteria)

    def _meets_merit_criteria(self, question_type, answer):
        """Check if answer meets merit criteria"""
        criteria = self.marking_criteria[question_type]["merit"]
        return all(self._check_criterion(answer, criterion) for criterion in criteria)

    def _meets_achievement_criteria(self, question_type, answer):
        """Check if answer meets achievement criteria"""
        criteria = self.marking_criteria[question_type]["achievement"]
        return any(self._check_criterion(answer, criterion) for criterion in criteria)

    def get_marking_guide(self, question_type):
        """Return marking guide for a specific question type"""
        if question_type in self.marking_criteria:
            return self.marking_criteria[question_type]
        return None 