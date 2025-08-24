import random

class ReviewerSimulation:
    """
    Agent responsible for simulating reviewer feedback on grant proposals.
    """
    
    def __init__(self):
        # In a real application, you would initialize your AI model here
        # For this example, we'll use a template-based approach
        self.feedback_templates = self._load_feedback_templates()
    
    def _load_feedback_templates(self):
        """Load feedback templates or use default ones if file doesn't exist"""
        try:
            # In a real application, you would load templates from a file
            # For this example, we'll use hardcoded templates
            templates = {
                "strengths": [
                    "The proposal clearly articulates the problem and its significance.",
                    "The methodology is well-designed and appropriate for the research questions.",
                    "The budget is reasonable and well-justified.",
                    "The timeline is realistic and achievable.",
                    "The proposal demonstrates a strong understanding of the current state of the field.",
                    "The expected outcomes are clearly defined and measurable.",
                    "The proposal aligns well with the funding agency's priorities.",
                    "The team has appropriate expertise for the proposed work.",
                    "The evaluation plan is comprehensive and will effectively measure success.",
                    "The proposal effectively addresses potential challenges and limitations."
                ],
                "weaknesses": [
                    "The problem statement lacks sufficient context and significance.",
                    "The methodology lacks detail on specific procedures.",
                    "The budget appears inflated in some categories without adequate justification.",
                    "The timeline seems overly ambitious for the proposed work.",
                    "The literature review is incomplete and misses key recent developments.",
                    "The expected outcomes are vague and difficult to measure.",
                    "The proposal does not clearly align with the funding agency's stated priorities.",
                    "The team appears to lack expertise in some key areas of the proposed work.",
                    "The evaluation plan lacks specific metrics for measuring success.",
                    "The proposal does not adequately address potential challenges and limitations."
                ],
                "suggestions": [
                    "Strengthen the problem statement by providing more context and evidence of significance.",
                    "Provide more detail on the specific methodological procedures to be used.",
                    "Revise the budget to better align with typical costs for similar projects.",
                    "Adjust the timeline to be more realistic or provide justification for the ambitious schedule.",
                    "Update the literature review to include more recent and relevant research.",
                    "Define more specific, measurable outcomes for the project.",
                    "More explicitly connect the proposal to the funding agency's stated priorities.",
                    "Consider adding team members or consultants with expertise in [specific area].",
                    "Develop more specific metrics for the evaluation plan.",
                    "Include a more thorough discussion of potential challenges and mitigation strategies."
                ]
            }
            return templates
        except Exception as e:
            print(f"Error loading feedback templates: {e}")
            # Return default templates
            return {
                "strengths": ["The proposal is well-written."],
                "weaknesses": ["The proposal lacks detail in some areas."],
                "suggestions": ["Consider adding more specific details to strengthen the proposal."]
            }
    
    def generate_feedback(self, topic, goals, funding_agency=None, outline=None, budget=None):
        """
        Generate simulated reviewer feedback based on the provided information.
        
        Args:
            topic (str): The research or project topic
            goals (str): The project goals
            funding_agency (str, optional): The target funding agency
            outline (str, optional): The proposal outline
            budget (dict, optional): The proposed budget
            
        Returns:
            str: Formatted reviewer feedback
        """
        # In a real application, you would use an AI model to generate the feedback
        # For this example, we'll use a template-based approach
        
        # Select random feedback points from each category
        num_strengths = random.randint(2, 4)
        num_weaknesses = random.randint(2, 4)
        num_suggestions = random.randint(2, 4)
        
        strengths = random.sample(self.feedback_templates["strengths"], num_strengths)
        weaknesses = random.sample(self.feedback_templates["weaknesses"], num_weaknesses)
        suggestions = random.sample(self.feedback_templates["suggestions"], num_suggestions)
        
        # Generate an overall score (1-5)
        score = random.randint(2, 5)
        
        # Format the feedback
        feedback = f"## Reviewer Feedback\n\n"
        feedback += f"### Overall Score: {score}/5\n\n"
        
        feedback += "### Strengths:\n"
        for i, strength in enumerate(strengths, 1):
            feedback += f"{i}. {strength}\n"
        
        feedback += "\n### Weaknesses:\n"
        for i, weakness in enumerate(weaknesses, 1):
            feedback += f"{i}. {weakness}\n"
        
        feedback += "\n### Suggestions for Improvement:\n"
        for i, suggestion in enumerate(suggestions, 1):
            feedback += f"{i}. {suggestion}\n"
        
        # Add specific comments based on provided information
        if outline:
            feedback += "\n### Comments on Outline:\n"
            if "Executive Summary" in outline:
                feedback += "- The executive summary provides a good overview of the project.\n"
            if "Methodology" in outline:
                feedback += "- The methodology section should be expanded to include more details on specific procedures.\n"
            if "Budget" in outline:
                feedback += "- Ensure the budget section includes detailed justifications for each category.\n"
        
        if budget:
            feedback += "\n### Comments on Budget:\n"
            total = sum(budget.values())
            feedback += f"- The total budget of ${total:,.2f} seems {'reasonable' if total < 200000 else 'high'} for this type of project.\n"
            
            # Comment on specific budget categories
            if "Personnel" in budget:
                personnel_percent = (budget["Personnel"] / total) * 100
                feedback += f"- Personnel costs represent {personnel_percent:.1f}% of the total budget, which is {'reasonable' if 40 <= personnel_percent <= 70 else 'outside the typical range'}.\n"
            
            if "Indirect Costs" in budget or "Administrative Overhead" in budget:
                indirect_key = "Indirect Costs" if "Indirect Costs" in budget else "Administrative Overhead"
                indirect_percent = (budget[indirect_key] / total) * 100
                feedback += f"- {indirect_key} represent {indirect_percent:.1f}% of the total budget, which is {'acceptable' if indirect_percent <= 35 else 'higher than typically allowed'}.\n"
        
        return feedback