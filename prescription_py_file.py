"""
AI-Powered Blockchain Prescription Tracking System
===================================================

ASSIGNMENT: Healthcare Prescription Tracking with LLM Validation

OBJECTIVE:
Create a blockchain-based prescription tracking system that uses an LLM to validate
and analyze prescription data before adding it to the blockchain.

LEARNING OUTCOMES:
1. Understand blockchain basics (blocks, hashing, chain validation)
2. Integrate AI/LLM for data validation
3. Implement healthcare data security concepts
4. Combine distributed ledger technology with intelligent analysis

SYSTEM ARCHITECTURE:
- Blockchain: Stores validated prescription records
- LLM Agent: Validates prescription data for safety and completeness
- API Interface: Handles prescription submissions

Author: Your Name
Date: November 2025
Version: 1.0
"""

import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional


# ============================================================================
# PART 1: BLOCKCHAIN IMPLEMENTATION
# ============================================================================

class Block:
    """
    Represents a single block in the blockchain.
    
    Each block contains:
    - index: Position in the chain
    - timestamp: When the block was created
    - prescription_data: The prescription information
    - validation_report: AI validation results
    - previous_hash: Hash of the previous block (creates the chain)
    - hash: This block's unique identifier
    """
    
    def __init__(self, index: int, timestamp: str, prescription_data: Dict, 
                 previous_hash: str, validation_report: Dict):
        """
        Initialize a new block.
        
        Args:
            index: Block number in the chain
            timestamp: ISO format timestamp
            prescription_data: Dictionary containing prescription details
            previous_hash: Hash of the previous block
            validation_report: AI validation results
        """
        self.index = index
        self.timestamp = timestamp
        self.prescription_data = prescription_data
        self.validation_report = validation_report
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calculate SHA-256 hash of block contents.
        
        This hash uniquely identifies the block and ensures data integrity.
        Any change to the block's data will result in a completely different hash.
        
        Returns:
            str: 64-character hexadecimal hash string
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "prescription_data": self.prescription_data,
            "validation_report": self.validation_report,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self) -> Dict:
        """
        Convert block to dictionary for easy serialization and display.
        
        Returns:
            dict: Block data as a dictionary
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "prescription_data": self.prescription_data,
            "validation_report": self.validation_report,
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }


class PrescriptionBlockchain:
    """
    Manages the prescription blockchain.
    
    This class handles:
    - Creating and maintaining the chain
    - Adding new blocks
    - Validating chain integrity
    - Querying prescription history
    """
    
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain: List[Block] = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """
        Create the first block in the chain (genesis block).
        
        The genesis block is the foundation of the blockchain and has
        a previous_hash of "0" since there's no block before it.
        """
        genesis_block = Block(
            index=0,
            timestamp=datetime.now().isoformat(),
            prescription_data={"type": "genesis"},
            previous_hash="0",
            validation_report={"status": "genesis_block"}
        )
        self.chain.append(genesis_block)
        print(f"✓ Genesis block created with hash: {genesis_block.hash[:16]}...")
    
    def get_latest_block(self) -> Block:
        """
        Return the most recent block in the chain.
        
        Returns:
            Block: The last block in the chain
        """
        return self.chain[-1]
    
    def add_block(self, prescription_data: Dict, validation_report: Dict) -> Block:
        """
        Add a new validated prescription block to the chain.
        
        Args:
            prescription_data: Dictionary containing prescription information
            validation_report: AI validation results
            
        Returns:
            Block: The newly created block
        """
        new_block = Block(
            index=len(self.chain),
            timestamp=datetime.now().isoformat(),
            prescription_data=prescription_data,
            previous_hash=self.get_latest_block().hash,
            validation_report=validation_report
        )
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the entire blockchain.
        
        This checks:
        1. Each block's hash is correct (no data tampering)
        2. Each block's previous_hash matches the actual previous block
        
        Returns:
            bool: True if chain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if the block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"✗ Invalid hash at block {i}")
                return False
            
            # Check if previous_hash matches
            if current_block.previous_hash != previous_block.hash:
                print(f"✗ Invalid previous_hash link at block {i}")
                return False
        
        return True
    
    def get_patient_history(self, patient_id: str) -> List[Dict]:
        """
        Retrieve all prescriptions for a specific patient.
        
        Args:
            patient_id: The patient's unique identifier
            
        Returns:
            list: List of prescription records for the patient
        """
        return [
            block.to_dict() 
            for block in self.chain[1:]  # Skip genesis block
            if block.prescription_data.get("patient_id") == patient_id
        ]
    
    def get_doctor_prescriptions(self, doctor_id: str) -> List[Dict]:
        """
        Retrieve all prescriptions written by a specific doctor.
        
        Args:
            doctor_id: The doctor's unique identifier
            
        Returns:
            list: List of prescription records by the doctor
        """
        return [
            block.to_dict() 
            for block in self.chain[1:]
            if block.prescription_data.get("doctor_id") == doctor_id
        ]
    
    def search_by_medication(self, medication_name: str) -> List[Dict]:
        """
        Search for prescriptions by medication name.
        
        Args:
            medication_name: Name of the medication to search for
            
        Returns:
            list: List of prescription records containing the medication
        """
        medication_lower = medication_name.lower()
        return [
            block.to_dict() 
            for block in self.chain[1:]
            if medication_lower in block.prescription_data.get("medication", "").lower()
        ]


# ============================================================================
# PART 2: LLM VALIDATION AGENT (Simulated)
# ============================================================================

class PrescriptionValidator:
    """
    Simulates an LLM-based prescription validator.
    
    In a real implementation, this would call Claude API or another LLM
    to analyze prescription safety, drug interactions, and completeness.
    
    Example of real LLM integration:
    
    import anthropic
    
    client = anthropic.Anthropic(api_key="your-api-key")
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"Analyze this prescription for safety: {prescription}"
        }]
    )
    """
    
    # Common drug interactions database (simplified)
    DRUG_INTERACTIONS = {
        "Warfarin": ["Aspirin", "Ibuprofen", "NSAIDs"],
        "MAOIs": ["SSRIs", "Tyramine-rich foods"],
        "Metformin": ["Alcohol", "Iodinated contrast"],
        "Statins": ["Grapefruit juice", "Fibrates"],
        "ACE Inhibitors": ["Potassium supplements", "NSAIDs"],
        "Digoxin": ["Diuretics", "Calcium channel blockers"]
    }
    
    @staticmethod
    def validate_prescription(prescription: Dict) -> Dict:
        """
        Validate prescription data using AI analysis.
        
        Performs multiple validation checks:
        1. Required fields presence
        2. Dosage format validation
        3. Drug interaction checking
        4. Safety recommendations
        
        Args:
            prescription: Dictionary containing prescription data
            
        Returns:
            dict: Validation report with results and recommendations
        """
        validation_result = {
            "is_valid": True,
            "confidence": 0.95,
            "checks_performed": [],
            "warnings": [],
            "recommendations": [],
            "errors": []
        }
        
        # ========== Check 1: Required Fields ==========
        required_fields = [
            "patient_id", 
            "patient_name", 
            "medication", 
            "dosage", 
            "doctor_id", 
            "doctor_name"
        ]
        missing_fields = [f for f in required_fields if f not in prescription]
        
        if missing_fields:
            validation_result["is_valid"] = False
            validation_result["errors"].append(
                f"Missing required fields: {', '.join(missing_fields)}"
            )
            validation_result["checks_performed"].append(
                "✗ Required fields check FAILED"
            )
        else:
            validation_result["checks_performed"].append(
                "✓ All required fields present"
            )
        
        # ========== Check 2: Dosage Format Validation ==========
        if "dosage" in prescription:
            dosage = prescription["dosage"]
            if any(char.isdigit() for char in dosage):
                validation_result["checks_performed"].append(
                    f"✓ Dosage format valid: {dosage}"
                )
            else:
                validation_result["warnings"].append(
                    "⚠ Dosage format unclear - verify with prescribing physician"
                )
                validation_result["checks_performed"].append(
                    "⚠ Dosage format needs verification"
                )
        
        # ========== Check 3: Drug Interaction Check ==========
        if "medication" in prescription:
            medication = prescription["medication"]
            interactions_found = []
            
            for drug, interactions in PrescriptionValidator.DRUG_INTERACTIONS.items():
                if drug.lower() in medication.lower():
                    interactions_found.append({
                        "drug": drug,
                        "interactions": interactions
                    })
                    validation_result["warnings"].append(
                        f"⚠ INTERACTION ALERT: {drug} - verify no concurrent use of {', '.join(interactions)}"
                    )
            
            if interactions_found:
                validation_result["checks_performed"].append(
                    f"⚠ Found {len(interactions_found)} potential interaction(s)"
                )
            else:
                validation_result["checks_performed"].append(
                    "✓ No known drug interactions detected"
                )
        
        # ========== Check 4: Patient Age Validation ==========
        if "patient_age" in prescription:
            age = prescription["patient_age"]
            if age < 18:
                validation_result["warnings"].append(
                    "⚠ Pediatric patient - verify dosage is age-appropriate"
                )
            elif age > 65:
                validation_result["warnings"].append(
                    "⚠ Geriatric patient - monitor for adverse effects and adjust dosage if needed"
                )
        
        # ========== Check 5: Duration Validation ==========
        if "duration" in prescription:
            duration = prescription["duration"]
            if "30" in duration or "month" in duration.lower():
                validation_result["recommendations"].append(
                    "📋 Standard 30-day supply - schedule follow-up appointment"
                )
            elif "90" in duration:
                validation_result["recommendations"].append(
                    "📋 Extended 90-day supply - ensure patient has stable condition"
                )
        
        # ========== General Safety Recommendations ==========
        validation_result["recommendations"].extend([
            "🔍 Verify patient allergy history before dispensing",
            "🆔 Confirm patient identification at pickup",
            "📞 Provide patient counseling on proper medication use"
        ])
        
        # ========== Calculate Confidence Score ==========
        if not validation_result["is_valid"]:
            validation_result["confidence"] = 0.0
        elif validation_result["warnings"]:
            validation_result["confidence"] = 0.75
        elif validation_result["errors"]:
            validation_result["confidence"] = 0.0
        
        # Add metadata
        validation_result["timestamp"] = datetime.now().isoformat()
        validation_result["validated_by"] = "LLM Prescription Validator v1.0"
        validation_result["validation_method"] = "Simulated AI Analysis"
        
        return validation_result


# ============================================================================
# PART 3: PRESCRIPTION MANAGEMENT SYSTEM
# ============================================================================

class PrescriptionTrackingSystem:
    """
    Main system integrating blockchain and LLM validation.
    
    This class orchestrates the entire prescription tracking workflow:
    1. Receive prescription submission
    2. Validate using LLM
    3. Store validated prescriptions in blockchain
    4. Provide query and reporting capabilities
    """
    
    def __init__(self):
        """Initialize the tracking system with blockchain and validator."""
        print("\n" + "="*70)
        print("INITIALIZING PRESCRIPTION TRACKING SYSTEM")
        print("="*70)
        self.blockchain = PrescriptionBlockchain()
        self.validator = PrescriptionValidator()
        print("✓ System ready")
    
    def submit_prescription(self, prescription_data: Dict) -> Dict:
        """
        Submit a new prescription for validation and blockchain storage.
        
        Workflow:
        1. Validate prescription using LLM
        2. If valid, add to blockchain
        3. Return submission result
        
        Args:
            prescription_data: Dictionary containing prescription information
            
        Returns:
            dict: Result of submission with status and details
        """
        print(f"\n{'='*70}")
        print("PROCESSING NEW PRESCRIPTION")
        print(f"{'='*70}")
        print(f"Patient: {prescription_data.get('patient_name', 'Unknown')}")
        print(f"Medication: {prescription_data.get('medication', 'Unknown')}")
        
        # Step 1: LLM Validation
        print("\n[STEP 1] Running AI validation...")
        validation_report = self.validator.validate_prescription(prescription_data)
        
        print(f"\n  Validation Status: {'✓ APPROVED' if validation_report['is_valid'] else '✗ REJECTED'}")
        print(f"  Confidence Score: {validation_report['confidence']:.1%}")
        print(f"\n  Checks Performed:")
        for check in validation_report['checks_performed']:
            print(f"    {check}")
        
        if validation_report['warnings']:
            print(f"\n  ⚠ Warnings:")
            for warning in validation_report['warnings']:
                print(f"    {warning}")
        
        if validation_report['errors']:
            print(f"\n  ✗ Errors:")
            for error in validation_report['errors']:
                print(f"    {error}")
        
        # Step 2: Add to blockchain if valid
        if validation_report["is_valid"]:
            print("\n[STEP 2] Adding to blockchain...")
            block = self.blockchain.add_block(prescription_data, validation_report)
            print(f"  ✓ Block #{block.index} created")
            print(f"  Block Hash: {block.hash[:32]}...")
            print(f"  Previous Hash: {block.previous_hash[:32]}...")
            
            result = {
                "status": "success",
                "message": "Prescription validated and added to blockchain",
                "block_index": block.index,
                "block_hash": block.hash,
                "validation_report": validation_report
            }
        else:
            print("\n[STEP 2] ✗ Blockchain entry REJECTED - validation failed")
            result = {
                "status": "rejected",
                "message": "Prescription validation failed - not added to blockchain",
                "validation_report": validation_report
            }
        
        print(f"{'='*70}\n")
        return result
    
    def view_blockchain(self):
        """Display the entire blockchain with all prescriptions."""
        print(f"\n{'='*70}")
        print("BLOCKCHAIN CONTENTS")
        print(f"{'='*70}")
        print(f"Total Blocks: {len(self.blockchain.chain)}")
        print(f"Chain Valid: {'✓ YES' if self.blockchain.is_chain_valid() else '✗ NO'}")
        print(f"{'='*70}")
        
        for block in self.blockchain.chain:
            print(f"\n{'─'*70}")
            print(f"BLOCK #{block.index}")
            print(f"{'─'*70}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            
            if block.index > 0:  # Skip genesis block details
                print(f"\nPrescription Data:")
                print(f"  Patient: {block.prescription_data.get('patient_name')} (ID: {block.prescription_data.get('patient_id')})")
                print(f"  Medication: {block.prescription_data.get('medication')}")
                print(f"  Dosage: {block.prescription_data.get('dosage')}")
                print(f"  Duration: {block.prescription_data.get('duration')}")
                print(f"  Doctor: {block.prescription_data.get('doctor_name')} (ID: {block.prescription_data.get('doctor_id')})")
                
                print(f"\nValidation Report:")
                print(f"  Status: {'✓ Valid' if block.validation_report.get('is_valid') else '✗ Invalid'}")
                print(f"  Confidence: {block.validation_report.get('confidence', 0):.1%}")
                
                if block.validation_report.get('warnings'):
                    print(f"  Warnings: {len(block.validation_report['warnings'])}")
        
        print(f"\n{'='*70}\n")
    
    def get_statistics(self) -> Dict:
        """
        Generate system statistics.
        
        Returns:
            dict: Statistics about prescriptions in the system
        """
        total_prescriptions = len(self.blockchain.chain) - 1  # Exclude genesis
        
        medications = {}
        doctors = {}
        patients = set()
        
        for block in self.blockchain.chain[1:]:
            med = block.prescription_data.get('medication')
            doc_id = block.prescription_data.get('doctor_id')
            pat_id = block.prescription_data.get('patient_id')
            
            if med:
                medications[med] = medications.get(med, 0) + 1
            if doc_id:
                doctors[doc_id] = doctors.get(doc_id, 0) + 1
            if pat_id:
                patients.add(pat_id)
        
        return {
            "total_prescriptions": total_prescriptions,
            "unique_patients": len(patients),
            "unique_doctors": len(doctors),
            "unique_medications": len(medications),
            "most_prescribed": max(medications.items(), key=lambda x: x[1]) if medications else None,
            "blockchain_valid": self.blockchain.is_chain_valid()
        }


# ============================================================================
# PART 4: DEMONSTRATION & TESTING
# ============================================================================

def print_section_header(title: str):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def main():
    """Run the prescription tracking system demonstration."""
    
    print_section_header("AI-POWERED BLOCKCHAIN PRESCRIPTION TRACKING SYSTEM")
    print("Demonstration of blockchain + AI for healthcare prescription management")
    print("="*70)
    
    # Initialize system
    system = PrescriptionTrackingSystem()
    
    # ========== TEST CASE 1: Valid Prescription ==========
    print_section_header("TEST CASE 1: Valid Prescription")
    prescription_1 = {
        "patient_id": "P001",
        "patient_name": "John Doe",
        "patient_age": 45,
        "medication": "Lisinopril",
        "dosage": "10mg once daily",
        "duration": "30 days",
        "doctor_id": "D101",
        "doctor_name": "Dr. Sarah Smith",
        "date_prescribed": "2025-11-09"
    }
    result_1 = system.submit_prescription(prescription_1)
    
    # ========== TEST CASE 2: Prescription with Warnings ==========
    print_section_header("TEST CASE 2: Prescription with Drug Interaction Warning")
    prescription_2 = {
        "patient_id": "P002",
        "patient_name": "Jane Smith",
        "patient_age": 62,
        "medication": "Warfarin",
        "dosage": "5mg daily",
        "duration": "90 days",
        "doctor_id": "D102",
        "doctor_name": "Dr. Michael Johnson",
        "date_prescribed": "2025-11-09"
    }
    result_2 = system.submit_prescription(prescription_2)
    
    # ========== TEST CASE 3: Invalid Prescription ==========
    print_section_header("TEST CASE 3: Invalid Prescription (Missing Required Data)")
    prescription_3 = {
        "patient_id": "P003",
        "medication": "Amoxicillin",
        "dosage": "500mg three times daily"
        # Missing: patient_name, doctor_id, doctor_name
    }
    result_3 = system.submit_prescription(prescription_3)
    
    # ========== TEST CASE 4: Pediatric Patient ==========
    print_section_header("TEST CASE 4: Pediatric Patient Prescription")
    prescription_4 = {
        "patient_id": "P004",
        "patient_name": "Tommy Wilson",
        "patient_age": 8,
        "medication": "Amoxicillin",
        "dosage": "250mg three times daily",
        "duration": "10 days",
        "doctor_id": "D103",
        "doctor_name": "Dr. Emily Chen",
        "date_prescribed": "2025-11-09"
    }
    result_4 = system.submit_prescription(prescription_4)
    
    # Display blockchain
    system.view_blockchain()
    
    # Verify blockchain integrity
    print_section_header("BLOCKCHAIN INTEGRITY VERIFICATION")
    is_valid = system.blockchain.is_chain_valid()
    print(f"Chain is valid: {'✓ YES' if is_valid else '✗ NO'}")
    print(f"Total blocks in chain: {len(system.blockchain.chain)}")
    print("="*70)
    
    # Query patient history
    print_section_header("PATIENT PRESCRIPTION HISTORY QUERY")
    patient_history = system.blockchain.get_patient_history("P001")
    print(f"\nPrescriptions for Patient P001 (John Doe): {len(patient_history)}")
    for record in patient_history:
        print(f"  • {record['prescription_data']['medication']} - "
              f"{record['prescription_data']['dosage']} - "
              f"Prescribed on {record['timestamp'][:10]}")
    
    # System statistics
    print_section_header("SYSTEM STATISTICS")
    stats = system.get_statistics()
    print(f"Total Prescriptions: {stats['total_prescriptions']}")
    print(f"Unique Patients: {stats['unique_patients']}")
    print(f"Unique Doctors: {stats['unique_doctors']}")
    print(f"Unique Medications: {stats['unique_medications']}")
    if stats['most_prescribed']:
        print(f"Most Prescribed: {stats['most_prescribed'][0]} ({stats['most_prescribed'][1]} times)")
    print(f"Blockchain Status: {'✓ Valid' if stats['blockchain_valid'] else '✗ Invalid'}")
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nNext Steps:")
    print("1. Review the blockchain structure and validation reports")
    print("2. Complete the assignment tasks to enhance the system")
    print("3. Integrate with real LLM API (Claude, OpenAI, etc.)")
    print("4. Add encryption for sensitive patient data")
    print("5. Build a web interface for easier interaction")
    print("="*70 + "\n")


# ============================================================================
# ASSIGNMENT TASKS FOR STUDENTS
# ============================================================================

"""
STUDENT TASKS:
=============

