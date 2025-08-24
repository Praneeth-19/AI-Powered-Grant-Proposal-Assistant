import json
import os
from datetime import datetime
import copy

class VersionTracker:
    """
    Utility class for tracking versions of proposals and their rationales.
    """
    
    def __init__(self, storage_file=None):
        """
        Initialize the version tracker.
        
        Args:
            storage_file (str, optional): Path to the file for storing versions.
                If not provided, versions will be stored in memory only.
        """
        self.storage_file = storage_file
        self.versions = []
        
        # Load existing versions if storage file exists
        if storage_file and os.path.exists(storage_file):
            try:
                with open(storage_file, 'r') as f:
                    self.versions = json.load(f)
            except Exception as e:
                print(f"Error loading versions from {storage_file}: {e}")
    
    def save_version(self, proposal, rationale):
        """
        Save a new version of the proposal with a rationale.
        
        Args:
            proposal (dict): The proposal data to save
            rationale (str): The reason for this version/change
            
        Returns:
            int: The version number (index + 1)
        """
        # Create a deep copy to avoid reference issues
        proposal_copy = copy.deepcopy(proposal)
        
        # Create version entry
        version = {
            'proposal': proposal_copy,
            'rationale': rationale,
            'timestamp': datetime.now().timestamp(),
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add to versions list
        self.versions.append(version)
        
        # Save to file if storage_file is provided
        if self.storage_file:
            try:
                with open(self.storage_file, 'w') as f:
                    json.dump(self.versions, f, indent=2)
            except Exception as e:
                print(f"Error saving versions to {self.storage_file}: {e}")
        
        return len(self.versions)
    
    def get_version(self, version_number):
        """
        Get a specific version by number (1-indexed).
        
        Args:
            version_number (int): The version number (1-indexed)
            
        Returns:
            dict: The version data, or None if not found
        """
        index = version_number - 1
        if 0 <= index < len(self.versions):
            return self.versions[index]
        return None
    
    def get_all_versions(self):
        """
        Get all versions.
        
        Returns:
            list: All version data
        """
        return self.versions
    
    def get_latest_version(self):
        """
        Get the latest version.
        
        Returns:
            dict: The latest version data, or None if no versions exist
        """
        if self.versions:
            return self.versions[-1]
        return None
    
    def compare_versions(self, version1, version2):
        """
        Compare two versions and return the differences.
        
        Args:
            version1 (int): First version number (1-indexed)
            version2 (int): Second version number (1-indexed)
            
        Returns:
            dict: Differences between the versions
        """
        v1 = self.get_version(version1)
        v2 = self.get_version(version2)
        
        if not v1 or not v2:
            return None
        
        # In a real application, you would implement a more sophisticated
        # comparison algorithm here. For this example, we'll just return
        # a simple comparison of the two versions.
        
        differences = {
            'version1': version1,
            'version2': version2,
            'timestamp1': v1['timestamp'],
            'timestamp2': v2['timestamp'],
            'rationale1': v1['rationale'],
            'rationale2': v2['rationale']
        }
        
        return differences