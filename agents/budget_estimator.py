import random
import json
import pandas as pd

class BudgetEstimator:
    """
    Agent responsible for estimating project budgets based on topic, goals, and parameters.
    """
    
    def __init__(self):
        # In a real application, you would initialize your AI model here
        # For this example, we'll use a template-based approach
        self.budget_templates = self._load_budget_templates()
        self.usd_to_inr_rate = 75  # Conversion rate: 1 USD = 75 INR
    
    def _load_budget_templates(self):
        """Load budget templates or use default ones if file doesn't exist"""
        try:
            # In a real application, you would load templates from a file
            # For this example, we'll use hardcoded templates
            templates = {
                "research": {
                    "Personnel": {"base": 50000, "per_person": 75000},
                    "Equipment": {"base": 15000, "per_month": 1000},
                    "Materials and Supplies": {"base": 5000, "per_month": 500},
                    "Travel": {"base": 3000, "per_month": 250},
                    "Publication Costs": {"base": 2000, "per_month": 100},
                    "Consultant Services": {"base": 10000, "per_month": 500},
                    "Computer Services": {"base": 5000, "per_month": 200},
                    "Indirect Costs": {"percentage": 0.35}
                },
                "nonprofit": {
                    "Personnel": {"base": 40000, "per_person": 60000},
                    "Program Supplies": {"base": 8000, "per_month": 600},
                    "Marketing and Outreach": {"base": 5000, "per_month": 300},
                    "Facilities": {"base": 12000, "per_month": 1000},
                    "Travel": {"base": 2000, "per_month": 150},
                    "Professional Development": {"base": 3000, "per_month": 200},
                    "Technology": {"base": 7000, "per_month": 300},
                    "Administrative Overhead": {"percentage": 0.25}
                },
                "general": {
                    "Personnel": {"base": 45000, "per_person": 65000},
                    "Equipment": {"base": 10000, "per_month": 800},
                    "Materials and Supplies": {"base": 6000, "per_month": 400},
                    "Travel": {"base": 2500, "per_month": 200},
                    "Services": {"base": 8000, "per_month": 400},
                    "Other Direct Costs": {"base": 4000, "per_month": 300},
                    "Indirect Costs": {"percentage": 0.3}
                }
            }
            return templates
        except Exception as e:
            print(f"Error loading budget templates: {e}")
            # Return default templates
            return {
                "general": {
                    "Personnel": {"base": 50000, "per_person": 70000},
                    "Equipment": {"base": 10000, "per_month": 500},
                    "Materials": {"base": 5000, "per_month": 300},
                    "Other": {"base": 3000, "per_month": 200},
                    "Indirect Costs": {"percentage": 0.3}
                }
            }
    
    def estimate_budget(self, topic, goals, funding_agency=None, duration=12, team_size=3):
        """
        Estimate a project budget based on the provided information.
        
        Args:
            topic (str): The research or project topic
            goals (str): The project goals
            funding_agency (str, optional): The target funding agency
            duration (int): Project duration in months
            team_size (int): Number of team members
            
        Returns:
            dict: A dictionary containing budget categories and amounts in USD
        """
        # In a real application, you would use an AI model to generate the budget
        # For this example, we'll use a template-based approach
        
        # Determine the template category based on the topic and funding agency
        category = "general"
        if any(keyword in topic.lower() for keyword in ["research", "study", "investigation", "analysis"]):
            category = "research"
        elif any(keyword in topic.lower() for keyword in ["nonprofit", "community", "social", "service"]):
            category = "nonprofit"
            
        # Get the appropriate budget template
        template = self.budget_templates.get(category, self.budget_templates["general"])
        
        # Calculate budget based on template, duration, and team size
        budget = {}
        direct_costs = 0
        
        for category, params in template.items():
            if "percentage" in params:
                # Skip percentage-based categories for now
                continue
                
            # Calculate base amount
            amount = params["base"]
            
            # Add per-month costs
            if "per_month" in params:
                amount += params["per_month"] * duration
            
            # Add per-person costs for personnel
            if category == "Personnel" and "per_person" in params:
                amount = params["per_person"] * team_size
            
            # Add some randomness to make it more realistic
            variation = random.uniform(0.9, 1.1)
            amount = round(amount * variation, -2)  # Round to nearest 100
            
            budget[category] = amount
            direct_costs += amount
        
        # Add percentage-based categories (like indirect costs)
        for category, params in template.items():
            if "percentage" in params:
                amount = round(direct_costs * params["percentage"], -2)  # Round to nearest 100
                budget[category] = amount
        
        return budget
    
    def convert_usd_to_inr(self, amount_usd):
        """
        Convert USD amount to INR.
        
        Args:
            amount_usd (float): Amount in USD
            
        Returns:
            float: Amount in INR
        """
        return amount_usd * self.usd_to_inr_rate