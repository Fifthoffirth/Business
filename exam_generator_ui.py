import sys
import os
import shutil
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QTextEdit, QLabel, 
                            QFileDialog, QSpinBox, QComboBox, QProgressBar,
                            QMessageBox, QGroupBox, QStackedWidget, QListWidget,
                            QListWidgetItem)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QPalette, QColor
import nltk
from exam_generator import ExamGenerator

class QuestionGeneratorThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(dict)
    
    def __init__(self, content, subject, topic):
        super().__init__()
        self.content = content
        self.subject = subject
        self.topic = topic
        self.generator = ExamGenerator()
        
    def run(self):
        questions = self.generator.generate_questions_from_text(
            self.content, 
            self.subject, 
            self.topic
        )
        self.finished.emit(questions)

class ExamGeneratorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Exam Generator")
        self.setMinimumSize(1000, 700)
        self.showMaximized()
        self.setup_folders()
        self.setup_ui()
        self.apply_dark_theme()

    def setup_folders(self):
        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create main subjects folder if it doesn't exist
        self.subjects_dir = os.path.join(script_dir, "subjects")
        if not os.path.exists(self.subjects_dir):
            os.makedirs(self.subjects_dir)
            
        # Create default subject folders
        default_subjects = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "English Literature",
            "History",
            "Geography"
        ]
        
        for subject in default_subjects:
            subject_path = os.path.join(self.subjects_dir, subject)
            if not os.path.exists(subject_path):
                os.makedirs(subject_path)
                # Create a sample file for each subject
                with open(os.path.join(subject_path, "sample.txt"), "w", encoding='utf-8') as f:
                    f.write(f"Sample content for {subject}\n")

    def setup_ui(self):
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        # Left panel for input
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Add subject selection before the input section
        subject_group = QGroupBox("Select Subject")
        subject_layout = QVBoxLayout()
        
        self.subject_combo = QComboBox()
        self.subject_combo.addItems(sorted(os.listdir(self.subjects_dir)))
        self.subject_combo.currentTextChanged.connect(self.on_subject_changed)
        
        subject_layout.addWidget(self.subject_combo)
        subject_group.setLayout(subject_layout)
        
        # Add topic selection after subject selection
        topic_group = QGroupBox("Select Topic/Exam")
        topic_layout = QVBoxLayout()
        
        self.topic_list = QListWidget()
        self.topic_list.itemSelectionChanged.connect(self.on_topic_changed)
        
        topic_layout.addWidget(self.topic_list)
        topic_group.setLayout(topic_layout)
        
        # Input section
        input_label = QLabel("Source Text")
        input_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Paste your source text here or use the 'Load File' button...")
        
        # Controls section
        controls_layout = QHBoxLayout()
        
        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)
        self.load_button.setMinimumHeight(40)
        
        self.generate_button = QPushButton("Generate Questions")
        self.generate_button.clicked.connect(self.generate_questions)
        self.generate_button.setMinimumHeight(40)
        
        controls_layout.addWidget(self.load_button)
        controls_layout.addWidget(self.generate_button)
        
        # Options section
        options_layout = QHBoxLayout()
        
        questions_label = QLabel("Questions per type:")
        self.questions_count = QSpinBox()
        self.questions_count.setRange(1, 20)
        self.questions_count.setValue(5)
        
        difficulty_label = QLabel("Difficulty:")
        self.difficulty = QComboBox()
        self.difficulty.addItems(["Easy", "Medium", "Hard"])
        
        options_layout.addWidget(questions_label)
        options_layout.addWidget(self.questions_count)
        options_layout.addWidget(difficulty_label)
        options_layout.addWidget(self.difficulty)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        
        # Add all to left panel
        left_layout.addWidget(subject_group)
        left_layout.addWidget(topic_group)
        left_layout.addWidget(input_label)
        left_layout.addWidget(self.input_text)
        left_layout.addLayout(controls_layout)
        left_layout.addLayout(options_layout)
        left_layout.addWidget(self.progress_bar)
        
        # Right panel for output
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        output_label = QLabel("Generated Questions")
        output_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        
        # Create stacked widget for questions
        self.question_stack = QStackedWidget()
        
        # Navigation buttons
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        self.submit_button = QPushButton("Submit Answer")
        
        self.prev_button.clicked.connect(self.previous_question)
        self.next_button.clicked.connect(self.next_question)
        self.submit_button.clicked.connect(self.check_answer)
        
        nav_layout.addWidget(self.prev_button)
        nav_layout.addWidget(self.submit_button)
        nav_layout.addWidget(self.next_button)
        
        # Progress label
        self.progress_label = QLabel("Question 0/0")
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add to right layout
        right_layout.addWidget(output_label)
        right_layout.addWidget(self.question_stack)
        right_layout.addLayout(nav_layout)
        right_layout.addWidget(self.progress_label)
        
        # Initialize question widgets list
        self.question_widgets = []
        
        # Add panels to main layout
        layout.addWidget(left_panel)
        layout.addWidget(right_panel)
        
        # Set layout proportions
        layout.setStretch(0, 1)
        layout.setStretch(1, 1)

    def apply_dark_theme(self):
        # Set application style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #000000;
            }
            QWidget {
                background-color: #000000;
                color: white;
                font-weight: bold;
            }
            QTextEdit, QListWidget, QComboBox, QSpinBox {
                background-color: #2F4550;
                color: white;
                font-weight: bold;
                border: 1px solid white;
                border-radius: 4px;
                padding: 4px;
            }
            QPushButton {
                background-color: #2F4550;
                color: white;
                font-weight: bold;
                border: 1px solid white;
                border-radius: 4px;
                padding: 6px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #3F5560;
            }
            QPushButton:pressed {
                background-color: #1F3540;
            }
            QLabel {
                color: white;
                font-weight: bold;
            }
            QGroupBox {
                border: 1px solid white;
                border-radius: 4px;
                margin-top: 8px;
                padding-top: 8px;
            }
            QGroupBox::title {
                color: white;
                font-weight: bold;
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 4px;
            }
        """)

        # Set dark palette for application
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#000000"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
        palette.setColor(QPalette.ColorRole.Base, QColor("#2F4550"))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#2F4550"))
        palette.setColor(QPalette.ColorRole.Text, QColor("white"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#2F4550"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("white"))
        self.setPalette(palette)

    def get_formatted_topic_name(self, filename):
        """Convert filename to a more readable format"""
        name = filename.replace('.txt', '')
        
        # Handle special cases
        if name.lower().startswith('as'):
            # Format assessment standards (e.g., AS91261)
            standard_num = name[2:7] if len(name) >= 7 else name[2:]
            description = name[7:] if len(name) > 7 else ''
            if standard_num == '91261':
                return f"NCEA L2 - Algebraic Methods (AS{standard_num}){description}"
            elif standard_num == '91262':
                return f"NCEA L2 - Calculus Methods (AS{standard_num}){description}"
            return f"Assessment Standard {name}"
        
        elif name.lower() == 'sample_content':
            return "General Topics"
        
        # Convert snake_case or kebab-case to Title Case
        return name.replace('_', ' ').replace('-', ' ').title()

    def on_subject_changed(self):
        # Clear the input text and topic list
        self.input_text.clear()
        self.topic_list.clear()
        
        # Get the selected subject
        subject = self.subject_combo.currentText()
        subject_path = os.path.join(self.subjects_dir, subject)
        
        # List and categorize available files for the subject
        files = [f for f in os.listdir(subject_path) if f.endswith('.txt')]
        
        # Sort files into categories
        assessment_standards = []
        general_topics = []
        other_topics = []
        
        for file in files:
            if file.lower().startswith('as'):
                assessment_standards.append(file)
            elif file.lower() == 'sample_content.txt':
                general_topics.append(file)
            else:
                other_topics.append(file)
        
        # Add files to topic list with categories
        if assessment_standards:
            self.topic_list.addItem("--- Assessment Standards ---")
            for file in sorted(assessment_standards):
                item = QListWidgetItem(self.get_formatted_topic_name(file))
                item.setData(Qt.ItemDataRole.UserRole, file)  # Store original filename
                self.topic_list.addItem(item)
        
        if general_topics:
            self.topic_list.addItem("--- General Topics ---")
            for file in sorted(general_topics):
                item = QListWidgetItem(self.get_formatted_topic_name(file))
                item.setData(Qt.ItemDataRole.UserRole, file)
                self.topic_list.addItem(item)
        
        if other_topics:
            self.topic_list.addItem("--- Other Topics ---")
            for file in sorted(other_topics):
                item = QListWidgetItem(self.get_formatted_topic_name(file))
                item.setData(Qt.ItemDataRole.UserRole, file)
                self.topic_list.addItem(item)
        
        # Select first actual item (not category header)
        for i in range(self.topic_list.count()):
            item = self.topic_list.item(i)
            if not item.text().startswith('---'):
                self.topic_list.setCurrentItem(item)
                break

    def on_topic_changed(self):
        # Clear the input text
        self.input_text.clear()
        
        # Get selected topic
        current_item = self.topic_list.currentItem()
        if current_item and not current_item.text().startswith('---'):
            # Get original filename from item data
            topic_file = current_item.data(Qt.ItemDataRole.UserRole)
            subject = self.subject_combo.currentText()
            file_path = os.path.join(self.subjects_dir, subject, topic_file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.input_text.setText(f.read())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error loading topic: {str(e)}")

    def load_file(self):
        subject = self.subject_combo.currentText()
        subject_path = os.path.join(self.subjects_dir, subject)
        
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Text File",
            subject_path,  # Start in the selected subject folder
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                # If file is from outside the subject folder, copy it to the subject folder
                if not file_name.startswith(subject_path):
                    new_path = os.path.join(subject_path, os.path.basename(file_name))
                    shutil.copy2(file_name, new_path)
                    file_name = new_path
                
                with open(file_name, 'r', encoding='utf-8') as file:
                    self.input_text.setText(file.read())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error loading file: {str(e)}")

    def generate_questions(self):
        content = self.input_text.toPlainText()
        if not content:
            QMessageBox.warning(self, "Warning", "Please enter or load some text first!")
            return
            
        self.progress_bar.setVisible(True)
        self.generate_button.setEnabled(False)
        self.load_button.setEnabled(False)
        
        # Get current subject and topic
        subject = self.subject_combo.currentText()
        current_item = self.topic_list.currentItem()
        topic = current_item.data(Qt.ItemDataRole.UserRole) if current_item else None
        
        self.thread = QuestionGeneratorThread(content, subject, topic)
        self.thread.finished.connect(self.display_questions)
        self.thread.start()

    def display_questions(self, questions):
        # Clear previous questions
        while self.question_stack.count():
            self.question_stack.removeWidget(self.question_stack.widget(0))
        self.question_widgets.clear()
        
        # Create widgets for each question
        question_number = 1
        for section, section_questions in questions.items():
            if section_questions:
                for question in section_questions:
                    # Create question widget
                    question_widget = QWidget()
                    q_layout = QVBoxLayout(question_widget)
                    
                    # Add section label
                    section_label = QLabel(section)
                    section_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
                    q_layout.addWidget(section_label)
                    
                    # Add question text
                    question_label = QLabel(f"{question_number}. {question}")
                    question_label.setWordWrap(True)
                    q_layout.addWidget(question_label)
                    
                    # Add answer input
                    answer_label = QLabel("Your Answer:")
                    q_layout.addWidget(answer_label)
                    
                    answer_input = QTextEdit()
                    answer_input.setPlaceholderText("Type your answer here...")
                    q_layout.addWidget(answer_input)
                    
                    # Add feedback label
                    feedback_label = QLabel("")
                    feedback_label.setStyleSheet("QLabel { color: gray; }")
                    q_layout.addWidget(feedback_label)
                    
                    # Store question info
                    self.question_widgets.append({
                        'widget': question_widget,
                        'answer_input': answer_input,
                        'feedback_label': feedback_label,
                        'question_text': question,
                        'section': section,
                        'number': question_number
                    })
                    
                    # Add to stack
                    self.question_stack.addWidget(question_widget)
                    question_number += 1
        
        # Enable/disable navigation buttons
        self.update_navigation_buttons()
        
        # Show first question
        if self.question_widgets:
            self.question_stack.setCurrentIndex(0)
            self.update_progress_label()

    def previous_question(self):
        current = self.question_stack.currentIndex()
        if current > 0:
            self.question_stack.setCurrentIndex(current - 1)
            self.update_navigation_buttons()
            self.update_progress_label()

    def next_question(self):
        current = self.question_stack.currentIndex()
        if current < self.question_stack.count() - 1:
            self.question_stack.setCurrentIndex(current + 1)
            self.update_navigation_buttons()
            self.update_progress_label()

    def update_navigation_buttons(self):
        current = self.question_stack.currentIndex()
        self.prev_button.setEnabled(current > 0)
        self.next_button.setEnabled(current < self.question_stack.count() - 1)

    def update_progress_label(self):
        current = self.question_stack.currentIndex() + 1
        total = self.question_stack.count()
        self.progress_label.setText(f"Question {current}/{total}")

    def check_answer(self):
        current_idx = self.question_stack.currentIndex()
        if 0 <= current_idx < len(self.question_widgets):
            question_info = self.question_widgets[current_idx]
            answer = question_info['answer_input'].toPlainText().strip()
            
            if not answer:
                question_info['feedback_label'].setText("Please enter an answer")
                question_info['feedback_label'].setStyleSheet("QLabel { color: orange; }")
                return
            
            # Here you can implement more sophisticated answer checking
            # For now, we'll just provide a basic response
            feedback = self.evaluate_answer(answer, question_info)
            question_info['feedback_label'].setText(feedback['message'])
            question_info['feedback_label'].setStyleSheet(
                f"QLabel {{ color: {feedback['color']}; }}"
            )

    def evaluate_answer(self, answer, question_info):
        # Basic answer evaluation - you can expand this
        question_text = question_info['question_text'].lower()
        answer = answer.lower()
        
        # Check for empty answer
        if not answer:
            return {
                'message': "Please provide an answer",
                'color': 'orange'
            }
        
        # Check for keywords based on question type
        if 'simplify' in question_text:
            if any(term in answer for term in ['x', 'y', 'a', 'b', '+', '-', '×', '/']):
                return {
                    'message': "Answer format looks correct. Check your simplification steps.",
                    'color': 'green'
                }
        elif 'solve' in question_text:
            if any(term in answer for term in ['=', 'x', 'y']):
                return {
                    'message': "Answer format looks correct. Verify your solution.",
                    'color': 'green'
                }
        elif 'express' in question_text:
            if any(term in answer for term in ['=', 'x', 'y', 'r', 'h']):
                return {
                    'message': "Answer format looks correct. Check your expression.",
                    'color': 'green'
                }
        
        return {
            'message': "Please show your working and verify your answer format",
            'color': 'orange'
        }

    def save_questions(self):
        if not self.output_text.toPlainText():
            QMessageBox.warning(self, "Warning", "No questions to save!")
            return
        
        subject = self.subject_combo.currentText()
        subject_path = os.path.join(self.subjects_dir, subject)
        default_filename = f"generated_exam_{subject.lower()}.txt"
        
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Questions",
            os.path.join(subject_path, default_filename),
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.output_text.toPlainText())
                QMessageBox.information(self, "Success", "Questions saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error saving file: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = ExamGeneratorUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 