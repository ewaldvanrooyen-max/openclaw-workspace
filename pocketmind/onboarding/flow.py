"""
PocketMind Onboarding Flow

Interactive CLI flow for collecting user information.
"""

import sys
import os
from typing import Dict, Optional

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from storage.json_store import ProfileStore
from onboarding.questions import OnboardingQuestions, format_profile_summary


class OnboardingFlow:
    """
    Interactive onboarding flow - asks 7 questions to build user profile.
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        self.store = ProfileStore(data_dir)
        self.questions = OnboardingQuestions.get_all_questions()
        self.answers: Dict = {}
    
    def run(self) -> Dict:
        """Run the complete onboarding flow."""
        self._print_welcome()
        
        for i, question in enumerate(self.questions, 1):
            self._print_progress(i, len(self.questions))
            
            answer = self._ask_question(question)
            
            # Handle skip
            if answer is None:
                if question.skip_option:
                    self._print_skip(question.skip_option)
                    self.answers[question.id] = None
                else:
                    self._print_required()
                    answer = self._ask_question(question)
            
            self.answers[question.id] = answer
        
        # Build and save profile
        profile = OnboardingQuestions.build_profile(self.answers)
        self.store.save_profile(profile)
        
        self._print_complete(profile)
        
        return profile
    
    def _print_welcome(self):
        print("\n" + "=" * 50)
        print("WELCOME TO POCKETMIND")
        print("=" * 50)
        print()
        print("I'm your personal AI assistant.")
        print("I'll learn about you to help better.")
        print()
        print("Let's get to know each other...")
        print()
    
    def _print_progress(self, current: int, total: int):
        print(f"\n--- Question {current}/{total} ---")
    
    def _print_skip(self, skip_text: str):
        print(f"  -> {skip_text}")
    
    def _print_required(self):
        print("  (This one's required, but you can be brief!)")
    
    def _print_complete(self, profile: Dict):
        print("\n" + "=" * 50)
        print("ONBOARDING COMPLETE")
        print("=" * 50)
        print()
        print(f"Nice to meet you, {profile.get('name', 'friend')}!")
        print()
        print("I now know:")
        print(format_profile_summary(profile))
        print()
        print("Ask me anything. I'm here to help.")
        print("=" * 50)
    
    def _ask_question(self, question) -> Optional[str]:
        print(f"\n{question.text}")
        
        if question.options:
            for i, option in enumerate(question.options, 1):
                print(f"  {i}. {option}")
            
            if question.skip_option:
                print(f"  0. {question.skip_option}")
            
            while True:
                try:
                    choice = input("\nEnter number: ").strip()
                    
                    if question.skip_option and choice == "0":
                        return None
                    
                    idx = int(choice) - 1
                    if 0 <= idx < len(question.options):
                        return question.options[idx]
                    else:
                        print("  Invalid number. Try again.")
                except ValueError:
                    print("  Please enter a number.")
        else:
            answer = input("> ").strip()
            
            if question.skip_option and answer.lower() in ["skip", "skip for now", "that's enough", "no"]:
                return None
            
            return answer


class QuickOnboarding:
    """Fast onboarding for testing - auto-fills with default values."""
    
    @staticmethod
    def run(data_dir: Optional[str] = None) -> Dict:
        store = ProfileStore(data_dir)
        
        test_answers = {
            "name": "Test User",
            "goal": "Productivity & tasks",
            "schedule": "9-5 office worker",
            "timezone": "UTC",
            "important_dates": "Test date",
            "response_style": "Brief & to the point",
            "additional_context": "Test user for development"
        }
        
        profile = OnboardingQuestions.build_profile(test_answers)
        store.save_profile(profile)
        
        print("Quick onboarding complete (test data)")
        return profile


def main():
    """CLI entry point for onboarding."""
    import argparse
    
    parser = argparse.ArgumentParser(description="PocketMind Onboarding")
    parser.add_argument("--quick", action="store_true", help="Run quick test onboarding")
    parser.add_argument("--data-dir", help="Custom data directory")
    args = parser.parse_args()
    
    if args.quick:
        QuickOnboarding.run(args.data_dir)
    else:
        flow = OnboardingFlow(args.data_dir)
        flow.run()


if __name__ == "__main__":
    main()