TASK 1: Enhance LLM Integration (15 points)
--------------------------------------------
Replace the simulated validator with actual Claude API calls.

Steps:
1. Install anthropic package: pip install anthropic
2. Set up API key: export ANTHROPIC_API_KEY='your-key'
3. Modify PrescriptionValidator.validate_prescription() to use real API
4. Parse LLM response and extract validation insights
5. Handle API errors gracefully

Example code:
```python
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[{
        "role": "user",
        "content": f"Analyze this prescription for safety: {json.dumps(prescription)}"
    }]
)
```


TASK 2: Add Comprehensive Drug Interaction Database (15 points)
---------------------------------------------------------------
Create a more extensive drug interaction checker.

Requirements:
- Expand DRUG_INTERACTIONS dictionary with at least 20 medications
- Add severity levels (critical, moderate, minor)
- Include food and supplement interactions
- Use LLM to analyze complex multi-drug interactions


TASK 3: Implement Patient Privacy & Security (20 points)
--------------------------------------------------------
Add encryption and access control.

Requirements:
- Encrypt sensitive patient data before blockchain storage
- Implement role-based access control (doctor, pharmacist, patient, admin)
- Create audit logs for all data access
- Add digital signatures for prescriptions


TASK 4: Smart Contract Logic (20 points)
----------------------------------------
Add prescription lifecycle management.

