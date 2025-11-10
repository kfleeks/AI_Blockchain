# AI_Blockchain
AI Blockchain project
# AI-Powered Blockchain Prescription Tracking System

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-educational-orange)

A healthcare prescription tracking system that combines blockchain technology with Large Language Model (LLM) validation to ensure secure, validated, and immutable prescription records.

---

## 🎯 Overview

This project demonstrates the integration of two cutting-edge technologies:
- **Blockchain**: Provides immutable, tamper-proof storage for prescription records
- **AI/LLM**: Validates prescription data for safety, completeness, and potential drug interactions

### Educational Purpose

This system is designed as an educational tool to help students understand:
1. Blockchain fundamentals (blocks, hashing, chain validation)
2. AI integration in healthcare applications
3. Data security and validation concepts
4. Combining distributed ledger technology with intelligent analysis

---

## ✨ Features

### Core Functionality
- ✅ **Blockchain-based Storage**: Immutable prescription records with cryptographic hashing
- ✅ **AI Validation**: Intelligent prescription analysis before blockchain entry
- ✅ **Drug Interaction Checking**: Automated detection of potential medication conflicts
- ✅ **Patient History Tracking**: Query all prescriptions for a specific patient
- ✅ **Chain Integrity Verification**: Ensures blockchain hasn't been tampered with
- ✅ **Comprehensive Validation Reports**: Detailed analysis of each prescription

### Security Features
- SHA-256 cryptographic hashing
- Chain integrity validation
- Immutable record storage
- Timestamp verification

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│           Prescription Submission Interface         │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│         LLM Validation Agent                        │
│  ┌──────────────────────────────────────────────┐   │
│  │ • Required Fields Check                      │   │
│  │ • Dosage Format Validation                   │   │
│  │ • Drug Interaction Analysis                  │   │
│  │ • Safety Recommendations                     │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  Valid?        │
         └────┬───────┬───┘
              │       │
          YES │       │ NO
              │       │
              ▼       ▼
    ┌─────────────┐  Reject &
    │ Blockchain  │  Report
    │             │
    │ Block 0     │ (Genesis)
    │ Block 1     │ (Prescription 1)
    │ Block 2     │ (Prescription 2)
    │ Block n     │ (Prescription n)
    └─────────────┘
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/yourusername/prescription-blockchain.git
   cd prescription-blockchain
   ```

2. **No external dependencies required!**
   
   The basic version uses only Python standard library:
   - `hashlib` - for SHA-256 hashing
   - `json` - for data serialization
   - `datetime` - for timestamps
   - `typing` - for type hints

3. **Run the demonstration**
   ```bash
   python prescription_blockchain.py
   ```

### Optional: For Real LLM Integration

To integrate with actual LLM APIs (Claude, OpenAI, etc.):

```bash
pip install anthropic  # For Claude API
# OR
pip install openai     # For OpenAI API
```

Then set your API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
# OR
export OPENAI_API_KEY='your-api-key-here'
```

---

## 💻 Usage

### Basic Usage

Run the demonstration script:

```bash
python prescription_blockchain.py
```

This will execute three test cases:
1. ✅ Valid prescription with all required fields
2. ⚠️ Valid prescription with drug interaction warning
3. ❌ Invalid prescription with missing required fields

### Programmatic Usage

```python
from prescription_blockchain import PrescriptionTrackingSystem

# Initialize the system
system = PrescriptionTrackingSystem()

# Create a prescription
prescription = {
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

# Submit for validation and blockchain storage
result = system.submit_prescription(prescription)

# View the blockchain
system.view_blockchain()

# Get patient history
history = system.blockchain.get_patient_history("P001")

# Check blockchain integrity
is_valid = system.blockchain.is_chain_valid()
print(f"Blockchain is valid: {is_valid}")
```

---

## 🔍 How It Works

### 1. Prescription Submission
When a prescription is submitted, it contains:
- Patient information (ID, name, age)
- Medication details (name, dosage, duration)
- Doctor information (ID, name)
- Prescription date

### 2. AI Validation Process

The LLM validator performs multiple checks:

```python
✓ Required Fields Check
  - Ensures all mandatory data is present
  - patient_id, patient_name, medication, dosage, doctor_id, doctor_name

✓ Dosage Format Validation
  - Verifies dosage contains numeric values
  - Checks format clarity

✓ Drug Interaction Analysis
  - Compares against known dangerous combinations
  - Flags potential interactions

✓ Safety Recommendations
  - Suggests additional precautions
  - Provides dispensing guidelines
```

### 3. Blockchain Storage

If validation passes:
```
1. Create new Block with:
   - Index (sequential number)
   - Timestamp
   - Prescription data
   - Validation report
   - Previous block's hash

2. Calculate SHA-256 hash of block contents

3. Add block to chain

4. Return success confirmation
```

### 4. Chain Integrity Verification

The system can verify that no blocks have been tampered with:
- Recalculates each block's hash
- Verifies previous_hash links match
- Ensures chain continuity

---

## 📝 Assignment Tasks

This project includes structured learning tasks for students:

### **Task 1: Enhance LLM Integration** (15 points)
Replace the simulated validator with actual Claude API calls.

