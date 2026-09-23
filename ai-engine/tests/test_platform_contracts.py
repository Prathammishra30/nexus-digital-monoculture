from ai_engine.models.model_config import ModelConfig
from ai_engine.models.model_router import ModelRouter, TaskCategory
from ai_engine.validation.confidence import ConfidenceEvaluator


def test_confidence_requires_evidence():
    evaluator = ConfidenceEvaluator()
    assert evaluator.status(0.95, True).value == "CONFIRMED"
    assert evaluator.status(0.95, False).value == "REJECTED"


def test_router_is_task_specific():
    router = ModelRouter({TaskCategory.EXTRACTION: ModelConfig(model_name="extractor")})
    assert TaskCategory.EXTRACTION in router._routes
