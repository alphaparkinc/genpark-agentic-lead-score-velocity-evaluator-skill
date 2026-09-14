import json
from typing import Dict, Any, List, Optional

class AgenticLeadScoreVelocityEvaluatorClient:
    """
    Production-grade buyer intent and conversion velocity scorer.
    Calculates behavioral engagement scores and predicts high-intent checkout triggers.
    """
    def __init__(self):
        pass

    def evaluate_lead_score(self, session_dwell_time_sec: int = 340, page_views_count: int = 6, cart_abandoned_previously: bool = True, coupon_applied: bool = True) -> Dict[str, Any]:
        # Scoring algorithm
        time_score = min(30, int((session_dwell_time_sec / 300.0) * 30))
        page_score = min(30, page_views_count * 5)
        intent_score = 25 if cart_abandoned_previously else 10
        promo_score = 15 if coupon_applied else 5

        total_lead_score = time_score + page_score + intent_score + promo_score

        if total_lead_score >= 80:
            stage = "HIGH_CONVERSION_HOT_LEAD"
            action = "OFFER_EPHEMERAL_FREE_EXPEDITED_SHIPPING"
        elif total_lead_score >= 50:
            stage = "ENGAGED_CONSIDERING_LEAD"
            action = "DISPLAY_FEATURE_COMPARISON_MODAL"
        else:
            stage = "TOP_OF_FUNNEL_BROWSING"
            action = "DISPLAY_BESTSELLER_SOCIAL_PROOF"

        return {
            "evaluation_id": "lead_vel_5519",
            "total_intent_score": total_lead_score,
            "funnel_stage": stage,
            "next_best_action": action,
            "urgency_level": "CRITICAL_ACTION_WINDOW_OPEN" if total_lead_score >= 80 else "STANDARD_RETENTION",
            "conversion_probability_pct": round(min(98.0, total_lead_score * 1.05), 1)
        }