**Hints:**
```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[{
        "role": "user",
        "content": f"Analyze this prescription for safety: {prescription}"
    }]
)
```

### **Task 2: Add Drug Interaction Database** (15 points)
Create a comprehensive drug interaction checker with real medical data.

### **Task 3: Implement Patient Privacy** (20 points)
- Add encryption for sensitive data
- Implement role-based access control
- Create audit logs

### **Task 4: Smart Contract Logic** (20 points)
- Prescription expiration tracking
- Refill limit enforcement
- Automated alerts

### **Task 5: Advanced Queries** (15 points)
- Search by medication name
- Filter by doctor
- Generate statistical reports

### **Task 6: Web Interface** (15 points)
Build a web UI using Flask or FastAPI.

### **Bonus: Multi-node Blockchain** (+10 points)
Implement distributed consensus mechanism.

---

## 📁 Project Structure

```
prescription-blockchain/
│
├── prescription_blockchain.py    # Main application code
├── README.md                      # This file
│
├── classes/
│   ├── Block                     # Blockchain block implementation
│   ├── PrescriptionBlockchain    # Blockchain management
│   ├── PrescriptionValidator     # LLM validation logic
│   └── PrescriptionTrackingSystem # Main system integration
│
└── tests/                        # (To be added by students)
    ├── test_blockchain.py
    ├── test_validator.py
    └── test_integration.py
```

---

## 🔌 API Reference

### PrescriptionTrackingSystem

#### `submit_prescription(prescription_data: Dict) -> Dict`
Submit a new prescription for validation and storage.

**Parameters:**
- `prescription_data` (dict): Prescription information

**Returns:**
- `dict`: Submission result with status and validation report

**Example:**
```python
result = system.submit_prescription({
    "patient_id": "P001",
    "patient_name": "John Doe",
    "medication": "Aspirin",
    "dosage": "100mg daily",
    "doctor_id": "D001",
    "doctor_name": "Dr. Smith"
})
```

#### `view_blockchain()`
Display the entire blockchain contents.

### PrescriptionBlockchain

#### `add_block(prescription_data: Dict, validation_report: Dict) -> Block`
Add a new block to the chain.

#### `is_chain_valid() -> bool`
Verify blockchain integrity.

#### `get_patient_history(patient_id: str) -> List[Dict]`
Retrieve all prescriptions for a specific patient.

### PrescriptionValidator

#### `validate_prescription(prescription: Dict) -> Dict`
Validate prescription using AI analysis.

**Returns:**
```python
{
    "is_valid": bool,
    "confidence": float,
    "checks_performed": List[str],
    "warnings": List[str],
    "recommendations": List[str],
    "timestamp": str,
    "validated_by": str
}
```

---

## 🚀 Future Enhancements

### Planned Features
- [ ] Real-time prescription monitoring dashboard
- [ ] Integration with pharmacy systems
- [ ] Multi-signature approval workflow
- [ ] Mobile application interface
- [ ] Prescription fulfillment tracking
- [ ] Insurance verification integration
- [ ] Telemedicine platform integration

### Advanced Blockchain Features
- [ ] Proof of Stake consensus
- [ ] Smart contract execution
- [ ] Cross-chain interoperability
- [ ] Zero-knowledge proofs for privacy

### AI Enhancements
- [ ] Personalized dosage recommendations
- [ ] Predictive adverse reaction analysis
- [ ] Natural language prescription parsing
- [ ] Automated generic substitution suggestions

---

## 🤝 Contributing

This is an educational project. Contributions are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include unit tests for new features
- Update README with new functionality

---

## 📚 Educational Resources

### Learn More About:

**Blockchain:**
- [Blockchain Basics](https://www.ibm.com/topics/blockchain)
- [How Hashing Works](https://en.wikipedia.org/wiki/Cryptographic_hash_function)

**Healthcare AI:**
- [AI in Healthcare](https://www.who.int/health-topics/artificial-intelligence)
- [Claude AI Documentation](https://docs.anthropic.com)

**Python Development:**
- [Python Official Documentation](https://docs.python.org/3/)
- [Type Hints Guide](https://docs.python.org/3/library/typing.html)

---

## ⚠️ Disclaimer

**This is an educational project and should NOT be used in production healthcare environments without:**
- HIPAA compliance implementation
- Professional medical validation
- Certified security audits
- Legal compliance review
- FDA approval (if applicable)
- Proper encryption and access controls

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👥 Authors

- **Kei'Chara Fleeks** - *Initial work* - (https://github.com/kfleeks)

---

## 🙏 Acknowledgments

- Inspired by real-world healthcare blockchain implementations
- Built for educational purposes to teach AI and blockchain integration
- Thanks to the open-source community for tools and libraries

---

## 📧 Contact

For questions, suggestions, or collaboration:

- Email: kfleeksjon@gmail.com
- GitHub: [@kfleeks](https://github.com/kfleeks)
- Project Link: (https://github.com/kfleeks/AI_Blockchain)

---

## 🌟 Star This Project

If you find this project helpful for learning, please consider giving it a star ⭐ on GitHub!

---

**Made with ❤️ for healthcare and education**
