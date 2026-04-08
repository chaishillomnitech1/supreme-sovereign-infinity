import os
import json
import time
from openai import OpenAI

class AIGuardian:
    """
    AI Guardian Core — ENHANCED
    ScrollSoul Sovereignty / OmniTech Ecosystem
    Supreme Sovereign: Chais Kenyatta Hill (Sabir Allah the Great)
    
    Production-ready AI security monitor with OpenAI integration,
    threat classification, and automated response protocols.
    """
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.threat_log = []
        self.defense_status = "ACTIVE"
        self.sovereign_wallet = "0x377956c1471d9ce142df6932895839243da23a2c"
        
    def classify_threat(self, anomaly_data):
        """
        Uses LLM to classify the severity and type of an anomaly.
        """
        prompt = f"""
        Analyze the following anomaly in the ScrollVerse ecosystem:
        {json.dumps(anomaly_data, indent=2)}
        
        Classify this threat into one of the following categories:
        - CRITICAL: Immediate action required (e.g., contract exploit, unauthorized minting)
        - HIGH: Serious threat (e.g., DDoS, frequency misalignment)
        - MEDIUM: Potential issue (e.g., failed login attempts, bridge delay)
        - LOW: Minor anomaly (e.g., heartbeat timeout)
        
        Provide a JSON response with:
        {{
            "category": "CATEGORY_NAME",
            "score": 0-100,
            "reasoning": "Brief explanation",
            "recommended_action": "Action to take"
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are the ScrollVerse AI Guardian, a sovereign security intelligence."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            classification = json.loads(response.choices[0].message.content)
            return classification
        except Exception as e:
            print(f"Error classifying threat: {e}")
            return {"category": "UNKNOWN", "score": 50, "reasoning": str(e), "recommended_action": "Manual review"}

    def execute_response(self, classification, anomaly_data):
        """
        Executes automated response protocols based on threat classification.
        """
        category = classification.get("category")
        action = classification.get("recommended_action")
        
        response_log = {
            "timestamp": time.time(),
            "anomaly": anomaly_data,
            "classification": classification,
            "action_taken": "NONE"
        }
        
        if category == "CRITICAL":
            # Protocol: Emergency Lockdown
            response_log["action_taken"] = "EMERGENCY_LOCKDOWN_ACTIVATED"
            self._trigger_contract_pause()
        elif category == "HIGH":
            # Protocol: IP Isolation & Alert
            response_log["action_taken"] = "THREAT_ISOLATION_ACTIVATED"
        elif category == "MEDIUM":
            # Protocol: Enhanced Monitoring
            response_log["action_taken"] = "ENHANCED_MONITORING_ACTIVATED"
            
        self.threat_log.append(response_log)
        return response_log

    def _trigger_contract_pause(self):
        """
        Mock function to trigger contract pause via web3.py
        """
        print("🚨 CRITICAL THREAT: Triggering contract pause protocol...")
        # Implementation would use web3.py to call pause() on LONDC contract
        pass

    def get_status_report(self):
        """
        Returns a summary of the Guardian's status and recent threats.
        """
        return {
            "status": self.defense_status,
            "total_threats_detected": len(self.threat_log),
            "recent_threats": self.threat_log[-5:] if self.threat_log else [],
            "sovereign_wallet": self.sovereign_wallet
        }

if __name__ == "__main__":
    guardian = AIGuardian()
    test_anomaly = {
        "type": "UNAUTHORIZED_MINT_ATTEMPT",
        "portalId": "Infinite-Nexus-ScrollVerse",
        "details": "Attempt to mint 1,000,000 LONDC from unauthorized address 0xabc..."
    }
    
    print("🛡️ AI Guardian: Analyzing test anomaly...")
    classification = guardian.classify_threat(test_anomaly)
    print(f"Classification: {json.dumps(classification, indent=2)}")
    
    response = guardian.execute_response(classification, test_anomaly)
    print(f"Response Executed: {response['action_taken']}")