Requirements:
- Track prescription expiration dates
- Implement refill limits (e.g., max 3 refills)
- Create automated alerts for expiring prescriptions
- Add prescription cancellation/modification workflow


TASK 5: Advanced Query & Reporting (15 points)
----------------------------------------------
Enhance data retrieval capabilities.

Requirements:
- Implement full-text search across all prescriptions
- Add date range filtering
- Create statistical reports (most prescribed drugs, prescribing patterns)
- Generate doctor performance analytics
- Export data to CSV/JSON


TASK 6: Web Interface (15 points)
---------------------------------
Build a user-friendly web application.

Requirements:
- Use Flask or FastAPI framework
- Create forms for prescription submission
- Display blockchain visually (timeline or graph)
- Add real-time validation feedback
- Implement user authentication


BONUS TASK: Multi-node Distributed Blockchain (+10 points)
---------------------------------------------------------
Implement distributed consensus.

Requirements:
- Create multiple validator nodes
- Implement proof-of-stake or proof-of-authority consensus
- Handle network synchronization
- Test Byzantine fault tolerance


GRADING RUBRIC:
--------------
- Code quality and documentation: 20%
- Functionality and completeness: 40%
- Error handling and edge cases: 20%
- Innovation and extra features: 20%

Total: 100 points + 10 bonus points possible
"""


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
