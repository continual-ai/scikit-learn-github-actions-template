import continual
import os

client = continual.Client()

run_id = os.environ.get("CONTINUAL_RUN_ID", None)
run = client.runs.create(description="Create and promote model", id=run_id)

model = run.models.create(id="test-model", replace_if_exists=True)
model_version = model.model_versions.create()

accuracy_metric = model_version.metrics.create(id="accuracy", direction="HIGHER")
accuracy_metric.log(value=0.8)

model.promotions.create(
	model_version=model_version.name, 
	reason="UPLIFT", 
	improvement_metric="accuracy", 
	improvement_metric_value=0.8, 
	base_improvement_metric_value=0.7, 
	improvement_metric_diff=0.1
)

run.complete()
