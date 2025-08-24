import openai
import os
import json
import yaml
import random

class OutlineDesigner:
    """
    Agent responsible for generating proposal outlines based on topic, goals, and funding agency.
    """
    
    def __init__(self):
        # In a real application, you would initialize your AI model here
        # For this example, we'll use a template-based approach
        self.templates = self._load_templates()
    
    def _load_templates(self):
        """Load outline templates or use default ones if file doesn't exist"""
        try:
            # In a real application, you would load templates from a file
            # For this example, we'll use hardcoded templates
            templates = {
                "general": [
                    "# {title}\n\n## Executive Summary\n\n## Problem Statement\n\n## Project Goals and Objectives\n\n## Methodology\n\n## Timeline\n\n## Budget Summary\n\n## Expected Outcomes\n\n## Evaluation Plan\n\n## Conclusion",
                    "# {title}\n\n## Abstract\n\n## Introduction\n\n## Background and Significance\n\n## Specific Aims\n\n## Research Design\n\n## Preliminary Results\n\n## Budget and Justification\n\n## Timeline\n\n## References"
                ],
                "research": [
                    "# {title}\n\n## Abstract\n\n## Introduction\n\n## Literature Review\n\n## Research Questions\n\n## Methodology\n\n## Data Collection and Analysis\n\n## Expected Results\n\n## Budget\n\n## Timeline\n\n## References",
                    "# {title}\n\n## Executive Summary\n\n## Background and Significance\n\n## Specific Aims\n\n## Research Strategy\n\n## Preliminary Studies\n\n## Approach\n\n## Timeline and Milestones\n\n## Budget\n\n## References"
                ],
                "nonprofit": [
                    "# {title}\n\n## Organization Overview\n\n## Need Statement\n\n## Project Description\n\n## Goals and Objectives\n\n## Implementation Plan\n\n## Evaluation Plan\n\n## Sustainability\n\n## Budget\n\n## Conclusion",
                    "# {title}\n\n## Executive Summary\n\n## Organization Background\n\n## Statement of Need\n\n## Project Description\n\n## Goals and Objectives\n\n## Methods and Timeline\n\n## Evaluation\n\n## Budget\n\n## Future Funding\n\n## Appendices"
                ]
            }
            return templates
        except Exception as e:
            print(f"Error loading templates: {e}")
            # Return default templates
            return {
                "general": ["# {title}\n\n## Executive Summary\n\n## Problem Statement\n\n## Project Goals\n\n## Methodology\n\n## Budget\n\n## Timeline\n\n## Conclusion"]
            }
    
    def generate_outline(self, topic, goals, funding_agency=None):
        """
        Generate a proposal outline based on the provided information.
        
        Args:
            topic (str): The research or project topic
            goals (str): The project goals
            funding_agency (str, optional): The target funding agency
            
        Returns:
            str: A formatted outline for the proposal
        """
        # In a real application, you would use an AI model to generate the outline
        # For this example, we'll use a template-based approach
        
        # Determine the template category based on the topic and funding agency
        category = "general"
        if any(keyword in topic.lower() for keyword in ["research", "study", "investigation", "analysis"]):
            category = "research"
        elif any(keyword in topic.lower() for keyword in ["nonprofit", "community", "social", "service"]):
            category = "nonprofit"
            
        # Select a random template from the appropriate category
        templates = self.templates.get(category, self.templates["general"])
        template = random.choice(templates)
        
        # Format the template with the provided information
        title = f"Grant Proposal: {topic}"
        outline = template.format(title=title)
        
        # Add custom sections based on goals and funding agency
        sections = outline.split("\n\n")
        
        # Add funding agency specific section if provided
        if funding_agency:
            sections.insert(-1, f"## Alignment with {funding_agency} Priorities")
        
        # Add goals section if not already included
        if not any("Goals" in section for section in sections):
            sections.insert(3, "## Project Goals and Objectives")
        
        # Reconstruct the outline
        outline = "\n\n".join(sections)
        
        return outline