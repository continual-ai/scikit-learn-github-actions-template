import continual
import os

client = continual.Client()
run_id = os.environ.get("CONTINUAL_RUN_ID", None)
run = client.runs.create(description="Create and promote model", run_id=run_id)
model = run.models.create("test_model")
model_version = model.model_versions.create()
model_version.metrics.create(
	key="accuracy",
	value=0.8,
	direction="HIGHER"
)
model.promotions.create(
	model_version_name=model_version.name, reason="UPLIFT"
)
run.complete()
